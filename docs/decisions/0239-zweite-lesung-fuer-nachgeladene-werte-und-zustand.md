---
format_version: 1
id: ADR-0239
status: accepted
created: 2026-11-16
accepted: 2026-11-16
scope: suite/skills
---

# Eine unabhängige zweite Lesung für nachgeladene Werte und Zustand

## Decision

Binding sections: complete

Der Eigentümer hat am 2026-11-16 nach Runde v35 entschieden, eine unabhängige zweite Lesung als Teil des Code-Skills zu erproben:

- Hat Frage 2 (erneut geladener Wert) oder Frage 3 (Zustand und Effekte) auf dem betroffenen Pfad einen Gegenstand und kann der Host einen getrennten Agenten starten, lässt der Autor die fertige Änderung einmal von einem Leser prüfen, der seine Begründung nicht kennt.
- Der Leser bekommt als ganzen Auftrag den Diff, den Ort des geänderten Codes und die Fragen 2 und 3 mit den Regeln 8 und 9. Er ändert nichts und startet keinen weiteren Agenten. So hat es der Eigentümer am 2026-11-16 nach den Runden v36 und v37 entschieden.
- Der Autor wartet auf die Antwort des Lesers. Er startet ihn nicht im Hintergrund und plant keine spätere Nachschau.
- Jeder Reviewer, der die gemeinsamen Review-Regeln erhält, auch der Workflow-Reviewer, beantwortet die Fragen 2 und 3 zuerst, mit Datei und Zeile.
- Unter Scoville Workflow ist das Step-Review dieses Review. Der Code-Skill startet dort keinen weiteren Leser, und der Hauptthread startet keinen eigenen Reviewer.
- Die Pflicht gilt nur für den Code-Skill. UI, Skillwriter, Plan, Cleanup, Handoff und Setup prüfen ihr Ergebnis weiter selbst.
- Für jeden Befund gilt die Grenze des betroffenen Pfads: Eine vorhandene Prüfung oder Zuweisung oder eine Garantie, die Regel 8 zulässt, beantwortet einen Befund; der Autor nennt sie. Fehlt die Prüfung oder Zuweisung und hängt das verlangte Ergebnis davon ab, wozu der Zustand und die Effekte gehören, die Regel 9 diese Änderung erhalten lässt, ergänzt er sie an jeder Stelle, die der Befund erfasst; ein Fall, den der Leser beschreibt, ist ein Beispiel und nicht der Umfang des Befunds. Was der alte Pfad erhielt und diese Änderung fallen lässt, stellt er wieder her, außer der Auftrag oder eine Projektregel entfernt es; „bewusste Änderung“ erledigt keinen Befund (seit v41, nach zwei Opus-Läufen in v40: einer ergänzte die Zuweisung nur für das Beispiel des Lesers, einer lehnte sie als bewusste Verhaltensänderung ab). Liegt sie außerhalb der Änderung, berichtet er den Mangel mit dem Verbraucher und dem Verhalten, die das zeigen. Dass die Lücke schon vorher bestand, erledigt keinen Befund (seit v39, nach der frischen Aufgabe R13 und der Gegenprüfung durch Sol 6.1; noch nicht gemessen). Eine Korrektur löst keine weitere Lesung aus.
- Reviewer starten keine Leser. Ohne getrennten Agenten entfällt der Schritt; eine Selbstlesung ersetzt ihn nicht.

Die Regeltexte zu den Fragen 2 und 3 werden für Opus nicht weiter umformuliert. Regel 9 nennt zusätzlich den Träger des zugewiesenen Zustands: ein Element, eine Liste oder einen Datensatz, dessen Inhalt der neue Pfad ändert.

## Problem

Über fünf Fassungen der Regeln (v31 bis v35) prüft Opus 5.5 high den erneut geladenen Wert in R2 in 8 von 15 Läufen (ohne Skills 0 von 3) und erhält die Auswahl in R1 in 6 von 15 (ohne Skills 4 von 5). Zwischen den Fassungen gibt es keinen Trend. In den Fehlläufen nennt der Autor die Stelle im Bericht und entscheidet sich mit einem Argument dagegen, das die Regel ausschließt. Sol 6.1 medium erfüllt beide Prüfungen mit Skill in 15 und 14 von 15 Läufen.

## Drivers

- Dieselbe Frage wird richtig beantwortet, wenn sie der ganze Auftrag ist: Sechs frische Opus-Leser fanden das ungeprüfte Nachladen in 2 von 2 fehlerhaften Diffs und ließen den richtigen Diff gelten.
- Weiteres Umformulieren derselben Sätze ist kein neuer Mechanismus.
- Skills sollen schlank bleiben; ein zusätzlicher Schritt braucht einen gemessenen Anlass.

## Considered alternatives

- v35 als Endkandidat und den Opus-Rest als nicht behoben dokumentieren: vom Hauptagenten empfohlen, vom Eigentümer nicht gewählt.
- Erst mehr Opus-Läufe mit v35: klärt die Raten, ändert nichts am Ergebnis.
- Zweite Lesung durch den Autor selbst: Das ist die Selbstprüfung aus Abschnitt 4, die in den Fehlläufen nicht gegriffen hat.
- Volles Scoville-Review durch den getrennten Agenten, Fragen 2 und 3 zuerst: vom Eigentümer zunächst gewählt, damit eigenständig und unter Workflow dieselben Regeln gelten, und in Runde v37 gemessen. Es fand echte Mängel. In zwei von 19 Läufen mit Reviewer setzte der Autor aber einen Befund außerhalb der zwei Fragen um und beschädigte damit eine vorher richtige Änderung. Der Leser nur mit den zwei Fragen (Runde v36, sechs Läufe) erzeugte keinen solchen Schaden.
- Externes Review der eigenen Arbeit in allen Skills: ohne gemessenen Anlass und gegen die Vorgabe schlanker Skills; vom Eigentümer nicht gewählt.

## Consequences

- Jeder betroffene Lauf kostet eine weitere Lesung. In der Probe waren das 39 bis 100 Sekunden und 74.000 bis 90.000 Token je Leser.
- Für den Auswahlverlust in R1 ist keine verlässliche Wirkung zu erwarten: Die Leser fanden ihn in 1 von 2 fehlerhaften Diffs und übernahmen im anderen das Argument des Autors.
- Die Messläufe mit Skill brauchen die Erlaubnis, einen getrennten Agenten zu starten. Das weicht von der Ausführung der gespeicherten Kontrollen ab und steht im Testbericht.
- Eigenständig und unter Workflow wird nicht dasselbe geprüft: eigenständig nur die zwei Fragen, unter Workflow das volle Step-Review.
- Der Schritt ist ein Versuch. Er bleibt nur, wenn die Messung bei Opus eine Verbesserung zeigt, die die Kosten trägt.

## Confirmation

Der Code-Skill enthält den Absatz in Abschnitt 4. Die Gesamtprüfung der Suite besteht. Die Wirkung messen Runde v36 (Leser nur mit den Fragen 2 und 3), Runde v37 (volles Review) und Runde v38 (Leser nur mit den Fragen 2 und 3, mit Warten auf die Antwort).

## Revisit when

Die Messung zeigt bei Opus keine Verbesserung, die Lesung erzeugt in richtigen Änderungen wiederholt unnötige Korrekturen, oder ein Host ohne getrennte Agenten wird zum Hauptziel.
