---
format_version: 1
id: PLAN-0010
status: completed
created: 2026-09-25
updated: 2026-09-25
---

# Scoville Code nach Skillwriter vereinfachen

## Goal

Scoville Code führt mit klaren, widerspruchsfreien Anweisungen vom beauftragten Ergebnis über den kanonischen Besitzer zur angemessenen Prüfung. Sprachliche Vereinfachungen bewahren den bestehenden Vertrag. Änderungen am vorgeschriebenen Verhalten bleiben getrennt entscheidbar und überprüfbar.

## Non-goals

- Keine Aktivierung oder Fortschreibung anderer Pläne. Die ausdrücklich beauftragte parallele Code-Umsetzung verändert den gemeinsamen aktiven Plan nicht.
- Keine Veröffentlichung, Installation, Commits oder Änderungen anderer Skills und gemeinsamer Familienverträge.
- Keine Änderung der Aktivierungsgrenzen, Berechtigungen, Risikoklassen, 2.000-Zeilen-Konvention oder Architekturvorgaben durch bloße Umformulierung.
- Keine Wirksamkeitsbehauptung aus Textlänge, Strukturprüfung oder Astra-Review allein.

## Work items

### W-001 Der bestehende Code-Vertrag ist verständlicher und ohne Bedeutungsverlust formuliert

Status: done
Depends on: []
Blocked by: []
Decisions: [ADR-0035]
Outcome: Einstieg, Referenzen und zugehörige README-Projektionen erklären den unveränderten Code-Vertrag mit eindeutigen Begriffen und jeweils einem Besitzer pro Regel.
Acceptance: Der vollständige Vorher-nachher-Vergleich erhält Aktivierung, Modi, Risikoeinstufung, Referenzpflichten, Autorisierung, Planhoheit und Akzeptanzgrenzen. Outcome/Owner/Risk/Proof, begrenzte Quellensuche, echte Grenzennachweise und dauerhafter Zustand vor Erfolg bleiben erhalten. Skill-Creator- und Paketprüfung bestehen oder konkrete Kompatibilitätsprobleme bleiben offen. Vergleichbare Verhaltensfälle zeigen keine offene Kandidatenregression. Fehlende Pflichtnachweise verhindern die Abnahme.
Steps:
1. Sichere vor Änderungen die exakten aktuellen Bytes von `members/scoville-code-anti-ai-slop/scoville-code-anti-ai-slop/`, den laut `suite.json` verwendeten README-Fragmenten und importierten Verträgen. Nutze eine Git-Revision nur bei Bytegleichheit, sonst `Z:/Projekts/AI/temp/YYYY-MM-DD-code-skillwriter/`. Halte die knappe Zuordnung von Regelbesitzern und Erhaltungsfällen in `members/scoville-code-anti-ai-slop/development/skillwriter-fix-evidence.md` fest.
2. Vereinfache `members/scoville-code-anti-ai-slop/scoville-code-anti-ai-slop/SKILL.md`: trenne Auftragsmodus, aktuelle Handlung und konkretes Risiko sprachlich, kürze die Beschreibung auf Einsatz und Abgrenzung und fasse vorhandene Routingregeln ohne geänderte Auswahl zusammen. Verlagere Spezialfälle nur bei weiterhin verlässlichem Ladeauslöser. Erhalte insbesondere Structural/High-Override und reine Klassifikation.
3. Konsolidiere dieselben Regeln in `references/planning-and-decisions.md`, `references/change-workflow.md` und `references/validation.md` innerhalb dieses Skill-Verzeichnisses. Stelle bei jeder entfernten Wiederholung sicher, dass der verbleibende Besitzer vor der betroffenen Handlung geladen wird. Kennzeichne Architekturvorgaben als bestehende Scoville-Defaults ohne ihre Bindung oder Ausnahmen zu ändern. Bewahre die durch den Vergleich vom 12. September belegte begrenzte Ausgabe großer Quellen.
4. Ergänze im kanonischen `development/readme/scoville-code-anti-ai-slop/compatibility-4055f96f435388ed.md` die Modelluntergrenze aus ADR-0035 und trenne sie von tatsächlicher Modellevidenz. Passe nur durch die Überarbeitung betroffene README-Fragmente an. Erzeuge Vorschau und Pakete über `development/build_suite.py` nach `development/shared/build/fragments.md`, ohne parallele Leser im gemeinsamen Release-Verzeichnis zu stören.
5. Vergleiche bisheriges Paket, Kandidat und einen einfachen Zielprompt an vorab festgelegten Fällen aus `members/scoville-code-anti-ai-slop/development/tests/evaluation-cases.json` und getrennten Schlussfällen. Decke kleine Änderung, reine Planung, High-Risk-Review ohne Schreibrecht, Structural-Klassifikation, begrenzte JSONL-Ausgabe, echte Verbrauchergrenze und fehlende Prüfmöglichkeit ab. Lege Modell, Effort, Laufzahl, Kostenrahmen und verfügbare Werkzeuge vor Ausführung fest. Werte Aufgabenresultat, unerlaubte Aktionen, Vertragsverluste und praktische Kosten aus. Belege OpenAI-/Anthropic-Aussagen nur durch vergleichbare Läufe auf beiden Zielsystemen.
Evidence: [Nutzer beauftragte parallele Umsetzung am 2026-09-25 ohne Wechsel des aktiven Suite-Plans, Baseline und W-001 bestanden zehn Entscheidungsfälle pro Arm gegen einen einfachen Zielprompt, Unabhängiges Quellreview ohne Befund, Paketprüfung bestanden; bestehende Skill-Creator-Kompatibilitätslücke dokumentiert, Nachweis: members/scoville-code-anti-ai-slop/development/skillwriter-fix-evidence.md]

### W-002 Prüfstopps richten sich nach verbleibenden entscheidenden Fragen

Status: done
Depends on: [W-001]
Blocked by: []
Decisions: [ADR-0038]
Outcome: Prüfregeln erlauben einen weiteren notwendigen Nachweis bei veränderten Bedingungen oder einer benannten offenen Frage und stoppen unbegründete Wiederholungen.
Acceptance: Neue Fälle unterscheiden unveränderte Wiederholung, behobenes Infrastrukturproblem, erforderliche zweite Alternativprüfung, nachträglich veränderten Baum und vollständig nachgewiesenes Verhalten. Der Kandidat beendet nutzlose Wiederholungen und erklärt fehlende Pflichtnachweise weiterhin als offen. Der bestehende Zwei-Korrektur-Trigger zur Ursachenprüfung bleibt erhalten. Vergleich mit dem W-001-Paket isoliert diese Verhaltensänderung.
Steps:
1. Setze ADR-0038 in `members/scoville-code-anti-ai-slop/scoville-code-anti-ai-slop/references/validation.md` um: Ersetze das feste Alternativprüfungsbudget und das absolute Verbot weiterer Befehle nach der Endinspektion durch die angenommene Bedingung. Formuliere erlaubte Wiederholung nach relevanter Zustandsänderung ausdrücklich.
2. Ergänze passende Aufgaben und Erwartungen in `members/scoville-code-anti-ai-slop/development/tests/evaluation-cases.json`, prüfe erhaltene Stopps und neue Ausnahmen gegen W-001 und aktualisiere nur betroffene README-Fragmente und gebaute Projektionen. Halte beobachtete Ergebnisse und Grenzen im Evidenzbericht aus W-001 fest.
Evidence: [ADR-0038 angenommen und umgesetzt, Vergleich erlaubte notwendige Wiederaufnahme und neue Endprüfung bei erhaltenen Wiederholungsstopps, Zwei-Korrektur-Trigger im Endkandidaten erhalten, Astra-Nachprüfung ergänzt den eigenständigen Zweit-Alternativfall; Ergebnisse und Grenzen im Evidenzbericht]

### W-003 Schutzregeln unterscheiden Greenwashing von autorisierten Vertragsänderungen

Status: done
Depends on: [W-001]
Blocked by: []
Decisions: [ADR-0039]
Outcome: Code schützt weiterhin erforderliche Garantien und erlaubt die Anpassung veralteter Tests oder Validatoren ausschließlich im Rahmen einer ausdrücklich autorisierten Vertragsänderung.
Acceptance: Die Regeln verbieten das Entfernen einer weiterhin erforderlichen Assertion zum Erreichen grüner Tests und erlauben die belegte Anpassung einer überholten Assertion bei autorisierter Verhaltensänderung. Sicherheits-, Datenschutz- und Integritätsgarantien werden nicht aus einer allgemeinen Änderungsbitte als aufgehoben interpretiert. Vergleichsfälle isolieren diese Änderung gegenüber W-001 oder einem dokumentierten bereits abgenommenen W-002-Stand.
Steps:
1. Setze ADR-0039 im pauschalen Schwächungsverbot in `members/scoville-code-anti-ai-slop/scoville-code-anti-ai-slop/SKILL.md` und seiner Anwendung in `references/validation.md` um. Binde jede erlaubte Anpassung an den autorisierten neuen Vertrag und dessen weiterhin erforderliche Nachweise.
2. Ergänze positive und negative Aufgaben in `members/scoville-code-anti-ai-slop/development/tests/evaluation-cases.json`, prüfe den vollständigen zusammengesetzten Skill und baue betroffene Projektionen neu. Halte Verhaltensnachweise, Paketprüfung und verbleibende Grenzen im Evidenzbericht aus W-001 fest. Bestehende Release-Gates einschließlich ADR-0011 bleiben für eine spätere Veröffentlichung verbindlich.
Evidence: [ADR-0039 angenommen und umgesetzt, Autorisierte Vertragsänderung erlaubt bei weiterhin wirksamem Schutz gegen das Entfernen erforderlicher Guards]

### W-004 Greenfield-Konventionen sind auslagerbar und ihre Anpassung ist dokumentiert

Status: done
Depends on: [W-001]
Blocked by: []
Decisions: []
Outcome: Ausschließlich vollständig neue Greenfield-Projekte erhalten nach Prüfung aller vorhandenen Projektvorgaben offizielle Sprach- und Framework-Konventionen mit einem minimalen allgemeinen Fallback für nicht vorgegebene Entscheidungen. Projektvorgaben werden zuerst beachtet. Nutzer können diese Regeln über ausdrücklich eingebundene externe Vorgaben anpassen und finden die vollständige Anleitung in den ausgelieferten READMEs.
Acceptance: Alle neuen oder geänderten README-Texte einschließlich ihrer Release-Projektionen entsprechen Benjamins Stimme gemäß `benjaminstelzer-imitate-me`. Die Code-README erklärt den Default-Pfad, den Ladeauslöser, die Rangfolge der Vorgaben, ein konkretes AGENTS.md-Einbindungsbeispiel und das Updateverhalten. Sie unterscheidet überschreibbare Dateien im installierten Skill von einer außerhalb der Installation gepflegten Nutzerdatei. Standalone- und Suite-Ausgaben sowie die verfügbaren Buildprofile enthalten die Anleitung oder einen funktionierenden direkten Verweis darauf. Verhaltensfälle prüfen vollständiges Greenfield ohne Vorgaben, vollständiges Greenfield mit vorrangigen Projektvorgaben, explizite Nutzerkonventionen und eine nicht lesbare ausdrücklich eingebundene Datei. Negative Fälle belegen, dass ein neues Modul, ein neuer Projektbereich, ein Refactoring oder fehlende Einzelvorgaben in einem Bestandsprojekt den Greenfield-Fallback nicht aktivieren. Persönliche EMPCO-Verzeichnisregeln werden nicht als Standard übernommen. Pflichtpfade des Frameworks bleiben funktionsfähig und Bestandsprojekte werden nicht automatisch umorganisiert.
Steps:
1. Erstelle nach Umsetzungsfreigabe `members/scoville-code-anti-ai-slop/scoville-code-anti-ai-slop/references/project-conventions.md` mit offiziellen Ökosystemkonventionen für Ordner, Dateinamen, Tests und Build-Ausgaben. Verwende ausschließlich bei vollständigem Greenfield und nach Beachtung vorhandener Projektvorgaben einen minimalen Fallback mit bedarfsweise angelegten `src/`, `tests/`, `docs/` und `scripts/`. Belege die Profile mit offiziellen Quellen wie Angular Style Guide, PEP 8, WordPress PHP Coding Standards, PSR-4 und Next.js Project Structure. Behaupte keinen universellen Industriestandard.
2. Verknüpfe die Referenz in `members/scoville-code-anti-ai-slop/scoville-code-anti-ai-slop/SKILL.md` und `references/change-workflow.md`. Prüfe zuerst die geltenden Projektvorgaben und die etablierte Organisation. Lade und verwende den Greenfield-Fallback nur beim erstmaligen Aufbau eines vollständig neuen Projekts. Ein neues Verzeichnis, Modul oder Teilprojekt innerhalb eines bestehenden Projekts sowie fehlende einzelne Vorgaben reichen nicht aus. Explizite Nutzeranweisungen und Projektvorgaben gehen den Defaults vor. Eine Nutzerdatei außerhalb der Skillinstallation wird nur durch einen ausdrücklichen Pfad in globalen oder projektlokalen AGENTS.md eingebunden. Definiere den Umgang mit nicht lesbaren Vorgaben ohne stillen Ersatz. Führe keine automatische Dateisuche oder neue Konfigurationssprache ein.
3. Schreibe die README-Ergänzungen mit `benjaminstelzer-imitate-me` in Benjamins Stimme und bewahre technische Bedeutung und Anforderungen. Ergänze die Bedienungsanleitung mit einem kopierbaren Einbindungsbeispiel in `development/readme/scoville-code-anti-ai-slop/usage.md`. Prüfe anhand `suite.json`, welche Suite-README-Fragmente auf diese Anleitung verweisen müssen. Erkläre, dass direkte Änderungen im installierten Skill bei Updates ersetzt werden können, während eine außerhalb gepflegte Nutzerdatei separat erhalten bleibt. Erkläre in der README ausdrücklich die Beschränkung auf vollständiges Greenfield und den Vorrang der Projektvorgaben. Dokumentiere Namenskonventionen als stackabhängig und nenne technische Framework-Anforderungen als Grenzen der Anpassung.
4. Nimm die neue Referenz in die Code-Paketdateien von `suite.json` auf und erzeuge betroffene README-Vorschauen und Pakete über `development/build_suite.py`. Prüfe Referenzauflösung, Anleitung und Links in Standalone- und Suite-Projektionen für die jeweils unterstützten Profile. Ergänze die genannten Verhaltensfälle in `members/scoville-code-anti-ai-slop/development/tests/evaluation-cases.json` und halte tatsächliche Ergebnisse im Evidenzbericht aus W-001 fest.
Evidence: [Greenfield-Grenze und externe Konventionen in Quelle und README umgesetzt, Sechs Entscheidungsfälle und zwei getrennte Bestandsprojekt-Fixtures geprüft, Neun reale Fixture-Tests bestanden, Drei unterstützte Code-Projektionen gebaut und geprüft, README-Ergänzungen nach benjaminstelzer-imitate-me formuliert, Nach Astra-Befund externe relative Konventionen praktisch sowie Teilprojekt und Refactoring zusätzlich geprüft; Grenzen im Evidenzbericht]
