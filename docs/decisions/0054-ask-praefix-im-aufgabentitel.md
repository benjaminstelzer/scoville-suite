---
format_version: 1
id: ADR-0054
status: superseded
created: 2026-09-25
accepted: 2026-09-25
scope: ask/naming-and-distribution
supersedes: ADR-0042
superseded_by: ADR-0055
---

# ASK steht am Anfang des Aufgabentitels

## Decision

Neue native ASK-Aufgaben heißen exakt `ASK <Titel der aufrufenden Aufgabe>`. Der Nutzer setzt ASK an den Anfang, damit die Kennzeichnung auch bei gekürzter Sidebar-Anzeige lesbar bleibt. Kein ASK-TASK-Suffix, keine Nummerierung, Modellnamen oder Adviser-ID im Titel. Soweit der Host die Sortierung unterstützt, stehen die Aufgaben weiterhin direkt über dem Aufrufer.

Die übrigen Festlegungen aus ADR-0042 bleiben erhalten: Der Skill heißt scoville-ask-for-codex, gehört zur Codex-Suite und wird zusätzlich im allgemeinen Suite-README einzeln installierbar mit dem Hinweis „Codex online“ angeboten. Die Ausnahme vom ausschließlichen Suite-Angebot betrifft ASK; Workflow bleibt unverändert. Die allgemeine Suite führt ASK nur im Katalog, nicht als zusätzliches Laufzeitmitglied.

## Problem

Bei langen Aufrufertiteln kann die bisher hinten stehende ASK-TASK-Kennzeichnung in der Sidebar abgeschnitten werden.

## Drivers

- Der Nutzer korrigiert die Reihenfolge ausdrücklich zu ASK vor dem Aufrufertitel.
- Zugehörigkeit und Lesbarkeit sollen ohne zusätzliche Titelbestandteile erkennbar sein.

## Considered alternatives

- Aufrufertitel mit ASK-TASK am Ende: Kennzeichnung kann außerhalb des sichtbaren Bereichs liegen.
- ASK vor dem Aufrufertitel: gewählte unmittelbar sichtbare Kennzeichnung.
- Adviser-ID oder Modellname ergänzen: nicht beauftragt und daher nicht Bestandteil der Änderung.

## Consequences

- Nur die Erzeugung neuer Titel ändert sich. Bestehende Aufgaben werden nicht rückwirkend umbenannt.
- Aufgaben werden weiter über Task-IDs und Handles zugeordnet; identische Titel sind keine Identität.
- Sidebar-Platzierung und Umgang mit fehlender Hostsortierung bleiben erhalten; fehlende Sortierung blockiert keinen ASK-Aufruf.
- README, Titelhelper und dessen direkte Verbraucher müssen dieselbe Form verwenden. Diese Entscheidung plant die Änderung und führt sie noch nicht aus.
- Vorhandene Veröffentlichungs- und Installationsgrenzen sowie die unveränderten Distributionsfestlegungen bleiben bestehen.

## Confirmation

1. Prüfe neue Titel für kurze, lange und Unicode-Aufrufertitel: ASK steht vorne und der Aufrufertitel bleibt erhalten.
2. Prüfe, dass keine zusätzlichen Modell-/Adviser-/Laufkennungen entstehen und ID-Zuordnung sowie Sidebarverhalten unverändert funktionieren.
3. Gleiche erzeugte Anleitung und Helperausgabe ab; bestehende Aufgaben bleiben unberührt.

## Revisit when

Der Nutzer weitere Titelbestandteile oder eine andere Sidebar-Anordnung wünscht.
