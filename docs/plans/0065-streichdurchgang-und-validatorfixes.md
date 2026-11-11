---
format_version: 1
id: PLAN-0065
status: active
created: 2026-11-10
updated: 2026-11-11
current_item: W-005
---

# Streichdurchgang und Validatorfixes

## Goal

Die Skilltexte so überarbeiten, dass aktuelle Modelle (Fable 5.2, Opus 5.5, GPT-6) mit ihnen besser arbeiten als ohne: zwei Fehler im Plan-Validator beheben, Gegenregeln und Vorab-Lesepflichten ohne belegten Anlass streichen, verbleibende Regeln begründen, Referenzen eine Ebene unter SKILL.md halten. Owner sind members/ und ../shared/. Schutzregeln zu korrekter Umsetzung, sinnvollen Tests, unabhängigen Reviews und begrenzten Kosten, Helper- und Datenformatverträge sowie die Vorlagen für Plan, Decision und Handoff bleiben erhalten. Der [Bericht](../testing/0065-streichdurchgang-und-validatorfixes.md) trennt Quellenänderung, mechanische Prüfung und Textvergleich von der noch offenen Wirkungsmessung.

Lokale Commits sind freigegeben. Pushs einschließlich privater CI, Exporte in öffentliche Repositories, Tags, Releases, lokale Installation und Modellläufe brauchen jeweils eine ausdrückliche Freigabe.

## Non-goals

- Keine Aussage über bessere Modellwirkung vor der Messung.
- Keine Streichung von Regeln mit belegtem Vorfall oder unklarer Herkunft.
- Keine neuen Regeln außer drei Illustrationsbeispielen und den vom Nutzer beauftragten Verhaltenskorrekturen in W-006.

## Work items

### W-001 Validatorfehler beheben

Status: done
Depends on: []
Blocked by: []
Decisions: []
Outcome: Abgebrochene abhängige Items und Profile ohne Decisions-Verzeichnis sind gültig.
Acceptance: WORK_DEPENDENCY_CANCELLED trifft nur nicht-terminale abhängige Items. Ein fehlendes docs/decisions gilt bei gültigem Index als leer, auch für --proposals und --next-id decision. Regressionstests schlagen mit dem alten Code fehl und bestehen mit dem neuen. Manuelle Routen beschreiben dasselbe Verhalten.
Instructions: []
Steps:
1. [status: done] validate_profile.py und select_context.py ändern, Regressionstests ergänzen, Fallbacks und progress.md angleichen; fertig bei grünen Plan-Tests.
Evidence: Beide Fehler behoben; vier neue Tests schlagen mit altem Validator fehl, 147 Plan-Tests bestehen. Fallbacks und progress.md angeglichen.

### W-002 Skilltexte überarbeiten und kleinere Korrekturen

Status: done
Depends on: []
Blocked by: []
Decisions: []
Outcome: Alle Skilltexte verlinken ihre Referenzen direkt, begründen ihre Regeln und enthalten keine pauschalen Vorab-Lesepflichten.
Acceptance: Jede SKILL.md verlinkt die gemeinsamen Referenzen mit sachlicher Bedingung; keine Referenz liegt tiefer als eine Ebene, ausgenommen die erzeugte No-Python-Route. Ersatzlos gestrichen sind nur Regeln ohne belegten Vorfall oder ausdrücklich benannte Stellen; Regeln mit unklarer Herkunft bleiben und sind im Bericht gelistet. output-delivery.md beschreibt Anlass, drei Aufrufe und Ergebnis; Fehlersemantik steht in den instruction-Feldern. Code enthält drei Illustrationsbeispiele. Ask-Preset fable nutzt claude-fable-5-2, Workflow hat genau einen expliziten Aufruf, Skillwriter-Quellen sind geprüft, Referenzen über 100 Zeilen haben ein Inhaltsverzeichnis.
Instructions: []
Steps:
1. [status: done] Herkunft der Verbots- und Stoppregeln aus Commits und Records bestimmen; fertig bei Klassifikation je Regel.
2. [status: done] Gemeinsame Regeln, Routing-Fragment und alle Mitglieder überarbeiten, Helper-Prompttexte und Checker-Meldungen angleichen; fertig bei bestehendem Build beider Profile.
3. [status: done] Modell-IDs, Skillwriter-Quellen, Workflow-Aufruf und Inhaltsverzeichnisse korrigieren; fertig bei geprüften Quellen und grünen Tests.
Evidence: Ladetiefe 1 in allen Skills, General-Fallback 2. Umfang unverändert, Einstiege +3 bis +25 %. 389 Regeln unklarer Herkunft erhalten und gelistet.

### W-003 Bedeutungsvergleich, Prüfung und Bericht

Status: done
Depends on: [W-001, W-002]
Blocked by: []
Decisions: []
Outcome: Der Stand ist gegen die Baseline verglichen, mechanisch geprüft und berichtet.
Acceptance: Ein unabhängiger Vergleich gegen Suite 3a6fb5d und Shared f7e16ae benennt verlorene oder geschwächte Schutzregeln, Erlaubnisse, Grenzen und Vertragsangaben; berechtigte Befunde sind korrigiert, nicht übernommene begründet. check_all.py besteht. Der Bericht nennt je Skill Größe vorher und nachher, Ladetiefe, gestrichene Regeln mit Grund, unsichere Stellen und den Messvorschlag mit Kosten, ohne Wirkungsbehauptung.
Instructions: []
Steps:
1. [status: done] Drei unabhängige Vergleiche ausführen und Befunde einarbeiten; fertig bei begründeter Behandlung jedes hohen und mittleren Befunds.
2. [status: done] Snapshot, README-Vorschauen und Changelogs aktualisieren, check_all.py ausführen, Bericht abschließen; fertig bei bestandenem Lauf und validiertem Profil.
Evidence: 104 Befunde, 81 Korrekturen, 5 begründet nicht übernommen; kein zweiter Vollvergleich. check_all 12 bestanden, 0 fehlgeschlagen. Bericht vollständig.

### W-004 Wirkungsmessung

Status: done
Depends on: [W-003]
Blocked by: []
Decisions: []
Outcome: Abbrüche, unnötige Rückfragen, Aufgabenerfolg und Token sind für drei Aufgaben ohne Skill, mit altem und mit neuem Stand gemessen.
Acceptance: Drei reale Aufgaben laufen je dreimal ohne Skill, mit den ausgelieferten Paketen und mit dem neuen Build. Modell und Effort sind aus den Sitzungsaufzeichnungen belegt. Der Bericht nennt je Zelle die vier Zählwerte und die gelesenen Skilldateien und trennt Stichprobe von Wirkungsaussage.
Instructions: []
Steps:
1. [status: done] Fixtures und Erfolgskriterien für die drei Aufgaben aus dem Messvorschlag anlegen; fertig bei reproduzierbarem Ausgangsstand je Aufgabe.
2. [status: done] Freigegebene Läufe ausführen und aus den Aufzeichnungen auswerten; fertig bei vollständiger Ergebnistabelle und benannten Grenzen.
Evidence: Variante A freigegeben: 27 Läufe gpt-6.1-sol/low. Erfolg alt und neu gleich, keine unnötige Rückfrage; neu liest weniger Skilldateien. Kein Erfolgsvorteil belegt; Fable ungemessen.

### W-006 Verhaltenskorrekturen für Opus 5.5 und Sol

Status: done
Depends on: [W-004]
Blocked by: []
Decisions: []
Outcome: Die in der zweiten und dritten Messreihe gefundenen Fehlverhalten von Plan, Code und UI sind an der Quelle korrigiert und nachgemessen.
Acceptance: Plan legt gewünschte Arbeit trotz Entscheidungskonflikt an, Code wird bei Diagnoseaufgaben aktiviert. Der UI-Skill lässt vorhandene Komponenten wiederverwenden, rendert beim Umsetzen nicht und misst im Review. Der Bericht nennt je Befund den Beleg vor und nach der Korrektur und die offenen Punkte.
Instructions: []
Steps:
1. [status: done] Dieselben Aufgaben mit Opus 5.5 medium und UI-Aufgaben mit beiden Modellen messen; fertig bei benannten Befunden.
2. [status: done] Plan, Code und UI an der Quelle korrigieren und nachmessen; fertig bei Belegen je Befund.
3. [status: done] UI-Regeln nach Nutzervorgabe fassen (Voraussetzung statt Gebot, kein Rendern beim Umsetzen, Messen im Review) und an zwei Umsetzungsaufgaben und einem Review nachmessen; fertig bei Ergebnistabellen und benannten Grenzen.
Evidence: Sol mit UI-Skill: Suche 21/32 erfüllt (ohne 0/8); Überschriftzeile 21/28 (ohne 0/6). Opus rendert beim Umsetzen nicht. Quellenreview eingearbeitet. Offen: Sol nicht durchgehend fehlerfrei.

### W-005 Auslieferung

Status: todo
Depends on: [W-003, W-006]
Blocked by: []
Decisions: []
Outcome: Der geprüfte Stand ist veröffentlicht und im freigegebenen Umfang installiert.
Acceptance: Die neue private Laufzeitmatrix für das geänderte paketierte Python besteht. Builds und Exporte beider Profile sind aus der committeten Quelle erzeugt und geprüft. Alle geänderten Ziele sind auf main remote verifiziert; lokale Installation nur im freigegebenen Umfang.
Instructions: Push nach GitHub am 2026-11-11 freigegeben. Lokale Installation, Tags und Releases sind nicht freigegeben.
Steps:
1. [status: todo] Laufzeitmatrix im privaten CI ausführen und Builds mit ihrem Lauf erzeugen; fertig bei bestandener Matrix und geprüften Paketen.
2. [status: todo] Exporte veröffentlichen, remote prüfen und freigegebene lokale Kopien aktualisieren; fertig bei Remote- und Installationsbelegen.
Evidence: []
