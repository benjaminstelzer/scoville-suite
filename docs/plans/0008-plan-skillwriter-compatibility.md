---
format_version: 1
id: PLAN-0008
status: completed
created: 2026-09-25
updated: 2026-09-25
---

# Scoville Plan nach Skillwriter überarbeiten und Bestandskompatibilität erhalten

## Goal

Scoville Plan erhält klare, widerspruchsfreie und gezielt geladene Anweisungen nach Skillwriter. Alte format-version-1-Pläne bleiben ohne Migration lesbar und weiterbearbeitbar. Ein Skill-Upgrade darf laufende Projekte weder blockieren noch ihre fachlichen Anforderungen, Autorisierung oder fortsetzbare Arbeit verändern. Die bestehenden getrennten general- und codex-Builds bleiben erhalten.

## Non-goals

- Keine eigenmächtige Umschaltung des aktiven Suite-Plans; andere laufende Arbeiten bleiben unverändert. Veröffentlichung und Installation sind nicht beauftragt.
- Keine Formatversion, neuen Pflichtfelder, Umbenennung bestehender Felder, Änderung der Helper-Schnittstellen oder Migration vorhandener Projektakten.
- Keine Änderung von Lifecycle, unveränderlicher Historie, Opt-out, Autorisierungsgrenzen, Schreibprofil-Auswahl oder Workflow-Dispatch-Verträgen.
- Keine Umstellung der zwei Buildprofile: general behält optionale Helper und Fallbacks bei fehlendem Python; codex setzt Python 3.11+ und Pflichthelper voraus und enthält keine Python-Fallbacks. Helperfehler werden nicht zu einem manuellen Erfolg umgedeutet.
- Keine Umsetzung des bisher zurückgestellten F03-Kandidaten für natürlichsprachliches Drafting und keine Erweiterung der Schreibbefugnisse durch redaktionelle Klarstellung.
- Keine Bereinigung fremder Arbeitsbaumänderungen oder bestehender Release-Verzeichnisse. Der beobachtete CHANGELOG-Rückstand ist kein Defekt der Profiltrennung und gehört nicht zu diesem Fix.

## Work items

### W-001 Anweisungen eindeutig zuordnen und bestehende Projekte sicher fortsetzen

Status: done
Depends on: []
Blocked by: []
Decisions: [ADR-0013, ADR-0014]
Outcome: Einstieg und Referenzen vermitteln dieselben bestehenden Regeln mit eindeutigen Besitzern; alte Pläne und laufende Projekte lassen sich mit der neuen Skillfassung ohne Datenänderung zum Zweck des Upgrades fortsetzen.
Acceptance: Alle bisherigen Aktivierungsfälle und Ausschlüsse bleiben erhalten. Jede ausgelagerte Regel ist auf allen betroffenen Lese-, Schreib-, Audit- und Recovery-Routen erreichbar. Read-only-Aufträge und ein Upgrade ohne Fachoperation lassen bestehende format-version-1-Dateien bytegleich. Fortschritt gestarteter Arbeit folgt den bisherigen Live-/Lifecycle-Regeln einschließlich der vorhandenen eng begrenzten Ausnahme für explizite Execute-Annotationen unperformter Steps. Separat autorisierte todo-Planpflege darf weiterhin Outcome, Acceptance, Steps und Reihenfolge im bisherigen Rahmen ändern; ihre erlaubten Diffs werden gesondert geprüft. Bestehende IDs, nicht betroffene Anforderungen, Entscheidungen und unveränderliche Historie bleiben geschützt. Baseline und Kandidat bestehen dieselben relevanten strukturellen und Verhaltensfälle; jede neue Blockade eines zuvor gültigen Projekts ist ein Fehler und verhindert Abnahme.
Steps:
1. Sichere vor Umsetzung die tatsächlichen unveränderten Ausgangsbytes von `members/scoville-plan/scoville-plan/`, den betroffenen README-Fragmenten und importierten Schreibregeln samt Arbeitsbaumänderungen temporär. Lies `C:/Users/benja/.codex/skills/benjaminstelzer-skillwriter/SKILL.md` und `C:/Users/benja/.codex/skills/.system/skill-creator/SKILL.md`. Ermittle in `suite.json` die konkreten Quellen und Konsumenten. Halte Regelbesitzer und betroffene Routen als temporären Vergleich fest; ändere keine gemeinsamen Regeln anderer Skills.
2. Straffe `members/scoville-plan/scoville-plan/SKILL.md` auf Zweck, bestehende Aktivierungsgrenzen, gemeinsame Invarianten und vollständige Routenauswahl. Ordne Detailregeln an vorhandenen Besitzern in `references/planning-granularity.md`, `native-plan-format.md`, `native-work-items.md`, `native-decision-format.md`, `native-project-lifecycle.md`, `native-editing.md`, `read-only.md` und `profile-validation.md` zu. Bewahre routeabhängige Erreichbarkeit, Sprachwahl, Step-Scope, offene Entscheidungen, direkte Planpflege und die getrennten Buildblöcke. Kürzere Beschreibung darf keine bisherigen Anwendungsfälle entfernen oder neue automatische Aktivierung einführen.
3. Prüfe Baseline und Kandidat mit isolierten Kopien unveränderter Altakten aus `members/scoville-plan/development/tests/fixtures/`, den historischen Member-Plänen sowie dem aktuellen Suite-Profil. Decke aktive Arbeit mit `in_progress`, pausierte Arbeit mit Rückkehrbedingung, Blocker und offene Decisions, Deferred-/Prioritized-Reihenfolge, Items ohne Steps und vorhandene Route-/Execute-Annotationen ab; ergänze fehlende Zustände nur in temporären Fixtures. Führe Statusabfrage und Recovery sowie Next-action-Fortschritt, Fortsetzen, Fertigstellen, erlaubte Nachfolgeauswahl, autorisierte todo-Verfeinerung und Umordnung sowie die bestehende Execute-Ausnahme auf diesen isolierten Projektkopien aus. Prüfe die tatsächlich geschriebenen Dateien und erlaubten Diffs; eine bloße Antwortsimulation ist kein ausgeführter Fortsetzungsnachweis. Vergleiche Semantik statt Formulierungen. Reale laufende Projekte bleiben read-only.
4. Gleiche vor dem Modellvergleich die betroffenen Sollwerte in `members/scoville-plan/development/tests/evaluation-cases.json` mit ADR-0013 und den bestehenden Step-Verträgen ab: `validator-unavailable-preserves-manual-fallback`, `large-plan-progress-selective-output` und `compact-plan-is-worker-ready`. Begründe notwendige Korrekturen aus dem Vertrag, niemals aus Kandidatenausgaben. Für gerenderte general-Pakete gilt: ohne Python der vorgesehene Ersatz; mit vorhandenem Python und fehlendem oder fehlerhaftem Helper Diagnose ohne Ersatz. Für gerenderte codex-Pakete blockieren fehlende geeignete Laufzeit oder Helper die betroffene Operation. Step-Sollwerte folgen Ergebnis und Abnahmegrenze statt Dateianzahl. Führe die betroffenen bestehenden Tests unter `members/scoville-plan/development/tests/` aus und prüfe die vorhandenen Workflow-Selector-Konsumenten nur an der unveränderten Schnittstelle. Prüfe `test_routing_contract.py` auf Bindung an verschobene Wortlaute: bewahre den fachlichen Vertragsnachweis und ersetze keine fehlgeschlagene Verhaltensprüfung durch bloß gelockerte String-Suchen. Vergleiche begrenzte reale Modellfälle für neuen Auftrag, Status ohne Mutation, laufendes Projekt und direkte Planpflege mit Baseline und Kandidat unter gleichen Bedingungen. Dokumentiere tatsächliche Artefakte, Modell/Reasoning, Grenzen und Aufwand; reine Textlektüre oder Strukturtests beweisen keine Upgrade-Verträglichkeit.
Evidence: [members/scoville-plan/development/skillwriter-implementation.md, Abschluss gemäß ADR-0053 nach vorhandener Umsetzungsevidenz einschließlich geschlossener Astra-P2-Nachprüfung]

### W-002 Gültige Beispiele und inhaltlich begründete Schreibregeln liefern

Status: done
Depends on: [W-001]
Blocked by: []
Decisions: [ADR-0014]
Outcome: Beispiele können ohne widersprüchliche Lifecycle-Metadaten übernommen werden; Formulierungsregeln unterstützen verständliche neue Akten, ohne bestehende Akten nachträglich ungültig zu machen.
Acceptance: Das minimale Decision-Beispiel ist ein gültiger Vorschlag; optionale Lifecycle-Felder sind mit ihren Bedingungen getrennt erläutert. Step-Beispiele stimmen mit den geltenden Verhaltens- und Abnahmegrenzen überein. Eine feste Work-Item-Anzahl und unnötige Satzvorgaben werden durch fachliche Kriterien ersetzt; maschinenrelevante Syntax bleibt unverändert. Kein alter gültiger Plan scheitert an neuen Stilanforderungen. Die bestehende Grenze zwischen zulässiger Formulierung und erfundenem Auftrag wird nicht erweitert.
Steps:
1. Ersetze in `members/scoville-plan/scoville-plan/references/native-decision-format.md` das bewusst ungültige Mischbeispiel durch einen gültigen Minimalvorschlag und erläutere bedingte Felder separat. Richte das Beispiel in `references/native-plan-format.md` an den bestehenden Regeln für zusammenhängende Steps aus. Prüfe Beispiele mit dem bestehenden Validator in isolierten vollständigen Profilen.
2. Formuliere in `references/planning-granularity.md` kleine Anwendungen als Beispiel ohne feste Anzahl von Work Items und in `references/native-decision-format.md` knappe Abschnitte nach Informationsbedarf statt pauschaler Satzanzahl. Bewahre nichtleere Pflichtabschnitte, einzeilige Werte und andere technische Formvorgaben. Vergleiche bestehende Akten und Neuentwürfe auf identische Anforderungen und nutzbare Reihenfolge.
3. Gleiche `references/native-project-lifecycle.md` mit den geltenden Autorisierungsregeln und dem zurückgestellten F03-Status in `members/scoville-plan/development/acceptance-astra.md` ab. Stelle nur belegte bestehende Grenzen klar. Erfordert eine gewünschte Klarstellung eine neue Befugnis oder ein anderes Drafting-Verhalten, belasse den Vertrag unverändert und lege diese konkrete Änderung separat zur Entscheidung vor; sie ist keine Voraussetzung für die übrigen redaktionellen Fixes.
Evidence: [members/scoville-plan/development/skillwriter-implementation.md, Abschluss gemäß ADR-0053 nach vorhandener Umsetzungsevidenz einschließlich geschlossener Astra-P2-Nachprüfung]

### W-003 Dokumentation und beide gebauten Varianten konsistent abschließen

Status: done
Depends on: [W-001, W-002]
Blocked by: []
Decisions: [ADR-0013, ADR-0014, ADR-0035]
Outcome: Die kanonische Dokumentation und ihre erzeugten Plan-Pakete enthalten die überarbeiteten Anweisungen, zutreffende Modellvoraussetzungen und unveränderte profilabhängige Helper-Verträge.
Acceptance: Die README setzt ausdrücklich ein Frontier-LLM aus Fable, Astra, SOL oder Opus ab Version 5.0 voraus und trennt dies von tatsächlich getesteten Modellen. Beide Profile entstehen aus demselben Quellenstand. general enthält die vier bestehenden Python-Fallback-Dateien und passende Verweise; codex enthält weder diese Dateien noch entsprechende Anweisungen und setzt Python 3.11+ sowie Pflichthelper voraus. Links und Templates sind vollständig aufgelöst. Die finale Kompatibilitätsprüfung gilt für genau die gebauten Bytes; historische Evidenz wird nicht als Nachweis der neuen Fassung ausgegeben. Offene relevante Regressionen verhindern Abnahme.
Steps:
1. Ergänze ausschließlich die kanonischen betroffenen Quellen unter `development/readme/scoville-plan/`, insbesondere `compatibility-16ef3bbbbcff0431.md`, gemäß ADR-0035. Ermittle ihre Projektionen über `suite.json` und regeneriere README-Vorschauen und Paketkopien über den bestehenden Builder; pflege keine generierte Kopie separat.
2. Nutze `development/build_suite.py` und den kanonischen Builder `../shared/build/build_suite.py` für general und codex. Koordiniere vor Schreibzugriff auf `E:/Dropbox/AI Projects/skills/temp/release/` bestehende Leser und Builds; ersetze keine belegten Artefakte fremder Arbeit. Prüfe den betroffenen Plan-Payload beider Profile und die relevanten Fälle in `../shared/tests/test_distribution_profiles.py` auf Dateiauswahl, aufgelöste Anweisungen, Links und Quellenübereinstimmung. Die Buildlogik selbst bleibt unverändert.
3. Validiere die installierbaren Pakete nach Skill Creator und trenne bekannte Validatorgrenzen wie das unterstützte `compatibility`-Metadatum von echten Paketfehlern. Wiederhole nur durch weitere Änderungen betroffene Kompatibilitätsfälle aus W-001/W-002 gegen die finalen Pakete. Halte eine knappe Ergebniszusammenfassung beim Member fest; Rohdaten bleiben temporär. Bestehende Veröffentlichungsgates einschließlich Luna bleiben Voraussetzung einer später separat beauftragten Veröffentlichung und werden durch Astra-Review nicht ersetzt.
Evidence: [members/scoville-plan/development/skillwriter-implementation.md, Abschluss gemäß ADR-0053 nach vorhandener Umsetzungsevidenz einschließlich geschlossener Astra-P2-Nachprüfung]
