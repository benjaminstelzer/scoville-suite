---
format_version: 1
id: ADR-0111
status: accepted
created: 2026-09-28
accepted: 2026-09-28
scope: workflow/claude-review
---

# Claude-Reviewer mit Bash und Diff-Kontrolle

## Decision

Nutzerentscheid: Reviewer unter Claude haben `Read`, `Grep`, `Glob` und `Bash`, damit sie Tests und den Checkpoint ausführen können. Sie schreiben laut Anweisung nicht. Nach jedem Review prüft der Coordinator den Arbeitsbaum. Eine Änderung durch den Reviewer wird gemeldet und blockiert die Abnahme, bis sie geklärt ist. Änderungen an Dateien, die Git ignoriert, zählen nicht. Adviser (ADR-0107) bleiben ohne `Bash`.

## Problem

Codex-Reviewer führen Checks und den Checkpoint per Shell in einer read-only-Sandbox aus. Plugin-Agents ignorieren `permissionMode`, und mit `Bash` ist ein Claude-Reviewer nicht technisch schreibgeschützt.

## Drivers

- Review-Qualität wie bei Codex, einschließlich Testläufen.
- Höchstens ein Schreiber.

## Considered alternatives

- Reviewer ohne `Bash`: technisch schreibgeschützt, aber ohne Testläufe und ohne Reviewer-Checkpoint.

## Consequences

Der Schreibschutz der Reviewer beruht auf Anweisung und nachträglicher Erkennung. Der Diff-Abgleich kostet einen Aufruf pro Review.

## Confirmation

W-008 zeigt, dass eine Reviewer-Änderung am Arbeitsbaum erkannt wird und die Abnahme blockiert.

## Revisit when

Plugin-Agents unterstützen `permissionMode`, oder `Bash` lässt sich pro Agent auf Lesen beschränken.
