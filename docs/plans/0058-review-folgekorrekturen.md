---
format_version: 1
id: PLAN-0058
status: completed
created: 2026-10-29
updated: 2026-10-29
---

# Folgekorrekturen am veröffentlichten Skillbestand

## Goal

Die beauftragten Reviewbefunde A1–A19 an den kanonischen Quellen prüfen und bestätigte Lücken mit kleinen Änderungen am verantwortlichen Owner beheben. Feste Schnittstellen, bewusste Profilunterschiede und dokumentierte Testgrenzen erhalten. Der [Befundabgleich](../testing/0058-review-folgekorrekturen.md) enthält die überprüfbaren Anforderungen und ihren Stand.

PLAN-0057 bleibt abgeschlossen und samt seinen Audits privat. Seine autorisierte Altbestandsbereinigung wird nicht erneut untersucht; gelöschte ADRs werden nicht wiederhergestellt. Betroffene erhaltene ADRs bekommen nur den freigegebenen Revisionsvermerk. Setup behält einen ausdrücklich menschlichen manuellen Weg für Sonderstufen; Agenten verwenden weiter den Helper.

Dieser Folgeplan und seine verlinkten Records sollen nach ADR-0225 öffentlich exportierbar sein. Quellen, gezielte Prüfungen und Build sind autorisiert. Am 2026-10-29 hat der Nutzer mit „alles pushen“ auch die Veröffentlichung freigegeben; bestandene Abnahmen und die Prüfung des Exportinhalts bleiben Voraussetzung. Nur main, keine lokale Installation. Quellenbesitzer sind die Suite und ihr Shared-Geschwisterrepo; Distributionen werden generiert.

## Non-goals

- Keine Wiederöffnung von PLAN-0057, Prüfung gelöschter ADRs oder Änderung ihrer bereits freigegebenen Bereinigung.
- Keine neuen Helper oder Prüfrahmen; vorhandene Verträge und Tests gezielt korrigieren.
- Keine Änderung bewusster Profilunterschiede oder historischer Testfälle; alte Luna-Harnessquellen bleiben kanonisch erhalten, aber werden nicht öffentlich exportiert.
- Kein Push ohne erneute Freigabe, keine Tags, Releases, Branches, Worktrees oder Installation.

## Work items

### W-001 Quellenbefunde prüfen und gezielt korrigieren

Status: done
Depends on: []
Blocked by: []
Decisions: []
Outcome: Die bestätigten Text-, Lade- und Rollenfehler sind am kanonischen Owner korrigiert und falsche Teilbehauptungen begründet verworfen.
Acceptance: A1–A5, A7, A10–A14, A17–A19 und B2 besitzen einen belegten Zustand. Ladezeitpunkte, belegte Gegenrede, Korrektheitsprüfung, bedingte Fachpfade und menschliche Sonderstufen sind konsistent. Rollenrechte und bestehende Schnittstellen bleiben erhalten; unbekannte Mention-Semantik wird nicht als bewiesen dargestellt.
Instructions: Unabhängige Code/UI- und Ask/Workflow/Setup-Bereiche dürfen parallel bearbeitet werden; gemeinsame Quellen haben einen Owner. Nur Scoville Plan als Arbeits-Skill, andere Skilltexte sind Prüfgegenstand.
Steps:
1. [status: done] Befunde mit den betroffenen Member- und Shared-Quellen abgleichen; bestätigen oder begründet verwerfen, bei A7 native Mention-Semantik prüfen. Fertig, wenn der Befundabgleich den tatsächlichen Umfang und verbleibende Unsicherheit nennt.
2. [status: done] Bestätigte Änderungen an bestehenden Auslösern, Rollenaufträgen, Links und Diagnosen umsetzen; der schmale A4-Vertragstest schützt Rollenrechte und Prüfbereich, ohne ganze Sätze festzuschreiben. Fertig, wenn scoped Diffreview und betroffene Membertests bestehen.
Evidence: ["Quellenreview; Plan 125 (1 skip), Shared 6, Ask 55, Setup 20, Dispatch 12 und native Creation 12 bestanden. Wirkungsprüfungen folgen in W-004."]

### W-002 Build-, Export- und Testnachweise berichtigen

Status: done
Depends on: []
Blocked by: []
Decisions: [ADR-0225]
Outcome: Öffentliche Quellen enthalten aktuelle Entwicklungswege und überprüfbare Nachweise ohne irreführende Harness- oder Skip-Erfolge.
Acceptance: A6, A9, A15 und A16 sind geprüft; unbenutzte Exportreste entfallen, kanonische historische Harnessquellen bleiben erhalten. Nur übersprungene Tests zählen nicht als ausgeführt. Herkunftsbelege und Paketnormalisierung erfüllen ihren tatsächlich zuständigen Vertrag auch bei CRLF. Der öffentliche Plan samt verlinkten Records ist vollständig und valide.
Instructions: Keine neue Exportinfrastruktur; vorhandene Filter und Checks gezielt anpassen. A16 zuerst gegen die tatsächlichen Belegverträge reproduzieren.
Steps:
1. [status: done] Consumers der alten Instruction-/Luna-Harnesspfade, Tests und Claude-Capabilities prüfen; öffentliche Testlinks und Exportfilter korrigieren, verwaiste Template-/README-Reste entfernen. Fertig, wenn aktive Consumer erhalten und ausgeschlossene historische Dateien kanonisch unverändert sind.
2. [status: done] Shared-Native-Ausgabetest und Skipzählung korrigieren; Normalisierung über Snapshot, Buildreceipt und Runtime prüfen und nur bestätigte Fehler beheben. Fertig, wenn unabhängige Gegenfälle in den vorhandenen Tests bestehen.
3. [status: done] Exportkontext nach ADR-0225 am vorhandenen Owner dokumentieren; Folgeplan und verlinkte Records exportierbar halten. Fertig, wenn Index/Verweise im Export auflösen und der bestehende Planvalidator dort besteht.
Evidence: ["Exportfilter, Skipzählung und CRLF-Gegenfälle bestanden; beide öffentlichen Profile valide: 0 Fehler/0 Warnungen, aktiver PLAN-0058 und alle verlinkten Records enthalten."]

### W-003 Dokumentation und freigegebene Revisionen

Status: done
Depends on: [W-001]
Blocked by: []
Decisions: [ADR-0225]
Outcome: README, Changelog und Records beschreiben die Profile, aktuelle Verfahren und Herkunft korrekt.
Acceptance: A8 und B1/B5 sind umgesetzt; nur betroffene erhaltene ADRs tragen den Revisionsvermerk. Historische Codefälle bleiben unverändert markiert. General und Codex nennen passende Skillzahlen und trennen technische Unterstützung von Modelltests. Frühere Changelogs bleiben außer der ausdrücklich freigegebenen General-Zahlkorrektur unverändert.
Instructions: README-Quellen und Revisionsnotizen parallel vorbereitet; nach W-002 fortgesetzt und zentral generiert.
Steps:
1. [status: done] Tatsächlich betroffene erhaltene ADRs ohne Zugriff auf gelöschte Records bestimmen und den knappen datierten Revisionsvermerk ergänzen; keine inhaltliche Änderung und kein Link auf den privaten Plan. Fertig, wenn Recorddiff und Validator bestehen.
2. [status: done] Profilzahlen, Kompatibilität, Dokumentationsindex und historische Testkennzeichnung korrigieren; neue Changelogs ergänzen. Fertig, wenn gebaute README-Texte zutreffend sind und alle Links auflösen.
Evidence: ["Zwölf autorisierte Revisionsnotizen; Profil-/Kompatibilitätstexte, historische Kennzeichnung und Changelogs gebaut. Code-Testkatalog unverändert, alle öffentlichen Planlinks valide."]

### W-004 Verhalten und technische Abnahme

Status: done
Depends on: [W-001, W-002, W-003]
Blocked by: []
Decisions: []
Outcome: Relevante Agentenhandlungen und technische Gegenfälle belegen die korrigierten Verträge mit klaren Grenzen.
Acceptance: Geänderte Ladeauslöser A1/A2/A5 und Reviewer-Auftrag A4 sind in isolierten tatsächlichen gpt-6.1-sol/low-Läufen geprüft. Betroffene Member-/Shared-Tests und check_all.py bestehen. Eine neue Actions-Matrix ist nur bei geändertem paketiertem Python oder dessen CI-Tests erforderlich. Kein Claude-Verhalten aus Sol abgeleitet.
Instructions: Unveränderte Erfolge nicht wiederholen; Wortlaut allein ersetzt keine Wirkungsprüfung. Keine weiteren Modelltestfamilien.
Steps:
1. [status: done] Isolierte Aufgaben für Datenanforderung, strittige Schlussfolgerung, Shell-/Datenladen und unabhängigen Reviewer aus echten Paketen/Helpern ausführen; vollständige nötige Texte und Effekte auswerten. Fertig, wenn Ergebnis, Modell/Effort und Grenzen je Fall dokumentiert sind.
2. [status: done] Betroffene technische Tests und Gesamtgate ausführen, Quellenreview integrieren; gegebenenfalls erforderliche Runtime-Matrix ausführen. Fertig, wenn bestätigte Fehler behoben oder echte Grenzen ausdrücklich benannt sind und Commits nur nach Gesamtgate erfolgen.
Evidence: ["14 Sol6.1/low-Proben mit benannten Grenzen; unabhängiger Quellenreview ohne offene Befunde; check_all 12/0, 2 leere Pfade; Runtime lokal 23/23 und Actions 40910346436 6/6."]

### W-005 Build und konkrete Veröffentlichungsvorlage

Status: done
Depends on: [W-004]
Blocked by: []
Decisions: [ADR-0225]
Outcome: Ein geprüfter zentraler Build und ein klar begrenzter Exportinhalt liegen dem Nutzer zur Veröffentlichungsfreigabe vor.
Acceptance: Paket-/README-Prüfung und Export-Planvalidator bestehen; neue öffentliche Records sind auf sensible Inhalte geprüft. Pro A-/B-Befund sind Quelle, Nachweis, Verwerfung oder offene Entscheidung genannt. Geplante Repositories, Exportinhalt und verbleibende Online-Grenzen sind offengelegt. Kein öffentlicher Push vor neuer Freigabe.
Instructions: Vor Veröffentlichung ausdrückliche Nutzerfreigabe einholen. Zugangsdaten, persönliche Pfade oder Drittnamen in neu exportierten Records dem Nutzer vorlegen und nicht still veröffentlichen.
Steps:
1. [status: done] Bestehenden Build zentral unter skills/temp/release erzeugen; Profile, gemeinsame Basis, README, Ausschlüsse, öffentliche Records und Links prüfen. Fertig, wenn verifizierte Exporte und ihre Grenzen vorliegen.
2. [status: done] Ergebnis je Befund und geplanten Exportinhalt vorlegen; bis zur ausdrücklichen Freigabe nicht veröffentlichen. Fertig, wenn der Nutzer eine konkrete Veröffentlichungsvorlage hat.
Evidence: ["Vier Builds: Struktur und Veröffentlichungsgate bestanden. General/Codex-Export valide; neue Records ohne sensible Funde. Nutzerfreigabe: alles pushen (2026-10-29)."]

### W-006 Freigegebene Veröffentlichung abschließen

Status: done
Depends on: [W-005]
Blocked by: []
Decisions: [ADR-0225]
Outcome: Nur der ausdrücklich freigegebene Stand ist auf main veröffentlicht und remote verifiziert.
Acceptance: Neue ausdrückliche Freigabe liegt vor; betroffene Distributionen mit Changelogs, öffentlichem Plan und verlinkten Records stimmen mit dem geprüften Build überein. Keine Installation, Tags oder Releases. Abschließender Planstatus und offene Grenzen sind korrekt.
Instructions: Nutzerfreigabe „alles pushen“ vom 2026-10-29 liegt vor; erst nach bestandener Abnahme und geprüftem Exportinhalt veröffentlichen.
Steps:
1. [status: done] Nach Freigabe unveränderten Kandidaten prüfen, Distributionen auf main veröffentlichen und Remote-Inhalt verifizieren; fertig, wenn Freigabeumfang und Remote übereinstimmen.
2. [status: done] Plan und Abschluss mit tatsächlichen Ergebnissen und Grenzen abschließen; fertig, wenn Profil valide und erforderliche Abschlussrecords veröffentlicht sind.
Evidence: ["Acht öffentliche main-Stände gepusht und Remote-Commit, Inventar, Inhalt sowie Sichtbarkeit verifiziert. Keine Installation, Tags oder Releases; Grenzen im Befundbericht."]
