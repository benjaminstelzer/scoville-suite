---
format_version: 1
id: ADR-0229
status: accepted
created: 2026-10-30
accepted: 2026-10-30
scope: suite/quality
---

# Gemeinsame fachliche Kriterien für Autoren und Reviewer

## Decision

Binding sections: complete

Autoren verwenden schon bei Entwurf und Lösungswahl dieselben einschlägigen fachlichen Kriterien wie ihre spätere Abnahme. Jeder Kriterienbestand bleibt bei seinem verantwortlichen Owner. Rollenrechte, Prüfverfahren und Ergebnisformate bleiben getrennt; ein unabhängiger Reviewer darf übersehene Defekte anhand dieser Kriterien und neuer Belege feststellen, aber keinen strengeren Maßstab allein aus seiner Rolle ableiten.

Codequalität, statische Aufwandsprüfung, Cachekorrektheit und die Grundlage fehlender wie zusätzlicher Absicherungen stehen gemeinsam in code-quality.md. Code, UI-Code, Workflow und Ask nutzen denselben Bestand über ihre passenden Ladewege. Andere Artefakte werden nach ihren zuständigen Autorenkriterien geprüft, nicht nach Codekriterien. Die Entscheidung schafft keine zusätzliche Reviewphase oder Pflicht zu optionalen Geschwister-Skills.

## Problem

Ausführliche Kriterien wurden teilweise erst zur Abnahme geladen; Reviewer erhielten nicht alle Kriterien, nach denen Autoren Absicherungen und Caches wählen sollten.

## Drivers

- Ausdrücklicher Nutzerauftrag zur gemeinsamen Grundlage vor Schreiben und Abnahme.

## Considered alternatives

- Getrennte Fassungen je Rolle: erlauben widersprüchliche Kriterien und doppelte Pflege.

## Consequences

Feste Rollen- und Transportverträge bleiben bei ihren bisherigen Ownern. Bereits vollständig geladene unveränderte Regeln werden weiterverwendet. Kriterienparität belegt keine zuverlässige Modellbefolgung und begrenzt nicht die Zahl echter neuer Befunde.

## Confirmation

Autoren- und Reviewer-Ladewege sowie echte Helperaufträge prüfen. Die zwei Absicherungsfälle aus PLAN-0062 mit gpt-6.1-sol/low je nativer Route dreimal ausführen und beobachtete Ergebnisse getrennt von technischen Nachweisen berichten. Claude-Modellverhalten bleibt ohne eigenen Lauf ungeprüft.

## Revisit when

Der Nutzer ändert einen fachlichen Maßstab, die Rollenrechte oder die beauftragten Reviewgrenzen.
