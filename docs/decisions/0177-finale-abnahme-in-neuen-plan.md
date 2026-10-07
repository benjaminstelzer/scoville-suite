---
format_version: 1
id: ADR-0177
status: accepted
created: 2026-10-05
accepted: 2026-10-05
scope: suite/evaluation-transfer
---

# Restabnahme nach PLAN-0035 übertragen und PLAN-0034 abschließen

## Decision

Der Nutzer beauftragt am 05.10.2026 ausdrücklich: die noch offenen finalen
Skill-, Modell- und CI-Nachweise aus PLAN-0034/W-014 als eigenen Abnahmepunkt
W-009 nach PLAN-0035 übertragen und PLAN-0034 abschließen. W-014 wird mit
erhaltenen Teilergebnissen cancelled, nicht als bestandene Abnahme done.
Erledigte Steps bleiben done, übrige Steps werden cancelled. Die anderen
erledigten Arbeitspunkte bleiben unverändert. PROJECT_INDEX wird idle.

W-009 steht vor dem letzten W-015. PLAN-0035 bleibt draft bis zur ausdrücklichen
Aktivierung. Das eigene Maximum von insgesamt 80 Luna-high-Versuchen nach
ADR-0175 umfasst auch diese Restabnahme. Alte Versuche bleiben im alten Register;
kein Umbuchen, keine neue Freigabe für dessen zusätzliche Versuche.
Bereits bestätigte Nachweise sind nur bei unverändertem geprüftem Stand weiter
gültig; invalidierte und fehlende Nachweise werden am finalen neuen Stand erneuert.

## Problem

Die Skill-Änderungen von PLAN-0034 sind umgesetzt und unabhängig geprüft.
W-014 enthält trotzdem offene Pflichtnachweise. Der Nutzer will diese gemeinsam
mit den folgenden Helper-Änderungen im neuen Plan belegen.

## Drivers

- Ausdrücklich bestätigter Transfer der Restabnahme und Abschluss des alten Plans.
- Kein fälschliches PASS und keine verlorenen Nachweise oder Pflichtreviews.

## Considered alternatives

- W-014 zuerst in PLAN-0034 abnehmen: vom Nutzer nicht gewählt.
- W-014 ohne ausstehende Nachweise done setzen: wäre eine falsche Abnahme.

## Consequences

PLAN-0034 ist als Umsetzung abgeschlossen, die Gesamt-Skill-Abnahme bleibt
bis W-009 offen. Das ist keine Veröffentlichung, Installation, Freigabe für
CI oder Erweiterung des unabhängigen achtzig-Versuche-Budgets. Frühere private
CI-Freigaben aus PLAN-0034 werden nicht automatisch in den neuen Plan übernommen.
Die ursprünglichen Anforderungen und Historie bleiben in W-014 lesbar; die
verbleibende Ausführung und deren Berichte gehören PLAN-0035.

## Confirmation

Nach Transfer alle anderen PLAN-0034-Items terminal, W-014 cancelled mit
erhaltenen Teilnachweisen, Plan completed ohne current_item und Index idle
validieren. W-009 muss die offenen Skill-, Trigger-, Helper-, Workflow-,
Portabilitäts-, CI-, README- und Abschlussnachweise übernehmen.

## Revisit when

Restabnahme oder notwendige Korrekturen überschreiten absehbar das neue Budget,
oder der Nutzer ändert Aktivierung, Umfang oder Freigaben.
