---
format_version: 1
id: ADR-0085
status: accepted
created: 2026-09-26
accepted: 2026-09-26
scope: suite/ask-native-ablauf
---

# Ask behält eigene Chats und direkt brauchbare Helper

## Decision

Die Vereinfachung gilt für alle in die Scoville-Suite integrierten Ask-Skills. Native Ask-Adviser behalten jeweils einen eigenen Codex-Chat; Subagenten sind kein Ersatz. Erstellung, Nachrichten und zulässige Archivierung verwenden Codex-Bordmittel direkt. Hostvorgaben für eine ausdrückliche Chatbeauftragung bleiben verbindlich; fehlende Autorisierung wird benannt und nicht durch einen anderen Ausführungsweg umgangen.

Verbleibende Helper liefern unmittelbar verwendbare Ergebnisse oder eindeutige Diagnosen. Der Agent muss keine Rückgaben reparieren oder fehlende Pflichtinformationen ergänzen. Dokumentiertes Auslesen und Parsen bleibt erlaubt. Die bestehende Claude-CLI-Route bleibt erhalten.

## Problem

Die integrierten Ask-Skills brauchen denselben schlanken Ablauf; reine Aufruftests prüfen die anschließende Verwendung der Helper-Rückgaben nicht.

## Drivers

- Nutzer verlangt einen schnelleren Ablauf ohne großes Zusatzsystem.
- Nutzer bestätigt ausdrücklich den eigenen Chat als beizubehaltenden Ask-Sonderfall.

## Considered alternatives

- Subagent statt Ask-Chat: erfüllt die gewünschte Ausführungsroute nicht.
- Rückgaben durch den Agenten korrigieren: verursacht zusätzlichen Aufwand und Fehler.

## Consequences

W-006 bearbeitet die in skills/private/scoville-suite integrierten Ask-Quellen und ihre kanonischen gemeinsamen Helper. Der Nutzer hat die Integration klargestellt; es gibt keinen separat zu suchenden Ask-Quellbestand und keinen separaten Build. W-007 und W-008 prüfen auch die unmittelbare Verwendung der Helper-Rückgaben.

## Confirmation

Reale Ask-Fälle verwenden eigene Chats. Helpertests führen den dokumentierten Folgeschritt ohne modellseitige Rückgabereparatur aus.

## Revisit when

Der Host unterstützt eigene Ask-Chats nicht oder ein Helper benötigt wiederholt Nacharbeit.
