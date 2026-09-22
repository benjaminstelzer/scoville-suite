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
