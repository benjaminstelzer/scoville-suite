# Scoville WordPress UI Backend Anti-AI-Slop

A plugin settings page can look tidy and still fight WordPress. Native controls
get rebuilt, spacing becomes inconsistent, and React is treated as proof that
the page uses the right platform components.

Scoville WordPress UI Backend implements and audits plugin-owned wp-admin
interfaces through the WordPress runtime that actually owns them. It keeps
controls, spacing, vertical flow, accessibility and translations consistent
without forcing a second UI system onto a working page.

## How it works

- Identify the supported surface and its Classic PHP, Core Components or mixed runtime.
- Reuse platform APIs, controls and spacing owners before adding custom rules.
- Batch related source corrections, measure spacing relationships, then inspect and operate the rendered page.
- Check scoped regions, smaller screens and relevant loading, error and permission states.
- Apply WordPress internationalization rules without turning an unrelated audit into a translation project.

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

- The complete contract is in [SKILL.md](https://github.com/benjaminstelzer/scoville-wordpress-ui-backend-anti-ai-slop/blob/main/scoville-wordpress-ui-backend-anti-ai-slop/SKILL.md).

## What it costs

- Inspecting spacing, responsive behavior and interactions in WordPress adds token usage and testing time.

## How it was developed

- Started as wordpress-backend-ui-skill and was integrated into Scoville Suite.
- Five varied tasks were tested with Luna Medium under SOL coordination, including a dedicated spacing case.
- Real-project findings drive further revisions. The suite owns sources and development material.

- Five simulated tasks tested routing and rule use, including spacing. The latest verification changes still need a live WordPress interface test.

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

## Sources

- [WordPress Settings API](https://developer.wordpress.org/plugins/settings/settings-api/)
  and [Administration Menus](https://developer.wordpress.org/plugins/administration-menus/)
  describe plugin-admin foundations.
- [WordPress package theming](https://developer.wordpress.org/block-editor/reference-guides/packages/packages-theme/)
  describes the theme-package boundary.
- [WordPress internationalization](https://developer.wordpress.org/plugins/internationalization/how-to-internationalize-your-plugin/)
  and [accessibility coding standards](https://developer.wordpress.org/coding-standards/wordpress-coding-standards/accessibility/)
  provide language and accessibility requirements.

## Family

- [Code](https://github.com/benjaminstelzer/scoville-code-anti-ai-slop) owns engineering scope, implementation, risk, and validation.
- [Plan](https://github.com/benjaminstelzer/scoville-plan) owns durable Plans, Work Items, Decisions, and lifecycle state.
- [Scribe](https://github.com/benjaminstelzer/scoville-scribe-anti-ai-slop) owns wording, terminology, factual meaning, and source fidelity.
- [UI](https://github.com/benjaminstelzer/scoville-ui-anti-ai-slop) owns framework-aligned implementation, interface mechanics, accessibility, and rendered evidence, with a standalone design fallback.
- [WordPress UI Backend](https://github.com/benjaminstelzer/scoville-wordpress-ui-backend-anti-ai-slop) owns plugin-owned WordPress admin interfaces, platform components, spacing, accessibility and internationalization.
- [Design](https://github.com/benjaminstelzer/scoville-design-anti-ai-slop) owns visual definition, art direction, design systems, critique, and repair.
- [Handoff](https://github.com/benjaminstelzer/scoville-handoff) transfers active work to another agent or session.
- [Research](https://github.com/benjaminstelzer/scoville-research) turns web, GitHub, and scholarly evidence into a decision-ready, claim-traceable result.
- [Brainstorm](https://github.com/benjaminstelzer/scoville-brainstorm) explores materially different mechanisms before selection.
- [Workflow Codex](https://github.com/benjaminstelzer/scoville-suite) coordinates explicit Plan execution through native Codex project tasks.

## License

MIT. See [LICENSE](LICENSE).

