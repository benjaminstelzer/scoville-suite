---
format_version: 1
id: PLAN-0067
status: active
created: 2026-11-14
updated: 2026-11-23
current_item: W-003
---

# Goodhart-Korrekturen nach dem Opus-Review

## Goal

Die Befunde des Reviews vom 2026-11-13 (sechs Prüfer, Opus 5.5 xhigh) an den Quellen beheben: Regeln, bei denen der Prozess zum Ziel wird, missverständliche Sätze, Widersprüche und Beispiele, die aus Messaufgaben stammen. Owner sind members/ und ../shared/. Schutzregeln, Helper- und Datenformatverträge bleiben erhalten. Die Aussagen des Berichts zu PLAN-0066 über die zweite Messreihe werden richtiggestellt. Ergebnisse stehen im [Bericht](../testing/0067-goodhart-korrekturen-nach-dem-opus-review.md).

Oberstes Qualitätsziel nach Nutzerpräzisierung vom 2026-11-15: Die Skills sollen wartungsfreundlichen, gut verständlichen und klar gekapselten Code ohne unnötige Komplexität hervorbringen. Verantwortlichkeiten und Schnittstellen müssen klar sein. Der notwendige Änderungsumfang folgt diesem Ziel und dem vollständigen fachlichen Vertrag, einschließlich der Laufzeit- und Zustandsgarantien; die Zahl geänderter Zeilen ist kein Qualitätsmaß. Die Auswertung beurteilt diese Eigenschaften am entstandenen Code neben Funktion und Skalierung. Bestehende Funktionen und das Verhalten der Anwendung bleiben erhalten, außer soweit der Nutzer eine Änderung beauftragt. Wartbarkeit, Einfachheit und Laufzeit rechtfertigen weder das Entfernen von Funktionen noch das Abschwächen erforderlicher Garantien (ausdrückliche Nutzerkorrektur vom 2026-11-15).

Nutzerauftrag vom 2026-11-15: Alle Skills werden parallel von unabhängigen Agenten auf ihren vollständigen Aufbau geprüft. Der jeweilige Ablauf soll schlüssig sein: Voraussetzungen vor Aktionen, eindeutige Zuständigkeiten, vollständige Kernpflichten und konsistente Bedingungen in Text und Diagrammen. Bestehendes Verhalten, Funktionen und echte Aktionsgrenzen bleiben erhalten. Die zwölf Strukturantworten und ihre Einordnung stehen im Bericht; die Überarbeitung wird als eigener Kandidat geprüft.

Lokale Commits sind freigegeben. Pushs einschließlich privater CI, Exporte in öffentliche Repositories und lokale Installation brauchen jeweils eine ausdrückliche Freigabe.

## Non-goals

- Keine Aussage über Modellwirkung ohne Messung an Aufgaben, deren Ersteller weder die Skills noch die bisherigen Aufgaben kannte.
- Keine zusätzliche Prüf-, Listen- oder Berichtspflicht in jeder Skill-Ausführung; die Freigabeprüfung einer Skill-Änderung folgt ADR-0236.
- Keine Änderung an Helper-Logik, Feldnamen oder Ausgabeformaten.

## Work items

### W-001 Befunde an den Quellen beheben

Status: done
Depends on: []
Blocked by: []
Decisions: [ADR-0232, ADR-0233, ADR-0234]
Outcome: Die bestätigten Befunde sind in den Skilltexten, Referenzen, gemeinsamen Regeln und Prompttexten der Helfer behoben; offen gelassene Befunde stehen mit Grund im Bericht.
Acceptance: Jeder Befund der sechs Prüfberichte ist im Bericht als behoben, verworfen oder offen geführt. Die drei Entscheidungen sind in Plan, UI und Workflow umgesetzt. Kein Beispiel der Skilltexte wiederholt Szenario oder Werte einer Messaufgabe. Der Bericht zu PLAN-0066 nennt die Grenzen der zweiten Messreihe. `python development/check_all.py` besteht.
Instructions: []
Steps:
1. [status: done] Korrekturen je Skill-Gruppe an members/ und ../shared/ ausführen und jede Änderung am Diff prüfen; fertig, wenn jeder Befund eine Einordnung hat.
2. [status: done] Tests an geänderte Formulierungen anpassen, Snapshot synchronisieren und die Gesamtprüfung ausführen; fertig bei bestandener Gesamtprüfung.
3. [status: done] Bericht unter docs/testing schreiben und den Bericht zu PLAN-0066 richtigstellen; fertig, wenn beide Berichte die Grenzen der Messung nennen.
Evidence: check_all 12/12; Suche nach 18 entfernten Beispielen ohne Treffer; Bericht führt jeden Befund; offen: 12 Befunde für den Eigentümer; keine Modellläufe.

### W-002 Ausliefern nach Freigabe

Status: done
Depends on: [W-001]
Blocked by: []
Decisions: []
Outcome: Der korrigierte Stand ist in den Ziel-Repositories veröffentlicht und lokal installiert.
Acceptance: Die private Laufzeit-CI hat für die geänderten Python-Helfer bestanden. `release_suite.py publish` meldet alle Ziele als geprüft. Die installierten Skills entsprechen dem veröffentlichten Stand.
Instructions: Push der privaten CI, Veröffentlichung und lokale Installation brauchen je eine eigene Freigabe des Nutzers.
Steps:
1. [status: done] Nach Freigabe die Laufzeit-CI pushen und ihr Ergebnis abwarten; fertig bei sechs bestandenen Jobs.
2. [status: done] Nach Freigabe mit release_suite.py vorbereiten und veröffentlichen; fertig, wenn published.json alle Ziele als geprüft führt.
3. [status: done] Nach Freigabe die installierten Skills aktualisieren; fertig, wenn sie dem Auslieferungsstand entsprechen.
Evidence: CI-Run 44552459961: 6/6 Jobs bestanden. publish von a0ef17c: acht Ziele remote=verified, Suite 2010941, Codex-Suite 2a4f856. Installiert für Claude und Codex am 2026-11-19.

### W-003 Offene Befunde entscheiden und Skills erneut prüfen

Status: paused
Depends on: [W-001]
Blocked by: []
Decisions: [ADR-0235, ADR-0236]
Outcome: Die offenen Befunde sind nach den Entscheidungen des Eigentümers umgesetzt, und eine zweite vollständige Prüfung der Skills hat keinen unbehandelten Mangel hinterlassen.
Acceptance: Jede Entscheidung aus ADR-0235 steht an der zuständigen Quelle. Jeder Befund der zweiten Prüfung ist behoben, begründet verworfen oder dem Eigentümer vorgelegt. Die Gesamtprüfung der Suite besteht.
Instructions: Die zweite Prüfung läuft mit Opus 5.5 und Reasoning-Aufwand xhigh, nur lesend. Push, Veröffentlichung und Installation brauchen je eine eigene Freigabe des Nutzers.
Steps:
1. [status: done] Entscheidungen an members/ und ../shared/ umsetzen; fertig bei bestandener Gesamtprüfung.
2. [status: done] Alle Skills von Opus 5.5 xhigh prüfen lassen; fertig, wenn jeder Bericht vorliegt.
3. [status: in_progress] Befunde beheben und jede Änderung am Diff prüfen; fertig, wenn jeder Befund eine Einordnung hat und die Gesamtprüfung besteht.
Evidence: ADR-0236 an Quellen umgesetzt; check_all 12/12. Keine neuen Modellläufe; übriger Zweitbefundabgleich und Entscheidungen offen, siehe Bericht zu PLAN-0067.

### W-004 Modellwirkung des korrigierten Stands vergleichen

Status: done
Depends on: [W-001]
Blocked by: []
Decisions: [ADR-0236, ADR-0237, ADR-0238, ADR-0239]
Outcome: Ein kontrollierter Vergleich zeigt für Sol und Opus die Ergebnisse des neuen Skill-Stands gegenüber keinen Skills, einschließlich einzelner Verschlechterungen.
Acceptance: Vergleichbare gültige Läufe decken bekannte Diagnosefälle und unabhängige Aufgaben ab. Exakte Versionen, tatsächliche Skill-Ladevorgänge, Ausführungsstatus und Ergebnisse sind getrennt belegt. Einzelne Verschlechterungen sind anhand von Artefakten geprüft; Grenzen und noch offene Vergleiche stehen im Bericht.
Instructions: Vom Nutzer am 2026-11-14 beauftragt und präzisiert: nur neue Skills gegen keine Skills; zuerst gpt-6.1-sol, danach Claude Opus 5.5 nach Freigabe des Fünf-Stunden-Limits, beide medium. Keine Veröffentlichung oder Installation; Skilltexte während des Vergleichs unverändert lassen.
Steps:
1. [status: done] Vergleichsstände einfrieren, unabhängige Aufgaben mit geprüften Bewertern erstellen und Sol in isolierten Arbeitsverzeichnissen ausführen; fertig bei ausgewerteten gültigen Vergleichsläufen.
2. [status: done] Nach Ablauf des Opus-Limits dieselben Aufgaben und Stände mit Opus ausführen; fertig bei ausgewerteten gültigen Vergleichsläufen.
3. [status: done] Verschlechterungen einzeln prüfen und Ergebnisse sowie Grenzen im Bericht zu PLAN-0067 festhalten; fertig bei nachvollziehbarer Bewertung je Modell und Aufgabenart.
Evidence: 48 gültige Aufgabenläufe. Opus N1: Datenerhalt mit Skills 1/2, ohne 2/2. Unabhängige Aufgaben überall bestanden; mehr Aufwand mit Skills. Einzelbefunde und Grenzen im Bericht; Korrekturen in W-005.

### W-005 Belegte Schwächen der Skills beheben und erneut messen

Status: done
Depends on: [W-004]
Blocked by: []
Decisions: [ADR-0236, ADR-0237, ADR-0238, ADR-0239]
Outcome: Die im Vergleich belegten Skill-Schwächen sind an ihren verantwortlichen Quellen behoben und die Wirkung der Korrekturen ist überprüft.
Acceptance: Belegte Mängel aus W-004 sind anhand ihrer beobachteten Ursachen geprüft und an der zuständigen Quelle behandelt. Die erforderlichen technischen Prüfungen bestehen. Vergleichsläufe mit beiden Modellen gegen keine Skills prüfen betroffene Diagnosefälle und unabhängige Änderungen an bestehenden Codebasen. Funktion, Bestandsschutz, vermeidbare Komplexität, Laufzeit und Tokens werden bewertet. Ein funktional richtiger quadratischer Gegenentwurf scheitert an der Skalierungsprüfung. Der Kandidat bietet einen belegten Gesamtkompromiss aus zuverlässigem Verhalten, einfacher Umsetzung und vertretbarem Aufwand. Einzelabweichungen und Unsicherheiten sind dokumentiert. Bestätigte schwere oder reproduzierbare Regressionen sind bearbeitet.
Instructions: Nach Nutzerentscheidung vom 2026-11-18 auf die Gesamtwirkung in beiden Modellen achten. Routinen mit nachgewiesen gleichwertigen Ergebnissen kürzen, den Schutz vor unnötiger und quadratischer Gesamtarbeit erhalten und Einzelprobleme im Verhältnis zu Qualität, Zeit und Tokens gewichten. Bei konkreten Problemen Opus 5.5 und Sol auf high beratend einbeziehen und ihre Vorschläge abgleichen. Astra 6.2 auf high prüft verbleibende Unklarheiten im Gesamtaufbau und hilft bei festgefahrenen Problemen. Neue Vergleiche verwenden gpt-6.2-sol und Claude Opus 5.5 auf medium. Frühere Modellversionen und Beratungen mit high getrennt ausweisen. Der Hauptagent bearbeitet die Quellen ohne Skills. Korrigierte Skills gegen keine Skills prüfen. Gültige Kontrollen bei identischer Modellversion, Aufgabe, Prüfung und relevanten Ausführungsbedingungen wiederverwenden. Kleine Fälle prüfen gezielte Regressionen. Bestehende Projekte nur in isolierten Kopien verwenden. Lokale Commits sind erlaubt. Pushs, Veröffentlichung und Installation erfordern eine eigene Freigabe.
Steps:
1. [status: done] Befunde aus W-004 an members/ und ../shared/ auf ihre Ursachen zurückführen und an den zuständigen Quellen wartbar korrigieren; fertig bei geprüftem Quellen-Diff und bestandenen betroffenen technischen Prüfungen.
2. [status: done] Korrigierte Pakete einfrieren und betroffene Diagnosefälle sowie frische unabhängige Änderungen in einer größeren realen Codebasis mit gpt-6.2-sol und Claude Opus 5.5 jeweils auf medium gegen keine Skills messen. Fertig bei getrennt geprüfter Funktion und Skalierung sowie eingeordneten Einzelverlusten.
3. [status: done] Bericht und Plan mit tatsächlichen Ergebnissen, Aufwand und verbleibenden Grenzen aktualisieren, Aufgaben und Rohbelege mit Review-Einstieg dauerhaft für Opus 5.5 sichern und die geprüften Quellen lokal committen; fertig bei gültigem Profil und nachvollziehbarem Ergebnis.
Evidence: Review 18 realer Mängel: mit Skill Sol 12, Opus 16, ohne je 10. Neue Anwendung: ab 277a457 Sol und Opus ohne Mehrfenster-Schutz; ab e599bcf meldet Opus Schreibfehler wieder. Bericht.

### W-006 UI-Skill an realen Korrekturläufen ausrichten und messen

Status: done
Depends on: [W-005]
Blocked by: []
Decisions: [ADR-0240]
Outcome: Der UI-Skill verhindert die UI-Fehler, die in zwei realen Projekten nachträglich korrigiert werden mussten, und seine Wirkung ist mit beiden Modellen gemessen.
Acceptance: Die Fehlerklassen aus den Korrekturläufen beider Projekte stehen im Bericht. Jede Regeländerung nennt den Mechanismus und steht einmal. Review- und Umsetzungsfälle aus den Projekten sind mit gpt-6.2-sol und Claude Opus 5.5 auf medium mit und ohne Skill gelaufen und blind bewertet. Wirkungslose Regeln sind gestrichen. Die Gesamtprüfung besteht.
Instructions: Nutzerauftrag vom 2026-11-19: gleiches Vorgehen wie beim Code-Skill. Produktprojekte nur lesend verwenden; keine Projektbeispiele im Skilltext. Lokale Commits sind erlaubt; Push und Installation brauchen je eine eigene Freigabe.
Steps:
1. [status: done] UI-Korrekturläufe in beiden Projekten auswerten und nach Mechanismus ordnen; fertig bei Fallliste mit einführendem und korrigierendem Commit.
2. [status: done] Fehlende Regeln an members/scoville-ui schreiben; fertig bei bestandener Gesamtprüfung.
3. [status: done] Review- und Umsetzungsfälle isolieren und mit beiden Modellen mit und ohne Skill ausführen; fertig bei gültigen Läufen und blinder Bewertung.
4. [status: done] Ergebnisse und Grenzen im Bericht festhalten, Wirkungsloses streichen und den Stand lokal committen; fertig bei gültigem Profil.
5. [status: done] Ohne Projektdokumentation neu messen, die Ursache von Sols unverlangten Review-Forderungen beheben und nachmessen; fertig bei gültigen Läufen, Bewertung und Bericht.
6. [status: done] Gezielte Tests, Fixplan mit zwei Prüfern und externer Prüfung umsetzen und am auslösenden Fall kontrollieren; fertig bei bestandener Gesamtprüfung und Bericht.
Evidence: Review ohne Doku: Treffer mit Skill +2 bis 3, Sols Unverlangtes 26–29 auf 18 (ohne 13). Kontrolle i10 mit 8b66460: kein Stash, Prüfung unverändert. check_all 12/12. Bericht W-006.

### W-007 Plan schlank und funktional machen; Python als Voraussetzung

Status: done
Depends on: [W-006]
Blocked by: []
Decisions: [ADR-0240, ADR-0241]
Outcome: Kein Skill der Suite enthält einen Ersatzweg ohne Python. Der Plan-Skill beschreibt seine Struktur einmal, ist auf den Alltag gekürzt und löst die Alltagsaufgaben mit beiden Modellen nicht schlechter als zuvor.
Acceptance: Ersatzdateien, ihre Paketeinträge und ihr Build-Code sind entfernt. Der Plan-Skill enthält keine Regeln für abgeschaffte Formate; seltene Abläufe stehen in einer nur auf Wunsch geladenen Referenz. Die Ausgabe von select_context.py erklärt sich selbst bei unveränderten Feldnamen; Workflow arbeitet damit unverändert. Ein Modellvergleich der Alltagsaufgaben mit gpt-6.2-sol und Claude Opus 5.5 auf medium zeigt keine Verschlechterung. Die Gesamtprüfung besteht.
Instructions: Nutzerauftrag vom 2026-11-20. Feldnamen und Aufbau der Skriptausgaben bleiben. Tests ohne die Projektregeln der Originalprojekte. Lokale Commits sind erlaubt; Push und Installation brauchen je eine eigene Freigabe; vor einem Push mit geändertem Python die Laufzeitprüfung.
Steps:
1. [status: done] Ersatzdateien in der ganzen Suite entfernen und Python als Voraussetzung festschreiben; fertig bei bestandener Gesamtprüfung.
2. [status: done] Aufbau des Plan-Skills unabhängig prüfen lassen und den Zielaufbau mit dem Nutzer abstimmen; fertig bei bestätigtem Zielaufbau.
3. [status: done] Plan-Skill kürzen und ordnen, Altformate streichen, Erklärungen in die Skripte verlagern; fertig bei bestandener Gesamtprüfung und bestandenen Skripttests mit Workflow.
4. [status: done] Alltagsaufgaben mit beiden Modellen gegen die vorige Fassung messen; fertig bei gültigen Läufen, Bewertung und Bericht.
Evidence: check_all 12/12. Plan 13.350 auf 5.670 Wörter. 40 Läufe alt/neu: erledigt Opus 9 gegen 8, Sol 10 gegen 7 von 10; kein Test gebrochen. Bericht W-007.

### W-008 Stand vom 2026-11-21 ausliefern

Status: done
Depends on: [W-006, W-007]
Blocked by: []
Decisions: []
Outcome: Der Stand nach den Korrekturen an UI, Plan, Handoff und den gemeinsamen Code-Regeln ist lokal installiert und nach Freigabe veröffentlicht.
Acceptance: Die private Laufzeit-CI hat für den Stand bestanden. Die installierten Skills entsprechen dem gebauten Stand. Nach Freigabe meldet `release_suite.py publish` alle Ziele als geprüft.
Instructions: Freigabe des Nutzers vom 2026-11-20 für den Push der privaten CI und die lokale Installation. Die Veröffentlichung braucht eine eigene Freigabe und vorher Changelog-Einträge in jeder geänderten Distribution. Das Quell-Repository hat keinen privaten Remote; sein origin ist das öffentliche Ziel und wird nie direkt gepusht.
Steps:
1. [status: done] Laufzeit-Snapshot in die private CI pushen und ihr Ergebnis abwarten; fertig bei sechs bestandenen Jobs.
2. [status: done] Pakete mit dem CI-Nachweis bauen und in die vorhandenen Installationsordner spiegeln; fertig, wenn sie dem Build gleichen.
3. [status: done] Nach Freigabe Changelog-Einträge schreiben, mit release_suite.py vorbereiten und veröffentlichen; fertig, wenn published.json alle Ziele als geprüft führt.
Evidence: CI-Run 44836940153: 6/6 Jobs. publish von dec276f am 2026-11-21: acht Ziele remote=verified, Suite 6a9637f, Codex-Suite d231397. Installiert in .claude, .codex, .agents; gleich dem Build.

### W-009 Installierte Codex-Skills über die CLI prüfen und korrigieren

Status: done
Depends on: [W-008]
Blocked by: []
Decisions: []
Outcome: Die installierten Codex-Skills sind mit gpt-6.2-sol über die Codex-CLI geprüft, und die dabei belegten Fehler sind an den Quellen behoben.
Acceptance: Fünf Aufgaben, eine Ask-Review und ein Workflow-Lauf sind unabhängig ausgewertet. Jede Korrektur nennt ihren Anlass. Die Suite-Prüfung und die private Laufzeit-CI bestehen für den korrigierten Stand.
Instructions: []
Steps:
1. [status: done] Die mitgelieferten Standardmodelle auf gpt-6.2 anheben und ausliefern; fertig, wenn die installierten Vorgaben gpt-6.2-sol und gpt-6.2-astra nennen.
2. [status: done] Fünf Aufgaben, eine Ask-Review und einen Workflow-Lauf als frische Sitzungen fahren und auswerten; fertig, wenn je Lauf Bytes, Git-Spuren, Tests, Profil und Skill-Zugriffe vorliegen.
3. [status: done] Belegte Fehler beheben und mit Kontrollläufen prüfen; fertig bei bestandener Suite-Prüfung und Laufzeit-CI.
Evidence: CLI-Läufe, drei Abschlussläufe und ein Nachlauf vom 2026-11-21 im Testprotokoll (W-009). check_all 12/12. CI-Run 44900592553: 6/6.

### W-010 Befunde der Astra-Gesamtprüfung beheben

Status: done
Depends on: [W-009]
Blocked by: []
Decisions: []
Outcome: Die berechtigten Befunde der Gesamtprüfung durch gpt-6.2-astra sind an den Quellen behoben.
Acceptance: Jeder Befund ist als übernommen oder nicht übernommen mit Grund festgehalten. Ein unabhängiger Review hat die Änderungen gegengelesen. Die Suite-Prüfung und die private Laufzeit-CI bestehen für den korrigierten Stand.
Instructions: []
Steps:
1. [status: done] Befunde an den Quellen nachlesen und einordnen; fertig, wenn jeder Befund eine Einordnung mit Grund im Testprotokoll hat.
2. [status: done] Übernommene Befunde beheben und gegenlesen lassen; fertig bei bestandener Suite-Prüfung.
3. [status: done] Den Plan-Satz ohne Beispiele einmal mit gpt-6.2-sol prüfen; fertig, wenn der Lauf ausgewertet ist.
4. [status: done] Laufzeit-CI für den korrigierten Stand fahren; fertig bei sechs von sechs Jobs.
Evidence: Einordnung, Gegenlesen und Sol-Lauf vom 2026-11-23 im Testprotokoll (W-010). check_all 12/12. CI-Run 45204759085: 6/6.

### W-011 Befunde der Astra-Nachprüfung beheben

Status: done
Depends on: [W-010]
Blocked by: []
Decisions: []
Outcome: Die berechtigten Befunde aus der Nachprüfung der W-010-Korrekturen sind an den Quellen behoben.
Acceptance: Jeder Punkt der Nachprüfung ist als übernommen oder nicht übernommen mit Grund festgehalten. Die Suite-Prüfung und die private Laufzeit-CI bestehen für den korrigierten Stand.
Instructions: []
Steps:
1. [status: done] Punkte an den Quellen nachlesen und einordnen; fertig, wenn jeder Punkt eine Einordnung mit Grund im Testprotokoll hat.
2. [status: done] Übernommene Punkte beheben; fertig bei bestandener Suite-Prüfung.
3. [status: done] Laufzeit-CI für den korrigierten Stand fahren; fertig bei sechs von sechs Jobs.
Evidence: Einordnung und Änderungen vom 2026-11-23 im Testprotokoll (W-011). check_all 12/12. CI-Run 45246766728: 6/6.
