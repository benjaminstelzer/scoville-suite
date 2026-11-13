---
format_version: 1
id: PLAN-0066
status: active
created: 2026-11-12
updated: 2026-11-13
current_item: W-006
---

# Konkrete Skilltexte und Auslieferungsbefehl

## Goal

Alle Skilltexte der Suite in eine Form bringen, die gpt-6.1-sol und Opus 5.5 ab Effort medium zuverlässig befolgen: konkrete Auslöser, Handlungen und vom Modell selbst prüfbare Ergebnisse statt abstrakter Grundsätze. Code und der WordPress-Adapter werden dafür zuerst an schwierigen Aufgaben gemessen und dort gekürzt, wo sie keine Wirkung zeigen. Die Auslieferung nach dem Build läuft über einen Befehl. Owner sind members/ und ../shared/. Schutzregeln, Helper- und Datenformatverträge sowie die Vorlagen für Plan, Decision und Handoff bleiben erhalten. Ergebnisse stehen im [Bericht](../testing/0066-konkrete-skilltexte-und-auslieferungsbefehl.md).

Lokale Commits und Modellläufe mit gpt-6.1-sol medium und Opus 5.5 medium sind freigegeben. Pushs einschließlich privater CI, Exporte in öffentliche Repositories, Tags, Releases und lokale Installation brauchen jeweils eine ausdrückliche Freigabe.

## Non-goals

- Keine Aussage über Modellwirkung ohne Messung.
- Keine Streichung einer Regel mit belegtem Vorfall. Regeln unklarer Herkunft fallen nur, wenn eine Messung keine Wirkung zeigt; sonst stehen sie im Bericht.
- Kein Umbau des Builds aus einer Quelle, der Profile oder der acht Auslieferungsziele.
- Keine Messung auf Effort low und keine Messung von Fable 5.2.

## Work items

### W-001 Auslieferungsbefehl

Status: done
Depends on: []
Blocked by: []
Decisions: []
Outcome: Ein Befehl bereitet eine Auslieferung vom committeten Quellenstand bis zu den bereitgestellten Ziel-Repositories vor, ein zweiter veröffentlicht sie nach Freigabe.
Acceptance: `prepare` baut die vier Paketansichten, prüft ihre Veröffentlichungsbelege, erzeugt und validiert beide Quellenexporte, durchsucht sie nach persönlichen Pfaden und stellt die Änderungen in allen Ziel-Repositories bereit, ohne zu committen oder zu pushen. `publish` committet, pusht main, vergleicht jeden Remote-Stand mit dem lokalen Commit und verweigert, wenn sich der Quellenstand seit `prepare` geändert hat. Jede Verweigerung nennt Ursache und Korrektur. Tests decken Spiegeln, Verweigerungen und Belegdatei ab; ein echter `prepare`-Lauf im Arbeitsbereich besteht. fragments.md und AGENTS.md beschreiben den Ablauf.
Instructions: []
Steps:
1. [status: done] ../shared/build/release_suite.py mit Tests unter ../shared/tests schreiben; fertig bei grünen Shared-Tests und einem bestandenen echten prepare-Lauf.
2. [status: done] Ablauf in ../shared/build/fragments.md und den Auslieferungsregeln in AGENTS.md beschreiben; fertig bei synchronem Snapshot und grüner Gesamtprüfung.
Evidence: Neun Tests bestehen (Shared 110). Echter prepare-Lauf gegen Kopien der acht Ziele in 53 s, Wiederholung und zwei Verweigerungen geprüft. publish nur gegen lokale Test-Remotes geprüft. check_all 12/12.

### W-002 Code an schwierigen Aufgaben messen und kürzen

Status: done
Depends on: []
Blocked by: []
Decisions: []
Outcome: Code enthält nur Regeln, die an schwierigen Aufgaben wirken oder einen belegten Schutz tragen.
Acceptance: Mindestens vier schwierige Aufgaben mit je einer Falle (Test abschwächen, offene materielle Wahl, versteckter Verbraucher, nicht freigegebene Aktion) sind mit gpt-6.1-sol medium und Opus 5.5 medium ohne und mit Skill gemessen. Jede Kürzung ist im Bericht mit Messung oder fehlendem Anlass belegt und nachgemessen, ohne Rückschritt bei den Fallen.
Instructions: []
Steps:
1. [status: done] Aufgaben, Fixtures und Auswertung im Messordner bauen und beide Modelle ohne und mit Skill laufen lassen; fertig bei Ergebnistabelle im Bericht.
2. [status: done] members/scoville-code nach Befund kürzen und konkret fassen, dann nachmessen; fertig bei Tabelle vorher und nachher.
Evidence: C1 bis C16 mit Sol und Opus medium ohne, alt und neu gemessen. Sol neu C12, C13, C14, C16 je 3 von 3 (alt 2, 0, 0, 0); übrige unterscheiden nicht. Referenzen halbiert. Bericht W-002.

### W-003 WordPress-Adapter gezielt prüfen

Status: done
Depends on: []
Blocked by: []
Decisions: []
Outcome: Der WordPress-Adapter von UI ist an eigenen Aufgaben gemessen und danach korrigiert oder gekürzt.
Acceptance: Mindestens drei wp-admin-Aufgaben (Umsetzen einer Plugin-Seite, Audit mit eingebauten Fehlern, Anfrage zu einer ausgeschlossenen Fläche) sind mit beiden Modellen ohne und mit Skill gemessen. Befunde sind an der Quelle korrigiert und nachgemessen. Der Bericht nennt die Grenzen, darunter die fehlende WordPress-Laufzeit.
Instructions: []
Steps:
1. [status: done] Aufgaben, Fixtures und Auswertung bauen und messen; fertig bei Ergebnistabelle im Bericht.
2. [status: done] members/scoville-ui/scoville-ui/references/wordpress nach Befund ändern und nachmessen; fertig bei Tabelle vorher und nachher.
Evidence: WPA, WPB, WPC mit beiden Modellen gemessen. Sol neu je 3 von 3 (ohne 2, 0, 0; alt 3, 3, 0). Prüfliste und Empfehlungen für fremde Flächen ergänzt. Ohne WordPress-Laufzeit. Bericht W-003.

### W-004 Alle Skilltexte konkret und prüfbar fassen

Status: done
Depends on: [W-002, W-003]
Blocked by: []
Decisions: []
Outcome: Jede SKILL.md, jede Referenz aller Mitglieder und die gemeinsamen Regeln nennen Auslöser, Handlung und prüfbares Ergebnis in konkreten Worten.
Acceptance: Jede Regel- und Referenzdatei unter members/ und ../shared/ ist überarbeitet oder im Bericht mit Grund als unverändert geführt. Verhalten, Schutzregeln, Helper- und Datenformatverträge und die Vorlagen bleiben erhalten; ein unabhängiger Bedeutungsvergleich gegen den Stand vor diesem Item hat keinen offenen Befund. Regeln unklarer Herkunft sind im Bericht gelistet.
Instructions: []
Steps:
1. [status: done] Schreibregeln aus den Messbefunden festhalten und je Mitglied anwenden; fertig bei bestehendem Build beider Profile.
2. [status: done] Unabhängiger Bedeutungsvergleich je Mitglied und Korrektur der Befunde; fertig bei null offenen Befunden.
Evidence: Texte aller neun Mitglieder, der gemeinsamen Regeln und 20 Helfer-Prompts in Python umgeschrieben, Bedeutungsvergleich korrigiert, 47 Wiederholungen gestrichen. Neuer CI-Lauf nötig. Bericht W-004.

### W-005 Nachmessung und Gesamtprüfung

Status: done
Depends on: [W-004]
Blocked by: []
Decisions: []
Outcome: Der überarbeitete Stand ist mit beiden Modellen nachgemessen und mechanisch geprüft.
Acceptance: Die Aufgaben für UI, Plan, Handoff, Skillwriter, Code und WordPress sind mit dem Stand nach W-004 auf gpt-6.1-sol medium und Opus 5.5 medium gemessen, ohne Rückschritt gegenüber dem Stand davor. `python development/check_all.py` besteht. Der Bericht trennt Gemessenes von Ungemessenem.
Instructions: []
Steps:
1. [status: done] Alle Aufgabenreihen mit dem neuen Stand laufen lassen und auswerten; fertig bei Vergleichstabelle im Bericht.
2. [status: done] Rückschritte an der Quelle beheben und die betroffene Reihe wiederholen; fertig ohne offenen Rückschritt und mit grüner Gesamtprüfung.
Evidence: Endstand mit Sol auf allen Reihen, mit Opus auf Auswahl gemessen, kein offener Rückschritt; UI-Review nach Schärfung 6 von 6. check_all 12 von 12. Große Projekte ungemessen. Bericht W-005.

### W-006 Auslieferung

Status: in_progress
Depends on: [W-001, W-005]
Blocked by: []
Decisions: []
Outcome: Der geprüfte Stand ist veröffentlicht und im freigegebenen Umfang installiert.
Acceptance: Die Auslieferung ist mit dem Befehl aus W-001 vorbereitet und geprüft. Alle geänderten Ziele sind nach Freigabe auf main veröffentlicht und remote verglichen; lokale Installation nur im freigegebenen Umfang.
Instructions: Export, Push und lokale Installation brauchen je eine ausdrückliche Freigabe des Nutzers.
Steps:
1. [status: done] Auslieferung vorbereiten und dem Nutzer Umfang und Prüfergebnis vorlegen; fertig bei bestandenem prepare-Lauf.
2. [status: in_progress] Nach Freigabe veröffentlichen und freigegebene lokale Kopien aktualisieren; fertig bei Remote- und Installationsbelegen.
Evidence: Privater CI-Lauf 43406929881 mit sechs Jobs bestanden. Probelauf von prepare gegen Kopien der acht Ziele bestanden. Push der Ziele am 2026-11-13 freigegeben; lokale Installation offen.
