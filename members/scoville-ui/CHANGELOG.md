# Changelog

## 2026-11-23 - WordPress checks match the base rules

The WordPress table reported a group of controls without `<fieldset>` and `<legend>` as a defect, although the base rule also accepts a group component that carries the group's name. A requested check of translation loading now asserts one translated string from each source the page ships, PHP and each registered script handle; it asked for a React string also on a page without script.

The rule against safeguards for a use nobody described no longer lists three such uses: a second writer at the same moment, a second open window, another process on the same data. They were the scenarios of the tasks that measured the rule. The rule still says that such a use is a question for the user, named in the report, and neither a mechanism to build nor a defect to report. Its effect was measured with the list and not again without it.

The size checker names the process ID when a capture was interrupted and its cleanup is unconfirmed, as it did after a timeout. The delivery reference now says what that ID is for: resolve the state of that process before a rerun.

## 2026-11-21 - The report says when no accessibility level is recorded

The statement that no accessibility level is recorded and the work was held to the base now stands in the report section. Where it stood before, one model left it out of a review and of an implementation report. After the move it appeared in the review and was still missing from the implementation report, one run each.

Naming an edit to an existing check or test, with its reason, is now a sentence of its own. It stood at the end of the sentence that says when such a test may change, and in two runs in Codex one model made an existing test stricter without naming the edit. In two later runs on the same tasks the model edited no existing test, so the new sentence is not shown to work.

The size checker gives a complete file its final name by rename on Windows. Codex's Windows sandbox refuses hard links in the project and in a temporary folder a helper creates, so saving a complete output as a file failed there. On Windows rename refuses an existing name, as the hard link does elsewhere. Checked inside that sandbox: the file is saved, and a second file under the same name is refused.

## 2026-11-21 - Fewer unrequested demands in reviews; existing files and checks stay intact

I measured the Skill on real review and implementation cases from two of my projects, in workspaces without project rules or documentation. In reviews both models found about three more of 22 known defects with it. One model also asked for about twice as many additions nobody had requested, and the cause was the Skill: references phrased points as duties to add hints, states, confirmations and controls, and the rule for additions accepted a reference as the need.

- Reference points now say what must not fail. Removed: the reason beside a disabled action, showing back and cancel paths, saying what must come first before an action, putting rare detail behind a disclosure, the error summary. Confirmation is asked only before an effect the user cannot undo. An error about one field stands at that field. A second trigger of a running action does not repeat its effect.
- An addition needs the request, a project rule, the product record, or a rule of this Skill that an element the change adds or alters would otherwise break. A review that asks for something the change does not contain needs the same. "Optional suggestions" are no longer a report category.
- New in the part that is always loaded: Every byte outside what the complete result needs stays as it was, line endings and encoding included. To look at or test the state before a change, the agent uses a copy, such as the project copied with the change reversed or the output of `git show` saved in a temporary folder, and does not stash, reset, check out or restore files in the working tree. A project check or test that passed before the change still passes after it; it is changed or removed only where the request changes or removes the guarantee it tests, or to keep testing that guarantee another way, and the report names the edit and its reason. In my tests one model converted whole files from LF to CRLF, through `git stash` under `core.autocrlf=true` and through scripts that rewrote files, and `git diff` hid it. Another replaced an assertion of a project check to fit its own change without reporting it.
- A new component is written in the layer that holds the project's own components of that kind. A rule I give for one place or case applies there, and elsewhere only where the same reason holds. Where a change alters what a state or place I did not name shows, the report says what it shows now and asks.
- Accessibility base: where a label gets its meaning only from the question of its group, that question is the group's name. Grouping inputs in general belongs to WCAG AA. The label row of the WordPress adapter no longer covers hidden inputs and buttons.

Tested: after the change the same model asked for 18 unrequested additions in 27 reviews instead of 26–29 (13 without the Skill), and both models found two to three more known defects than without the Skill. The rule on files and checks held in one run per model on the case where both failures had happened, in a wording that has since been narrowed in scope. One model asks the question about unnamed states, the other does not. The component rule showed no effect in one run per model. Its current wording, the base addition and the reference changes made after the review measurement are not tested with models. In implementation the Skill reduces spacing deviations and unrequested additions, but neither model avoided the original defect more often with it: most of those defects could not be derived from the request and the repository alone.

## 2026-11-20 - Python is required

The bundled text-size checker now always needs Python 3.11+. The manual no-Python route and its reference file are gone: without a suitable Python the size check stops and says so, as it already did after a helper error. I removed the manual route because a host without Python is rare, an agent following a prose copy of a helper makes mistakes the program does not, and every copy was one more wording of the same rules to keep in step.

## 2026-11-20 - One clear structure

After several rounds of changes the Skill had become hard to read as a whole. This reorders it. The one rule it adds: a source review may run static checks and tests without a browser where the request permits execution.

- The table that says when to read which reference has one row per file. Geometry and the consistency audit have rows of their own.
- "Implementation" is split into three sections named for when they apply: before changing an existing element, the states of what you add, and using what exists, with custom styling under its own heading. "Integrity floor" is gone; what it added stands there.
- How to read a supplied mockup or an ambiguous word for position stands with mode and scope. The two routes for source reviews are one.
- Spacing has five steps instead of six, and the rule for literal values stands once, together with keeping the authored unit, which is now always loaded.
- One report format for all findings and audits: place, rule, observation, effect, simplest correction; confirmed apart from suspected; ordered by impact.
- Quality and Layout are one reference, "Interface structure and layout". Every reference opens by saying what it holds and when it is read.
- WordPress: bundled experimental components at the 7.0 pin stand in one file, each code example stands once, and the structured classification output is removed; I never asked for it.
- Terms are used with one meaning: audit is the mode, a read of source is a review, looking at the running interface is a rendered check; accessibility speaks of frontend and backend.

Not tested with models yet.

## 2026-11-20 - Accessibility is set per frontend and backend; translation readiness in every WordPress plugin

- Not every project needs all of WCAG AA, so the Skill no longer assumes it. A small base holds everywhere: every control works with the keyboard and shows its focus, is the element that carries its meaning, and has a label or a name. Beyond that there is one level, WCAG AA in full (version 2.1, which the laws cite, unless the project chooses 2.2), set for frontend and backend in the project's rule file: the frontend can be bound to it by law while the backend keeps the base. The Skill asks once and records the answer as one line. A review or a run without a user to ask works to the base and says that no level is recorded.
- What WCAG AA adds stands in one new reference. It is read whenever the frontend or backend being worked on is at that level, by whoever writes and whoever reviews, so both work to the same level. Where the base holds, nothing beyond it is built or reported as missing.
- Translation readiness is required for every WordPress plugin and theme, in wp-admin and elsewhere: every string a user sees or assistive technology reads goes through a translation function with the plugin's or theme's text domain. Translation files are still produced only on request.
- The addition to the rule for additions ("or that a reference describes it") is removed again; it contradicted the same sentence and showed no effect. Not tested with models yet.

## 2026-11-20 - Clearer structure

- The accessible-name rule stands once, in the wording reference: the visible text is in the name, at its start where possible. That reference also loads when a control's accessible name changes.
- The rule for literal values and the paragraph on computed sizes sit after the spacing steps they refer to; the section is now called "Spacing, size, alignment and literal values". "Implementation and acceptance" is now "Implementation". The WordPress fallback sentence moved to the WordPress spacing reference. Headings that held a single line are folded into their neighbours. Not tested with models yet.

## 2026-11-19 - Only what the task needs

These rules come from interface corrections in two of my projects: what agents built and I had removed or reworked. A first test on 37 of those cases with gpt-6.2-sol and Claude Opus 5.5 showed a small gain in reviews and fewer spacing deviations, and no gain in avoiding the original mistakes. The points on computed sizes, alignment and precedent below follow from reading why. A second test on the same cases then showed more of the original defects found in reviews (Opus 14 of 22 against 7 to 9 without the Skill, gpt-6.2-sol 10 against 6) and more of them avoided when implementing. The reviews with the Skill also asked for more additions nobody had requested; the last point answers that and is not tested yet.

- An addition to the interface needs a need: no sentence about what does not happen, no success line for a visible result, no second copy of a status, no explanation of the implementation, no step the product can do itself. Internal phases stay internal.
- A supplied mockup or example is part of the request and decides between two readings of a word for position or size.
- Before adding a rule, handler or state to an existing element, find what already acts on it, including more specific rules, global handlers and the host platform.
- For each new or conditional element, go through the values its data can take, including zero and nothing to do; where it cannot help, it is not shown. An element produced by two paths is changed in both.
- Spacing: whitespace between inline elements and the host platform's rules for an element count as sources of space.
- Wording: text is written from the user's position and claims only what the code does in that state.
- The interaction reference describes how the task's controls and states behave; it is no list of things to add.
- What the source determines, such as a size or a gap, is computed and judged instead of being left as unverified. A reference requirement is a finding where the change breaks it.
- Alignment and size follow the neighbours: texts line up on the baseline, an icon takes its size from its label's text, and the empty space inside a larger pointer target counts as spacing.
- A literal size, spacing or colour value needs a precedent on an element of the same role; that the value occurs somewhere is not enough.
- The rule for additions holds for what a review asks for as well as for what is built. That a reference describes something is not a need.
- Each rule is now written once and holds for implementing and reviewing alike. The final check points to the sections instead of listing their subjects again, and copies of a rule in SKILL.md, the references and the WordPress references are reduced to one place with links to it. Not tested with models yet.
- The shared code rules no longer end with questions that repeated them; a reviewer checks every rule in order.

## 2026-11-19 - Compatibility before release

- Shared code rules: a break in compatibility is usually wanted while a product has not been released; "during development" also described released software.

## 2026-11-18 - Each rule once

- The final check asks whether the change does what the Skill and the selected references require; the size and state rules are no longer listed a second time.
- Repeated work in lists points to rule 1 of the code rules. Page frame, messages, styling exceptions and spacing rejections stand once, in the adapter checklist or the Skill.
- Audit findings are ordered by impact everywhere. Not tested with models yet.

## 2026-11-16 - Reviewers answer two questions first

- Shared review rules: a reviewer answers the questions on reloaded values and on state across a change first, by file and line. A missing line is a finding; a comment or an argument is not such a line.

## 2026-11-16 - Holder of assigned state

- Shared code rules: the rule on assigned state names its holder, an element, list or record whose content the new path changes, also when the item the state points to stays untouched.

## 2026-11-16 - Assigned state is set again; a named bound for few items

- Shared code rules: where the old path assigned a selection, a value, the focus or a flag, the new path sets the same value after each of its steps. The author no longer has to judge whether that state can change.
- Shared code rules: a query, request, read or parse per item stays only where code, the contract or a project rule that the author names bounds the real callers to a few items.

## 2026-11-16 - Reloads inside helpers

- Shared code rules: the question about a value that is loaded again also covers loads inside the helpers the path calls.

## 2026-11-15 - Rules that contradicted each other

- An audit changes no product file. It may run the checks its evidence route allows, with disposable output.
- A correction of interface text on a `wp-admin` page also reads the internationalization reference when it changes a placeholder, plural, context or escaping.
- Sizes: a neighbour whose size comes from a one-off override is no model for a new control; match the component, variant or token the project uses deliberately.
- WordPress: the Settings API applies to a new options page and to a page that already uses it; a working hand-written `.form-table` form keeps its pattern for added fields.
- WordPress: plugin CSS that consumes Core tokens always goes through the runtime branch, and the fallback spacing rules cover an existing plugin-owned relationship as well as a new one.
- WordPress: the implementation report also contains what Scoville Code's report requires where that Skill applies.
- Shared code-review rules follow the Code changes of this date: repeated work is judged at realistic sizes, and new code written because reuse would have been quadratic or more complex is no defect.
- Shared rules: a reply uses the language of the request, while a record or file you edit keeps the language it is written in. Files saved with `--publish-full` are delivered output, so cleanup leaves them in place. A rule that holds only until something happens states that end in the rule.

## 2026-11-14 - Resolve review choices from the project

- Shared code-review rules use the request, project decisions and conventions before asking about an unresolved material choice. Routine implementation decisions stay with the author; read-only reviewers still report without editing.

## 2026-11-14 - Goodhart corrections

- A code review of interface source or of a diff reads the source and renders nothing. Rendering and measuring belong to a requested review of how an interface looks or behaves, a requested rendered check, and a reported visual defect whose cause the source does not show.
- Interactions are written as properties the code must have, not as steps to operate, so implementing no longer starts the interface.
- Sizes: compare the resulting height, font size and radius of a new control with its neighbours instead of listing variants; the report line applies to controls added beside existing ones.
- Reviews report defects and what stayed unverified; no status per passing entry and no fixed report sections.
- WordPress: remove steps that started WordPress, a browser or several releases while implementing; one rationale for a styling exception; use the plugin's existing text domain; no label or source tag on every statement.
- WordPress: move the instructions for revalidating the pinned sources out of the Skill into a development note.
- Remove examples that repeated our own test tasks.
- Shared rules: a final report after a small change no longer loads the writing reference, a test runner's console summary is not machine data, and a complete copy of a reference in context counts as read.

## 2026-11-13 - Review corrections

- When implementing, treat the interaction rules as requirements on the code. Operating a flow in a running interface, comparing computed styles and measuring contrast in the actual theme belong to a requested review, audit or check.
- WordPress: a targeted audit walks only the checklist rows of the named concern; a whole-page audit walks all.
- Describe a new control in the report as the code stands, and replace rule examples that came from our own test tasks.

## 2026-11-12 - Concrete instructions and release command

- Add a source checklist for classic WordPress plugin pages: page frame, Settings API, labels, Notices, buttons, where styles load and what they select, widths, status beyond color and translatable strings.
- Name the host mechanism to recommend for surfaces a plugin does not own, such as a Block Editor panel, a metabox or a Dashboard widget, instead of withholding advice.
- In a review, take the list of added sizes and values from the added lines of the diff, so that none is skipped. For a plugin-owned WordPress page, read the adapter before the first edit or finding.
- State each rule as a trigger, an action and a result the agent can check itself, and remove statements that reach the same reader twice.
- Remove contents lists and maintainer provenance notes from the WordPress references.
- Reword the shared writing, machine-data, shell and output-delivery rules the same way.

## 2026-11-11 - Size check for placed components and tested models

- Check the size of every component a change places, including one left at its default, against the neighbours it has to match, and report each new control with the control it copies.
- Correct a layout defect the source explains from the source. On Classic WordPress pages, write changes from the documented Core declarations and report the distance as unverified; reviews and requested checks measure it.
- Name the tested models and the minimum reasoning effort in the README.

## 2026-11-10 - Leaner instructions and Plan validator fixes

- Link the shared writing, machine-data, shell, output-delivery and Python references directly from SKILL.md, each with its reading condition, instead of chained read-first rules.
- Shorten the shared rules: drop permission disclaimers that have no recorded incident and state scope and reason for the stop rules that remain.
- Reduce output delivery to when the checker is needed, its three calls and how to read a result. Every capture failure now names its next step in the helper's `instruction` field.
- Link every UI and WordPress reference directly from SKILL.md and add contents lists to references over 100 lines.
- Add always-loaded rules for spacing, size and alignment, worked from the outside in: take sizes from the nearest existing control or row, fit reused components to their place, count each source of space once and check every added value against the project's existing ones.
- Use an existing framework component, class or token where the project has one; a hand-written copy is a defect.
- Apply these rules while writing the code without rendering every change. Reviews, audits and requested checks measure the render.
- Trigger references by kind of task and start UI work by reading them.

## 2026-10-30 - Source reading and UTF-8 diagnostics

- Clarify direct source reading and producer-owned instruction-design loading while preserving report evaluation.
- Explain retained bytes, child status and unresolved text interpretation after invalid UTF-8.
- Remove redundant layout wording without changing activation or sibling requirements.

## 2026-10-30 - Capture and diagnostic follow-up

- Support complete command capture without a numeric token limit and retain primary failure diagnostics.

## 2026-10-30 - Shared criteria and focused helper fixes

- Apply common Code quality while designing UI code and before acceptance, without requiring optional Code for the inline repair stop.
- Preserve complete command captures and describe the development cycle.

## 2026-10-29 - Repair and overflow checks

- Give unsupported repeated repairs a clear exit while retaining open findings and valid evidence.
- Compare document overflow with clientWidth; a Windows scrollbar counterexample and permitted local scrolling were exercised.
- Preserve original capture failures and distinguish needed source text from report data through the shared rules.

## 2026-10-29 - Follow-up corrections

- Load data rules before requesting output and writing rules for disputed conclusions; align consistency evidence and conditional validation routes.

## 2026-10-29

- Consolidate authority and reference routing; select source, concept, geometry,
  visual and interaction evidence by the claim while preserving scoped coverage,
  independent targets and accessibility requirements.
- Keep shared code review for UI construction and updates; consolidate WordPress
  checks and localization scope without changing platform ownership or pins.
- Load machine-data, Python and output-helper rules when their operations need them.
- Update validation evidence with the paired local browser test and its limits.

## 2026-10-28

- Use one authority order for approved product decisions and require only missing
  decisions before changes outside the authorized scope.
- Keep structured WordPress prohibition identifiers within their canonical list.
- Match translation artifacts to the selected delivery process and consolidate
  WordPress reference routing with explicit consistency-evidence links.

- Assess algorithmic costs within reachable input bounds; correct an unsupported complexity claim without demanding an unnecessary algorithm change.

- Count an unnecessary mechanism with added state, work or maintenance as a concrete review defect.

## 2026-10-27

- Require code reviews to inspect simplicity, maintainability, foreseeable extension and clarity for later agents. Trace loops, recursion and scanning calls for avoidable nonlinear repeated work without requiring benchmarks.
- Apply the same static review to UI construction, updates and the final source diff.

## 2026-10-20

- Keep required text complete when choosing how to read it. File size and metadata remain optional, and completed reads need no verification reread.
- Separate source, geometry, visual and interaction evidence. Load the geometry reference before measuring and compare selected relationships in code before display.

## 2026-10-19

- Write reports as compact lists of checked scope, results and relevant gaps. Group equivalent outcomes and refer to existing evidence instead of retelling the run.
- Apply one shared evidence rule in user and agent exchanges: defend supported conclusions, correct demonstrated errors, and respect user decisions without treating them as factual proof.

## 2026-10-18

- Reuse known results and request only the scope the next decision needs. Narrow direct tool requests before display when code preprocessing is unavailable.

## 2026-10-15

- Process complete reports in code, including saved captures and failures. Load the rules before data, preserve required original text, and keep parser errors from echoing stored state. Evaluate producer output before display, retain one-time results, and distinguish saved captures from missing output.

## 2026-10-14

- Compare nested report data in code and display only decisive results and necessary diagnostics, including structured state stored in text fields.


- Interpret actual report values through their documented meaning. Allow equivalent wording while preserving exact contracts and unresolved outcomes.
- Process machine reports through code before displaying results. Avoid redundant shared-rule reads and keep check reports focused on decisive evidence.
- Parse machine reports completely and display checked facts and all in-scope deviations. Reuse fully read shared rules across Skills without hiding required inputs.

## 2026-10-13

- Clarify WordPress ownership and version routing. Unknown runtimes require clarification, and older pins keep their tested fallback limits.
- Load detailed command capture and full-file delivery only when needed. Keep complete output, failure diagnostics and role permissions.

- Keep saved oversized results out of Git status with `.scoville/temp/.gitignore`;
  existing ignore files and tracked files stay unchanged.
- Send oversized results as a file path only; recipients read the whole file
  without hash checks. Save composed text without a separate verification pass.
- Simplify shared writing rules; command-specific size details now live in the
  shell-command rules.

## 2026-10-12

- Return complete command output directly when it fits; save only oversized
  captures. Verify supplied artifacts once and compare saved native Finals
  directly, avoiding repeated hash checks for unchanged text.

- Point the authored-unit styling contract directly to its geometry rules.

## 2026-10-11

- Put reference-routing conditions in one table while preserving progressive reads and evidence limits.

- Read required files completely with an agent-chosen method. Remove the document-reading helper and multipart protocol; keep output capture and result delivery separate.

## 2026-10-10

- Load command capture and large-result delivery only when needed; preserve complete outputs and role permissions.
- Route wording, layout, interaction, geometry, consistency audit and optional translation delivery to dedicated references while retaining applicable validation requirements.
- Keep agent messages and internal commentary compact. Reference readable source text instead of copying it; preserve required facts and exact controls.
- Keep the full reading procedure in one reference and load host command details when needed. Preserve complete reads and existing permissions.

## v2.1.14 - 2026-10-10

- Reject direct Python script capture before execution with an actionable no-start diagnostic; preserve explicit interpreter calls and source reads.

## v2.1.13 - 2026-10-10

- Save temporary read captures only when the current role and phase permit that specific file. Keep takeover and complete-reading safeguards.

## v2.1.12 - 2026-10-09

- Use exact search paths and keep filename patterns in rg's -g filters. Existing files, directories and regular expressions remain available.

## v2.1.11 - 2026-10-09

- Keep the verified Python interpreter and all required arguments when capturing a helper command. Small direct calls remain available.

## v2.1.10 - 2026-10-09

- Clarify which path runs the reader and which document it reads, including source files from another Skill.

## v2.1.9 - 2026-10-09

- Keep the verified reader and launcher unchanged between document parts or Skills, so a document change does not become a broken program path.

## v2.1.8 - 2026-10-09

- Use a complete reader command when continuing document reads, and an existing directory with a file filter when searching. Prefer direct shell commands for simple file inventories.

## v2.1.7 - 2026-10-09

- Classify a plugin page independently from its runtime. Keep unknown placement and host ownership explicit, even when the experimental runtime was selected.

## v2.1.6 - 2026-10-08

- Make UI implementation and verification sequences explicit, keeping framework, user-state and rendered-result conditions beside the action they govern.

## v2.1.5 - 2026-10-08

- Clarify the shared writing and document-reading instructions so the next action and its prerequisites are easier to identify.

## v2.1.4 - 2026-10-08

- Diagnose shortened output from the observed failing layer; a later shortened query does not prove that the original capture lost information.

## v2.1.3 - 2026-10-08

- Route WordPress admin work to its adapter before classification and keep unknown ownership from falling into the general route.
- Clarify spacing ownership and document reads while preserving the existing layout and access boundaries.

## v2.1.2 - 2026-10-08

- Read complete UTF-8 input in bounded parts and preserve command status through safe output capture. Keep the manual route available without Python.

## v2.1.1 - 2026-10-07

- Check complete text before large reads and preserve Python launcher arguments when invoking the size checker. Keep records limited to facts needed for further development.

## v2.1.0 - 2026-10-07

- Preserve complete oversized UI findings through compaction or a hashed temporary file, with the manual helper procedure available only without Python.
- Keep checks tied to the requested interface result and its actual consumers, and reuse evidence for unchanged behavior.
- Follow the applicable Codex or Claude Code project rules while preserving framework ownership and required rendered proof.

## v2.0.7 - 2026-10-02

- Check keyboard operation, focus, contrast and reflow against applicable accessibility requirements, and compare the rendered hierarchy with the main task.
- Follow the product's UI language and keep shared styling with its owner. Report measurement evidence without imposing a fixed report format.

## v2.0.6 - 2026-10-01

- Choose a visual direction from the project and user when a new interface has no existing owner. Apply shared values at the smallest owner used by related views.
- Check the rendered layout and relevant interactions against independent requirements. Keep host-owned WordPress surfaces and unverified versions outside the admin-page adapter.
- Include internal text placement in rendered component checks, including non-interactive status labels and stretched or wrapped layouts.

## v2.0.4 - 2026-09-28

- Own new interface wording and keep terminology consistent across views, states and translations.
- Derive unsettled navigation and task flow from user needs, and choose controls by their meaning.
- Reassess the affected composition and responsive behavior when interface elements change.

## v2.0.3 - 2026-09-28

- Keep pure visual concepts for a future WordPress admin page outside the implementation adapter, while retaining it for implementation advice and audits.

## v2.0.2 - 2026-09-27

- Remove the blanket network-access claim from the compatibility description.

## v2.0.1 - 2026-09-26

- Route component constraints to the visual decision owner and distinguish evidence review from a simple unverified-status boundary.
- Apply WordPress adapter routing to hypothetical implementation advice as well as execution.

## v2.0.0 - 2026-09-25

- Merge general UI and WordPress admin guidance into `scoville-ui`.
- Load WordPress rules only for relevant admin surfaces and share quality and validation rules.

## v1.2.9 - 2026-09-22

- Route supported WordPress plugin administration surfaces to
  `scoville-wordpress-ui-backend-anti-ai-slop`, the renamed specialist.

## v1.2.8 - 2026-09-20

- Clarify the WordPress specialist boundary and load UI references only for
  questions that remain open.

## v1.2.7 - 2026-09-20

- Make source-only, evidence-only, composed, and page-consistency routing
  explicit so each mode loads the references its requested judgment needs.
- Separate source inspection, runtime measurement, viewed rendering, and
  interaction evidence. Audits report source defects without repairing them.
- Clarify that discovering another family Skill does not activate it, while
  independently authorized work continues and a user opt-out applies only to
  the excluded Skill.

## v1.2.6 - 2026-09-19

- Keep framework UI implementation, accessibility mechanics, interaction, and
  rendered proof here. Visual concept work remains outside this Skill, while
  WordPress plugin-owned wp-admin pages route to their specialist.

## v1.2.2 - 2026-09-11

- Group related UI changes before source checks, measurements and visual
  inspection. Run validation after the completed batch instead of taking
  screenshots after each small edit.
- Group any corrections found during validation and recheck affected concerns
  after that correction batch is complete. Final evidence still needs to match
  the final revision, content and state.

## v1.2.0 - 2026-09-10

- Require source correction before measurement and viewed-render checks. Add a
  consistency inventory and explicit visual comparisons, with authored units,
  independent expectations and before-write custom styling justification.
- Keep framework owners and platform exceptions intact across standalone and
  composed audits.

## v1.1.3 - 2026-09-09

- Require host-provided render and interaction tools for visual proof. Source
  and build checks alone cannot establish rendered behavior.

## v1.1.0 - 2026-09-04

- Let an approved product decision own visual direction and hierarchy,
  typography, spacing judgment, and art direction.
- Keep framework implementation, component states, semantics, focus and input
  behavior, announcements, responsive mechanics, accessibility, and rendered
  proof with Scoville UI.
- Preserve the incumbent product design system above a new proposal.
- Keep a bounded Greenfield direction when no visual owner exists.
- Return an unresolved visual decision to its owner instead of silently
  redesigning the interface.

## v1.0.11 - 2026-08-11

- Made every Scoville Skill optional and independently usable. Discovering a
  sibling does not install or activate it.

## 2026-08-07 - Progressive disclosure

- Load framework diagnosis, detailed quality guidance, and rendered validation
  only when the current interface task needs them.
- Keep framework ownership, family boundaries, interface integrity, and
  reference routing in the Core.
- Require every missing requested proof, such as mobile, zoom, keyboard, touch,
  screen reader, reduced motion, or automated accessibility coverage, to remain
  visible in the conclusion.

## 2026-08-06 - Greenfield direction and representative evidence

- Require polished Greenfield work to choose a deliberate visual direction
  grounded in the product domain without prescribing a palette or template.
- Require representative populated evidence at each requested viewport, with
  realistic density, content length, hierarchy, and interaction state.
- Keep primary populated states separate from error and recovery evidence.

## 2026-08-06 - Cross-input validation

- Require a relevant cross-input handoff check when focus, selection, capture,
  composition, or shared state can change behavior between input methods.
- Do not treat separate clean-start pointer, keyboard, or touch passes as proof
  of a stateful transition.

## 2026-08-03 - Initial release

- Added framework-aware implementation and audit guidance for web, native
  mobile, desktop, and terminal interfaces.
- Added routing for design systems, headless libraries, utility frameworks,
  platform UI stacks, mixed stacks, and true Greenfield work.
- Added guidance for hierarchy, states, responsive adaptation, accessibility,
  and rendered evidence without prescribing a visual style.
