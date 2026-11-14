---
format_version: 1
id: ADR-0233
status: accepted
created: 2026-11-14
accepted: 2026-11-14
scope: suite/ui
---

# UI: Ein Code-Review liest nur den Quelltext

## Decision

Binding sections: complete

Scoville UI unterscheidet zwei Arten von Review:

1. Ein Code-Review von Oberflächen-Quelltext oder eines Diffs liest den Quelltext. Es rendert, misst und bedient nichts. Die Regeln zu Größe, Abstand und Ausrichtung prüft es am Quelltext und nennt als ungeprüft, was nur ein gerendertes Bild zeigt.
2. Ein Review, wie eine Oberfläche aussieht oder sich verhält, und eine verlangte gerenderte Prüfung rendern und messen.

Verlangt der Nutzer ein Review einer UI-Änderung, ohne Aussehen, Verhalten oder eine gerenderte Prüfung zu nennen, gilt Fall 1.

Diese Entscheidung ergänzt ADR-0230, die das Rendern beim Umsetzen ausschließt.

## Problem

ADR-0230 erlaubt das Rendern bei einem verlangten Review. Der UI-Skill benutzte „Review" für beides: für die Prüfung von Aussehen und Verhalten und für das Code-Review eines Diffs. Bei der Bitte „reviewe die UI-Änderungen in diesem Pull Request" konnte ein Modell nicht entscheiden, ob es einen Browser starten soll. Ein Review mit Opus 5.5 am 2026-11-13 meldete den Begriff als doppeldeutig.

## Drivers

- Ein gerendertes Review kostet das Zwei- bis Dreifache und braucht eine lauffähige Umgebung.
- Die häufigsten sichtbaren Mängel, abweichende Größen und Abstände neben bestehenden Elementen, lassen sich am Quelltext erkennen.
- Der Nutzer kann eine gerenderte Prüfung jederzeit ausdrücklich verlangen.

## Considered alternatives

- Jedes Review einer UI-Änderung rendert und misst: findet auch Mängel, die nur im Bild sichtbar sind, kostet aber bei jedem Review den Start der Oberfläche.

## Consequences

Ein Code-Review findet nicht, was nur gerendert sichtbar ist, etwa einen Überlauf bei schmaler Breite oder eine Verschiebung durch geerbte Regeln. Es meldet das als ungeprüft.

## Confirmation

SKILL.md und die Referenzen von Scoville UI nennen die beiden Arten überall beim Namen. Die Gesamtprüfung der Suite besteht.

## Revisit when

Code-Reviews übersehen wiederholt sichtbare Mängel, die ein gerendertes Review gefunden hätte, oder der Nutzer will die Grenze verschieben.
