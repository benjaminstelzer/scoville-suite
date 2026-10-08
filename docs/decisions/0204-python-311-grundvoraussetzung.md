---
format_version: 1
id: ADR-0204
status: accepted
created: 2026-10-08
accepted: 2026-10-08
scope: suite/runtime
---

# Python 3.11 als Grundvoraussetzung

## Decision

Python 3.11+ ist die freigegebene Mindestvoraussetzung für die Python-Helper der Suite.

## Problem

Plan-General nennt teilweise Python 3.10, der gemeinsame Textprüfer verlangt 3.11.

## Drivers

- Eine einheitliche Runtime-Zusage soll widersprüchliche Aufrufanweisungen vermeiden.

## Considered alternatives

- Unterschiedliche Mindestversionen je Helper: zusätzliche Unterscheidungen beim Aufruf.

## Consequences

Runtime-Anweisungen und Kompatibilitätsangaben werden auf 3.11+ vereinheitlicht. Bestehende Profil- und Fallbackgrenzen bleiben erhalten.

## Confirmation

Gebautes Paket und betroffene Helperaufrufe unter Windows und Linux prüfen.

## Revisit when

Ein benötigter Host kann 3.11 nicht bereitstellen und eine unterstützte Alternative ist begründet.
