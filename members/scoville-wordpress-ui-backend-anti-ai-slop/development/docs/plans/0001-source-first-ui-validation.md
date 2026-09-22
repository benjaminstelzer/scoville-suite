---
format_version: 1
id: PLAN-0001
status: active
created: 2026-09-10
updated: 2026-09-10
current_item: W-002
---

# Fix WordPress source-first UI validation

## Goal

Require source-first validation, native owner reuse, justified CSS exceptions and measured spacing, height and alignment proof for affected plugin-owned admin UI. Separate source-backed Classic patterns from WPDS tokens and Skill-defined fallback composition so native spacing never becomes a false defect. Obtain the user-requested final Astra review at high effort before implementation, replacing Fable as explicitly requested. Align the sequence with the Scoville UI companion while retaining standalone operation.

## Non-goals

Do not edit EMPCO or other plugin installations. Skill implementation, local Skill updates and publication are now explicitly authorized after clean final reviews and required checks. Do not migrate Classic UI to React or WPDS, restyle native primitives, change WordPress version contracts, force identical native control heights, introduce a universal spacing minimum or expand a targeted check into a whole-page, translation or RTL audit.

## Work items

### W-001 Make WordPress checks mandatory in the correct order

Status: done
Depends on: []
Blocked by: []
Decisions: [ADR-0001, ADR-0002, ADR-0003]
Outcome: WordPress Backend UI independently requires source correction before actual geometry measurement and visual inspection, using the owning WordPress runtime and narrowly justified CSS exceptions.
Acceptance: Inspect SKILL.md and affected routing.md, spacing.md, responsive.md, examples.md, sources.md and version-compatibility.md for the sequence and standalone/composed consistency; run available package validation and git diff --check. Confirm separate Classic and WPDS references with context/version provenance, isolated fallback guidance, no Classic normalization target from token or Skill scales, and explicit Core/WPDS/WCAG/Skill-Norm labels at recommendations and examples. All customization requires concrete evidence; audit/source-only/i18n boundaries remain intact. Behavioral proof belongs to W-002.
Steps:
1. Inspect source and runtime evidence for each affected region: semantic markup, components and their sizing/layout props, classes, enqueued styles, selectors and parent/child spacing responsibility. Verify version-specific APIs only when the changed recommendation depends on them.
2. Correct source-visible misuse before any visual inspection: duplicate spacing owners, fallback spacing added over native rhythm, unjustified fixed dimensions, arbitrary overrides and custom CSS duplicating an available native capability. Check PHP/JS syntax and relevant existing tests/builds without equating build success with conformity.
3. Enforce the existing CSS ownership ladder before writing every custom styling exception. Record the actual API/class/component checked and why it fails; a token reference alone is not justification. Distinguish legitimate plugin composition from primitive restyling, and inspect the final CSS/inline-style diff for obsolete compensation.
4. Before the evaluated measurement, record reference elements/edges, expected relation and justified tolerance from the unchanged native owner/variant or a demonstrably suitable reference; use Skill-Norm only for an actual owner gap. Never choose tolerance after seeing results or derive expectations from candidate CSS. Unresolved expectations stay unresolved. After the source gate, measure gaps, content edges and relevant heights across peers sharing role, variant, state, typography and layout conditions; explain deliberate differences. Peer equality alone does not prove conformity when peers share a faulty override. Identify margins, padding, hidden slots, wrapping and line-height causes rather than equalizing unrelated controls.
5. Require a compact relation/state/viewport/expected-source/actual/tolerance/result record and a concrete final visual routine: inspect the region in context for grouping, then details for shared label/content edges, intended baseline/top/center alignment, apparent whitespace and line-height, control size and internal padding, icon/text alignment, wrapping, clipping, overlap and hidden-content holes. Compare equivalent peers against their native owner; record located defects or scoped passes for applicable lenses and explain exclusions. A viewed screenshot and explicit optical judgment are required even when DOM boxes match. Stable fonts and settled layout are measurement preconditions. Recheck affected narrow widths, expanded labels and visible help/error states; apply RTL only under the existing language rule.
6. Add a short worked example in a routed reference: equal outer boxes with different text positions beside a legitimate native difference. Compare at the same scale using reference edges or guides where useful; retain the unaltered crop and context. State the visual observation first, then test hypotheses against font/line-height, padding, alignment props and icon viewBox. Distinguish hypothesis from confirmed cause; unresolved optics stay unverified without invented baseline values. Do not mandate overlays or repetitive per-lens prose for every image.
7. Repeat affected source checks before renewed measurements and visual inspection after each layout correction. Explicitly report unavailable source/runtime evidence; usable available tools cannot be skipped. Audit stays read-only, reports source defects first and may then measure without repairs; missing proof never becomes a pass.
8. Replace the mixed spacing-reference presentation with separate Classic source patterns and WPDS token references, using ADR-0002 anchors as verified starting evidence. Classic entries identify selector/markup, version, authored declarations with original units/expressions, margins on both axes, padding, typography, display, specificity, media conditions and source; resolved computed values and measured geometry are separate fields with their font/root/container basis. Preserve em/rem/px/percent, unitless line-height, calculations and token references instead of substituting equal current pixel values. In particular retain Core margin 1em 0, not a new 13px rule. WPDS entries identify token, value, family, version and stylesheet/runtime without inferring a Classic relationship. Keep fallback compositions separate and reachable only after demonstrating a missing native owner; inspect native markup options before calling a relationship missing.
9. Carry the separation through routing, audit instructions, examples and version guidance. Label the Flex prop combination and gap 4/2, general one-column fallback and selected 390/600px test widths as Skill choices; bind Core 782px behavior to its actual selectors. Keep modern Page padding bound to its reverified component/package. Treat WCAG reflow and target-size criteria separately with applicable exceptions. Never import EMPCO's project-specific minimum into the reusable Skill or flag native values merely for missing a 4/8px scale.
10. Before runtime claims, inspect actual loaded/minified assets, stylesheet order and final Notice placement; file presence or enqueue registration is not proof of loading. Verify computed cascade and geometry after the source gate at relevant desktop/narrow conditions, including ordinary versus Notice paragraphs inside form-table and different mobile Notice selector paths. Keep mandatory gates in SKILL.md and mechanics in routed references; reuse compatible evidence when composed without requiring Scoville UI activation.
Evidence: [2026-09-10 canonical source gates and unit-preserving rules implemented; source inspection and package structure checks passed; behavior deferred, 2026-09-10 Fable review not performed: requested claude-fable-5-1 high returned HTTP 429 usage credits exhausted; session 9f924450-7635-4ada-a22f-3a3b37f8c306, Astra UI-FIXPLAN-ASTRA-20260910-01 conditionally approved; task 01a08bb2-d93b-74c2-93ca-57a2006e0896; requested gpt-6-astra high; actual metadata unknown; context fresh, ADR-0002 records 2026-09-10 source verification; ten local implementation files match the pinned Core bytes; rendering unverified; expansion not Astra-reviewed, Astra UI-FIXPLAN-ASTRA-20260910-02 conditional: units wording + audit acceptance + sampling; all resolved in -03, Astra UI-FIXPLAN-ASTRA-20260910-03 approved final contract; task 01a08bb2-d93b-74c2-93ca-57a2006e0896; requested gpt-6-astra high; actual metadata unknown; context continued, Final review verified authored units + read-only audit acceptance + sampling limits; source/plan review only; runtime efficacy remains unverified]


### W-003 Make page-consistency audits complete and traceable

Status: done
Depends on: [W-001]
Blocked by: []
Decisions: [ADR-0001, ADR-0002, ADR-0003]
Outcome: A request such as Pruefe Seite X gegen WordPress Backend UI und Scoville UI auf Einheitlichkeit uses the existing Audit mode with a consistency focus and an explicit coverage inventory, without requiring a new mode or special command.
Acceptance: Routing and result contracts require every in-scope region/component family/exception to map to owner-backed source, geometry and visual results or an explicit evidence gap. A complete consistency pass requires no uncovered or required-unverified entries. Native differences remain valid, source defects are reported before rendered checks, and the audit neither changes the plugin nor expands to unrelated admin pages. W-002 executes standalone/composed omission tests.
Steps:
1. Inventory the named page from source before rendered inspection: Core shell boundaries and plugin regions, headings, paragraph/label/help/status text, controls, actions, icons, groups, toolbars, data views and footer/pagination where present. Record stable targets and native runtime/variant owners. Reconcile the source inventory against final DOM after Core Notice relocation and include content below the fold and in nested scroll containers.
2. Cover relevant same-page tabs, disclosures, menus and overlays through read-only interactions. Never save settings, submit actions or create external effects for coverage. Name inaccessible permission/data states as unverified. Inventory all distinct variants and exceptions; representative sampling of repeated/virtualized rows must identify its limits and cannot imply every record was inspected.
3. For each target or justified equivalent group, record expected owner/reference and source/measurement/visual pass, defect, unverified or justified not-applicable status. Compare equivalent relations across page regions as well as within them; never normalize Classic values against WPDS tokens or fallback mappings. Report source defects first; Audit may continue with measurements without repairing them.
4. Reconcile discovered targets with completed evidence before reporting. Add newly revealed elements to the inventory; omitted entries are coverage gaps. Return a concise coverage statement and named unverified/excluded areas alongside prioritized findings. Keep consistency scope distinct from whole-page accessibility, localization production or whole-plugin review.
5. Keep this profile fully usable in WordPress Backend UI alone. With active Scoville UI, use its shared coverage/evidence mechanism once while this Skill owns WordPress comparisons and valid exceptions; do not require duplicate inventories or tests. No blanket completeness claim follows from one screenshot, a DOM count or agent self-report.
Evidence: [2026-09-10 entrypoint and reference inventory routes inspected; source/measurement/sight coverage and read-only limits implemented; behavior deferred]

### W-002 Verify standalone and composed WordPress behavior

Status: todo
Depends on: [W-001, W-003]
Blocked by: [USER-DEFERRED-TESTS]
Decisions: [ADR-0001, ADR-0002, ADR-0003]
Outcome: Real agent and browser tasks establish that WordPress checks catch the reported defects while preserving legitimate native behavior.
Acceptance: Execute matched old/revised Skill tasks with fixed WordPress/component versions, content and tools across Classic, Core Components and standalone/composed modes; require Step 3 ordering plus final source, geometry and visual evidence. Implement cases detect and correct seeded in-scope defects. Audit cases accurately locate reachable/testable seeded defects and preserve target artifacts; evaluator-established unavailable evidence/unreachable states require explicit gaps, not generic unverified for reachable defects. Preserve authored margin 1em 0 against 4px normalization and pixel/rem substitution, contextual form-table td p 4px/0 and all valid negative controls. Verify loaded assets/cascade; report untested runtimes. Composed acceptance requires the revised UI contract as external readiness, not a cross-project Work Item ID dependency.
Steps:
1. Add repository-owned regression definitions under development/tests for native spacing plus added gap, mismatched component sizing props, unnecessary control overrides, different apparent spacing despite equal tokens, text misalignment, wrapping and hidden help/error slots.
2. Add paired regressions for Core paragraph margin 1em 0 (resolved 13px only at the checked 13px font) and ordinary form-table td p margins 4px/0. Require preservation of the source declarations, not just their initial pixel output. Vary element and root font conditions independently to detect em/rem/px substitutions and fixed replacement of unitless line-height; preserve the owning expression while measuring each state. Specify markup, stylesheet order, viewport, adjacent flow and measured edges without equating margin with universal visible distance. Include Notice-paragraph exceptions, mobile Notice specificity, native button size variants, gap-xl 24px versus padding-xl 20px, tokens available on Classic without normalization, legitimate composition, source-only audit and missing runtime.
3. Run fresh isolated old/revised tasks with independently validated defects and expected answers kept by the evaluator. Give both conditions identical binding user rules without revised solution steps. Require source checks and known in-scope corrections before the first layout measurement, measurement before the first viewed rendered image, and concrete customization justification before its styling write. Source/API/stylesheet inspection is not a layout measurement. After a relevant edit repeat the affected chain; final measured and viewed evidence must share revision and state. Audit cases report source defects first and may measure without repairs. Include a post-screenshot edit and verify the equal-box optical diagnosis against its known cause while preserving the native negative control.
4. Run a composed case once the companion contract is ready and check that source and browser evidence are reused without conflicting ownership or duplicate testing. Report each case and actual tool sequence; fix failures and rerun affected cases.
5. Test the ordinary page-consistency request in standalone and composed modes with evaluator-known targets below the fold, in a collapsed same-page section, in an overlay and among repeated field labels. Require inventory/evidence coverage and located findings for reachable/testable targets; explicit unverified is reserved for evaluator-established limitations, including a truly unreachable state. Preserve target artifacts. A clean first viewport or partial sample must never yield an unqualified complete-page pass.
6. Keep raw runs and render artifacts temporary and retain only a concise maintenance summary under the workspace retention policy. Do not infer efficacy from textual scenario walkthroughs.
Evidence: [2026-09-10 user explicitly deferred extensive Skill behavior testing until later; no browser or live-agent qualification claimed]
Next action: Resume the specified regression tasks when the user requests testing; do not execute them during this implementation and release.

### W-004 Install and publish the reviewed Skills

Status: done
Depends on: [W-001, W-003]
Blocked by: []
Decisions: []
Outcome: The locally installed Skills and new GitHub releases match the reviewed canonical packages.
Acceptance: Final Astra high review has no open findings. Lightweight source and structural checks pass; behavior testing is explicitly deferred by the user and remains W-002. Verify installation file manifests, release assets, published commit, repository layout, visibility and one-current-release retention for both named repositories.
Steps:
1. Obtain the requested final Astra high review of both completed Skills and resolve findings without weakening acceptance.
2. Update the existing local Skill installations and verify exact package hashes while preserving unrelated customization.
3. Prepare coherent English README, changelog and release notes, publish new versions and verify assets before retiring older release records/tags.
Evidence: [2026-09-10 v1.2.0 published and final remote audit passed; one stable release and one annotated version tag; ZIP and checksum downloaded and byte-verified, Published commit 66b0b243f25d19a70d8514afd913714e69815be8, ZIP SHA-256 0a32864f1e81536d3b17decf84ac61fe7c940e77eac2d9135f0ce0771d8eb846, 2026-09-10 final Astra implementation review UI-SKILL-IMPLEMENTATION-ASTRA-20260910-01 approved with no actionable findings, Requested gpt-6-astra high; actual metadata unknown; context continued; reviewer archived; summary development/implementation-review.md, Codex and Claude Code local package manifests match canonical sources; behavior testing deferred]
