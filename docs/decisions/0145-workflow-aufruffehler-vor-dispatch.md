---
format_version: 1
id: ADR-0145
status: accepted
created: 2026-10-02
accepted: 2026-10-02
scope: workflow/dispatch
---

# Aufruffehler vor dem Agentenstart korrigieren

## Decision

Der Dispatchvertrag nennt den absoluten Projektpfad und die Pflichtargumente je
Rolle vor dem Aufruf. Ein frisches Review erhält das ursprüngliche Worker-Ergebnis.
Ein eindeutig diagnostizierter Argumentfehler erlaubt einen korrigierten
Helfer-Aufruf mit bereits belegten Fakten, solange kein Agentenstart versucht
wurde und keine Zuweisungsdatei oder andere Wirkung entstanden ist.

## Problem

Bei empco wurden ein relativer Projektpfad und ein Review ohne Worker-Ergebnis
abgewiesen. Die Anleitung führte das Pflichtargument als optional und zeigte
einen unvollständigen Review-Aufruf. Behebbare Aufruffehler erschienen als Blocker.

## Drivers

- Der Nutzer hat die begrenzte Korrektur und klarere Pflichtargumente bestätigt.
- Validierung, ursprüngliche Ergebnisse und die Sperre gegen Spawn-Wiederholungen bleiben erhalten.

## Considered alternatives

- Sofort eskalieren: unterbricht den Nutzer auch bei vollständig bekannten Korrekturen.
- Uneingeschränkt wiederholen: kann unbekannte Wirkungen oder doppelte Starts erzeugen.

## Consequences

Eine erfolgreiche Korrektur braucht keine sichtbare Blockermeldung. Fehlende
Fakten, ein gescheiterter Korrekturaufruf, andere Helferfehler und unklare
Wirkungen oder Agentenzustände bleiben sichtbare Blocker. Ergebnisse dürfen
nicht erfunden und fehlgeschlagene Ausgaben nicht repariert werden.

## Confirmation

Fehlende Review-Ergebnisse und relative Projektpfade müssen weiterhin ohne
Zuweisung scheitern. Korrigierte Aufrufe müssen vollständige native Argumente
liefern. Anleitung, Eskalation und unveränderte Spawn-Sperren gemeinsam prüfen.

## Revisit when

Der Builder erzeugt vor der Argumentprüfung Wirkungen oder der Host ändert
seine Start- und Wiederholungssemantik.
