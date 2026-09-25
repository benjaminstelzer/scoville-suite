---
format_version: 1
id: ADR-0062
status: accepted
created: 2026-09-25
accepted: 2026-09-25
scope: prompting/worker-profiles
supersedes: ADR-0014
---

# Plan schreibt ohne Modellprofilresolver

## Decision

Gemäß angenommener ADR-0048 schreibt Plan direkt nach kompakten vollständigen Regeln. Modellprofilresolver, Profilkonfiguration und Profilreferenzen entfallen aus Plan. Workflow darf seine bereits vorhandenen Profile für zusätzliche Empfängeranweisungen zunächst behalten; W-010 prüft ihren Nutzen.

## Problem

Die bisherige gemeinsame Profilpflicht blockiert einfache Planänderungen und Python-3.10-Nutzung ohne Nutzen für die Zustandsregeln.

## Drivers

- Der Nutzer priorisiert weniger Komplexität und Tokenverbrauch.
- Empfänger erhalten weiterhin notwendige Fakten und keine vorausgesetzte Gesprächshistorie.

## Considered alternatives

- Profilpflicht mit Fallback behalten: zusätzliche Pfade für dieselbe Schreibaufgabe.
- Planprofil entfernen: gewählte direkte Vereinfachung.

## Consequences

- Workflow verändert den kanonischen Planpunkt beim Dispatch weiterhin nicht. Nur eigene Zusatzanweisungen können seinem verbleibenden Profil folgen.
- Risiko, Route, Modellwahl, Autorisierung und Abnahme bleiben von Formulierungshilfen unabhängig.
- Gemeinsame Schreibgrundsätze bleiben gültig; das Planpaket benötigt keinen zusätzlichen Profilimport.

## Confirmation

1. Prüfe das general-Planpaket unter Python 3.10 bis zur erfolgreichen Recordvalidierung.
2. Prüfe die weiterhin gebündelten Workflow-Helper und vergleiche die festgelegten Planfälle vor und nach der Änderung.

## Revisit when

Reale Planänderungen notwendige Empfängerinformationen verlieren.
