---
format_version: 1
id: PLAN-0009
status: draft
created: 2026-09-25
updated: 2026-09-25
---

# Scoville Handoff nach Skillwriter vereinfachen

## Goal

Scoville Handoff vermittelt seinen bestehenden Übergabevertrag mit eindeutigen Quellenregeln, widerspruchsfreier Vorlage und weniger wiederholten Anweisungen. Die Überarbeitung erhält alle für eine sichere Fortsetzung notwendigen Fakten und Grenzen.

## Non-goals

- Keine Änderung der expliziten Aktivierung, Leseautorität, Geheimnisredaktion, Pflichtfakten, Verlustlosigkeit auf ausdrücklichen Wunsch oder Behandlung zu kleiner Ausgabelimits.
- Keine Aufgabenfortsetzung während der Übergabe und keine Änderung gemeinsamer Suite-Verträge oder anderer Skills.
- Keine Veröffentlichung, Installation, Commits oder Umstellung des aktiven PLAN-0007.
- Keine Wirksamkeitsbehauptung allein aus kürzerem Text, Strukturvalidierung oder Review.

## Work items

### W-001 Der Übergabevertrag ist klar und ohne Bedeutungsverlust formuliert

Status: todo
Depends on: []
Blocked by: []
Decisions: []
Outcome: Einstieg, Quellenregeln und Fortsetzungsvorlage beschreiben denselben bestehenden Ablauf ohne redundante Verbote oder unklare Statuswerte.
Acceptance: Der vollständige Vergleich mit der gesicherten Ausgangsfassung erhält Aktivierung, vier Hauptabschnitte, feste Receiver-Anweisungen in ihrer Bedeutung, Pflichtfakten, Quellenzuordnung, Autorisierung, Eigentum, Geheimnisredaktion, laufende Handles, Evidenzgrenzen, begrenzte Lesewiederholung und Limitkonflikte. Gesprächsfakten benötigen keinen zusätzlichen Quellenzugriff; fehlende Information bleibt unknown und keine bekannten Vorkommnisse bleiben none known. Abgeschlossene Arbeit erzeugt keine neue Aufgabe oder unnötige Wiederholungsprüfung. Die angepassten Fallbeschreibungen decken Gespräch ohne Dateiquellen, unbekannten Status, abgeschlossene Arbeit und Arbeit ohne Git zusätzlich zu den vorhandenen Fällen ab. Ein begrenzter tatsächlicher Vergleich zwischen einfacher Aufforderung, gesicherter Vorversion und Neufassung bewertet Reparaturfälle, erhaltenes korrektes Verhalten und praktische Kosten unter gleichen Bedingungen. Die Neufassung besteht die vorab festgelegten Pflichtkriterien ohne offene Regression. Ohne die erforderlichen autorisierten Läufe bleibt W-001 offen; Quellreview und Fallbeschreibungen ersetzen diesen Nachweis nicht.
Steps:
1. Sichere vor der freigegebenen Überarbeitung die exakten Ausgangsbytes von `members/scoville-handoff/scoville-handoff/SKILL.md`, `members/scoville-handoff/scoville-handoff/assets/continuation-prompt.md`, betroffenen Testfällen und README-Quellen einschließlich uncommitteter Änderungen in der vorgesehenen temporären Ablage. Sichere ebenfalls die exakten konsumierten Ausgangsbytes aus `suite.json`, `../shared/runtime/skill_composition.md` und den durch das Manifest ausgewählten gemeinsamen README-Eingaben. Erfasse den gesamten wirksamen Anweisungssatz einschließlich uncommitteter Imports; aufgelöste Ausgangsprojektionen dürfen ihn ergänzen. Ändere diese gemeinsamen Besitzer nicht und trenne spätere fremde Inputänderungen beim Schlussvergleich von eigenen Änderungen.
2. Kürze in `members/scoville-handoff/scoville-handoff/SKILL.md` die Description auf Zweck, ausdrücklichen Übergabe-Trigger und relevante Ausschlüsse. Ersetze Dispatch-, Machine- und Ledger-Sprache durch direkte Anweisungen. Formuliere das für den gesamten Ablauf geltende Verbot der Aufgabenfortsetzung einmal zentral; erhalte die erlaubten Lesezugriffe und deren Wiederherstellungsgrenzen ausdrücklich.
3. Präzisiere in derselben `SKILL.md` die Nutzung bereits bekannter Gesprächsfakten, ohne zusätzliche Dateisuche zu erlauben. Unterscheide unknown von none known und unzutreffende optionale Felder von unbekannten relevanten Angaben. Erhalte den Ausschluss bloß zufälligen Hostzustands als Aufgabenfakt.
4. Gleiche `members/scoville-handoff/scoville-handoff/assets/continuation-prompt.md` und die Render-/Check-Regeln in `SKILL.md` ab: Git-Prüfung gilt nur bei vorhandener Versionsverwaltung, abgeschlossene Arbeit braucht nur Zustandsabgleich. Behalte vier H2-Abschnitte, feste Receiver-Bullets, Markdown-Block und bestehende Schrittstruktur bei; eine variable Schrittzahl wäre eine separate Vertragsänderung und ist hier nicht vorgesehen.
5. Korrigiere `members/scoville-handoff/development/tests/evaluation-cases.json` beim Fall not-started-transfer und ergänze dort die fehlenden Quellen-, Status- und Abschlussfälle. Erhalte sämtliche Fälle in `members/scoville-handoff/development/tests/recovery-cases.json`. Prüfe den gesamten finalen Anweisungssatz gegen die Baseline und die festgelegten Fälle, statt nur einzelne Formulierungen abzugleichen.
6. Lege gemäß Skillwriters `references/sources-and-evaluation.md` getrennte Entwicklungs- und Schlussfälle, Pflichtkriterien, Modell, Host, Effort und begrenztes Laufbudget vorab fest. Vergleiche nach entsprechender Autorisierung einfache Aufforderung, Vorversion und Neufassung auf Gespräch ohne Dateiquellen, unknown/none known, abgeschlossener Arbeit, nicht-Git-Arbeit sowie Autoritäts- und Recovery-Erhaltung. Bewerte beobachtete Ergebnisse und Kosten; beanspruche ohne vergleichbare Läufe auf beiden Zielsystemen keine modellübergreifende Verbesserung.
Evidence: [Umsetzung vom Nutzer beauftragt; kurzzeitige Warteanweisung ausdrücklich aufgehoben; aktive Planroute unverändert, Skill und Vorlage sowie Regressionfälle und README-Quellen umgesetzt; exakte Baseline vor Änderungen gesichert und final verglichen, Astra-Review in 01a0d7a3-5d5a-7213-85b3-25cd2c2017b2 mit angefordertem gpt-6-astra high fortgesetzt; letzte Referenz handoff-directory-astra-high-20260925-05 ohne Restbefund, SOL-Tests mit gpt-6-sol medium angefordert: 17 unterschiedliche Kandidatenszenarien bestanden einschließlich gezielter Retests; tatsächliche Modelltelemetrie vom Host nicht offengelegt, Echte benannte Quelldatei gelesen und vollständig übergeben; Fixture-Hashes unverändert und Taskbefehl-Sentinel fehlt; reale I/O-Fehler-Recovery nicht geprüft, 8 Vergleichsfälle mit einfacher Aufforderung und Vorversion geprüft; keine breite Überlegenheit behauptet; frühe encodingbelastete Läufe ausgeschlossen, Ausgabeumfang über 8 Vergleichsfälle: einfacher Prompt 5516 Zeichen; Vorversion 18238; Kandidat nach betroffenen Retests 14529; kein Token- oder Effizienzbeweis, Fallgruppen teilen Kontext je Vergleichsarm; einzelne Stichproben statt statistischer Aussage; keine systemübergreifende oder Luna-Release-Qualifikation]
Next action: Inhaltliche Umsetzung und beauftragtes Review samt SOL-Prüfung sind abgeschlossen. Den offenen Strukturkonflikt aus W-002 klären; native Abschlussübergänge nicht durch einen Wechsel des laufenden Workflow-Plans erzwingen.

### W-002 Dokumentation und erzeugte Pakete entsprechen dem überarbeiteten Vertrag

Status: todo
Depends on: [W-001]
Blocked by: []
Decisions: [ADR-0035]
Outcome: Kanonische README-Bausteine und daraus erzeugte Handoff-Ausgaben beschreiben den tatsächlichen Vertrag und die verbindliche Modellvoraussetzung ohne unbelegte Testbehauptungen.
Acceptance: `development/readme/scoville-handoff/compatibility-f77ff2edbfe28893.md` und alle erzeugten Handoff-README-Projektionen nennen ein Frontier-LLM aus Fable, Astra, SOL oder Opus ab Version 5.0; tatsächliche Modelltests sind davon getrennt. Skill-Creator-Prüfung und bestehende Suite-Prüfungen bestätigen Paketstruktur, aufgelöste Includes, gültige Links und aktuelle Projektionen. Bekannter Ausgangskonflikt: Skill Creators quick_validate.py lehnt das vorhandene Frontmatter-Feld compatibility ab. Solange dieser Konflikt nicht gesondert geklärt ist, bleibt die Strukturabnahme und damit W-002 offen; der Check wird als fehlgeschlagen geführt. Weder Skill Creator noch compatibility werden für einen grünen Check geändert. Eine später vereinbarte alternative Konformitätsprüfung erhält eine getrennte Aussage. Der abschließende Quellenvergleich erfasst Skill, Vorlage, geladene Fragmente und README-Bausteine; offene Verhaltensnachweise bleiben benannt. Kein Paket wird installiert oder veröffentlicht.
Steps:
1. Ergänze `development/readme/scoville-handoff/compatibility-f77ff2edbfe28893.md` gemäß ADR-0035. Gleiche `mechanism.md` und `requirements.md` im selben Verzeichnis mit W-001 ab, soweit dessen Änderungen ihre Aussagen betreffen; unterscheide Mindestanforderungen von tatsächlich ausgeführten Modelltests.
2. Erzeuge die betroffenen README- und Paketprojektionen über `development/build_suite.py` und die in `suite.json` festgelegten Quellen. Nutze für Release-Builds ausschließlich `E:/Dropbox/AI Projects/skills/temp/release/`; stimme einen Refresh mit vorhandenen Lesern ab. Prüfe die betroffenen allgemeinen und Codex-Ausgaben sowie Standalone- und Suite-Verträge anhand der bestehenden Build-Dokumentation, ohne fremde Quelländerungen als eigenen Fix auszugeben.
3. Validiere das gebaute Handoff-Paket mit Skill Creator und den vorhandenen Source-, README- und Paketprüfungen. Vergleiche den finalen Text mit der in W-001 gesicherten Baseline. Halte nur eine knappe zulässige Ergebniszusammenfassung beim kanonischen Besitzer und entferne temporäre Rohdaten erst nach abgeschlossenem Vergleich und entsprechend den Retentionsregeln.
Evidence: [Drei Handoff-Payloadvarianten general standalone und general suite sowie codex suite mit kanonischem Builder erzeugt; Includes und lokale Links geprüft, Astra bestätigte Quellen- und Projektionsgleichheit; Member-README aus kanonischen Fragmenten regeneriert; ADR-0035-Mindestanforderung enthalten, Zwei gezielte Family-Fragment-Tests bestanden; breiterer Lauf auf zwischenzeitlichen Nutzerstopp abgebrochen und nicht als bestanden gewertet, quick_validate scheitert weiterhin am bestehenden compatibility-Feld; weder Feld noch Skill Creator für einen grünen Check verändert; keine Installation oder Veröffentlichung]
Next action: Den bestehenden quick_validate-Konflikt mit compatibility gesondert klären. Strukturabnahme bleibt offen; keine erneute Handoff-Implementierung oder Wiederholung unverändert bestandener Prüfungen ohne neuen Befund.
