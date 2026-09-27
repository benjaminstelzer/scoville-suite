---
format_version: 1
id: ADR-0101
status: accepted
created: 2026-09-27
accepted: 2026-09-27
scope: workflow/continuation
---

# Direkte Übergaben und konkrete Diagnosen

## Decision

Der Nutzer beauftragt direkte Übergaben statt eines verpflichtenden Cursors. Höchstens ein Worker schreibt gleichzeitig im Projekt. Der Nachfolger erhält den nötigen Fortsetzungsstand, bestätigt den Empfang und der Vorgänger archiviert sich. Plan und Chats reichen zur gezielten Wiederaufnahme nach einem Abbruch.

Startabsichten und Chat-IDs benötigen kein zweites Register. Nicht mehr benötigte Kinder archivieren sich nach einer Nachricht des Koordinators. Ergebnisse sind kurze normale Nachrichten mit eindeutigem Status und benötigten Tatsachen, ohne Versionsmarker, Änderungsflags oder strikte Feldsyntax. Nach Abschluss eines Workerauftrags fordert der Koordinator dessen Archivierung an. Reviewer liefern einmal ein vollständiges Ergebnis einschließlich fehlender Prüfbarkeit und erhalten danach direkt die Archivierungsaufforderung; Rückfragerunden entfallen. Korrekturen gehen als neuer Auftrag an einen neuen Worker; eine eigene Fixer-Rolle entfällt. Jeder Auftrag darf bei Bedarf per Rollover fortgesetzt werden; wiederholtes Scheitern führt zu einer Ursachenentscheidung statt automatischer Modellsteigerung nach Versuchszähler. Review, fachliche Abnahme und Kontextschwellen bleiben erhalten.

Validatoren nennen Fundstelle, konkrete Verletzung, erwarteten Wert und die kleinste zulässige Korrektur. Formatkorrekturen verändern weder Abnahme noch nachgewiesene Tatsachen. Diese Entscheidung ersetzt frühere Vorgaben nur hinsichtlich Cursor, Ergebnisformat und Reparaturleiter; historische Nachweise bleiben unverändert.

## Problem

Mehrfach gespeicherter Ablaufzustand und formale Ergebnisverträge erzeugen Verwaltungsarbeit und Reparaturrunden. Eine allgemeine Evidence-Fehlermeldung verschweigt die verletzte Grenze von 200 Zeichen.

## Drivers

- Expliziter Nutzerauftrag: Komplexität reduzieren und konkrete Validator-Hinweise testen.
- So kurz wie möglich, nur so lang wie für richtige Fortsetzung und Abnahme nötig.

## Considered alternatives

- Cursor weiter absichern: zusätzliche Pflege für rekonstruierbare Ausnahmefälle.
- Prüfungen entfernen: würde fachliche Fehler verdecken statt den Ablauf vereinfachen.

## Consequences

Worker werden im gesamten Workflow-Lauf fortlaufend nummeriert. Jeder neue Chat erhält die nächste Nummer, ob neuer Auftrag, Rollover oder Korrektur nach Review. Es gibt keinen gesonderten Reparaturzähler und keinen Neustart der Workernummer je Planpunkt.

Der Reviewer übernimmt die Nummer des Workers, dessen Ergebnis er prüft. Ein Reviewer-Rollover behält diese Zuordnung; ein eigener Reviewerzähler entfällt.

Seltene Abbrüche können eine gezielte Rekonstruktion erfordern. Keine automatischen Wiederholungen bei unklarem Start, keine parallelen Schreiber und keine fiktive Abnahme. Technische Konfiguration bleibt strukturiert.

## Confirmation

Defekte Planfixtures liefern konkrete Diagnosen und bestehen nach der beschriebenen Korrektur. Gebaute Aufträge übernehmen normale Nachrichten unverändert. Luna High simuliert Übergabe, Abbruch, Korrektur und offene Abnahme; Astra Medium prüft auf ausdrückliche aktuelle Modellvorgabe Ergebnisse und finalen Vertrag. Der Nutzer beauftragt die Umsetzung des konkret beschriebenen Fixplans einschließlich gezielter Helper-/Luna-Prüfung und anschließender lokaler Aktualisierung und neuer Releases. Für diesen Kandidaten gilt dieser gezielte Prüfungsumfang; bestehende Build-, Sichtbarkeits- und Remote-Nachweise bleiben erforderlich.

## Revisit when

Eine direkte Übergabe verliert notwendige offene Arbeit oder verursacht parallele Projektänderungen.
