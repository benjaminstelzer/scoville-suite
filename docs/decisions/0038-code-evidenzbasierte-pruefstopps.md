---
format_version: 1
id: ADR-0038
status: accepted
created: 2026-09-25
accepted: 2026-09-25
scope: code/validation-stops
---

# Prüfstopps an offene Nachweisfragen binden

## Decision

Empfohlen ist, weitere Prüfungen nur bei einer benannten offenen Akzeptanzfrage, relevanten Zustandsänderung oder verbindlichen Projektanforderung zu erlauben. Das feste Budget einer alternativen Infrastrukturprüfung und das absolute Befehlsverbot nach der Endinspektion entfallen. Der Zwei-Korrektur-Trigger bleibt bestehen.

## Problem

Die bisherigen absoluten Stopps können einen notwendigen und autorisierten Nachweis verhindern, obwohl sein Nutzen konkret benannt ist.

## Drivers

- Skillwriter verlangt verhältnismäßige Vorgaben statt universeller Verbote aus Einzelfällen.
- Fehlende erforderliche Nachweise dürfen weder als Erfolg gelten noch Berechtigungen erweitern.

## Considered alternatives

- Bisherige Regeln erhalten: klare Obergrenze, aber auch sachlich begründete weitere Prüfungen werden blockiert.
- Evidenzabhängige Stopps: ermöglichen zielgerichtete Fortsetzung, verlangen jedoch Urteil über den zusätzlichen Erkenntniswert.

## Consequences

- W-002 ändert vorgeschriebenes Verhalten und braucht eine eigene Zustimmung.
- Ein weiterer Versuch muss seine offene Frage benennen. Unveränderte Wiederholungen ohne Erkenntnisgewinn bleiben ausgeschlossen.
- Diese Empfehlung ist aus Textanalyse abgeleitet. Eine Leistungsverbesserung ist noch nicht beobachtet.

## Confirmation

Vergleiche Infrastrukturwechsel, notwendige Alternativprüfung, aktualisierten Baum und nutzlose Wiederholung gegen den unveränderten Vertrag. Erforderliche Acceptance bleibt bei fehlenden Nachweisen offen.

## Revisit when

Vergleichsläufe zeigen unbegründete Wiederholungen oder weiterhin blockierte notwendige Nachweise.
