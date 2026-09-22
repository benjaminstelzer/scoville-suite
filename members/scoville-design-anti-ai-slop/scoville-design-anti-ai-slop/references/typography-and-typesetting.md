# Typography and typesetting

Status: `draft`  
Intervention: `external-verification`  
Sources: `SRC-TYPE-CANON`, `SRC-TYPE-SELECTION`, `SRC-TYPE-DETAIL`, `SRC-TYPE-EMPIRICAL`, `SRC-FONT-TECH`, `SRC-PACKAGE-LOCAL-SYNTHESIS`, `SRC-HEADLINE-BREAKS`

## Load when

Load when type roles, face selection or combination, Latin glyph
differentiation, hierarchy, measure, leading, paragraph rhythm, alignment,
justification, hyphenation, punctuation, numerals, microtypography, breaks, or
an expressive type exception materially affects the design. Do not load for a
font-file, coverage, shaping, fallback-metric, bidi, vertical, embedding, or
licence problem alone; that is font-technology ownership. Non-Latin work gets
only the stop/escalation floor here, not simulated native typesetting advice.

## Inputs and formal variables

Work from real text and actual fonts. Type can lead exploration: try provisional
faces and treatments before proving each choice. Use the fields below only to
resolve open decisions; consolidate retained choices and audit the final setting.

- `R`: semantic roles and reading priority - display, heading levels, body,
  navigation, action, caption, annotation, data, code/identifier, and fallback;
- `T`: exact strings, language/locale, case, numerals, punctuation, critical
  confusables, longest/shortest values, and translation variants;
- `V`: target size, distance, medium, column/viewport, scrolling or paging,
  lighting, resolution, and intended renderer;
- `F`: candidate family files, styles, weights, widths, optical sizes, axes,
  features, repertoire, metrics, fallback, licence, and delivery constraints;
- `P`: protected content, hierarchy, brand voice, layout relations, access
  floors, and intentional character;
- `E`: source, font inspection, render, print, native-reader, and human-review
  evidence, with untested states named.

Separate legibility (character recognition), readability (sustained use),
hierarchy, voice, and technical coverage. A face may succeed at one and fail at
another.

## Generate and decide

1. **Relate faces to reading roles.** Map content relationships and required
   distinctions; an exploratory face can suggest the direction. Coordinate size,
   weight, width, style, spacing, case, placement or colour to clarify adjacent
   and recurring roles; consolidate using the setting comparison below.
2. **Screen each face by job and evidence.** Inspect actual text for character
   differentiation, counters/apertures, x-height and cap height, width and
   proportion, stroke contrast/stress, terminals, texture/typographic colour,
   true italic/bold distinction, required numerals/punctuation, available
   styles/features, and target rendering. For codes, prices, dates, URLs, IDs,
   or safety-critical strings, build a target-size specimen of likely
   confusables such as `I/l/1` and `O/0`; ordinary word reading and identifier
   recognition are different tasks.
   Where a subject has its own typographic environment, inspect its documents,
   labels, signage, packaging, code, data, era or script. Compare the candidate
   with the default or incumbent: does hierarchy, reading, recognition or the
   piece's declared character gain visibly? Retain a suitable settled face;
   change it only for a supported gain within the open decision.
3. **Treat family count as an outcome.** Start with one family or superfamily
   when it covers the roles. Retain another for a visible gain in function,
   voice, contrast, density, repertoire, fallback, or production. Compare
   families by proportions, x/cap height, stroke and terminal character,
   texture, metrics, and deliberate contrast - not merely serif versus sans.
   Reject accidental near-similarity or competing voices, not variety itself.
4. **Set text as a coupled system.** Tune size, measure, leading, paragraph
   spacing/indent, alignment, columns, and line/paragraph breaking together on
   actual copy. Measure depends on face width, language, task, distance,
   scrolling/paging, column context, and leading. Compare plausible settings;
   do not pass a remembered character count or ratio automatically.
5. **Separate spacing causes.** Kerning is pair positioning; tracking changes a
   run; word spacing marks boundaries. Begin with the font's positioning, then
   inspect representative pairs, caps, small text, numerals, punctuation,
   marks, and word boundaries. Do not use tracking to rescue an unsuitable face
   or apply Latin all-cap logic to another writing system.
6. **Set paragraphs and details deliberately.** Choose leading-edge, centred,
   or justified setting by reading job, language, measure, engine, and medium.
   For justification, inspect rag/control, word and character expansion,
   dictionary/language, consecutive hyphens, rivers, and last lines. Apply the
   applicable locale or house style to quotes, apostrophes, dashes, ellipses,
   spaces, decimal/grouping signs, brackets, emphasis, and optical punctuation.
7. **Use numerals and font features by role.** Choose proportional/tabular,
   lining/oldstyle, fractions, small caps, distinct zero, and optical size only
   when the actual font supports them and the role benefits. Prefer supported
   high-level controls; never assume a feature tag, axis, or synthesised style
   works because its name is known.
8. **Compose breaks as a system.** Inspect widows, orphans, headings stranded
   from content, short final lines, column/page breaks, and reflow. Repair text
   fit, paragraph style, keep settings, measure, or geometry before inserting
   manual breaks or nonbreaking spaces. In display headings, judge phrase
   boundaries before balancing line lengths; keep meaningful groups and
   multiword names together where feasible. With unfamiliar language or script,
   keep semantic judgment unverified and use the existing escalation route.
   Default manual shaping to fixed formats; check required reflow before
   carrying those breaks into responsive output.

When font substitution can affect the delivered artifact or a requested
editable derivative, declare a controlled fallback and inspect a substitution
render. A fixed raster-only deliverable has no runtime font fallback; do not
invent that check. Escalate when metrics, features, loading, embedding, shaping,
or unfamiliar scripts become material.

## Build a setting comparison

Compare real heading, subheading, paragraph and caption together against reading
priorities. Test adjacent roles with one signal removed when useful; weight and
spacing can establish hierarchy without a size increase at every level.

For sustained text, begin with a plausible face and reading size, set the real
column, and inspect line endings and vertical texture. Compare a narrower
measure at unchanged size, then adjust leading for that measure if needed.
Keep the untouched setting beside it. Name the intended variables and allow
their dependent line-break changes; do not silently change copy to improve one
specimen. Inspect a full paragraph and its neighbours, not only a short line.

When a pairing is uncertain, compare the same heading/body in the pair and a
one-family control for role contrast, apparent size, texture and voice. Equal
nominal sizes need not look equal. These comparisons prescribe no measure,
leading range or font-pair formula; display exceptions stay with their role.

Commit the selected setting as shared source styles before extending the rough:
`role | family/style | size | leading | weight | measure | consumers`.
Include tracking, case or features only when they carry a distinction. Start
with the roles the content actually needs, often title, supporting heading,
reading text and annotation on a compact piece. These are example roles, not
a mandatory set or a cap. Data and expressive display can justify additional
roles; different roles can share a size. A scale supplies candidates, not a
requirement to use every step.

Consolidate after free exploration: inspect text voice, apparent reading size
and text/image balance in the whole at intended presentation size -> locate
competing roles, width/weight treatments or semantic breaks -> change the
smallest supported cause, or compare one controlled alternative if uncertain ->
recheck the whole.
Retain contrast, distortion and extra families for visible reading or expressive
gain; coherent variety is not a defect. Rationale cannot excuse unreadable copy.
Audit effective styles against the role map, including inheritance, transforms
and responsive states. Repeated roles share definitions; isolated variants need
a distinct job or supported exception. One size or weight may suffice when
another signal carries hierarchy; raw declaration counts prove neither quality
nor inconsistency.

Check the longest real label and a full multiline specimen with neighbours.
Derive fixed header/container height from the real line count and leading plus
intended insets. Font size, baseline, line box and visible glyph band differ;
centering an em box does not prove optical centering. For mixed-case text include
ascenders, descenders and marks, not x-height alone. A baseline grid may govern
body rhythm without forcing every display glyph or box onto it.

Two bounded teaching assets show the record in use: [role-map source](../examples/spatial-proof/type-role-map.svg)
with its [render](../examples/spatial-proof/type-role-map.png), and [optical
correction source](../examples/spatial-proof/optical-correction.svg) with its
[render](../examples/spatial-proof/optical-correction.png). They demonstrate
declared roles and a local optical adjustment; they do not prescribe sizes.

When text fails to fit, repair the common role, measure, line breaks or container
before shrinking each occurrence. Preserve exact copy and successful voice.
Typography owns the role map and visual result; use the actual renderer's font
metrics through Font Technology only when those mechanics are independently open.

## Critique: signatures and causes

| Failure signature | Likely cause to distinguish |
| --- | --- |
| Adjacent levels collide or one role has many arbitrary variants | semantic role map or shared type style is wrong, not one heading |
| Pair looks accidental or families compete | insufficient structural/voice contrast, mismatched metrics, or no distinct job |
| `I/l/1`, `O/0`, punctuation, or numerals are ambiguous | face/weight/size/fallback fails the actual recognition task |
| Uneven pairs, uniformly loose/tight runs, or blurred word boundaries | kerning, tracking, and word spacing have been conflated |
| Cramped or disconnected lines; weak paragraph rhythm | leading is mismatched to glyph extents, measure, marks, line count, or paragraph treatment |
| Rag is distracting; rivers or colour bands appear | measure, justification, hyphenation language/engine, or word-space expansion is wrong |
| Punctuation or numerals feel inconsistent or change meaning | locale/house style, glyph feature, or role-specific numeral choice is wrong |
| A widow/orphan returns after resize, translation, or font load | manual patch hides a paragraph-style, geometry, language-break, or substitution cause |
| Fallback changes wrapping, density, control size, or page count | primary/fallback metrics differ; route the technical repair rather than nudging layout |
| Tight-tracked geometric display sans with gradient fill on every heading | template scale displaced a role map; display treatment spread to ordinary reading roles |
| Eyebrow, display size or weight jump with no role change | hierarchy signal applied by habit rather than a real distinction |

Keep a repeated treatment when it consistently marks a real role. Otherwise
repair the role map and remove only redundant signals, preserving useful defaults.

Localise the observation, likely reading effect, severity, confidence, parent
owner, smallest repair, preserved strength, and regression target. Do not turn a
reviewer's stylistic preference into a defect.

## Smallest repair and preservation

Freeze `P`. Repair in causal order: wrong content/role -> unsuitable face or
combination -> shared hierarchy style -> measure/leading/paragraph system ->
alignment/hyphenation/justification -> feature/numeral/punctuation -> break
control -> local optical adjustment. Apply the change at the shared owner and
rerender all consumers. Preserve exact copy, successful voice, clear hierarchy,
layout intent, valid eccentric display work, and data alignment. Revert a repair
that improves one specimen but harms body reading, fallback, translation,
responsive fit, pagination, or production.

## Rules and exceptions

There is no universal family count, serif/sans pairing, body size, measure,
leading, modular scale, tracking value, or alignment. Numerical guidance is a
supplied constraint, a standard in exact scope, a measured observation, or a
provisional comparison value - not an unexplained quality gate. Category labels,
font popularity, similarity scores, and specimen charts do not prove fit.

Expressive distortion, extreme tightness/spacing, unusual measure, deliberate
widow, low contrast, or unconventional pairing may serve a bounded display
role. State purpose, protected reading/access floor, compensating structure,
accepted cost, and falsifier. Do not let display freedom silently govern body,
data, navigation, identifiers, or unfamiliar scripts.

## Proof, ownership, and claim ceiling

Render real `T` at intended `V`: whole hierarchy, paragraph/page context,
critical strings and applicable narrow/wide, column or substitution states. Compare
candidates or before/after with non-intervention variables held constant,
including content, size, width, renderer, colour and assets where unchanged.
Declare the intended variables and their dependent effects, such as changed
line breaks after a size repair. Inspect detail plus whole-page/sequence context.
For print, inspect target-size output and request the relevant font/preflight/
provider evidence; for web, test actual loading and applicable resize, reflow,
and text-spacing states through their owners. Mark every unrun lane unverified.

Typography owns type roles, selection/combination, hierarchy, typesetting, and
Latin microtype. Composition owns macro spatial relations; fixed media owns
page/sequence context; font technology owns files, metrics, shaping, fallback,
scripts, deployment, and font proof; UI owns framework implementation; production
owns export and supplier acceptance. Do not infer universal
readability, accessibility, native quality, licence clearance, print approval,
audience preference, or an objectively best typeface or pairing.
