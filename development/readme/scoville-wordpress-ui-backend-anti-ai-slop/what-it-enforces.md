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
