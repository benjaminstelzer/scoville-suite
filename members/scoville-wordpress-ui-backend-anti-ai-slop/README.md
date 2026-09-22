# Scoville WordPress UI Backend Anti-AI-Slop

A plugin settings page can look tidy and still fight WordPress. Native controls
get rebuilt, a second spacing scale appears, and React is treated as proof that
the page uses WPDS. None of those choices follows from the task.

Scoville WordPress UI Backend implements and audits plugin-owned `wp-admin`
interfaces through the WordPress layer that actually owns them. It covers
Classic PHP pages, Core Components and supported mixed runtimes, with explicit
rules for spacing, responsive behavior, states, accessibility and i18n.

It owns implementation and UI acceptance for those surfaces. Scoville UI does
not run a second acceptance process. Frontends, the editor canvas and extensions
inside Core screens remain outside this Skill's scope.

## Why "Scoville"?

The family is named for useful signal that remains detectable after dilution.
Here, the signal is WordPress ownership. A local layout change should not bury
it under another design system.

## How to use

Ask for the specific page and concern:

```text
Use $scoville-wordpress-ui-backend-anti-ai-slop to fix spacing on this plugin settings page. Preserve its Classic markup and keep the change within this page.
```

```text
Audit this plugin-owned wp-admin workflow for responsive behavior, accessibility and error recovery. Report findings without changing code.
```

The Skill selects Implement or Audit from the request. An audit stays read-only.
"Check and fix" permits corrections within the stated scope, not a redesign.
A design-only request does not authorize implementation.

It first checks who owns the surface and each affected runtime region.
Editor extensions, Core screens and another plugin's UI do not inherit its
plugin-page shell or spacing rules.

## Compatibility

Agent Skills host with reference access. Implementation needs the plugin's
PHP/JavaScript toolchain for WordPress 7. Rendered proof needs running wp-admin,
DOM geometry inspection and viewed images. Interactions need browser control.
Source-only or screenshot-only tasks report evidence limits. Developed for
Codex and Claude Code. Other hosts are untested.

## Install

### Install this Skill

In a local Codex or Claude Code session, ask:

```text
Install this Agent Skill for all my projects from this exact package directory:
https://github.com/benjaminstelzer/scoville-wordpress-ui-backend-anti-ai-slop/tree/main/scoville-wordpress-ui-backend-anti-ai-slop
Preserve existing customizations and ask before overwriting conflicting files.
Report the installed location and whether the host discovers the Skill.
```

The agent needs source access and permission to write to its personal Skills
location. Manual fallback: [Codex Skills guide](https://learn.chatgpt.com/docs/build-skills)
or [Claude Code Skills guide](https://code.claude.com/docs/en/skills).

Install only the linked package for the focused option.

### Install the complete Scoville suite

Get the complete suite from the
[Scoville Suite monorepo](https://github.com/benjaminstelzer/scoville-suite).
Install its released Skill packages, not development templates.

## What it enforces

- **WordPress before custom CSS.** Reuse APIs, semantic markup, Core classes,
  components and available tokens before adding a narrowly scoped rule.
- **Runtime ownership.** Classic, Core Components and experimental WPDS are
  separate paths. React alone does not choose one.
- **No forced migration.** Keep working native controls and margins.
  WordPress 7.1 token availability is not a reason to rebuild a PHP page.
- **One spacing owner.** The parent owns gaps in new plugin compositions.
  Native margins and component padding retain their existing owners.
- **Usable states.** Loading, empty, error and permission states preserve the
  task, keyboard access, focus and recovery.
- **Translation readiness.** Use WordPress i18n APIs and test text expansion.
  Translation catalogs are required only when translation delivery is in scope.
  RTL checks follow the supported or explicitly planned language scope.
- **Evidence in order.** Inspect and correct source, measure relationships,
  then view and operate the affected interface. A screenshot or build alone
  cannot prove the complete result.

The complete contract is in
[SKILL.md](scoville-wordpress-ui-backend-anti-ai-slop/SKILL.md).

## How it works

The Skill identifies the mode, surface and runtime, then loads only the
references needed for the requested concern. A spacing audit stays a spacing
audit. It does not become a translation project because the page contains PHP.

Implementation batches related corrections before measuring and viewing the
result. An ordinary page-consistency audit inventories the scoped regions,
variants and relevant states, including content below the fold. Missing
evidence remains a named gap, not a whole-page pass.

The spacing rules distinguish WordPress defaults from this Skill's own
composition rules. Existing native margins keep their owner, and a new CSS
exception needs a demonstrated gap that the platform cannot already express.

## Scoville family

Each Skill works independently. Combine only the concerns the task actually
needs:

- [Brainstorm](https://github.com/benjaminstelzer/scoville-brainstorm) explores materially different mechanisms before selection.
- [Research](https://github.com/benjaminstelzer/scoville-research) turns web, GitHub, and scholarly evidence into a decision-ready, claim-traceable result.
- [Code](https://github.com/benjaminstelzer/scoville-code-anti-ai-slop) owns engineering scope, implementation, risk, and validation.
- [Design](https://github.com/benjaminstelzer/scoville-design-anti-ai-slop) owns visual definition, art direction, design systems, critique, and repair.
- [UI](https://github.com/benjaminstelzer/scoville-ui-anti-ai-slop) owns framework-aligned implementation, interface mechanics, accessibility, and rendered evidence, with a standalone design fallback.
- [WordPress UI Backend](https://github.com/benjaminstelzer/scoville-wordpress-ui-backend-anti-ai-slop) owns plugin-owned WordPress admin interfaces, platform components, spacing, accessibility and internationalization.
- [Scribe](https://github.com/benjaminstelzer/scoville-scribe-anti-ai-slop) owns wording, terminology, factual meaning, and source fidelity.
- [Plan](https://github.com/benjaminstelzer/scoville-plan) owns durable Plans, Work Items, Decisions, and lifecycle state.
- [Handoff](https://github.com/benjaminstelzer/scoville-handoff) transfers active work to another agent or session.
- [Workflow Codex](https://github.com/benjaminstelzer/scoville-suite) coordinates explicit Plan execution through native Codex project tasks.

## Status

Five theoretical comprehension cases cover routing and rule use, including
spacing. They do not prove rendered WordPress behavior. The latest source-first
verification scheduling still needs a live WordPress interface test.

## Sources

- [WordPress Settings API](https://developer.wordpress.org/plugins/settings/settings-api/)
  and [Administration Menus](https://developer.wordpress.org/plugins/administration-menus/)
  describe plugin-admin foundations.
- [WordPress package theming](https://developer.wordpress.org/block-editor/reference-guides/packages/packages-theme/)
  describes the theme-package boundary.
- [WordPress internationalization](https://developer.wordpress.org/plugins/internationalization/how-to-internationalize-your-plugin/)
  and [accessibility coding standards](https://developer.wordpress.org/coding-standards/wordpress-coding-standards/accessibility/)
  provide language and accessibility requirements.

## Development

Maintained in the suite. Individual repositories contain generated packages.

[Source](https://github.com/benjaminstelzer/scoville-suite/tree/main/members/scoville-wordpress-ui-backend-anti-ai-slop) | [Tests](https://github.com/benjaminstelzer/scoville-suite/blob/main/development/luna-tests/wordpress-sol-results.md) | [Notes](https://github.com/benjaminstelzer/scoville-suite/blob/main/members/scoville-wordpress-ui-backend-anti-ai-slop/development/README.md)

## License

MIT. See [LICENSE](LICENSE).

