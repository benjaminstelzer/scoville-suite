---
format_version: 1
id: ADR-0171
status: accepted
created: 2026-10-05
accepted: 2026-10-05
scope: workflow/direct-handoff
---

# Gerichteten Manager-Handoff ohne Hashprüfung fortsetzen

## Decision

Wenn der Vorgänger den exakten Nachfolger nach dessen authentifizierter Anfrage
mit `live agent path ... not found` nicht per `send_message` erreicht, darf er
denselben fachlichen Handoff in eine UTF-8-Datei im gemeinsamen temporären
Workspace schreiben. Der Runner leitet nur den Pfad an den bekannten Nachfolger
weiter und liest keinen Inhalt. Der Nachfolger liest vollständig, gleicht mit
Plan und Dateien ab und bestätigt direkt beim Vorgänger. Native Abschlüsse und
TAKEOVER_COMPLETE bleiben Pflicht. Unklare Zustellung und andere Fehler bleiben
blockiert; es gibt keinen Respawn oder generischen Retry.

Im ausgelieferten Skill- und Workflow-Lauf keine Hashwerte zur Verifizierung
dieses oder anderer Handoffs verlangen. Hashes als Kennungen sind zulässig.
Build-/CI-Prüfsummen für Paketnachweise sind davon getrennt.

## Problem

Ein realer, wiederaufgenommener Manager konnte einen laufenden neuen Sibling
einseitig nicht adressieren. Der bestehende Vertrag blockierte korrekt, hatte
aber keinen Weg zur Fortsetzung desselben Handoffs.

## Drivers

Der Nutzer erlaubt Skill-Korrekturen und verlangt einen einfachen Dateiweg ohne
Hashprüfung oder zusätzliche Sicherheitslayer, auch gegenüber bestehenden
Skill-Anweisungen. Hashes für Kennungen hat er ausdrücklich zugelassen.

## Considered alternatives

Inhalt über den Runner weiterzureichen verletzt dessen Rollenbegrenzung.
Blindes Wiederholen oder ein neuer Manager behebt die beobachtete Route nicht.
Bloßes Blockieren lässt den konkret wiederherstellbaren Auftrag stehen.

## Consequences

Der Pfad ist temporärer Transport, kein neues Plan- oder Berichtsspeicherformat.
Exakte Agentenidentitäten, kanonischer Abgleich, direkte Quittung und
Schreibergrenze gelten unverändert. Die Hostursache bleibt extern.
Während der Übernahme beendet ein einzelner Wait-Timeout weder die Wartephase
des Vorgängers noch die des Nachfolgers. Beide warten mit begrenzten einzelnen
Aufrufen weiter, bis die authentifizierte Quittung und Freigabe eintreffen oder
STOP beziehungsweise ein tatsächlich ungelöstes BLOCKED den Übergang beendet.
Das vermeidet einen künstlichen Abbruch vor der Pflichtquittung; ein ausgebliebener
Hostschritt wird nicht als Erfolg behandelt.

## Confirmation

Die gebauten Skill-Texte und echte Manager-Verbraucher auf den normalen und
den eindeutig abgewiesenen Pfad prüfen. Fehler und unvollständige Leseausgabe
dürfen nicht als erfolgreiche Übergabe erscheinen. Bestehende Laufzeitstellen
auf Hash-Verifizierung prüfen; Kennungsbildung und Build-/CI-Nachweise getrennt
ausweisen.

## Revisit when

Der Host einen verlässlich funktionierenden direkten Nachrichtenweg anbietet
oder die Rollen- und Quittungsgrenzen geändert werden.
