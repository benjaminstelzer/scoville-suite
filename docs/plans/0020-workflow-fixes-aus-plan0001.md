---
format_version: 1
id: PLAN-0020
status: completed
created: 2026-09-29
updated: 2026-09-29
---

# Workflow-, Plan- und Ask-Fixes aus dem EMPCO-Lauf PLAN-0001

## Goal

Scoville Workflow for Codex wartet ohne regelmäßige Statusabfragen, erhält beim Kontextwechsel seine tatsächlichen Einstellungen und offenen Entscheidungen und beauftragt zusammenhängende Korrekturen vollständig. Grundlage ist der EMPCO-Lauf ab 28.09.2026 mit acht Managern, 17 Workern und elf Reviewern im ausgewerteten Stand. Umsetzung am 29.09.2026 vom Nutzer beauftragt.

Zusätzlich autorisiert ein ausdrücklicher Nutzeraufruf von Scoville Ask nach ADR-0115 die benötigten Berater-Chats und die auftragsbezogene Kommunikation mit dem aufrufenden Chat ohne getrennte Bestätigungen.

Erweiterung: Die im Ablauf-Audit begründeten Helper werden umgesetzt. Jeder ausgelieferte Helper erhält eine einheitliche, beim Build strikt geprüfte Profilregel: General bevorzugt Helper und bietet einen getrennt ladbaren No-Python-Fallback; Codex enthält diese Fallbacks nicht. Testläufe und ihre Artefakte liegen im vom Nutzer angelegten Desktop-Projekt test.

Kanonischer Änderungsort für Workflow ist `members/scoville-workflow-for-codex/scoville-workflow-for-codex/`, insbesondere `references/operations.md`, `operations-rollover.md` und `operations-dispatch.md`. Plan und Ask liegen unter `members/scoville-plan/` und `members/scoville-ask-for-codex/`. Tests liegen jeweils unter `development/tests/`. Selector und Validator gehören zu `members/scoville-plan/scoville-plan/scripts/`, auch wenn der Selector nach Workflow exportiert wird. Nur die tatsächlich dort beheimateten Shared-Helper werden in `../shared/` gepflegt; generierte Kopien und Distributionen werden nicht direkt gepflegt.

## Non-goals

Keine Änderungen am laufenden EMPCO-Projekt oder Claude-Verhalten. PLAN-0019 bleibt auf ausdrücklichen Nutzerwunsch draft und wird nicht ausgeführt. Keine neue Setup-Pflicht, Zustandsdatei oder Bestätigungsrunde. Benennung, explizite Workflow-Aktivierung, alleiniger Produktschreiber, Deltareviews, Kontextschwellen, Archivierung und vollständiger Workflow-Ausstieg bleiben erhalten. Keine automatische Aufhebung historischer Nutzerstopps oder ungeprüfte Änderung der Plan-Semantik. Keine Installation, Veröffentlichung oder Releasefreigabe durch diesen Entwurf.

## Work items

### W-001 Ergebniszustellung und Host-Warten sind widerspruchsfrei

Status: done
Depends on: []
Blocked by: []
Decisions: []
Outcome: Der Manager wartet gemäß Host-Vertrag auf Ergebnisse, ohne regelmäßige Statusabfragen oder doppelte Dispatches aus Timeouts abzuleiten.
Acceptance: Fälle für Erststart, Timeout bei laufendem Kind, Ergebniszustellung, Nutzerunterbrechung, Wiederaufnahme und unklare Zustellung führen jeweils zu genau einem zulässigen nächsten Schritt. Host-Pflichten bleiben erfüllt. Kein periodisches wait_threads/read_thread-Polling; gezielte Wiederherstellung fehlender Fakten bleibt möglich. Fortschrittsvorgaben des Projekts werden ohne routinemäßige Abfragen behandelt. Keine behauptete Tokenersparnis ohne Messung.
Steps:
1. Aktuellen Host-Vertrag gegen operations.md und dispatch abgleichen. An einem konkreten fehlgeschlagenen Ablauf unterscheiden, ob Handlungsdetails fehlen, eine Host-Grenze wirkt oder eine vorhandene Regel nicht befolgt wurde. Der beobachtete Stand enthält 144 wait_threads-Aufrufe, davon 80 wiederholte Zielabfragen mit Timeout; die Zahlen allein beweisen weder Ursache noch durchgehende Inaktivität.
2. Eine knappe Ablaufregel beim bestehenden Owner formulieren: Erststart, Timeout, Rückkehr zum Nutzer und Fortsetzung durch Ergebnis oder Nutzereingabe. Widersprechende Anweisungen ersetzen.
3. Verhalten mit kontrollierten Host-Ereignissen prüfen; erlaubte Wiederherstellung von Polling unterscheiden.
Evidence: docs/plan0020-implementation-evidence.md: Timeout-Fall mit Luna bestanden, technische Workflow-Tests bestanden.

### W-002 Rollover erhält Modell, Effort und offene Rückfragen

Status: done
Depends on: []
Blocked by: []
Decisions: []
Outcome: Der Nachfolger übernimmt die tatsächliche Manager-Modellkombination und den aktuellen Entscheidungsstand, unabhängig von Worker-/Reviewer-Routen.
Acceptance: Abweichende Projektdefaults und Worker-Modelle ändern das Manager-Paar nicht. Ein ausdrücklich autorisierter Modellwechsel bleibt möglich. Unbekannte tatsächliche Einstellungen werden nicht erfunden. Eine offene Frage wird samt Geltungsbereich und Antwortstand übernommen, eine vorhandene Antwort verarbeitet; dieselbe offene Frage wird nicht allein wegen Rollover erneut gestellt. Bei Unklarheit erfolgt gezielte Wiederherstellung. Nutzerstopps und sole-writer-Grenzen bleiben wirksam.
Steps:
1. operations-rollover.md und den tatsächlich verwendeten Erstellungsweg prüfen. Manager 1–7 liefen mit gpt-6-sol/high; Manager 8 wurde ausdrücklich mit gpt-6-astra/medium erstellt. Sechs frühere Übergaben ohne explizite Parameter behielten dasselbe Paar. Vor zusätzlichen Regeln die konkrete Lücke gegenüber dem bereits vorgeschriebenen Erhalt des gestarteten Paars bestimmen.
2. Herkunft und Weitergabe des tatsächlichen Manager-Paars sowie offene Frage, Antwortstand und nächste zulässige Aktion im bestehenden kompakten Handoff präzisieren, ohne neue Zustandsdatei.
3. Modellwechsel, fehlende Metadaten, unbeantwortete Frage und Antwort während der Übergabe mit erhaltenen Stops prüfen.
Evidence: docs/plan0020-implementation-evidence.md: Modell-/Frageübernahme in Luna-Fällen bestanden; Herkunft und Parameter präzisiert.

### W-003 Korrekturaufträge erfassen den betroffenen fachlichen Zusammenhang

Status: done
Depends on: []
Blocked by: []
Decisions: [ADR-0102]
Outcome: Wiederkehrende Befunde derselben Zustandsunterscheidung werden als begrenzter zusammenhängender Korrekturauftrag behandelt.
Acceptance: Der Fall unbekannt/bestätigt geändert/Pflichtlücke/Dynamikwarnung umfasst die direkt betroffenen Statusverbraucher und Negativfälle. Ein isolierter Befund bleibt klein. Neue Nutzeranforderungen werden von vorhandenen Defekten unterschieden. Kein pauschales Vollreview oder zusätzliche Pflichtmatrix; unveränderte geprüfte Bereiche werden weiter wiederverwendet und frühere Reviews nicht abgeschafft.
Steps:
1. Bestehende Regeln zu Ursache, zwei Korrekturversuchen und Deltareview gegen die W-315-Kette prüfen. Die zwischenzeitliche Nutzerpräzisierung gehört zur Ursache der Umfangsänderung.
2. Im Dispatch-/Korrekturvertrag eine begrenzte Prüfung der betroffenen Zustandsunterscheidung und direkten Verbraucher verankern; nötigenfalls eine kleine Falltabelle im Auftrag, keine neue globale Prozessstufe.
3. Zusammenhängende Fehlerkette, isolierten Fehler und veränderte Nutzeranforderung als Gegenfälle prüfen.
Evidence: docs/plan0020-implementation-evidence.md: Zusammenhängende Korrektur und neue Nutzeranforderung im Modellfall korrekt abgegrenzt.

### W-004 Deployment-Zuständigkeit ist entscheidungsreif beschrieben

Status: done
Depends on: []
Blocked by: []
Decisions: []
Outcome: Eine kurze Entscheidungsvorlage grenzt Auslieferungsarbeit von Koordination und Planpflege ab, ohne eine neue Rollenregel vorwegzunehmen.
Acceptance: Die Vorlage vergleicht Worker-Auslieferung mit Manager-Auslieferung anhand von Schreibzuständigkeit, vorhandener Autorisierung, Fehlerbehandlung, Kontextkosten und Wiederaufnahme. Sie unterscheidet Produktänderung, Deployment und Migration. Der autorisierte W-315-Deploy wird nicht als Berechtigungsverstoß bezeichnet. Eine Rollenänderung bleibt bis zur Nutzerentscheidung unimplementiert.
Steps:
1. Den vorhandenen Rollenvertrag und W-315-Ablauf prüfen: Worker 14 bereitete Pakete vor, Manager 5 führte wesentliche Auslieferungs- und Migrationsarbeiten aus.
2. Begründete Empfehlung als vorgeschlagene Decision nach dem Plan-Format ablegen und offene Umsetzung separat kennzeichnen. Dieses Item endet mit der entscheidungsreifen Vorlage, nicht mit einer Rollenänderung.
Evidence: docs/decisions/0116-workflow-auslieferung-worker.md ist entscheidungsreif; Rollenregel unverändert.

### W-005 Plan-Skill und Workflow erlauben eine eindeutige Abschluss- und Fortsetzungsentscheidung

Status: done
Depends on: []
Blocked by: []
Decisions: []
Outcome: Plan-Skill und Workflow enthalten den abgestimmten Abschluss-/Fortsetzungsvertrag; notwendige Korrekturen sind umgesetzt und gezielt geprüft.
Acceptance: Geprüft sind scoville-plan/SKILL.md, references/edit.md, native-project-lifecycle.md und die tatsächlichen Selector-/Validator-Verträge samt relevanten Tests. Fälle: abgenommener Punkt mit eindeutigem Nachfolger; unbekannter Nachfolger; abhängigkeitsbereiter, aber blockierter gewöhnlicher Nachfolger; blockierter ausdrücklich aufgezeichneter Rückkehrpunkt; widersprechende historische Priorität; alter bloßer Fortsetzungsstopp versus ausdrückliche neue Gesamtfreigabe; echter fachlicher/Sicherheits-/Kostenstopp; letzter Planpunkt; begrenzter Workflow-Auftrag. Für jeden Fall sind terminaler Status, current_item, Index, zulässige Fortsetzung und nötige Rückfrage konsistent. Beobachtete Abnahme wird nicht mit Ausführungsfreigabe gleichgesetzt. Notwendige Instruktions-/Helperkorrekturen sind umgesetzt und die betroffenen Tests bestehen. Eine Entscheidungsvorlage allein erfüllt die Acceptance nicht; eine offene materielle Entscheidung blockiert nur die davon abhängige Umsetzung. Erweist sich keine Korrektur als nötig, ist der unveränderte Vertrag anhand derselben Fälle belegt.
Steps:
1. Unter members/scoville-plan/ die kanonischen Instruktionen, Helper-Owner und Tests prüfen. Die aktuelle Regel fordert beim Abschluss einen zulässigen genauen Nachfolger. EMPCO ADR-0245 klärte nachträglich die Gesamtfreigabe; dies ist kein universeller Vorrang vor allen Stopps.
2. Prüfen, ob präzisere Fortsetzungs-/Prioritätsregeln genügen oder ob fachlicher Abschluss und Nachfolgerwahl entkoppelt werden sollten. Minimalen Fix mit konkreten Zustandsübergängen, betroffenen Dateien und überprüfbarer Acceptance ausarbeiten; erforderliche Nutzerentscheidungen kennzeichnen.
3. Materielle Semantikänderungen vor Umsetzung mit Alternativen und Migration/Kompatibilität als vorgeschlagene Decision vorlegen. Nach deren Annahme Instruktionen und gegebenenfalls Selector/Validator samt gezielten Tests gemeinsam anpassen; bereits autorisierte semantisch unveränderte Präzisierungen benötigen keine weitere Freigaberunde. Bestehende Planhistorie und Profile bleiben gültig oder erhalten eine ausdrücklich entschiedene Migration.
Evidence: docs/plan0020-implementation-evidence.md: Plan-Fälle bestanden; 80 Tests und Lifecycle-Test grün, Statusmodell unverändert.

### W-006 Gezielte Verhaltensprüfung belegt Fixes und erhaltene Abläufe

Status: done
Depends on: [W-001, W-002, W-003, W-005]
Blocked by: []
Decisions: []
Outcome: Ein kompakter Vergleich belegt die reparierten Abläufe und bewahrt das funktionierende Verhalten.
Acceptance: Ausgangsstand und Kandidat werden mit denselben relevanten Fällen verglichen. Einfache Prompt-Baseline wird für die geänderten Instruktionen mitgeführt. Verhaltensfälle prüfen Entscheidungen/Aktionen statt bloßer Wortvorkommen. Richtige Titel, explizite Aktivierung, ein Produktschreiber, hilfreiche Reviews, erhaltene Implementierung beim Handoff und klarer Abschluss ohne spätere implizite Reaktivierung bleiben erhalten. Struktur-/Helpertests und Modellbeobachtungen werden getrennt berichtet; Astra-Planreview gilt nicht als Ausführungsnachweis. Offene Host- oder Modelltests bleiben ausdrücklich offen.
Steps:
1. Bestehende Tests und Modellfall-Harness wiederverwenden. Gezielte Fälle aus W-001 bis W-003 und W-005 sowie Gegenfälle für die zu erhaltenden Abläufe auswählen.
2. Nach Umsetzungsfreigabe die betroffenen technischen Tests und gezielte Luna-Verhaltensfälle nach Repository-Vorgaben ausführen; bei Helperänderungen erfolgreiche Ausgabe direkt am vorgesehenen Consumer prüfen.
3. Ergebnisse, Grenzen und gegebenenfalls README-Auswirkungen dokumentieren. Kein Release oder Installation ohne entsprechenden Auftrag.
Evidence: docs/plan0020-implementation-evidence.md und docs/plan0020-helper-audit.md: gezielte technische und Luna-Vergleiche bestanden, Grenzen dokumentiert.

### W-007 Ask-Aufruf autorisiert Berater-Chats und ihre Kommunikation

Status: done
Depends on: []
Blocked by: []
Decisions: [ADR-0115, ADR-0117]
Outcome: Ask führt den Nutzerauftrag vollständig aus: Berater-Chats starten, nötige Nachrichten austauschen und Ergebnisse zurückgeben. Der Aufruf genügt; Ask hat kein eigenes Genehmigungssystem.
Acceptance: Ein ausdrücklicher Ask-Aufruf führt ohne zusätzliche Freigabeprüfung oder Bestätigung durch den gesamten Beratungsablauf. Es gibt keine Autorisierungsfelder, Zustimmungsbelege oder erneute Berechtigungsprüfung durch den Berater. Ein nativer Fall belegt Chat-Erstellung, Rückfrage und Ergebniszustellung an den richtigen aufrufenden Chat. Bloße Erwähnungen starten Ask nicht. Ausdrückliche Nutzergrenzen, Read-only und höherrangige Host-Vorgaben bleiben wirksam.
Steps:
1. In members/scoville-ask-for-codex/scoville-ask-for-codex/ SKILL.md, references/native.md, native-delivery.md, adviser.md und agents/openai.yaml die separaten Genehmigungsregeln entfernen. Eine Regel genügt: Der Nutzeraufruf beauftragt alle zur Beratung nötigen Schritte einschließlich Chat-Erstellung und Kommunikation. Der Berater braucht Auftrag und Beratungsreferenz, keinen Autorisierungsnachweis. Er antwortet normal im eigenen Chat; der Caller übernimmt Ergebnis und Rückfragen nach ADR-0117.
2. Die kanonischen README-Fragmente unter development/readme/scoville-ask-for-codex/ und vorhandene Tests unter members/scoville-ask-for-codex/development/tests/ nachführen. Generierte Dateien ausschließlich bauen.
3. Den vollständigen Ablauf sowie Nichtaufruf und ausdrücklichen Nutzerstopp gezielt prüfen; ohne neue Polling-Schleife oder Empfangsbestätigung.
Evidence: docs/plan0020-implementation-evidence.md: Native Astra-Rückfrage und Ergebnisabholung nach ADR-0117 bestanden.

### W-008 Ask erzeugt den nativen Beraterprompt direkt verwendbar

Status: done
Depends on: [W-007]
Blocked by: []
Decisions: []
Outcome: Ein kleiner Helper setzt Frage, Umfang, Beratungsreferenz und die kanonischen Berater-/Zustellregeln zu einem Klartextprompt zusammen.
Acceptance: Erfolgreicher Helper-Output wird ohne Reparatur direkt an create_thread übergeben; der Caller übernimmt Antwort und nötige Rückfrage aus dem bekannten nativen Beraterchat. Fehlende Eingaben liefern eine konkrete Diagnose ohne Teilprompt. UTF-8-Inhalte bleiben erhalten. Keine Autorisierungsfelder, eigene Modellentscheidung oder Threadverwaltung oder zweite Regelkopie im Helper.
Steps:
1. scripts/build_adviser_prompt.py beim Ask-Member ergänzen und über suite.json ausliefern; Frage aus UTF-8-Datei, Modus, Umfang und Referenz als Parameter, optionale Caller-Herkunft aus CODEX_THREAD_ID oder explizitem Override. Native Startargumente übernehmen aufgelöste Berater-ID, Modell und Effort; Titel SC-ASK-ADVISER: Text ohne Nummer oder Projekt.
2. Native Aufrufanleitung auf Helper plus direkten create_thread-Aufruf reduzieren; README und gezielte Tests nachführen.
3. Erfolgreichen Output direkt in einem beauftragten nativen Beratungsfall verwenden und Fehler-/Unicodefälle testen.
Evidence: docs/plan0020-implementation-evidence.md: Unverändertes Helper-JSON nativ verwendet; 33 Ask-Tests einschließlich finalem Titel bestanden.

### W-009 Gesamtablauf zeigt sinnvolle Helper-Grenzen und erhält die Profiltrennung

Status: done
Depends on: [W-008]
Blocked by: []
Decisions: []
Outcome: Ein gezielter Durchlauf von Workflow, Ask und Plan-Anbindung benennt belegte Helper-Lücken und überflüssige Automatisierung.
Acceptance: Einstieg, Auswahl, Worker-/Reviewer-/Korrekturprompt, Rückfragen, Kontextübergabe, Ergebnisannahme und Abschluss sind mit tatsächlich verfügbaren Helpern und begrenzten Modellfällen geprüft. Der Bericht trennt ausgeführte Checks, Simulation und ungetestete Host-Interaktion. Empfehlungen nennen vermiedenen Fehler und kleinsten Helper; keine Geschwindigkeitsbehauptung ohne Messung. Codex hat keinen manuellen Helper-Fallback. Allgemeine Skills bevorzugen Helper und laden nur bei fehlendem Python einen separaten Fallbacktext.
Steps:
1. Reale Helper in einem Wegwerfprojekt über Auswahl, Review, Korrektur, Handoff und Planabschluss verbinden; keine Live-Produktarbeit.
2. Modellfälle mit erzeugten Prompts prüfen und manuell zusammengesetzte Übergänge identifizieren.
3. Codex-/General-Ausgaben vergleichen und begründete Helper-Empfehlungen dokumentieren, ohne neue Ablaufverwaltung einzuführen.
Evidence: docs/plan0020-implementation-evidence.md: Gesamtablauf geprüft; native/simulierte Checks und Hostgrenzen im Bericht getrennt.

### W-010 Native Startargumente und Manager-Übergaben werden deterministisch gebaut

Status: done
Depends on: []
Blocked by: []
Decisions: []
Outcome: Ein Manager-Builder und die erweiterten Ask-/Dispatch-Builder liefern direkt verwendbare native Startargumente samt korrektem Titel, Modell und Effort. Titel beginnen mit SC-WRK-n, SC-MGR-n, SC-REV-n oder SC-ASK-n, gefolgt vom exakten Projektnamen. Nur die Kürzel sind uppercase; eingesetzte Inhalte behalten ihre Schreibweise; alle erzeugten Chats werden anhand ihrer zurückgegebenen ID angepinnt.
Acceptance: Worker, Reviewer, Korrektur und Fortsetzung behalten die bestehenden Zähler- und Scope-Regeln. Manager übernehmen ihr eigenes tatsächlich gestartetes Modell/Effort statt Astra-medium-Reviewerwerten oder Defaults. Fehlende Identität oder Einstellungen ergeben Diagnose ohne Teilauftrag. Offene Fragen, Stops und erledigte Arbeit bleiben in der kompakten Übergabe erhalten. Erfolgreiche Ausgaben sind direkt am vorgesehenen Consumer geprüft; keine neue Ablaufverwaltung.
Steps:
1. Manager-Übergabe-Builder beim Workflow-Member ergänzen und die vorhandenen Ask-/Dispatch-Builder um native Erstellungsargumente erweitern.
2. Aufrufreferenzen und kanonische README-Fragmente nachführen, aus den Quellen bauen und Regressionen einschließlich falscher Manager-Einstellungen prüfen.
Evidence: docs/plan0020-implementation-evidence.md: Native Consumer, eigene Manager-Einstellungen und finale Titel/Rollover-Reihenfolge geprüft.

### W-011 Jeder Helper hat einen strikt geprüften profilspezifischen Fallback-Vertrag

Status: done
Depends on: []
Blocked by: []
Decisions: []
Outcome: Manifest, Projektregeln und kanonischer Shared-Builder erzwingen eine einheitliche Helper-first-Struktur für jede ausgelieferte Runtime-Datei.
Acceptance: General-Einzelpakete und allgemeiner Suite-Build haben pro aufrufbarem Helper genau einen getrennten, nur ohne Python ladbaren Fallback unter references/fallbacks/. Codex hat weder diese Dateien noch ihre optionalen Aufrufregeln. Bibliotheken sind ausdrücklich erfasst. Nicht registrierte Helper, fehlende Fallbacks, falsche Verlinkung, bedingungslose Einbindung und Codex-Leaks lassen Build und Paketprüfung fehlschlagen. Negativtests belegen jede Grenze; bestehende gültige Pakete bleiben baubar.
Steps:
1. Helper-Inventar im Manifest erfassen, vorhandene Plan-Fallbacks vereinheitlichen und gemeinsame Routingtexte daraus erzeugen.
2. Kanonische Build-/Verify-Wege und Projektregeln ergänzen, beide General-Layouts und Codex mit positiven und mutierten negativen Fällen prüfen.
Evidence: docs/plan0020-implementation-evidence.md: 37 Suite- und 4 Profiltests bestanden, einschließlich isolierter Exporte und negativer Fallback-Verträge.
