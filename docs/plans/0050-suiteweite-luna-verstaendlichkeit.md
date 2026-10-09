---
format_version: 1
id: PLAN-0050
status: completed
created: 2026-10-09
updated: 2026-10-09
---

# Alle Suite-Skills für Luna verständlich machen

## Goal

Die Routen und kritischen Entscheidungen aller Suite-Skills mit Luna 6/Medium prüfen und belegte Verständnisprobleme durch klarere, kürzere Texte beheben.

## Non-goals

Keine Prüfung realer Aufgabenimplementierung durch Luna, Installation, Veröffentlichung oder EMPCO-Aktionen. Keine Zugriffe auf XMAPI, XMTEST, Holzbau oder Zugangsdaten. Keine abgeschwächten Schutzregeln oder Erfolgsgarantie für ungesehene Aufgaben.

## Work items

### W-001 Routen und nötige Verständnisaufgaben bestimmen

Status: done
Depends on: []
Blocked by: []
Decisions: [ADR-0207, ADR-0208]
Outcome: Alle acht Skills haben eine begründete Aufgabenabdeckung ihrer unterschiedlichen Routen und kritischen Entscheidungen.
Acceptance: Einstiege, relevante Referenzen, gemeinsame Texte, Profile, Fallbacks und instruierende Helperausgaben sind berücksichtigt; jede relevante Entscheidung ist einer Aufgabe mit vorab festgelegten Kriterien zugeordnet; Anzahl und verbleibende Abdeckungslücken sind sichtbar; Opus 5.5/High hat Plan und konkrete Testaufgaben hinsichtlich des Verständnisziels abgenommen.
Instructions: []
Steps:
1. [status: done] Aktuelle Suitequellen und erzeugte General-/Codex-Texte einschließlich verlinkter Regeln lesen; unterscheidbare Routen und kritische Grenzen ableiten.
2. [status: done] Realistische Aufgaben, Rohfixtures und getrennte Kriterien vorbereiten; unabhängige Transferfälle vor Textkorrekturen einfrieren; ähnliche Fälle nur ohne Verlust einer entscheidenden Variante zusammenfassen.
3. [status: done] Plan, Aufgaben und Kriterien von der ursprünglichen Opus-5.5/High-Session b89b0e56-0d55-45ba-9df2-2bbe6ce859fe auf echte Verständnismessung prüfen lassen und verpflichtende Designfindings vor Dispatch beheben.
Evidence: Opus nahm 109 Aufgaben ab. Sol fror korrigierte Transferdaten vor Textarbeit ein; Astra prüfte die geänderten Stellen. docs/testing/0050-suiteweite-luna-verstaendlichkeit.md.

### W-002 Ausgangsverständnis mit Luna prüfen

Status: done
Depends on: [W-001]
Blocked by: []
Decisions: [ADR-0207]
Outcome: Die vorbereiteten Aufgaben haben unabhängige Luna-6/Medium-Antworten und konkrete Verständnisbefunde.
Acceptance: Sämtliche Aufgaben wurden mit aktuellen relevanten Texten ohne Lösungs- oder Findinghinweise beantwortet und gegen unveränderte Kriterien ausgewertet; Testprobleme, falsches Verständnis, unvollständige Antworten und Transportfehler sind getrennt beurteilt.
Instructions: []
Steps:
1. [status: done] Frische Luna-6/Medium-Testteilnehmer mit den nötigen Skilltexten und fiktiven Rohfakten beauftragen; nur Lesen und Antworten erlauben.
2. [status: done] Vollständige Antworten auswerten; bestätigte Verständnisfehler, richtige Entscheidungen und offene Grenzen knapp festhalten.
Evidence: 109 Rohantworten vollständig bewertet; Testprobleme und Skillbefunde getrennt. Initialurteile und Grenzen: docs/testing/0050-suiteweite-luna-verstaendlichkeit.md.

### W-003 Texte gezielt vereinfachen und erneut prüfen

Status: done
Depends on: [W-002]
Blocked by: []
Decisions: [ADR-0207]
Outcome: Belegte Verständnisfehler sind durch präzisere Skilltexte behoben, ohne erforderliches Verhalten zu verlieren.
Acceptance: Geänderte Texte bewahren Intent, Zuständigkeit, Reihenfolge, Berechtigungen und Schutzregeln; Korrekturen vereinfachen vorrangig bestehenden Text und sollen ihn verkürzen; jede neue Regel oder notwendige Erweiterung ist mit einer belegten Lücke begründet; frische Luna-Proben verstehen die korrigierten Entscheidungen; frühere Fehlschläge bleiben sichtbar; ursprüngliche Reviewer prüfen die Änderungen.
Instructions: []
Steps:
1. [status: done] Unveröffentlichten Ausgangsstand im temporären Bereich sichern; nur die zuständigen kanonischen Texte ändern und generierte Verbraucher aktualisieren.
2. [status: done] Fehlerfälle und erhaltenswerte richtige Entscheidungen mit frischen Luna-Medium-Proben erneut prüfen; bei verbleibendem Fehlverständnis Ursache klären und gezielt weiter korrigieren.
3. [status: done] Sol-6.1/Xhigh-Agent ask_sol0047_consensus und den vom Nutzer als Opus-Ersatz beauftragten Astra-Medium-Agent ask_astra0050_boundaries tatsächliche Änderungen und Belege prüfen lassen; bestätigte Findings bearbeiten.
Evidence: V5: zehn Textquellen, Guards erhalten; gezielte Entscheidungen neu verstanden. Sol und Astra nahmen Änderungen ab. docs/testing/0050-suiteweite-luna-verstaendlichkeit.md.

### W-004 Abdeckung und Endstand abnehmen

Status: done
Depends on: [W-003]
Blocked by: []
Decisions: [ADR-0207]
Outcome: Der verständlichere Endstand hat belegte Abdeckung, unabhängige Kontrolle und passende technische Integritätschecks.
Acceptance: Alle definierten kritischen Entscheidungen bestehen frische Verständnisfälle einschließlich neuer Transferfälle; relevante unveränderte Grenzen bleiben erhalten; Reviewerfindings sind verarbeitet; nur betroffene technische Checks bestehen unter Windows und Linux; Grenzen der Stichproben sind ausdrücklich benannt.
Instructions: []
Steps:
1. [status: done] Vom Entwicklungsfeedback getrennte Transferfälle mit frischen Luna-Medium-Teilnehmern prüfen und verbleibende Verständnisfehler im bestehenden Umfang beheben.
2. [status: done] Aus tatsächlichen Änderungen nötige Format-, Generierungs- und Verbraucherchecks ableiten; anwendbare Ergebnisse wiederverwenden und nur betroffene Checks unter Windows/Linux ausführen.
3. [status: done] Abdeckung, tatsächliche Ergebnisse, Reviewerprüfung und Grenzen knapp festhalten; erst nach belegter Acceptance Plan und Index abschließen.
Evidence: 26 Transferfälle und gezielte Ergänzungen geprüft; Sol/Astra nahmen V6 ab. Vier Checks je Windows/Linux PASS. Grenzen: docs/testing/0050-suiteweite-luna-verstaendlichkeit.md.
