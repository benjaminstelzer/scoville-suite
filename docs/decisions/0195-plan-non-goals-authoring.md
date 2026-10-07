---
format_version: 1
id: ADR-0195
status: accepted
created: 2026-10-06
accepted: 2026-10-06
scope: suite/plan-authoring
---

# Weitergabe von Non-goals beim Plan-Schreiben erklären

## Decision

Nach Erklärung von Wirkung und Grenze bestätigt der Nutzer:
„Ja, Astras Hinweis übernehmen“. Die Codex-Plan-Anleitung erklärt, dass Workflow
Non-goals wörtlich in jeden Child-Auftrag einschließlich Fortsetzungen kopiert.
Beim Schreiben oder ausdrücklich beauftragten Überarbeiten gehören erledigte
Entwurfsnotizen in Evidence. Astras engere Fassung wird übernommen.

## Problem

Ein historischer Entwurfshinweis in PLAN-0035 erreichte Children als laufender
Ausschluss. Seine konkrete Verschiebung ist bereits durch ADR-0194 genehmigt.
Die Anleitung nennt diesen Weitergabeeffekt bisher nicht.

## Drivers

Laufende Grenzen und abgeschlossene Beobachtungen verständlich einordnen,
ohne neue Aufräumroutine oder zusätzliche Befugnisse einzuführen.

## Considered alternatives

Keine Ergänzung: der Weitergabeeffekt bleibt unerklärt. Automatisches Entfernen
bei Aktivierung: von Astra abgelehnt, weil Aktivierung weder Ausführung noch
Autorisierung zum Entfernen bestehender Fakten bedeutet.

## Consequences

Nur der Codex-Hinweis wird ergänzt. Bestehende Freigabe-, Historien- und
Verschiebungsregeln bleiben verbindlich. Keine automatische Bereinigung,
keine Änderung weiterer Plan-Fakten oder der Recovery-Übergabe.

## Confirmation

Astra/high-Fassung und vollständiges Review liegen in
development/plan-evidence/0035-w009-external-followup-astra-high-review.json.
Profilprojektion, Bedeutungsvergleich und Paketprüfung genügen für diese
Erklärung. Kein zusätzlicher Luna-Lauf allein für den Hinweis.

## Revisit when

Der Hinweis als automatische Berechtigung zum Entfernen geltender Grenzen
verstanden wird.
