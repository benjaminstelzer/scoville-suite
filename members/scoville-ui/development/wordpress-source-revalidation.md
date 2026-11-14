# WordPress source revalidation

Maintenance of `scoville-ui/references/wordpress/`. The shipped files keep
the pins in `sources.md` as facts; an agent using the Skill does not recheck
them.

Recheck a pinned source when its condition applies:

| Source in `sources.md` | Recheck before |
| --- | --- |
| `WordPress/wordpress-develop` `7.0` | a Skill release, a new 7.x target, or drift of the branch |
| `WordPress/gutenberg` `wp/7.0` | a Skill release, a package upgrade, or a change of package stability |
| `WordPress/WordPress` tag `7.0` | relying on it for new runtime facts, or a target change |

When the WordPress target changes, recheck the supported Core release, its
built exports, token names and documentation, and the values in
`classic-patterns.md` for each newly supported version.

When a source changes, update the fact label first, then recheck each
Skill-Norm derived from it. Do not keep a stale number or experimental rule.
