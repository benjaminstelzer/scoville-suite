# Abschluss der bisherigen Skill-Updates

Stand: 2026-09-25. Der Nutzer beauftragt Abschluss und Driftprüfung gemäß ADR-0053. Diese Prüfung ändert Plan- und Ergebnisdokumentation, keine Skillquellen und keine Releases.

| Owner | Beobachteter Stand | Abschluss |
| --- | --- | --- |
| UI, PLAN-0006 | Astra-Abnahme, fünf Buildtests, drei Paketprüfungen und isolierter Wiederaufbau; sichtbarer SOL-High-Lauf für Greenfield und Änderung mit i18n-Vorbereitung und Tastaturbedienung | Umsetzung abgeschlossen. Der ursprüngliche kontrollierte Vergleich bleibt unausgeführt; keine Überlegenheitsbehauptung. |
| Plan, PLAN-0008 | 78 automatisierte Tests, zwei Buildprofile, SOL-Fälle, Astra-Abnahme und geschlossene P2-Nachprüfung | Umsetzung abgeschlossen; die dokumentierte ursprüngliche Modellabweichung und Grenzen der Nachtests bleiben erhalten. |
| Handoff, PLAN-0009 | Astra-Abnahme, 17 Kandidatenszenarien und acht Vergleichsfälle, drei Payloadvarianten | W-001 abgeschlossen. W-002 wegen verbliebener Validator-Teilabnahme geschlossen als cancelled; Restfrage besitzt PLAN-0011/W-007. |
| Code, PLAN-0010 | Bereits completed mit verlinkten Fixture-, Build- und Astra-Nachweisen | Kein Statuswechsel erforderlich. |
| Workflow, PLAN-0007 | Bereits completed mit Vertrags-, Paket-, nativen Modell- und Astra-Nachweisen | Kein Statuswechsel erforderlich. |
| ASK, PLAN-0002/W-001–W-002 | 17 Tests, drei Buildprojektionen, Astra-Nachabnahme, reale Claude-/SOL-/Astra-Aufrufe samt Fortsetzung | W-001 abgeschlossen. Integrationsarbeit belegt; W-002 als alte Gesamtstufe cancelled, weil Altquellenentfernung noch fehlt und bereits PLAN-0011/W-013 gehört. |

## Behobene Statusabweichungen

- UI meldete noch TEST-POLICY und verlangte einen neuen Implementierungslauf. Der spätere sichtbare SOL-Lauf führte beide Aufgaben innerhalb von 22 Minuten aus. Sein Bericht ist `development/ui-visible-sol-results.md`.
- Plan und Handoff behielten trotz tatsächlicher Ausführung draft/todo, um den damaligen aktiven Suite-Plan nicht umzuschalten. Die Dokumentation ihres Startansatzes bleibt unverändert; nur Lifecycle und Evidence werden abgeglichen.
- ASK wartete formal noch auf UI-Abschluss; seine separat beauftragte Umsetzung ist bereits nachgewiesen. Veraltete Aussagen über einen noch nicht begonnenen Ask-Umbau werden aus den offenen Release-Schritten entfernt.
- Die alten UI-Member-Verzeichnisse sind nach der angekündigten Nutzerbereinigung nicht mehr vorhanden. Der neue `members/scoville-ui` bleibt vorhanden. Ältere Berichte über die damalige Löschsperre bleiben historische Nachweise.
- Der Release-Preflight enthielt die alte Mitgliedschaft und die überholte UI-Testsperre. Er wird auf aktuelle Besitzer und begrenzte Nachweise aktualisiert.

## Bewusst offen und nicht als erledigt ausgegeben

- PLAN-0002/W-010 und W-011: Veröffentlichung der allgemeinen und der Codex-Suite samt abschließenden Releasegates. Lokale Änderungen ersetzen keine Veröffentlichung.
- PLAN-0011: neuer unabhängiger Review-Fixplan. Seine Vorschläge ADR-0047 bis ADR-0051 bleiben unentschieden; dieser Abschluss nimmt sie nicht an.
- Handoff und weitere Skills: `quick_validate.py` lehnt das vorhandene `compatibility`-Feld ab. Syntax-/Paketnachweise und dieser fehlgeschlagene Check bleiben getrennt. Die neue Reviewarbeit besitzt die grundsätzliche Klärung.
- ASK-Altquelle `../ask-suite-for-codex` besteht noch. Ihr Backup ist dokumentiert; ihre Entfernung ist kein bestandener Migrationsschritt.
- Der historische Workflow-Member-Plan trägt noch einen damaligen active-Status und offene Qualifikations-, Release- und Viewer-Punkte. Laut Member-README und Suite-AGENTS besitzt das Suite-Profil aktuelle Arbeit. Die historischen Punkte werden weder aktiviert noch als ausgeführt umetikettiert. Entsprechendes gilt für das cancelled Plan-Member-Experiment mit erhaltenen todo-Punkten. Testfixture-Pläne sind Testdaten.
- UI: keine kontrollierte Ohne-Skill-/Baseline-Wirkungsmessung, kein vollständiger WCAG-Nachweis und kein getesteter Übersetzungskatalog. Der Nutzer erklärte Übersetzungsauslieferung in der sichtbaren Testaufgabe ausdrücklich für nicht verpflichtend.

## Nachweise

- UI: `members/scoville-ui/development/merge-evidence.md` und `development/ui-visible-sol-results.md`.
- Plan: `members/scoville-plan/development/skillwriter-implementation.md` einschließlich P2-Nachtrag.
- Handoff: Evidence in PLAN-0009 mit Task-IDs und Vergleichsgrenzen.
- Code: `members/scoville-code-anti-ai-slop/development/skillwriter-fix-evidence.md` und PLAN-0010.
- Workflow: PLAN-0007 mit den jeweiligen finalen Paket- und Modellnachweisen.
- ASK: `members/scoville-ask-for-codex/development/test-evidence.md`.
