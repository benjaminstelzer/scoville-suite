// Run with an existing Playwright installation; no dependency installation.
// SCOVILLE_PLAYWRIGHT_MODULE may name its absolute module path.
// node tests/measure_layout.browser.cjs <new-output-directory> [original-svg]
const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');
const { chromium } = require(process.env.SCOVILLE_PLAYWRIGHT_MODULE || 'playwright');
const packageRoot = path.resolve(__dirname, '../../scoville-design-anti-ai-slop');
const source = fs.readFileSync(path.join(packageRoot, 'scripts/measure-layout.js'), 'utf8');
const output = path.resolve(process.argv[2]);
fs.mkdirSync(output, {recursive:false});

(async () => {
  const browser = await chromium.launch({channel:'msedge', headless:true});
  try {
    const page = await browser.newPage({viewport:{width:1400,height:1100}});
    await page.setContent(`<!doctype html><style>
      body {margin:0;font-family:Arial} .box {position:absolute;box-sizing:border-box}
      #box {left:20px;top:20px;width:200px;height:100px;background:#ddd}
      #a {left:12px;top:8px;width:80px;height:30px;background:#aca}
      #b {left:104px;top:8px;width:50px;height:30px;background:#aac}
      #paint {left:0;top:0;width:200px;height:20px;background:#ddd}
      .body {font-size:20px;line-height:28px;font-weight:400}
      #label {position:absolute;left:20px;top:160px}
      #hidden {display:none} #rotated {position:absolute;transform:rotate(10deg);width:30px;height:30px}
      #individual {position:absolute;rotate:10deg;width:30px;height:30px}
      #scaled {position:absolute;left:300px;top:20px;width:100px;height:100px;transform:scale(2);transform-origin:0 0}
      #scaled-child {position:absolute;left:10px;top:10px;width:20px;height:20px}
      </style><div id="box" class="box"><div id="paint" class="box"></div>
      <div id="a" class="box"></div><div id="b" class="box"></div></div>
      <div id="label" class="body">Actual body text</div><div id="hidden">Hidden</div>
      <div id="rotated"></div><div id="individual"></div>
      <div id="scaled"><div id="scaled-child"></div></div>
      <svg width="200" height="100" style="position:absolute;top:230px">
      <g transform="rotate(15)"><rect id="svg-rotated" width="50" height="30"/></g></svg>`);
    const measure = checks => page.evaluate(({source,checks}) => eval(source)({checks}), {source,checks});
    const inset = {id:'inset',kind:'inset',content:'#a',container:'#box',
      min:{left:12,right:12,top:8,bottom:8},tolerance:0};
    const aligned = {id:'aligned',kind:'align',first:'#a',second:'#b',axis:'y',anchor:'start',expected:0,tolerance:0};
    const gap = {id:'gap',kind:'gap',first:'#a',second:'#b',axis:'x',expected:12,tolerance:0};
    const style = {id:'body',kind:'style',selector:'.body',expected:{fontSize:'20px',lineHeight:'28px',fontWeight:'400'}};
    const good = await measure([inset,aligned,gap,style]);
    assert.equal(good.status,'pass');
    assert.deepEqual(good.checks[0].observed,{left:12,right:108,top:8,bottom:62});
    // Intentionally asymmetric padding and paint overlap must not create findings.
    assert.equal(good.checks.length,4);
    await page.locator('#b').evaluate(e=>e.style.left='111px');
    const changedGap = await measure([gap]);
    assert.equal(changedGap.status,'fail');
    assert.equal(changedGap.checks[0].observed,19);
    await page.locator('#b').evaluate(e=>e.style.top='12px');
    assert.equal((await measure([aligned])).checks[0].observed,-4);
    await page.locator('#label').evaluate(e=>e.style.fontSize='21px');
    assert.equal((await measure([style])).status,'fail');
    const scaled = await measure([{...inset,id:'scaled',content:'#scaled-child',container:'#scaled',
      min:{left:20,right:20,top:20,bottom:20}}]);
    assert.equal(scaled.status,'pass');
    assert.equal(scaled.checks[0].observed.left,20);
    const invalidCases = [
      [], [inset,inset], [{...inset,id:'missing',content:'#missing'}],
      [{...inset,id:'hidden',content:'#hidden'}],
      [{...inset,id:'multiple',content:'.box'}],
      [{...inset,id:'tolerance',tolerance:-1}],
      [{...inset,id:'nan',tolerance:NaN}],
      [{...inset,id:'rotation',content:'#rotated'}],
      [{...inset,id:'individual-rotation',content:'#individual'}],
      [{...inset,id:'svg-rotation',content:'#svg-rotated'}],
      [{...aligned,id:'baseline',anchor:'baseline'}],
      [{...style,id:'bad-style',expected:{bogus:'20px'}}],
      [{...inset,id:'self',container:'#a'}]
    ];
    const invalid = [];
    for (const checks of invalidCases) {
      const result = await measure(checks);
      assert.equal(result.status,'unverified',JSON.stringify(result));
      invalid.push(result);
    }
    const receipt = {browser:browser.version(),good,changedGap,scaled,invalid,
      boundary:'Browser geometry regression checks, not a Skill-versus-no-Skill experiment.'};
    await page.setContent(`<!doctype html><style>
      body {margin:0;font:20px/28px Arial}
      #box {position:relative;margin:20px;width:200px;height:100px;background:#ddd}
      #text {position:absolute;left:12px;top:12px;width:176px;white-space:nowrap}
      #text.generated::before {content:'X'}
      </style><div id="box"><div id="text">This actual label extends far beyond its allocated block and container.</div></div>`);
    const textCheck = {...inset,id:'html-text',content:'#text',
      min:{left:12,right:12,top:12,bottom:12}};
    const htmlOverflow = await measure([textCheck]);
    assert.equal(htmlOverflow.status,'fail');
    assert.ok(htmlOverflow.checks[0].observed.right < -400);
    assert.equal(htmlOverflow.checks[0].contentMetric,'HTML text Range rectangles');
    const boxOnly = await measure([{...textCheck,contentMetric:'box'}]);
    assert.equal(boxOnly.status,'pass');
    assert.equal(boxOnly.checks[0].contentMetric,'element client rectangle');
    await page.screenshot({path:path.join(output,'html-overflow.png')});
    // Ellipsis can hide text inside a larger enclosure without geometric overflow.
    await page.locator('#box').evaluate(e=>e.style.width='1000px');
    await page.locator('#text').evaluate(e=>{e.style.overflow='hidden';e.style.textOverflow='ellipsis';});
    const ellipsis = await measure([textCheck]);
    assert.equal(ellipsis.status,'fail');
    assert.equal(ellipsis.checks[0].clippedOverflow,true);
    assert.ok(ellipsis.checks[0].observed.right > 0);
    // Repair by wrapping and giving real content enough height, preserving text.
    const originalText = await page.locator('#text').textContent();
    await page.locator('#box').evaluate(e=>{e.style.width='200px';e.style.height='200px';});
    await page.locator('#text').evaluate(e=>{e.style.whiteSpace='normal';e.style.overflow='visible';e.style.textOverflow='clip';});
    const wrapped = await measure([textCheck]);
    assert.equal(wrapped.status,'pass');
    assert.equal(await page.locator('#text').textContent(),originalText);
    await page.screenshot({path:path.join(output,'html-wrapped.png')});
    await page.locator('#text').evaluate(e=>{e.style.height='28px';e.style.overflow='hidden';});
    const clippedLines = await measure([textCheck]);
    assert.equal(clippedLines.status,'fail');
    assert.equal(clippedLines.checks[0].clippedOverflow,true);
    await page.locator('#text').evaluate(e=>{e.style.height='auto';e.style.overflow='visible';});
    await page.locator('#text').evaluate(e=>{e.innerHTML='<strong>This actual label</strong> extends far beyond its allocated block and container.';});
    assert.equal((await measure([textCheck])).status,'pass');
    await page.locator('#text').evaluate(e=>e.classList.add('generated'));
    const generated = await measure([textCheck]);
    assert.equal(generated.status,'unverified');
    await page.locator('#text').evaluate(e=>{e.className='';e.innerHTML='Label <img alt="icon">';});
    const mixed = await measure([textCheck]);
    assert.equal(mixed.status,'unverified');
    await page.setContent(`<svg id="viewport" width="400" height="100">
      <g id="pill"><rect id="shape" x="10" y="10" width="200" height="40" rx="20"/>
      <text id="t" x="24" y="36" font-size="18">Anmeldung am Hallentresen bitte</text></g></svg>`);
    const svgCheck = {...inset,id:'svg-enclosure',content:'#t',container:'#pill',
      min:{left:0,right:0,top:0,bottom:0}};
    const group = await measure([svgCheck]);
    assert.equal(group.status,'unverified');
    const shape = await measure([{...svgCheck,container:'#shape'}]);
    assert.equal(shape.status,'fail');
    assert.ok(shape.checks[0].observed.right < -40);
    const explicitGroup = await measure([{...svgCheck,containerMetric:'bounds'}]);
    assert.equal(explicitGroup.status,'pass');
    assert.equal(explicitGroup.checks[0].containerMetric,'bounds');
    const viewport = await measure([{...svgCheck,container:'#viewport'}]);
    assert.equal(viewport.status,'pass');
    // SVG design units must be converted; a known 16-unit inset is 32 CSS px.
    await page.setContent(`<svg width="400" height="200" viewBox="0 0 200 100">
      <rect id="shape" width="200" height="100"/>
      <rect id="label" x="16" y="16" width="20" height="20"/></svg>`);
    const scale = await page.locator('#label').evaluate(e=>e.getScreenCTM().a);
    assert.equal(scale,2);
    const units = await measure([{...inset,id:'converted-svg-units',content:'#label',container:'#shape',
      min:{left:16*scale,right:16*scale,top:16*scale,bottom:16*scale}}]);
    assert.equal(units.status,'pass');
    assert.equal(units.checks[0].observed.left,32);
    receipt.reviewRegressions={htmlOverflow,boxOnly,ellipsis,wrapped,clippedLines,generated,mixed,
      group,shape,explicitGroup,viewport,units};
    if (process.argv[3]) {
      const original = fs.readFileSync(path.resolve(process.argv[3]),'utf8');
      await page.setContent(original);
      await page.evaluate(() => {
        const text = [...document.querySelectorAll('text')].find(e=>e.textContent==='Die Änderung betrifft nur die Hülle.');
        const box = [...document.querySelectorAll('rect')].find(e=>e.getAttribute('x')==='1000');
        text.id='measured-label';box.id='measured-box';
      });
      const realCheck = {...inset,id:'recorded-overflow',content:'#measured-label',container:'#measured-box',
        min:{left:16,right:16,top:16,bottom:16}};
      const before = await measure([realCheck]);
      assert.equal(before.status,'fail');
      assert.ok(before.checks[0].observed.right < -40);
      await page.screenshot({path:path.join(output,'recorded-before.png')});
      const exactText = await page.locator('#measured-label').textContent();
      await page.evaluate(() => {
        const text = document.querySelector('#measured-label');
        text.textContent='';
        for (const [index,value] of ['Die Änderung betrifft ','nur die Hülle.'].entries()) {
          const span=document.createElementNS('http://www.w3.org/2000/svg','tspan');
          span.setAttribute('x','1031');span.setAttribute('dy',index ? '24' : '0');
          span.textContent=value;text.append(span);
        }
        document.querySelector('#measured-box').setAttribute('height','152');
      });
      assert.equal(await page.locator('#measured-label').textContent(),exactText);
      const after = await measure([realCheck]);
      assert.equal(after.status,'pass');
      await page.screenshot({path:path.join(output,'recorded-after.png')});
      receipt.recordedCase={before,after,exactTextPreserved:true,
        scope:'In-memory diagnostic correction of this relationship only. Original SVG/PNG unchanged; no whole-design acceptance.'};
      // A passing repaired subtitle must not hide the remaining enclosed labels.
      await page.evaluate(() => {
        for (const [index,value] of ['GLEICHER','PRODUKTINHALT'].entries())
          [...document.querySelectorAll('text')].find(e=>e.textContent===value).id='header-'+index;
      });
      const enclosedLabels = await measure([realCheck,...[0,1].map(index=>({...realCheck,
        id:'enclosed-header-'+index,content:'#header-'+index}))]);
      assert.equal(enclosedLabels.status,'fail');
      assert.equal(enclosedLabels.checks[0].status,'pass');
      assert.equal(enclosedLabels.checks[2].status,'fail');
      assert.ok(enclosedLabels.checks[2].observed.right < 16);
      receipt.recordedCase.enclosedLabels=enclosedLabels;
    }
    fs.writeFileSync(path.join(output,'receipt.json'),JSON.stringify(receipt,null,2)+'\n');
    console.log('PASS: real browser relationships, style drift, invalid evidence and preservation controls.');
  } finally { await browser.close(); }
})().catch(error=>{console.error(error);process.exitCode=1;});
