# Ask: Abschluss einer Review-Session

Nutzerauftrag vom 29.09.2026: Der Caller fragt nach dem Review, ob die Sessions
noch benötigt werden. Nein oder eine andere Nachricht statt einer Antwort
beendet sie. Die Berater fragen nicht. Bloßes Schweigen löst nichts aus.

Umgesetzt beim bestehenden Owner: SKILL.md enthält den gemeinsamen Ablauf,
native.md die Archivierung über die genaue Berater-ID, claude.md den Abschluss
ohne native Archivierung. adviser.md gilt über beide Prompt-Helper auch für
Claude. Keine neue Zustandsdatei, kein zusätzlicher Helper oder Fallback nötig:
die Entscheidung ist Gesprächsinterpretation, die Aktion ein natives Tool.

Claude Code 2.1.283 und dessen --help wurden gelesen. Ask verwendet -p und wartet
auf das Prozessende; gespeicherte Session-IDs erlauben --resume. Die geprüfte
CLI bietet keine Archivierung dieser Print-Sessions. stop/rm betreffen andere
Hintergrund-Sessions und werden dafür nicht verwendet. Abschluss bedeutet hier
keine automatische Wiederverwendung, nicht Löschung der gespeicherten Historie.
Ohne continuation_available wird kein Offenhalten angeboten.

Nachweise unter C:/Users/benja/Desktop/test/ask-review-lifecycle/:
before.zip enthält die uncommittete Ausgangsfassung; ask-tests.txt meldet
34 bestandene Tests. Die Adaptertests prüfen Print-Modus, exakte Resume-ID und
fehlende Fortsetzbarkeit bei deaktivierter Persistenz mit simuliertem CLI-Ergebnis.
claude-help.txt und claude-version.txt belegen die lokale CLI-Prüfung.
Keine kostenpflichtige Claude-Beratung wurde für diese Instruktionsänderung gestartet.

Modelltest: Desktop/test/plan0020/runs/review-closure-v1-review-closure,
Chat 01a0ec26-9ba1-7493-97f8-13ccdf2a4f44, Luna/medium. Zwölf Fälle inhaltlich
bestanden: Caller/Reviewer-Zuständigkeit, Ja, Nein, Themenwechsel, Schweigen,
Review-Follow-up, getrennte Sessionwahl, noch laufender Reviewer, Claude-Abschluss,
fehlende Fortsetzbarkeit, gewöhnliche Beratung und Archivierungsfehler.
Der Test simuliert Entscheidungen; er führt keine echten Archivierungsaktionen
für diese Fälle aus. README aus kanonischen Fragmenten erzeugt; Abgleich und
git diff --check bestanden. Installation und Release unverändert.
