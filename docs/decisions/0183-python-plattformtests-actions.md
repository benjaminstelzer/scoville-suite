---
format_version: 1
id: ADR-0183
status: accepted
created: 2026-10-05
accepted: 2026-10-05
scope: suite/platform-acceptance
supersedes: ADR-0178
---

# Python-Plattformabnahme über Actions, WSL als ergänzender Linux-Host

## Decision

Der Nutzer stellt klar: Es gibt keine separaten Testhosts. Die Python-Tools
werden unter Windows, macOS und Linux über GitHub Actions geprüft. Native
Luna-Verbraucher auf dem verfügbaren Windows-Host bleiben erforderlich;
fehlende macOS-/Linux-Codex-Testhosts verhindern keinen Abschluss.
Der Nutzer beauftragt zusätzlich die Einrichtung eines Linux-Testhosts über
WSL. Vorhandenes WSL bevorzugen, Testumgebung isolieren und zusätzliche
Modellversuche vorab im gemeinsamen 80er-Register reservieren.

## Problem

ADR-0178 verlangte native Codex-Lektüre je OS und blockierte die Fortsetzung
wegen nicht vorhandener Hosts. Dies entspricht nicht der geklärten Abnahme.

## Drivers

Nutzer: „Es gibt keine testhosts, die Python Tools sollen über github Actions
getestet werden“. Ergänzung: „Linux Test host könntest du über WSL einrichten“.

## Considered alternatives

Separate macOS-/Linux-Codex-Hosts voraussetzen: vom Nutzer nicht vorgesehen.

## Consequences

Actions belegt Python-Mechanik und Shell-/Pfadverhalten je OS am exakten Stand.
Lokale native Consumer belegen direkt nutzbare Ausgaben und Rollenprotokolle.
Keine native macOS- oder eingeschränkte Sandbox-Wirkung aus CI ableiten.
WSL ist ein zusätzlicher Linux-Nachweis, kein macOS-Ersatz und keine allgemeine
Freigabe für Skill-Installation, Veröffentlichung oder Viewer-Kompilierung.
Bestehende Snapshot-Freigabe ADR-0182 bleibt auf ihren konkreten Umfang begrenzt.

## Confirmation

Matrix, Joblinks, Paketbindung, native Consumer und WSL-Ergebnisse getrennt
unter PLAN-0035 sichern. Fehlende oder abgeschnittene Nachweise offen ausweisen.
Die bisherigen Host-Blocker in W-002 entfallen nach dieser Nutzerentscheidung.

## Revisit when

Actions-Fälle neue Python-Änderungen nicht abdecken, WSL ungeeignet ist oder
ein weiterer freigabepflichtiger Snapshot beziehungsweise Build erforderlich wird.
