# Workflow-Grenzen: gezielte Prüfung vom 2026-09-28

Basis: 45706f2, danach lokale Änderungen aus ADR-0102 / PLAN-0018 W-013.
Kein Release, kein Eingriff in laufende DIVI-Chats oder Projektdateien.

## Ergebnis

Die beauftragten Verhaltensfälle bestehen mit GPT-6 Luna High und GPT-6 SOL
Medium. Tatsächliches Modell und Effort wurden gegen die nativen Turn-Aufzeichnungen
geprüft. 24 Modellläufe insgesamt: 20 bestanden, zwei ursprüngliche Handoff-Fälle
fehlgeschlagen und nach Vertragskorrektur bestanden, zwei gemischte Rollenfixtures
nicht als Abnahme gewertet und durch getrennte Rollenfälle ersetzt.

| Verhalten | Luna High | SOL Medium |
| --- | --- | --- |
| Koordinator-Rollover vor Worker-Nachfolger, fälliges Fix-Review erhalten | PASS, Nachtest | PASS, Nachtest |
| Dritter Handoff teilt offene Restarbeit in geordnete Steps | PASS | PASS |
| Review vor abhängigen umfangreichen Tests; Projektvorgabe geht vor | PASS | PASS |
| Gebauter Workerauftrag endet nach geprüftem Produktfix | PASS | PASS |
| Koordinator prüft Fixdelta und lässt restliche Step-Tests offen | PASS | PASS |
| Reine Testnachweise lösen kein Zwischenreview aus | PASS | PASS |
| Finalreview übernimmt unveränderte frühere Bewertungen | PASS | PASS |
| Gebauter Reviewerauftrag begrenzt das Delta und prüft betroffene Interaktionen | PASS | PASS |
| Fachfremder Auftrag bleibt separat in Plan und Commit erkennbar | PASS | PASS |
| Sechs freie Statusnachrichten, einschließlich fehlendem Pflichtnachweis | PASS | PASS |

Der erste Handoff-Vertrag und sein Testschlüssel waren zu pauschal: Ein Handoff
allein löst kein Review aus, ein darin enthaltener geprüfter Produktfix bleibt
aber reviewpflichtig. Beide Modelle übersprangen anfangs dieses Review. Nach
Präzisierung erhalten beide es über den Koordinator-Rollover hinweg.

Der erste Workerfall vermischte Koordinatorregeln und einen echten Workerauftrag.
Luna ergänzte einen unnötigen Checkpoint, SOL verlangte Defaults statt zu antworten.
Der Builder nennt den geprüften Fix jetzt ausdrücklich als Abschluss des aktuellen
Auftrags. Getrennte Tests verwenden die tatsächlich erzeugten Worker-/Reviewer-
Prompts unverändert. Beide Modelle liefern verwendbare normale Antworten und
erfinden trotz Offline-Grenze keine Zustellung oder fachliche Abnahme.

## Mechanische Prüfung und Installation

Python 3.14.3: 223 Tests bestanden: Workflow 19, Suite 32, Shared 62,
Shared-Build 1, Plan 80, Ask 27, Setup 2. Der neue Checkpoint-CLI-Test prüft
fehlende/leere Grenze, Korrektur nach Diagnose, alten Parameteralias und das
Entfernen eines unzulässigen Workerparameters. Die vorhandenen Tests sichern
40/60 und Compaction. README-/Sourcechecks und Git-Whitespacecheck bestehen.

Der allgemeine Skill-Creator-Validator lehnt das bestehende Frontmatter-Feld
`compatibility` ab, identisch am unveränderten vorherigen Paket. Dieser
unabhängige Check ist daher nicht grün; Suitebuild und eigene Paketprüfungen
bleiben die hier verwendeten Nachweise. Kein Frontmatter wurde dafür entfernt.

Gebauter Workflow und Plan wurden vor der Installation mit `.codex/skills`
verglichen: sechs geänderte Workflow-Dateien, eine Planreferenz, keine zusätzlichen
oder fehlenden Dateien. Danach stimmen die Paketdateien einschließlich Hashes
überein; Python-Caches sind ausgenommen. Der Build enthält lokale Änderungen
und ist kein veröffentlichter Versionsstand.

## Grenzen und nächste Beobachtung

Dies sind Offline-Verständnisfälle mit echten Modellen und gebauten Aufträgen,
kein realer Mehrchat-Projektlauf. Prüferwartungen wurden vor den jeweiligen
Läufen gespeichert und nicht an Antworten angepasst. Die Korrektur des ersten
Handoff-Schlüssels ist oben ausdrücklich dokumentiert. 327.041 Input- und
20.169 Output-Tokens laut Turn-Nutzung über alle 24 Läufe sind Testverbrauch,
kein Nachweis eines Koordinationsanteils oder einer Kostenersparnis.

Im nächsten echten Lauf beobachten: Checkpoint nach Worker-Handoff; Aufteilung
beim dritten Handoff; Deltareview nach Produktfix und vor umfangreicher
abhängiger Prüfung; Umfang des Finalreviews; Koordinatoranteil an Input-Tokens.
Die README-Größenordnung 5–10 % ist die vom Nutzer gewählte Orientierung aus
dem externen Opus-Bericht, keine neue Messung dieses Tests.

Originalantworten, Modellidentitäten und semantische Bewertung: `answers.json`
im unten genannten temporären Nachweisordner.
Erwartungen: `expected.md`, `followup-expected.md`. Vollständige Prompts, Rohlogs,
Runner, Build- und Installationsnachweise bleiben unter
`../../../../../temp/2026-09-28-workflow-boundaries/` erhalten.

## Geänderte Dateien

- Workflow `SKILL.md`: verweist auf die Review-Regel, Checkpoints nach Handoffs und aktualisierte Step-Referenzen nach Aufteilung.
- Workflow `references/operations.md`: regelt frühe Deltareviews, dritten Handoff, sichere Checkpoints und getrennte fachfremde Änderungen.
- Workflow `references/operations-rollover.md`: übergibt zuerst den Koordinator und erhält ausstehende Worker-Handoffs, Reviews und Aufteilungen.
- Workflow `references/operations-dispatch.md`: nutzt vorhandenen Zusatzkontext für Review-Diff und frühere Bewertungen.
- Workflow `scripts/build_dispatch_prompt.py`: beendet den Workerauftrag nach geprüftem Produktfix und begrenzt Reviewer auf das ungeprüfte Delta.
- Workflow `scripts/check_context_checkpoint.py`: verwendet `--boundary`, behält `--accepted-unit` als Alias und erklärt ungültige Aufrufe konkret.
- Workflow `development/tests/test_coordinator_context.py`: prüft den echten CLI-Aufruf einschließlich Diagnose und anschließender Korrektur.
- Plan `references/edit.md`: erlaubt die geordnete Aufteilung offener Arbeit gestarteter Steps bei unverändertem fachlichen Auftrag.
- `development/readme/scoville-workflow-codex/mechanism.md`: erklärt Review-Grenzen und ergänzt den Handoff-Zweig im bestehenden Ablaufdiagramm.
- `development/readme/scoville-workflow-codex/costs.md`: nennt die gewünschte Größenordnung und möglichen Cacheeffekt.
- `members/scoville-workflow-for-codex/README.md`: wurde aus den kanonischen Fragmenten neu erzeugt.
- `docs/decisions/0102-uebergabegrenzen-und-deltareviews.md` und PLAN-0018 W-013: halten Auftrag, Grenzen und Abnahme fest.
- Dieser Nachweisordner: bewahrt Ergebnisse, Originalantworten und Testschlüssel.

Workflow-Pfade liegen unter `members/scoville-workflow-for-codex/`, Laufzeitdateien
im darin enthaltenen Ordner `scoville-workflow-for-codex/`. Plan-Laufzeitdateien
liegen unter `members/scoville-plan/scoville-plan/`.
