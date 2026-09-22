/* Browser function expression: evaluate this file, then await inventory({root:'svg'}).
 * Read-only SVG discovery in viewport CSS pixels. No dependencies or DOM edits.
 * This is a candidate inventory, NEVER a semantic parent detector or verdict.
 * Rectangular candidates use centre inclusion and paint order; adjacent artwork/
 * text uses authored siblings; repeated rows use equal rendered dimensions.
 * These are explicit discovery heuristics. Assign actual roles before judging.
 * provisionalRecords seeds the existing working notes with unresolved queue
 * rows. It supplies geometry, never intent, owner, target or a design verdict.
 * Bounds exclude general paint/ink, stroke, filters, clipping and optical mass.
 * Hidden/unused definitions are excluded; unsupported artwork remains manual.
 */
(async function inventorySvgLayout(options = {}) {
  await document.fonts?.ready;
  const roots = document.querySelectorAll(options.root || 'svg');
  const root = roots[0];
  const limits = [
    'SVG only; no HTML, canvas, shadow-root or cross-frame coverage',
    'Client rectangles are not painted edges, glyph ink, optical mass or clipping proof',
    'Visibility filtering excludes definitions/display/visibility/zero-opacity cases, not every transparent or clipped shape',
    'Geometric candidates are not actual semantic parents or confirmed defects',
    'Enclosure discovery uses rect elements only, not path-based panels or nonrectangular regions',
    'Content whose centre lies outside its intended region and nonadjacent internal relations require manual mapping',
    'foreignObject HTML content requires a separate HTML inventory and measurement',
    'Nested group/instance candidates can describe one issue; never count them as independent defects',
    'Source grouping and equal dimensions are discovery hints, not design requirements'
  ];
  if (roots.length>1) return {status:'ambiguous-root', rootMatches:roots.length, limits, items:[], candidates:[], reviewQueue:[], provisionalRecords:[]};
  if (!root || root.localName !== 'svg') return {status:'unsupported', limits, items:[], candidates:[], reviewQueue:[], provisionalRecords:[]};
  const box = el => {
    const b = el.getBoundingClientRect();
    return {left:b.left, top:b.top, right:b.right, bottom:b.bottom, width:b.width, height:b.height};
  };
  const selector = el => {
    if (el.id) return '#' + CSS.escape(el.id);
    if (el === root) return options.root || 'svg';
    const siblings = [...el.parentElement.children].filter(e => e.localName === el.localName);
    return selector(el.parentElement) + ' > ' + el.localName + ':nth-of-type(' + (siblings.indexOf(el)+1) + ')';
  };
  const visible = el => {
    if (el.closest('defs,symbol,clipPath,mask,marker,pattern')) return false;
    for (let p=el; p && p!==root.parentElement; p=p.parentElement) {
      const s=getComputedStyle(p);
      if (s.display==='none' || Number(s.opacity)===0) return false;
    }
    if (getComputedStyle(el).visibility !== 'visible') return false;
    const b=box(el);
    return b.width>0 || b.height>0;
  };
  const elements = [...root.querySelectorAll('g,use,image,text,rect,circle,ellipse,path,polygon,polyline,line')].filter(visible);
  const index = new Map(elements.map((el,i)=>[el,i]));
  const isArt = el => ['use','image'].includes(el.localName) ||
    (el.localName==='g' && !el.querySelector('text') && !!el.querySelector('use,image,path,polygon,polyline,circle,ellipse'));
  const items = elements.map((el,i)=>({
    id:'e'+i, selector:selector(el), tag:el.localName,
    roleHint:el.localName==='text' ? 'text' : isArt(el) ? 'artwork' : el.localName==='rect' ? 'rectangle' : 'geometry',
    label:el.getAttribute('aria-label') || (el.localName==='text' ? el.textContent.trim() : el.getAttribute('href') || el.getAttribute('xlink:href')) || null,
    parent:index.has(el.parentElement) ? 'e'+index.get(el.parentElement) : null,
    box:box(el), boundsKind:el.localName==='g' ? 'group-union-not-enclosure' : 'client-rectangle'
  }));
  const byElement = new Map(elements.map((el,i)=>[el,items[i]]));
  const area = b => b.width*b.height;
  const insets = (a,b) => ({left:a.left-b.left, right:b.right-a.right, top:a.top-b.top, bottom:b.bottom-a.bottom});
  const candidates=[];
  const paint=new Map();
  const rectangles=items.filter(i=>i.tag==='rect' && area(i.box)>0 && (()=>{
    const s=getComputedStyle(elements[Number(i.id.slice(1))]);
    const coloured=value=>value!=='none' && value!=='transparent' && !/^rgba\([^)]*,\s*0(?:\.0*)?\)$/.test(value);
    const filled=coloured(s.fill) && Number(s.fillOpacity)>0;
    const stroked=coloured(s.stroke) && Number(s.strokeOpacity)>0 && parseFloat(s.strokeWidth)>0;
    paint.set(i.id,{filled,stroked});
    return filled || stroked;
  })());
  for (const item of items.filter(i=>['artwork','text'].includes(i.roleHint))) {
    const el=elements[Number(item.id.slice(1))], b=item.box;
    const cx=(b.left+b.right)/2, cy=(b.top+b.bottom)/2;
    const possible=rectangles.filter(r=>{
      const enclosure=elements[Number(r.id.slice(1))];
      const before=!!(enclosure.compareDocumentPosition(el)&Node.DOCUMENT_POSITION_FOLLOWING);
      return r.id!==item.id && !el.contains(enclosure) &&
        (before || (!paint.get(r.id).filled && paint.get(r.id).stroked)) &&
        cx>=r.box.left && cx<=r.box.right && cy>=r.box.top && cy<=r.box.bottom;
    }).sort((a,b)=>area(a.box)-area(b.box));
    // Retain the smallest geometric candidate and its containing rectangle chain.
    // The nearest candidate is explicitly NOT promoted to a semantic parent.
    let previous=null;
    for (const candidate of possible) {
      if (previous && Object.values(insets(previous.box,candidate.box)).some(v=>v<0)) continue;
      candidates.push({kind:'possible-local-enclosure', object:item.id, region:candidate.id,
        smallerThanObject:area(candidate.box)<area(b),
        paintOrder:(elements[Number(candidate.id.slice(1))].compareDocumentPosition(el)&Node.DOCUMENT_POSITION_FOLLOWING) ? 'before' : 'after-stroke-only',
        insets:insets(b,candidate.box), status:'needs-role-and-visual-review'});
      previous=candidate;
    }
    if (!possible.length) candidates.push({kind:'unmapped-content', object:item.id, status:'needs-manual-region-map'});
  }
  for (const el of elements.filter(isArt)) {
    // Only the next visible authored sibling: no arbitrary all-pairs alarms.
    let next=el.nextElementSibling;
    while (next && !byElement.has(next)) next=next.nextElementSibling;
    if (!next || next.localName!=='text') continue;
    const a=byElement.get(el), b=byElement.get(next);
    candidates.push({kind:'adjacent-artwork-text', objects:[a.id,b.id],
      horizontalGap:b.box.left-a.box.right, verticalGap:b.box.top-a.box.bottom,
      boxIntersection:{width:Math.max(0,Math.min(a.box.right,b.box.right)-Math.max(a.box.left,b.box.left)),
        height:Math.max(0,Math.min(a.box.bottom,b.box.bottom)-Math.max(a.box.top,b.box.top))},
      status:'needs-intent-and-visible-ink-review'});
  }
  // Exact rounded coordinate clustering is a source-pattern hint, not a fit tolerance.
  const number=v=>Math.round(v*1e6)/1e6;
  for (const axis of ['x','y']) {
   const start=axis==='x' ? 'left' : 'top', end=axis==='x' ? 'right' : 'bottom';
   const crossStart=axis==='x' ? 'top' : 'left', crossEnd=axis==='x' ? 'bottom' : 'right';
   const extent=axis==='x' ? 'width' : 'height';
   const groups=new Map();
   for (const r of rectangles) {
    const key=[r.box[crossStart],r.box.width,r.box.height].map(number).join(':');
    if (!groups.has(key)) groups.set(key,[]);
    groups.get(key).push(r);
   }
   for (const row of groups.values()) {
    if (row.length<2) continue;
    row.sort((a,b)=>a.box[start]-b.box[start]);
    if (row.some((r,i)=>i && r.box[start]<row[i-1].box[end])) continue;
    const first=row[0].box,last=row[row.length-1].box;
    const anchors=items.filter(i=>!row.includes(i) &&
      (i.tag==='rect' || (i.tag==='line' && number(i.box[axis==='x'?'height':'width'])===0)) &&
      number(i.box[start])===number(first[start]) &&
      (i.box[crossStart]<first[crossStart] || i.box[crossStart]>first[crossEnd]) && i.box[extent]>first[extent]);
    candidates.push({kind:axis==='x'?'repeated-row':'repeated-column', axis, objects:row.map(i=>i.id),
      span:{[start]:first[start],[end]:last[end]}, gaps:row.slice(1).map((r,i)=>r.box[start]-row[i].box[end]),
      possibleExternalAnchors:anchors.map(a=>({anchor:a.id,startDelta:first[start]-a.box[start],endDelta:last[end]-a.box[end]})),
      status:'needs-shared-anchor-intent-review'});
   }
  }
  const byId=new Map(items.map(i=>[i.id,i]));
  candidates.forEach((c,i)=>{
    c.id='r'+i;
    if (c.kind!=='possible-local-enclosure') return;
    const el=elements[Number(c.object.slice(1))], b=byId.get(c.object).box;
    const prior=candidates.slice(0,i).find(p=>p.kind===c.kind && p.region===c.region &&
      elements[Number(p.object.slice(1))].contains(el) &&
      ['left','top','right','bottom'].every(k=>byId.get(p.object).box[k]===b[k]));
    if (prior) c.duplicateOf=prior.duplicateOf || prior.id;
  });
  const reviewQueue=candidates.filter(c=>
    c.kind==='unmapped-content' ||
    (c.kind==='possible-local-enclosure' && Object.values(c.insets).some(v=>v<0)) ||
    (c.kind==='adjacent-artwork-text' && c.boxIntersection.width>0 && c.boxIntersection.height>0) ||
    (['repeated-row','repeated-column'].includes(c.kind) && c.possibleExternalAnchors.some(a=>a.startDelta!==0 || a.endDelta!==0))
  ).map(c=>({...c, involved:[...new Set([c.object,c.region,...(c.objects||[]),...(c.possibleExternalAnchors||[]).map(a=>a.anchor)].filter(Boolean))]
    .map(id=>({id,selector:byId.get(id).selector,label:byId.get(id).label,box:byId.get(id).box}))}));
  // Seed every queued candidate into the existing concern record. Identity and
  // observations survive transcription; all semantic fields still need a reviewer.
  const queueIds=new Set(reviewQueue.map(c=>c.id)), recordGroups=new Map();
  for (const c of reviewQueue) {
    const key=c.duplicateOf && queueIds.has(c.duplicateOf) ? c.duplicateOf : c.id;
    if (!recordGroups.has(key)) recordGroups.set(key,[]);
    recordGroups.get(key).push(c);
  }
  const provisionalRecords=[...recordGroups.values()].map(group=>{
    const selectors=ids=>[...new Set(ids.filter(Boolean))].map(id=>byId.get(id).selector).join(', ');
    const objects=selectors(group.flatMap(c=>c.object ? [c.object] : c.kind==='adjacent-artwork-text' ? c.objects.slice(0,1) : c.objects || []));
    const references=selectors(group.flatMap(c=>[c.region,...(c.possibleExternalAnchors||[]).map(a=>a.anchor),...(c.kind==='adjacent-artwork-text' ? c.objects.slice(1) : [])]));
    const c=group[0];
    const geometry=Object.fromEntries(['insets','horizontalGap','verticalGap','boxIntersection','axis','span','gaps','possibleExternalAnchors']
      .filter(key=>key in c).map(key=>[key,key==='possibleExternalAnchors'
        ? c[key].map(a=>({...a,anchor:byId.get(a.anchor).selector})) : c[key]]));
    return {candidateIds:group.map(c=>c.id), record:
      `${objects} -> candidate reference(s): ${references || '?'} | intent ?, target ?, basis ? | owner ? | discovery ${c.kind}: ${JSON.stringify(geometry)} (client rectangles, viewport CSS px); metric ?, visual view ? | unverified`};
  });
  return {status:'inventory-only', units:'viewport-css-px', viewport:{width:innerWidth,height:innerHeight,dpr:devicePixelRatio},
    root:box(root), reviewQueue, provisionalRecords,
    queueMeaning:'Pointers for local inspection, not defects. Empty queue is not coverage or acceptance.', limits,
    unhandledForeignObjects:[...root.querySelectorAll('foreignObject')].map(el=>({selector:selector(el),box:box(el),status:'needs-html-content-inventory'})),
    candidates, items};
})
