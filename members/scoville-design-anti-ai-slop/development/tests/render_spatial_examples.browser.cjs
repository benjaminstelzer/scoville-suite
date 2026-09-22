const fs=require('node:fs');
const path=require('node:path');
const crypto=require('node:crypto');
const {chromium}=require(process.env.SCOVILLE_PLAYWRIGHT_MODULE || 'playwright');
const root=path.resolve(__dirname,'../../scoville-design-anti-ai-slop/examples/spatial-proof');
const ids=['repeated-card-span','type-role-map','longest-content-fit','optical-correction','intentional-asymmetry','decoration-control'];
const digest=p=>crypto.createHash('sha256').update(fs.readFileSync(p)).digest('hex');
(async()=>{const browser=await chromium.launch({channel:'msedge',headless:true});try{const entries=[];for(const id of ids){const source=path.join(root,id+'.svg'),render=path.join(root,id+'.png');const page=await browser.newPage({viewport:{width:640,height:400},deviceScaleFactor:1});await page.goto('file:///'+source.replace(/\\/g,'/'));await page.screenshot({path:render});await page.close();entries.push({id,source:id+'.svg',render:id+'.png',source_sha256:digest(source),render_sha256:digest(render),viewport:[640,400],review:'pending-native-image-view'});}fs.writeFileSync(path.join(root,'manifest.json'),JSON.stringify({schema_version:1,scope:'bounded teaching assets; values are example-specific',entries},null,2)+'\n');}finally{await browser.close();}})().catch(e=>{console.error(e);process.exit(1)});
