# PLAN-0036/W-002: Goal-first-Skill-Fixes

Der Nutzer verlangt die dauerhafte Skill-Korrektur ausdrücklich und nimmt sie
in PLAN-0036 auf (ADR-0197). W-002 hat Vorrang vor weiteren Recovery-Tests.
W-001 ist mit erhaltenem Stand pausiert. Danach gilt die Rückkehr zu W-001
und PLAN-0035/W-009; W-015 bleibt zuletzt.

Die vollständige externe Quelle liegt unter
`C:/Users/benja/.codex/attachments/4dc68d1b-9c20-4a4a-b5eb-cd9f4335cb7c/Eingefügter Text.txt`.
Ihre statistischen Angaben wurden hier nicht neu gezählt.

Astra/high prüft die Vorschläge gemeinsam, read-only, vor Source-Änderungen.
Handle: `/root/plan0035_thread_ritual_astra_high`.
Referenz: `plan0036-external-bookkeeping-ritual-review`.
Scope: `Assess the new external bookkeeping-ritual review and the smallest proportionate corrections`.
Vollständige Frage: `temp/2026-10-06-plan0035/external-bookkeeping-ritual-astra-question.txt`
im Workspace. Nutzerpriorität und Aufnahme in PLAN-0036 wurden nativ ergänzt.
Tatsächlich `gpt-6-astra/high`, vollständig nativ abgeschlossen.
[Kompletter Befund](0036-w002-astra-review.json).

Aktuell 174 von 300 gemeinsamen Luna/high-Reservierungen und 170 berichtete
Starts. Diese Planergänzung startet keine Modelle. Bestehende erforderliche
Nachtests, Reviews, Freigabegrenzen und historische Nachweise bleiben erhalten.

## Umsetzung

Die vier von Astra konkret geprüften Prose-Korrekturen sind umgesetzt:
Plan fragt nur bei ungedeckten materiellen Entscheidungen, setzt nach
Compaction am erhaltenen Stand fort und validiert zusammenhängende Profilupdates
statt einzelne Felder oder reine Berichte. Evidence führt einen owning Bericht
bei Bedarf fort. Code beendet zusätzliche Nachweisverwaltung nach ausreichender
Evidenz und setzt Umsetzung fort; erforderliche Reviews gelten am fertigen
Scope. [Direkter Vorher-/Nachher-Diff](0036-w002-skill-changes.diff).

Keine neue Quote, automatische Budgeterhöhung, Test-Ausnahme oder Review-Kette.
Die bestehenden Stale-Evidence-, Materialitäts-, Ein-Editor- und Fehlerregeln
bleiben. Ein neuer attempts-CLI ist für diese Skill-Korrektur nicht erforderlich
und wird hier nicht vorgeschaltet. Die bestehende Reserve-Funktion und die
vorhandene Manifest-Mechanik bleiben Owner der unterstützten Operationen.

Profilergänzung vor Umsetzung: PASS, 0 Fehler, 2 unveränderte absichtliche
Mojibake-Beispiele im alten W-007. Keine Validierung für diese reine
Berichtsaktualisierung. Praktische Wirkung und finaler Sol-Blockreview offen.

## Gezielte praktische Probe

Aktueller vollständiger Codex-Suite-Testkandidat und Input-Inventar:
`temp/2026-10-06-plan0036/skill-fixes-runtime-candidate` im Workspace.
Erzeugung und Integrität PASS; aktuelle Code-/Plan-Projektionen in den drei
betroffenen Varianten erhalten die Korrekturen. Codex-Standalone enthält diese
beiden Member in diesem Runtime-Kandidaten nicht. Neue Runtime- oder Release-
Zertifizierung wird daraus nicht abgeleitet und hier kein CI-Replay gestartet.

Eine native Luna/high-Probe, reserviert vor Start mit
`76fc39fcee3348cf9bcda09656e4658b`, läuft unter
`/root/plan0036_goal_first_practical_luna`. Vollständiger Auftrag, Eingabebindung,
Fixture und unveränderte bestehende Tests:
`temp/2026-10-06-plan0036/goal-first-practical` im Workspace.
Sie korrigiert eine konkrete Endpreisformel und schließt den bereits autorisierten
Plan ab. Kein breiter Benchmark oder Wiederholen alter Code-Fälle.

## Tatsächliches Ergebnis der praktischen Probe

Native Luna/high-Probe vollständig abgeschlossen. Aktuelle Identität,
actual contexts, vollständige finale Antwort, Rohsession, finaler Dateistand und
Usage stehen in `goal-first-practical/native-result.json` neben der Manifest-
Bindung. Endpreisformel korrigiert; zwei unveränderte Node-Fälle bestanden.
Plan/W-001 abgeschlossen und Index inaktiv; bestehender Bericht fortgeführt.
Keine neue Datei im Fixture. Finaler Validator: PASS, 0 Fehler, 0 Warnungen.
Die alte unverbindliche Prüfanregung wurde nicht zur Abnahmehürde erhoben.
Ein tatsächlicher Einzelfall belegt diese Verwendung, keine allgemeine Garantie
oder gemessene Zeitersparnis. Unabhängiger Sol-Blockreview folgt jetzt.

## Abschluss

W-002 abgeschlossen. Tatsächlicher Sol6.1/high-Blockreview: **PASS**,
[vollständiger nativer Befund](0036-w002-sol-review.json). Die vier Skill-Fixes
und die gezielte praktische Ausführung sind abgenommen. Sol bestätigt auch
unveränderte Tests, vollständige Kandidatenbindung und gültigen Planabschluss.
Zwei Profilvalidierungen im Fixture hatten unterschiedliche Profilstände.

Beobachtete Ausführungsfehler bleiben ausgewiesen: anfänglich zu breites
Referenzlesen mit anschließender vollständiger Nachlese und ein korrigierter
JavaScript-Aufruf beim Berichtsschreiben. Sie begrenzen den Einzelfall und
begründen weder eine neue Source-Regel noch eine identische Wiederholung.
Kein Nachweis allgemeiner Zeitersparnis, Compaction-Liveverhalten oder neuer
Plattformzertifizierung. Keine weitere Prüfphase für diesen bestandenen Block.
Weiter mit der erhaltenen Recovery-Umsetzung W-001.
