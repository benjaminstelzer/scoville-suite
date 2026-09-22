const assert = require("node:assert/strict");
const fs = require("node:fs");
const crypto = require("node:crypto");
const {spawnSync} = require("node:child_process");
const factory = eval(fs.readFileSync(process.argv[2], "utf8"));
const envelope = JSON.parse(fs.readFileSync(0, "utf8"));
const lifecycle = process.argv[3], python = process.argv[4];
const copy = x => JSON.parse(JSON.stringify(x));
function setup() {
  const memory = new Map(); let builds = 0, sends = 0, sent;
  const api = factory((k,v)=>memory.set(k,copy(v)), k=>copy(memory.get(k) ?? null));
  const build = async()=>{builds++;return {exit_code:0,output:JSON.stringify(envelope)};};
  const check = async e => {
    const p = spawnSync(python, ["-B",lifecycle], {input:JSON.stringify({
      operation:"message",handle:{state:"ready",threadId:"test-writer",hostId:"local"},
      prompt:e.prompt,delivery_state:"not_sent"}),encoding:"utf8"});
    assert.equal(p.status,0,p.stderr);
    return {binding:e.binding,arguments:JSON.parse(p.stdout).arguments,
      guard:{ok:true,workflow_id:"test-workflow",generation:1,revision:7,
        state:"writer_active",writer:{active:true,task_id:"test-writer",
          role:"executor",unit:"W-003/step-2",dispatch_key:"test-dispatch"}}};
  };
  const send = async args=>{sends++;sent=args.prompt;return {accepted:true};};
  return {api,memory,build,check,send,counts:()=>({builds,sends,sent})};
}
(async()=>{
  let s=setup();
  const receipt=await s.api.prepare("d",s.build);
  assert(!JSON.stringify(receipt).includes("plan_context"));
  assert.equal(receipt.sha256,crypto.createHash("sha256").update(envelope.prompt).digest("hex"));
  // A shortened display never touches retained bytes or invokes the builder.
  JSON.stringify(receipt).slice(0,12);
  s.api.inspect("d");
  await s.api.send("d",s.check,s.send);
  assert.deepEqual(s.counts(),{builds:1,sends:1,sent:envelope.prompt});
  assert.equal(s.api.inspect("d").delivery_state,"send_unknown");
  assert.deepEqual(s.api.takeReply("d"),{accepted:true});
  await assert.rejects(()=>s.api.prepare("d",s.build),/already retained/);
  await assert.rejects(()=>s.api.send("d",s.check,s.send),/never replay/);
  for(const change of [
    v=>v.binding="changed",
    v=>v.guard.revision++,
    v=>v.guard.writer.task_id="wrong",
    v=>v.arguments.prompt+="modified",
    v=>v.arguments.threadId="wrong"
  ]) {
    s=setup(); await s.api.prepare("d",s.build);
    await assert.rejects(()=>s.api.send("d",async e=>{const v=await s.check(e);change(v);return v;},s.send));
    assert.equal(s.counts().sends,0);
  }
  s=setup(); await s.api.prepare("d",s.build);
  await assert.rejects(()=>s.api.send("d",s.check,async()=>{throw Error("timeout");}));
  await assert.rejects(()=>s.api.send("d",s.check,s.send),/never replay/);
  s=setup(); await assert.rejects(()=>s.api.send("missing",s.check,s.send),/reconcile/);
  s=setup(); await assert.rejects(()=>s.api.prepare("d",async()=>({exit_code:0,output:'{"prompt":'})));
  await assert.rejects(()=>s.api.prepare("d",s.build),/already retained/);
  s=setup(); await s.api.prepare("d",s.build);
  const state=s.memory.get("d");state.envelope.prompt+="tamper";
  assert.throws(()=>s.api.inspect("d"),/integrity/);
  s=setup(); await s.api.prepare("d",s.build);
  const attempts=await Promise.allSettled([s.api.send("d",s.check,s.send),s.api.send("d",s.check,s.send)]);
  assert.equal(attempts.filter(x=>x.status==="fulfilled").length,1);
  assert.equal(s.counts().sends,1);
  // Reviewer creation uses the actual lifecycle create contract, never a writer grant.
  const review=copy(envelope);
  review.prompt=review.prompt.replace('scoville_role=executor\n','scoville_role=reviewer\n');
  review.receipt.role='reviewer';review.receipt.target='project:test-project';
  review.receipt.sha256=crypto.createHash('sha256').update(review.prompt).digest('hex');
  review.receipt.characters=Array.from(review.prompt).length;review.receipt.bytes=Buffer.byteLength(review.prompt);
  s=setup();await s.api.prepare('r',async()=>({exit_code:0,output:JSON.stringify(review)}));
  await s.api.send('r',async e=>{
    const p=spawnSync(python,['-B',lifecycle],{encoding:'utf8',input:JSON.stringify({
      operation:'create',family:'workflow',role:'reviewer',projectId:'test-project',
      reference:e.receipt.reference,prompt:e.prompt,model:'gpt-5.6-terra',thinking:'medium',
      unit:'W-003/step-2',attempt:1,creation_authorized:true,prior_state:'not_started'})});
    assert.equal(p.status,0,p.stderr);const result=JSON.parse(p.stdout);
    assert.equal(result.handle.state,'creation_unknown');
    return {binding:e.binding,arguments:result.arguments,guard:{ok:true,
      workflow_id:'test-workflow',generation:1,revision:7,state:'coordinator_active',writer:null}};
  },s.send);
  assert.equal(s.counts().sent,review.prompt);
  // Independent SHA vectors exercise padding boundaries and Unicode.
  for(const size of [0,1,55,56,63,64,65,1000]){
    const e=copy(envelope);e.prompt="scoville_role=executor\n"+"ä😀".repeat(size);
    e.receipt.sha256=crypto.createHash("sha256").update(e.prompt).digest("hex");
    e.receipt.characters=Array.from(e.prompt).length;e.receipt.bytes=Buffer.byteLength(e.prompt);
    const t=setup();await t.api.prepare("sha",async()=>({exit_code:0,output:JSON.stringify(e)}));
  }
  console.log("transport cases passed: once-only, hidden bytes, stale inputs/guard, mutation, loss, unknown, concurrent, truncation, SHA");
})().catch(e=>{console.error(e);process.exitCode=1;});
