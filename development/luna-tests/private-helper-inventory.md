# Private Skill-Helper: Inventar

Stand 2026-09-26. Kanonische Skills; generierte Pakete nicht doppelt gezählt. Scriptdateien sind Kandidaten, ihre dokumentierten Laufzeitaufrufe und Verbraucher werden in den Testberichten unterschieden. Imports werden über ihren tatsächlichen aufrufenden Helper geprüft.

| Skillquelle | Scripts |
| --- | --- |
| benjaminstelzer/benjaminstelzer-github-skill/benjaminstelzer-github/SKILL.md | audit_publication.py, check_repository_structure.py, verify_suite_build.py |
| benjaminstelzer/benjaminstelzer-imitate-me-skill/benjaminstelzer-imitate-me/SKILL.md | Keine eigenen Scripts |
| benjaminstelzer/benjaminstelzer-skillwriter-skill/benjaminstelzer-skillwriter/SKILL.md | Keine eigenen Scripts |
| scoville-suite/members/scoville-ask-for-codex/scoville-ask-for-codex/SKILL.md | ask.py, ask_claude.py, ask_settings.py, list_models.py, scoville_config.py, task_lifecycle.md, task_lifecycle.py |
| scoville-suite/members/scoville-code/scoville-code/SKILL.md | Keine eigenen Scripts |
| scoville-suite/members/scoville-handoff/scoville-handoff/SKILL.md | Keine eigenen Scripts |
| scoville-suite/members/scoville-plan/scoville-plan/SKILL.md | select_context.py, validate_profile.py |
| scoville-suite/members/scoville-setup/scoville-setup/SKILL.md | setup.py |
| scoville-suite/members/scoville-ui/scoville-ui/SKILL.md | Keine eigenen Scripts |
| scoville-suite/members/scoville-workflow-for-codex/scoville-workflow-for-codex/SKILL.md | build_dispatch_prompt.py, check_context_checkpoint.py, inspect_native_context.py, parse_role_result.py, resolve_model_pair.py, scoville_config.py, task_lifecycle.md, task_lifecycle.py, workflow_settings.py |

Gemeinsame Quellen: `../shared/runtime/`. Build-Tools werden durch den Paketbau und dessen Verbraucher geprüft. Die Liste belegt Inventarisierung, noch keine bestandene Abnahme.

## Tatsächliche Laufzeitpfade des finalen Kandidaten

Die obige Dateiliste umfasst auch verbliebene Quellartefakte. Für die Abnahme
zählen die dokumentierten Aufrufe im gebauten Paket:

| Skill | Dokumentierte Aufrufarten |
| --- | --- |
| Ask | ask.py resolve; Claude-Vorbereitung und Claude-Ausführung |
| Plan | validate_profile.py; select_context.py für aktuellen Punkt, Work Item, Step und zusammenhängenden Bereich |
| Setup | setup.py show und set; gespeicherte Werte gehen an Ask/Workflow |
| Workflow | resolve_model_pair.py für Executor, Reviewer und Repair; build_dispatch_prompt.py für Auftrag, Review, Reparatur, Restarbeit und Zusatzkontext; check_context_checkpoint.py für Coordinator und Workerrollen |
| GitHub | Strukturprüfung; Build-Verifikation einschließlich release; Publikationsaudit einschließlich pre-cleanup, skill-package, source-only und Familie |

task_lifecycle.py und parse_role_result.py sind keine ausgelieferten
Laufzeitabhängigkeiten. Imports werden durch ihre tatsächlichen Aufrufer
geprüft; dafür werden keine künstlichen separaten CLI-Modi erfunden.

Verbrauchermatrix: temp/2026-09-26-private-helper-tests/helper-gap-audit.md.
Der positive release-Verifier wurde inzwischen mit einem echten sauberen,
lokal committeten Testquellbaum und unverändertem Builder-Receipt ausgeführt:
release-verifier-evidence.md. Das belegt den Helper, keine Freigabe der
ungecommitteten gepflegten Suite. Live-Familien-/source-only-Audits melden
weiterhin abweichende veröffentlichte Namen und Reihenfolge; deren Änderung
gehört in den Releaseplan und wird hier nicht vorgenommen.
