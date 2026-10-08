---
format_version: 1
id: PLAN-0037
status: completed
created: 2026-10-07
updated: 2026-10-08
---

# Scoville im laufenden EMPCO-Projekt beobachten

## Goal

Die im EMPCO-Workflow belegten allgemeinen Fehler in Workflow, Plan und Code ursachengerecht beheben, gezielt nachtesten und die korrigierten Skills lokal sowie auf GitHub ausliefern. Entwicklung, passende Tests und unabhängige Reviews mit geringem Verwaltungsaufwand unterstützen.

## Non-goals

Keine Änderungen oder Testausführung im EMPCO-Projekt. Erst nach geprüfter lokaler Installation und verifiziertem GitHub-Release den bestehenden EMPCO-Runner zum Neuladen/Fortsetzen auffordern. Keine Zugriffe auf XMAPI, XMTEST, Holzbau oder private Zugangsdaten. Keine vollständigen Reviewarchive, Laufhistorien oder Tests auf beliebige Source-Wörter.

## Work items

### W-001 Scoville-Verhalten im EMPCO-Lauf beurteilen

Status: done
Depends on: []
Blocked by: []
Decisions: []
Outcome: Relevante Fehler des beobachteten Laufs sind eingeordnet und mit notwendigen Fixvorschlägen für Workflow, Plan oder Code aufbereitet.
Acceptance: Befunde unterscheiden belegte Abweichungen von Verdacht und ungeprüften Phasen; sie nennen Quelle, Wirkung und zuständigen Skill. Sol 6.1/high prüft neue relevante Befunde auf Ursache und kleinsten sinnvollen Fix. Der Abschluss bewertet nur tatsächlich beobachtetes Verhalten.
Instructions: Die Beobachtung endet mit diesem konkreten Workflow oder einem Nutzerstopp; keine automatische Übernahme eines anderen Laufs.
Steps:
1. [status: done] Prüfe den Ausgangsstand des Threads 01a116ce-ac9b-77f0-a6cc-db641fb26f4b im Projekt <observed-project>, seine tatsächlichen Agenten und deren geladene Skill-Regeln.
2. [status: done] Beobachte alle fünf Minuten neue relevante Aufträge, Änderungen, Tests, Reviews und Planfortschritte. Lass relevante Befunde gebündelt über Scoville Ask von Sol 6.1/high beurteilen und pflege nur entscheidungsrelevante Fehler und Fixvorschläge in docs/testing/empco-workflow-observation.md; keine Laufhistorie oder Reviewtexte.
3. [status: done] Halte bei Ende dieses Laufs das Ergebnis und unbeobachtete Grenzen knapp fest und beende die zugehörige Überwachung.
Evidence: Nutzerstopp umgesetzt; Runner bestätigt beendete Kinder/Schreiber. Überwachung beendet. F-001 bis F-011 bestätigt; H-001 offen. Quelle: docs/testing/empco-workflow-observation.md.

### W-002 Allgemeine Ursachen aller Findings in der Suite beheben

Status: done
Depends on: []
Blocked by: []
Decisions: [ADR-0202]
Outcome: Die belegten Ursachen der gesammelten Findings sind in den zuständigen Skills, Aufrufbeispielen oder Helpern behoben; ungeklärte Ursachen bleiben ausdrücklich offen.
Acceptance: Bestätigte Fehler erhalten eine ursachengerechte allgemeine Korrektur; vorhandene Regeln oder lokale EMPCO-Behebungen allein reichen nicht. Astra/high prüft Opus 5.5/xhighs Lösungen vor Änderungen. Dieselbe Opus-Session und Astra/high nehmen Fixes und gezielte Nachtestergebnisse ab. Ungeklärte Befunde bleiben offen; Schreibrechte, Informationsvollständigkeit und Multi-OS-Unterstützung bleiben erhalten.
Instructions: Nur ursachenbezogene Korrekturen; neue Reviewfindings prüfen, bestätigte Fehler korrigieren und erneut gezielt testen.
Steps:
1. [status: done] Opus 5.5/xhigh prüft Plan, Befunde und kanonische Ursachen. Astra/high prüft seine konkreten Lösungen; übernimm bestätigte Lösungen in die betroffenen Steps.
2. [status: done] F-001/F-004/F-006: Direkt verwendbaren --run-Capture und begrenzten UTF-8-Teilread im vorhandenen Checker mit tatsächlicher Labelgröße, Fortschritt bei kleinen Budgets und General-Fallback ergänzen. Vollständige UTF-8-Erfassung ab erstem Aufruf, Exitstatus und Größenprüfung vor sichtbarer Ausgabe in gemeinsamen Writing-Regeln, Plan-Beispielen und Workflow-Aufträgen konkretisieren. Gerenderte Ausgabe statt Dateigröße messen. Reviewerwrites auf erlaubte Ergebnislieferung begrenzen; Quelldiffs stellt der Manager bereit.
3. [status: done] F-002/F-003: Dokumentread, Textchecker und Checkpoint-CLI mit gültigen Argumenten eindeutig und direkt verwendbar zeigen; nötige Argumentdiagnosen korrigieren.
4. [status: done] F-005/F-007/H-001: Aufträge und Managerhandoff an neuem Beitrag, unreviewtem Diff, notwendigen Ownerbelegen und nächster Handlung ausrichten. Unveränderte angenommene Grundlagen wiederverwenden; historische Details nur bei benannter Relevanz. Benötigte Hashes eindeutig Datei und Feld zuordnen; fehlende Originalquelle nicht erfinden.
5. [status: done] F-008/F-009: Code references/validation.md auf entscheidende Ergebnisse statt unnötige Zahlen ausrichten; nötige PowerShell-Zähler über @(...).Count bilden. Zustandsnachweise vom Aufruf über Factory/Konfiguration zum selben beobachteten Bestand binden, auch in getrennten Prozessen.
6. [status: done] F-010: Workflow operations.md unterscheidet normales Fortschreiben angenommener Ergebnisse von materiellen Dokumentänderungen. Separate Dokumentaufträge/Reviews brauchen konkrete Änderung oder bindende Nutzer-/Planpflicht; generierte Berichte begründen diese nicht selbst.
7. [status: done] F-011: Einmalige wirkungslose Builder-Inputkorrektur nach sicher zugestelltem Progress für denselben unveränderten Auftrag ermöglichen; kein Spawnversuch oder Assignment. Eigenes Selectorbudget von echter harter Grenze unterscheiden. operations-dispatch.md, run-feedback.md und Builderdiagnose abstimmen; unsichere Effekte und Teilprompts bleiben gesperrt.
8. [status: done] F-012: Im vorhandenen Teilreader das nächste Segment mit next=M und das vollständige Ende mit last kennzeichnen; tatsächliche Labelgröße einhalten. Aufrufanweisungen abstimmen. Gezielte Consumer- und praktische Lesefälle auf Windows/Linux prüfen.
9. [status: done] Dieselbe Opus-Session und Astra/high nehmen Fixes und gezielte Nachtestergebnisse ab. Nur entscheidende Ergebnisse und verbleibende Grenzen festhalten.
Evidence: Opus/Astra nehmen Fixes und Nachtests ab. F-012-Leser Windows/Linux vollständig; CI 37730708565 bestanden. Frühere Praxis-FAILs/H-001 bleiben: docs/testing/empco-workflow-observation.md.

### W-003 Korrigierte Skills installieren und veröffentlichen

Status: done
Depends on: [W-002]
Blocked by: []
Decisions: [ADR-0202]
Outcome: Die geprüften korrigierten Skills sind lokal für Codex und Claude installiert und ihre geänderten Distributionen auf GitHub veröffentlicht.
Acceptance: Kanonischer Build und betroffene Paketstruktur bestehen; lokale Installationen entsprechen den freigegebenen Paketen. Geänderte autorisierte Distributionen besitzen verifizierte neue GitHub-Releases. Sichtbarkeit und Codex-only-Grenzen bleiben erhalten.
Instructions: Genau ein aktueller Build unter skills/temp/release. EMPCO bleibt bis zur verifizierten Auslieferung gestoppt.
Steps:
1. [status: done] Versionen und Changelogs der tatsächlich betroffenen Pakete fortschreiben; aus kanonischen Quellen bauen und relevante Struktur-/Helperchecks durchführen.
2. [status: done] Verifizierte Exporte an die festen Distributionen synchronisieren und betroffene lokale Codex-/Claude-Installationen aktualisieren; Paketbytes prüfen.
3. [status: done] Autorisierte geänderte Distributionen pushen, Releases erstellen und den veröffentlichten Stand sowie ersetzte Release-Tags prüfen.
4. [status: done] Nach verifizierter Auslieferung den bestehenden EMPCO-Runner auffordern, aktuelle installierte Workflow-Regeln zu laden, Agenten-/Schreib-/Entscheidungszustände protokollgerecht zu klären und denselben gestoppten Umfang fortzusetzen. Fortgesetzte Manager lesen nötige aktualisierte Referenzen vor der nächsten Fachaktion neu. Tatsächliche Zustellung prüfen und Plan abschließen.
Evidence: Paketbindung Windows/Linux bestanden; 13 Skills lokal bytegleich. Sieben Releases/Tags verifiziert, Vorgänger bereinigt. EMPCO-Runner bestätigt Neuladen/Wiederaufnahme. Details im Befundbericht.
