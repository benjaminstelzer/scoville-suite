---
format_version: 1
id: PLAN-0064
status: completed
created: 2026-10-30
updated: 2026-10-30
---

# Lesewege und UTF-8-Diagnosen präzisieren

## Goal

Die freigegebenen kleinen Klarstellungen zu Layout und Quelldaten umsetzen, UTF-8-Diagnose und abhängige Stopps präzisieren und tatsächliche Lesewege in begrenzten gpt-6.1-sol/low-Läufen untersuchen. Owner sind ../shared/ und members/. Originalbytes, Kindstatus, vollständige erforderliche Texte und Rohdump-Schutz bleiben erhalten. Keine automatische Encodingvermutung oder Wiederholung von Produzenten. Der [Bericht](../testing/0064-lesewege-und-utf8-diagnosen.md) trennt Quellenprüfung, beobachtete Reads und Wirkung.

Auslieferung samt privater CI und öffentlichen main-Pushs ist freigegeben. Lokal Codex vollständig, bei Claude Code ausschließlich Plan aktualisieren. Keine neuen Tags, Releases oder unabhängigen Reviewpflichten. Die bereits freigegebene relevante Testauswahl in AGENTS.md wird mitgenommen.

## Non-goals

- Keine neue Ladeverwaltung, generelle Reviewschleife oder feste Rundengrenze.
- Kein erneuter Fix für den nicht mehr vorhandenen Ausdruck bundled Scoville Plan.
- Keine ungeprüfte Verkürzung erforderlicher Regeln oder Aussage über abgerechnete Tokens.

## Work items

### W-001 Klare Quellenlese- und UTF-8-Verträge
Status: done
Depends on: []
Blocked by: []
Decisions: []
Outcome: Die gemeinsamen Texte unterscheiden Quellen, Maschinendaten und Dekodierungsfehler eindeutig.
Acceptance: Layoutrest entfällt ohne geänderte Aktivierung. Quellsuchtreffer und Quelldiffs sind direkt lesbar, eingebettete Berichte bleiben auswertungspflichtig. UTF-8-Fehler erhalten Originalbytes und Kindstatus, benennen die offene Textauswertung und blockieren nur davon abhängige Arbeit. Keine Ersatzzeichen, Encodingvermutung oder Wiederholung. Betroffene Regressionen bestehen.
Instructions: Vorherigen unveränderten Gesamtpass wiederverwenden, nur betroffene Tests ausführen.
Steps:
1. [status: done] skill_composition.md, machine-data.md, output-delivery.md und check_text_size.py eng ändern; fertig nach Quellenvergleich und gezielten UTF-8-/Capturetests.
Evidence: Quellenänderung und gezielte Prüfungen dokumentiert; Originalbytes, Kindstatus, Rollen und vollständige Texte erhalten.

### W-002 Tatsächliche Lesewege untersuchen
Status: done
Depends on: [W-001]
Blocked by: []
Decisions: []
Outcome: Reale Reads und vermeidbare Ladekosten sind an begrenzten Aufgaben belegt.
Acceptance: Codeempfehlung und echter helpergenerierter Reviewauftrag werden mit gpt-6.1-sol/low ausgeführt. Native Aktionsbelege unterscheiden tatsächliche Reads, wiederholte Reads, Ausgabevolumen und Grenzen gegenüber Paketgröße oder Tokens. Nur beobachtete unnötige Reads begründen Änderungen; keine Regeländerung auf Verdacht. Reviewrechte und notwendiger Kontext bleiben erhalten.
Instructions: Read-only-Fixtures verwenden. Laufende Projektchats nicht einbeziehen. Kein neuer Runner oder Registry.
Steps:
1. [status: done] Bestehende Paket-/Prompthelper verwenden, zwei native Empfänger starten und deren tatsächliche Reads aus Turnaufzeichnungen auswerten; fertig bei je Fall konkretem Ladebefund und nachvollziehbarer Ergebnisgrenze.
2. [status: done] Nur belegte Ladeprobleme am zuständigen Quellenowner korrigieren und betroffene Fälle nachprüfen; fertig bei Korrekturbeleg oder begründeter unveränderter Regel. Reviewgrenzen und nicht vorhandenen Wortlaut im Bericht abschließen.
Evidence: Drei native Sol6.1/low-Fälle mit tatsächlichen Reads ausgewertet. Kein allgemeiner Ladegewinn belegt; Instruktionsdesign-Ladeauslöser präzisiert.

### W-003 Relevante Integrationsprüfung und Auslieferung
Status: done
Depends on: [W-001, W-002]
Blocked by: []
Decisions: []
Outcome: Der geprüfte Stand ist veröffentlicht und im freigegebenen lokalen Umfang installiert.
Acceptance: Betroffene Tests, Paket-/Link-/Exportprüfungen und erforderliche neue Python-Matrix bestehen. Alle geänderten manifestierten Ziele sind auf main remote verifiziert. Codex-Kopien und ausschließlich Claude-Plan sind aktuell, übriges Claude unverändert. Abgeschlossener Plan und Bericht enthalten ehrliche Grenzen.
Instructions: Unveränderte Prüfungen wiederverwenden, Metadatenupdates mit Profilvalidator prüfen. Keine unaufgeforderte Sessionfortsetzung.
Steps:
1. [status: done] Shared-Snapshot und Changelogs aktualisieren, gezielt prüfen und Kandidaten committen; fertig bei geprüfter Quelle und passenden Consumerpaketen.
2. [status: done] Erforderliche CI ausführen, bestehende Builds/Exporte veröffentlichen und lokale Pakete aktualisieren; fertig bei Remote- und Installationsbelegen im vorgegebenen Umfang.
3. [status: done] Plan und Bericht korrekt abschließen und Abschlussrecords ausliefern; fertig bei validiertem abgeschlossenem Profil und sauberer Quelle.
Evidence: Relevante Tests und Runtime-Matrix 41078747966 bestanden. Sieben Ziele remote geprüft, 17 lokale Kopien aktualisiert, übriges Claude unverändert. Ladegrenzen im Bericht.
