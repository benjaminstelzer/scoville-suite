const assert=require('node:assert/strict');
const fs=require('node:fs');
const path=require('node:path');
const {chromium}=require(process.env.SCOVILLE_PLAYWRIGHT_MODULE || 'playwright');
const helper=fs.readFileSync(path.resolve(__dirname,'../../scoville-design-anti-ai-slop/scripts/inventory-svg-layout.js'),'utf8');
if (!process.argv[2]) throw new Error('Provide a new, non-existing output directory.');
const output=path.resolve(process.argv[2]);
(async()=>{
  fs.mkdirSync(output,{recursive:false});
  const browser=await chromium.launch({channel:'msedge',headless:true});
  try {
    const page=await browser.newPage({viewport:{width:1200,height:500},deviceScaleFactor:1});
    await page.setContent(`<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="500" viewBox="0 0 1200 500">
      <defs><g id="glyph"><circle cx="20" cy="20" r="20"/></g><rect id="unused" width="20" height="20"/></defs>
      <rect id="screen" x="50" y="50" width="500" height="250" fill="#eee"/>
      <rect id="panel" x="200" y="100" width="100" height="100" fill="#aca"/>
      <use id="spill" href="#glyph" x="188" y="120"/>
      <use id="contained" href="#glyph" x="250" y="155"/>
      <use id="hidden" href="#glyph" x="188" y="120" style="display:none"/>
      <rect id="scaled-panel" x="400" y="100" width="100" height="120" fill="#aca"/>
      <use id="scaled" href="#glyph" transform="translate(390 120) scale(2)"/>
      <g id="mark" transform="translate(650 100)"><path d="M0 0 H80 V20" fill="none" stroke="black" stroke-width="10"/></g>
      <text id="word" x="710" y="125" font-family="Arial" font-size="28">NAME</text>
      <line id="anchor" x1="50" x2="390" y1="330" y2="330" stroke="black"/>
      <rect id="r1" x="50" y="350" width="100" height="50"/><rect id="r2" x="180" y="350" width="100" height="50"/><rect id="r3" x="310" y="350" width="100" height="50"/>
      <rect id="small-panel" x="580" y="200" width="30" height="30" fill="#aca"/>
      <use id="oversize" href="#glyph" x="575" y="195"/>
      <use id="after-content" href="#glyph" x="650" y="200"/>
      <rect id="after-frame" x="660" y="205" width="40" height="40" fill="none" stroke="black"/>
      <rect id="c1" x="950" y="50" width="50" height="40"/><rect id="c2" x="950" y="110" width="50" height="40"/>
      <line id="column-anchor" x1="930" x2="930" y1="50" y2="160" stroke="black"/>
      <foreignObject id="html-part" x="1000" y="250" width="160" height="100"><div xmlns="http://www.w3.org/1999/xhtml">Embedded HTML</div></foreignObject>
      <g id="wrapper"><use id="wrapped" href="#glyph" x="190" y="170"/></g>
    </svg>`);
    const before=await page.locator('svg').evaluate(e=>e.outerHTML);
    const result=await page.evaluate(async code=>await eval(code)({root:'svg'}),helper);
    assert.equal(result.status,'inventory-only');
    const item=id=>result.items.find(i=>i.selector==='#'+id);
    const enclosed=(id,region)=>result.candidates.find(c=>c.kind==='possible-local-enclosure' && c.object===item(id).id && c.region===item(region).id);
    assert.equal(enclosed('spill','panel').insets.left,-12);
    assert.equal(enclosed('spill','screen').insets.left,138);
    assert.ok(Object.values(enclosed('contained','panel').insets).every(v=>v>=0));
    assert.equal(enclosed('scaled','scaled-panel').insets.left,-10);
    assert.equal(item('scaled').box.width,80);
    assert.equal(item('hidden'),undefined);
    assert.equal(item('unused'),undefined);
    assert.equal(item('glyph'),undefined);
    assert.equal(enclosed('oversize','small-panel').smallerThanObject,true);
    assert.equal(enclosed('oversize','small-panel').insets.left,-5);
    assert.equal(enclosed('after-content','after-frame').paintOrder,'after-stroke-only');
    assert.equal(enclosed('after-content','after-frame').insets.left,-10);
    const column=result.candidates.find(c=>c.kind==='repeated-column' && c.objects.includes(item('c1').id));
    assert.deepEqual(column.gaps,[20]);
    assert.equal(column.possibleExternalAnchors.find(a=>a.anchor===item('column-anchor').id).endDelta,-10);
    assert.equal(result.unhandledForeignObjects[0].selector,'#html-part');
    assert.equal(result.unhandledForeignObjects[0].status,'needs-html-content-inventory');
    assert.equal(enclosed('wrapped','panel').duplicateOf,enclosed('wrapper','panel').id);
    const pair=result.candidates.find(c=>c.kind==='adjacent-artwork-text' && c.objects[0]===item('mark').id);
    assert.equal(pair.objects[1],item('word').id);
    assert.equal(pair.horizontalGap,-20);
    const row=result.candidates.find(c=>c.kind==='repeated-row' && c.objects.includes(item('r1').id));
    assert.deepEqual(row.gaps,[30,30]);
    assert.deepEqual(row.possibleExternalAnchors.find(a=>a.anchor===item('anchor').id),{anchor:item('anchor').id,startDelta:0,endDelta:20});
    assert.ok(result.candidates.every(c=>c.status.startsWith('needs-')),'Candidates never produce a design verdict, including intentional bleed controls.');
    assert.ok(result.reviewQueue.some(c=>c.object===item('spill').id && c.region===item('panel').id));
    assert.ok(!result.reviewQueue.some(c=>c.kind==='possible-local-enclosure' && c.object===item('contained').id));
    assert.ok(result.reviewQueue.some(c=>c.kind==='adjacent-artwork-text'));
    assert.ok(result.reviewQueue.some(c=>c.kind==='repeated-row'));
    const recordedIds=result.provisionalRecords.flatMap(r=>r.candidateIds);
    assert.deepEqual([...recordedIds].sort(),result.reviewQueue.map(c=>c.id).sort(),'Every queued candidate is seeded exactly once.');
    for (const candidate of result.reviewQueue) {
      const record=result.provisionalRecords.find(r=>r.candidateIds.includes(candidate.id));
      for (const involved of candidate.involved) assert.ok(record.record.includes(involved.selector),'Every involved selector survives in its provisional row.');
      assert.ok(record.record.includes('intent ?, target ?, basis ? | owner ?'));
      assert.ok(record.record.endsWith('metric ?, visual view ? | unverified'),'Discovery cannot fill semantic or evidence fields.');
    }
    const rowRecord=result.provisionalRecords.find(r=>r.candidateIds.includes(row.id));
    assert.ok(rowRecord.record.includes('"startDelta":0,"endDelta":20'));
    assert.ok(rowRecord.record.includes('#anchor'));
    const columnRecord=result.provisionalRecords.find(r=>r.candidateIds.includes(column.id));
    assert.ok(columnRecord.record.includes('"endDelta":-10'));
    const spillRecord=result.provisionalRecords.find(r=>r.candidateIds.includes(enclosed('spill','panel').id));
    assert.ok(spillRecord.record.includes('"left":-12'));
    const duplicateRecord=result.provisionalRecords.find(r=>r.candidateIds.includes(enclosed('wrapped','panel').id));
    assert.ok(duplicateRecord.candidateIds.includes(enclosed('wrapper','panel').id),'Duplicate candidates share a row without losing either identity.');
    assert.equal(await page.locator('svg').evaluate(e=>e.outerHTML),before,'Discovery must not alter input.');
    await page.screenshot({path:path.join(output,'fixture.png')});
    await page.setContent('<main>HTML requires another inventory.</main>');
    const unsupported=await page.evaluate(async code=>await eval(code)({root:'main'}),helper);
    assert.equal(unsupported.status,'unsupported');
    assert.deepEqual(unsupported.items,[]);
    assert.deepEqual(unsupported.provisionalRecords,[]);
    await page.setContent('<svg></svg><svg></svg>');
    const ambiguous=await page.evaluate(async code=>await eval(code)(),helper);
    assert.equal(ambiguous.status,'ambiguous-root');
    assert.equal(ambiguous.rootMatches,2);
    assert.deepEqual(ambiguous.items,[],'Never silently inspect only the first SVG.');
    assert.deepEqual(ambiguous.provisionalRecords,[]);
    fs.writeFileSync(path.join(output,'receipt.json'),JSON.stringify({result,unsupported,ambiguous},null,2)+'\n');
    console.log('PASS: local/canvas and oversized bounds, transformed instances, hidden definitions, later frames, adjacent art/text, row/column anchors, duplicates, foreignObject limits, no automatic verdict, unchanged DOM and unsupported source.');
  } finally {await browser.close();}
})().catch(e=>{console.error(e);process.exitCode=1;});
