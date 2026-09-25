---
format_version: 1
id: ADR-0070
status: accepted
created: 2026-09-25
accepted: 2026-09-25
scope: suite/legacy-members
---

# Vier nicht mehr enthaltene Altmitglieder ausmustern

## Decision

Der Nutzer beschließt: scoville-brainstorm, scoville-research, scoville-design-anti-ai-slop und scoville-scribe-anti-ai-slop ersatzlos aus der Suite ausmustern. Ihre Repositories werden erst beim freigegebenen Release privat. Die lokale Vorbereitung erfolgt jetzt; die GitHub-Sichtbarkeit wird erst in W-009 geändert.

## Problem

Die vier veröffentlichten Skills fehlen im aktuellen Manifest. Ihr endgültiger Verbleib musste für die Release-Migration festgelegt werden.

## Drivers

- W-001 benötigt eine eindeutige Zuordnung aller historischen Pakete.
- Fehlende Manifestmitgliedschaft allein begründet keine Stilllegung.

## Considered alternatives

- Ausmustern: Entspricht der aktuellen kleineren Suite und entfernt die alten Installationen bei der beauftragten Migration.
- Eigenständig behalten: Bewahrt die vier Angebote und erfordert eigene Zielnamen sowie einen klaren Ausschluss aus der Suite-Bereinigung.

## Consequences

- Die Entscheidung bestimmt Deprecated-Liste und Migration in W-003 und W-006.
- W-009 darf die Sichtbarkeit nur nach Annahme und erfüllten Releasegates ändern.
- Historie bleibt erhalten; die Entscheidung erlaubt keine pauschale Quelllöschung.

## Confirmation

1. Prüfe die ausdrückliche Nutzerentscheidung.
2. Gleiche Namenszuordnung und Migrationsprompt damit ab.
3. Prüfe beim Release die vier Remote-Sichtbarkeiten.

## Revisit when

Der Nutzer möchte eines der vier Angebote weiterführen oder ein belegter Nachfolger wird benannt.
