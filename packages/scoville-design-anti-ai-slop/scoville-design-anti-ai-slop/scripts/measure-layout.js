/* Read-only function expression for an already loaded HTML/SVG document.
 * Browser tool: const measure = <contents of this file>; await measure(spec).
 * Playwright: await page.evaluate(<contents as a function expression> +
 *                              '(' + JSON.stringify(spec) + ')').
 * No browser, Node package or network dependency is introduced by this helper.
 *
 * spec = { checks: [
 *   {id:'label-fit', kind:'inset', content:'#label', container:'#box',
 *    contentMetric:'auto', min:{left:12,right:12,top:6,bottom:6}, tolerance:0},
 *   {id:'caption-gap', kind:'gap', first:'#image', second:'#caption',
 *    axis:'y', expected:12, tolerance:0.5},
 *   {id:'shared-edge', kind:'align', first:'#a', second:'#b',
 *    axis:'x', anchor:'start', expected:0, tolerance:0.5},
 *   {id:'body-role', kind:'style', selector:'.body',
 *    expected:{fontSize:'20px',lineHeight:'28px',fontWeight:'400'}}
 * ] }
 * Values above are illustrative, not recommended design defaults. Insets are
 * measured from the outer client rectangle; include any required border inset
 * in the target. Gap = second.start - first.end; alignment = first - second.
 * 'align' supports start/center/end, not baselines or optical centering.
 * Box selectors must match exactly one element; style checks cover all matches.
 * Style checks compare computed CSS values, not post-transform apparent size.
 * Missing/hidden geometry, rotation/skew and invalid checks are unverified.
 * Only declared relationships are checked. No semantic parent is inferred.
 * Inset contentMetric: auto (default) uses text Range rectangles for HTML text,
 * SVG client rectangles for SVG, otherwise element boxes. text requires text;
 * box explicitly checks only the element box, never its text fit.
 * HTML text supports DOM text with nested text markup and br, not generated
 * content, replaced elements, shadow roots or mixed text/icon groups.
 * Inset containerMetric: enclosure (default) rejects SVG union groups; select
 * the drawn shape. bounds explicitly permits group unions, not enclosure proof.
 * SVG viewport targets remain valid. All target values are viewport CSS px,
 * not SVG user units. Text bounds are font cells, not ink or full line boxes.
 */
(async function measureLayout(spec) {
  const metric = 'axis-aligned element or text Range rectangles in viewport CSS pixels';
  const limits = [
    'Not glyph ink, painted strokes, general clipping, optical balance or meaning.',
    'Pass covers declared checks only; style values exclude transform scaling.',
    'Font readiness does not identify the font file used for every glyph.'
  ];
  const result = (checks) => ({
    metric, limits, fontStatus: document.fonts?.status ?? 'unavailable',
    status: checks.some(c => c.status === 'fail') ? 'fail'
      : checks.length && checks.every(c => c.status === 'pass') ? 'pass' : 'unverified',
    checks
  });
  if (!spec || !Array.isArray(spec.checks) || !spec.checks.length)
    return result([{status:'unverified', reason:'A nonempty checks array is required.'}]);
  if (!document.fonts)
    return result([{status:'unverified', reason:'Font readiness is unavailable.'}]);
  await document.fonts.ready;
  const finite = value => typeof value === 'number' && Number.isFinite(value);
  const require = (condition, reason) => { if (!condition) throw new Error(reason); };
  const select = (selector) => {
    require(typeof selector === 'string' && selector.trim(), 'Missing selector.');
    const elements = [...document.querySelectorAll(selector)];
    require(elements.length > 0, `No matches: ${selector}`);
    return elements;
  };
  const one = selector => {
    const elements = select(selector);
    require(elements.length === 1, `Expected one element: ${selector}`);
    return elements[0];
  };
  const rect = (element) => {
    require(element.isConnected, 'Detached element.');
    for (let node = element; node; node = node.parentElement) {
      const style = getComputedStyle(node);
      require(style.display !== 'none' && style.visibility === 'visible'
        && Number(style.opacity) > 0 && style.contentVisibility !== 'hidden',
      'Hidden element or ancestor.');
      if (style.transform !== 'none') {
        const matrix = new DOMMatrixReadOnly(style.transform);
        require(matrix.is2D && Math.abs(matrix.b) < 1e-9 && Math.abs(matrix.c) < 1e-9,
          'Rotation/skew/3D needs a different geometry metric.');
      }
      // Individual CSS transform properties need separate treatment from transform.
      require(!style.rotate || style.rotate === 'none' || style.rotate === '0deg',
        'Individual CSS rotation needs a different geometry metric.');
      require(!style.perspective || style.perspective === 'none',
        'Perspective needs a different geometry metric.');
    }
    if (typeof element.getScreenCTM === 'function') {
      const matrix = element.getScreenCTM();
      require(matrix && Math.abs(matrix.b) < 1e-9 && Math.abs(matrix.c) < 1e-9,
        'SVG rotation/skew needs a different geometry metric.');
    }
    require(element.getClientRects().length > 0, 'No rendered client rectangle.');
    const b = element.getBoundingClientRect();
    require([b.left,b.right,b.top,b.bottom].every(finite)
      && b.width > 0 && b.height > 0, 'Empty or invalid geometry.');
    return {left:b.left,right:b.right,top:b.top,bottom:b.bottom,width:b.width,height:b.height};
  };
  const supportedStyles = new Set(['fontFamily','fontSize','lineHeight','fontWeight',
    'fontStyle','fontStretch','letterSpacing','textTransform','fontVariationSettings']);
  const textBounds = (element) => {
    rect(element);
    let clippedOverflow = false;
    for (const node of [element, ...element.querySelectorAll('*')]) {
      require(node instanceof HTMLElement && !node.shadowRoot
        && !/^(IMG|INPUT|TEXTAREA|SELECT|CANVAS|VIDEO|AUDIO|IFRAME|OBJECT|EMBED)$/.test(node.tagName)
        && (node.textContent.trim() || node.tagName === 'BR'),
      'Text metric needs a DOM text-only subtree; measure mixed content separately.');
      const style = getComputedStyle(node);
      for (const pseudo of ['::before','::after'])
        require(['none','normal','""'].includes(getComputedStyle(node,pseudo).content),
          'Generated content needs separate measurement.');
      if (node.tagName === 'BR') continue;
      rect(node);
      clippedOverflow ||= (style.overflowX !== 'visible' && node.scrollWidth > node.clientWidth)
        || (style.overflowY !== 'visible' && node.scrollHeight > node.clientHeight);
    }
    const walker = document.createTreeWalker(element, NodeFilter.SHOW_TEXT);
    const boxes = [];
    while (walker.nextNode()) {
      if (!walker.currentNode.textContent.trim()) continue;
      const range = document.createRange();
      range.selectNodeContents(walker.currentNode);
      boxes.push(...[...range.getClientRects()].filter(b => b.width > 0 && b.height > 0));
    }
    require(boxes.length > 0, 'No rendered text rectangles.');
    const left = Math.min(...boxes.map(b=>b.left)), right = Math.max(...boxes.map(b=>b.right));
    const top = Math.min(...boxes.map(b=>b.top)), bottom = Math.max(...boxes.map(b=>b.bottom));
    require([left,right,top,bottom].every(finite), 'Invalid text geometry.');
    return {bounds:{left,right,top,bottom,width:right-left,height:bottom-top},clippedOverflow};
  };
  const contentBounds = (element, mode) => {
    require(['auto','text','box'].includes(mode), 'Unsupported content metric.');
    const hasText = Boolean(element.textContent.trim());
    require(mode !== 'text' || hasText, 'Text metric requires text.');
    if (mode !== 'box' && element instanceof HTMLElement && hasText)
      return {...textBounds(element),metric:'HTML text Range rectangles'};
    require(mode !== 'text' || element instanceof SVGTextContentElement,
      'Text metric requires HTML text or SVG text.');
    return {bounds:rect(element),clippedOverflow:false,metric:'element client rectangle'};
  };
  const ids = spec.checks.map(c => c?.id);
  const checks = spec.checks.map(check => {
    try {
      require(check && typeof check.id === 'string' && check.id.trim(), 'Missing check id.');
      require(ids.filter(id => id === check.id).length === 1, 'Duplicate check id.');
      if (check.kind === 'style') {
        const expected = check.expected;
        require(expected && typeof expected === 'object' && !Array.isArray(expected)
          && Object.keys(expected).length > 0, 'Expected style values are required.');
        for (const [key,value] of Object.entries(expected))
          require(supportedStyles.has(key) && typeof value === 'string' && value.length > 0,
            `Unsupported or invalid style expectation: ${key}`);
        const observed = select(check.selector).map(element => {
          rect(element);
          const style = getComputedStyle(element);
          const values = Object.fromEntries(Object.keys(expected).map(key => [key,style[key]]));
          return {element:element.id || element.tagName, values,
            matches:Object.entries(expected).every(([key,value]) => values[key] === value)};
        });
        return {id:check.id,kind:check.kind,expected,observed,
          status:observed.every(item => item.matches) ? 'pass' : 'fail'};
      }
      require(finite(check.tolerance) && check.tolerance >= 0, 'Explicit nonnegative tolerance required.');
      if (check.kind === 'inset') {
        const sides = ['left','right','top','bottom'];
        require(check.min && Object.keys(check.min).length === 4
          && sides.every(side => finite(check.min[side]) && check.min[side] >= 0),
        'Declare all four nonnegative minimum insets.');
        const content = one(check.content), container = one(check.container);
        require(content !== container, 'Content and container must differ.');
        const containerMetric = check.containerMetric ?? 'enclosure';
        require(['enclosure','bounds'].includes(containerMetric), 'Unsupported container metric.');
        require(containerMetric === 'bounds' || !(container instanceof SVGElement
          && ['g','a','switch','symbol'].includes(container.localName)),
        'SVG union group is not a drawn enclosure; select its shape or explicitly request bounds.');
        const measured = contentBounds(content, check.contentMetric ?? 'auto');
        const a = measured.bounds, b = rect(container);
        const observed = {left:a.left-b.left,right:b.right-a.right,
          top:a.top-b.top,bottom:b.bottom-a.bottom};
        return {id:check.id,kind:check.kind,expected:check.min,tolerance:check.tolerance,
          contentMetric:measured.metric,containerMetric,clippedOverflow:measured.clippedOverflow,
          bounds:{content:a,container:b},observed,
          status:!measured.clippedOverflow && sides.every(side => observed[side] + check.tolerance >= check.min[side]) ? 'pass' : 'fail'};
      }
      require(check.kind === 'gap' || check.kind === 'align', 'Unknown check kind.');
      require(check.axis === 'x' || check.axis === 'y', 'Axis must be x or y.');
      require(finite(check.expected), 'Explicit finite expected value required.');
      const first = one(check.first), second = one(check.second);
      require(first !== second, 'Compared elements must differ.');
      const a = rect(first), b = rect(second);
      const start = check.axis === 'x' ? 'left' : 'top';
      const end = check.axis === 'x' ? 'right' : 'bottom';
      let observed;
      if (check.kind === 'gap') observed = b[start] - a[end];
      else {
        require(['start','center','end'].includes(check.anchor), 'Unsupported alignment anchor.');
        const anchor = box => check.anchor === 'center' ? (box[start]+box[end])/2
          : box[check.anchor === 'start' ? start : end];
        observed = anchor(a) - anchor(b);
      }
      return {id:check.id,kind:check.kind,expected:check.expected,tolerance:check.tolerance,
        bounds:{first:a,second:b},observed,error:observed-check.expected,
        status:Math.abs(observed-check.expected) <= check.tolerance ? 'pass' : 'fail'};
    } catch (error) {
      return {id:check?.id ?? null,kind:check?.kind ?? null,status:'unverified',reason:String(error.message)};
    }
  });
  return result(checks);
})
