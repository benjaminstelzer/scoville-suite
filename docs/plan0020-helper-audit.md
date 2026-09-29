# Helper-Prüfung des vollständigen Ablaufs

Geprüft am 29.09.2026: Workflow und Ask einschließlich Plan-Anbindung.
Technische Grundlage: 25 Workflow-, 33 Ask- und 80 Plan-Tests; zusätzlicher
Luna-medium-Durchlauf vom ersten Dispatch bis Abschluss und Nichtaktivierung.
Details und Grenzen stehen in `plan0020-implementation-evidence.md`.

| Abschnitt | Vorhandener Mechanismus | Bewertung |
| --- | --- | --- |
| Einstieg/Scope | Skill-Aktivierung, Plan lesen | Beim Agenten belassen: Nutzerabsicht ist keine mechanische ID-Operation. |
| Plan/Step auswählen | select_context.py | Wiederverwenden; kein zweiter Selector. Strukturelle Auswahl erteilt keine Startfreigabe. |
| Worker-/Reviewer-Modell | resolve_model_pair.py | Bereits deterministisch. Risikoeinschätzung bleibt fachlich. |
| Worker/Review/Korrektur/Fortsetzung | build_dispatch_prompt.py | Schon umgesetzt und im verbundenen Test ausgeführt. Fehlender Worker-Befund ergibt Diagnose, keinen manuellen Ersatzprompt. |
| Ask-Modell | ask.py resolve | Bestehenden Helper behalten. |
| Ask-Auftrag | neuer build_adviser_prompt.py | Sinnvoll und implementiert: liest Regeln einmal, erhält UTF-8-Frage und Beratungsreferenz. Tatsächlicher create_thread-Consumer geprüft. |
| Kontextgrenze | check_context_checkpoint.py | Behalten; unbekannte Telemetrie wird nicht geschätzt. |
| Manager-Übergabe | build_manager_handoff.py | Implementiert: eigene native Modellparameter und erste Übernahmenachricht deterministisch. |
| Titel/Startparameter | gemeinsame native_task_arguments.py plus vorhandene Builder | Implementiert: native Argumente und endgültige Titel ohne manuelle Reparatur. |
| Ergebnisbewertung/Nachfolger | Agent, Planregeln und Validator | Nicht durch einen Statusparser ersetzen: Acceptance, Nutzerstopps und Materialität erfordern Bewertung. |
| Nachrichtenzustellung | native Task-Werkzeuge | Ask holt normale Beraterantworten nativ ab; ADR-0117 umgesetzt und mit Astra geprüft. |
| Abschluss/Archivierung | native Tools und Planvalidator | Kein neuer Helper nötig; zusätzliche Empfangs-/Archivierungsprüfungen würden Aufwand erhöhen. |

## Umgesetzte Erweiterungen

Der Manager-Übergabe-Builder erzeugt den Prompt und die zugehörigen
nativen Erstellungsargumente aus denselben Fakten: Plan, Managernummer,
verifiziertes eigenes Modell/Effort, Vorgänger-ID und kompakter Handofftext.
Er gibt die Angaben direkt an create_thread weiter, ohne eigene Threads,
Wartezustände, Konfigurationsdatei oder manuelle Fallbackroute.
Offene Frage/Antwortstand, erledigte Arbeit und nächste Handlung bleiben
inhaltliche Auswahl des Managers. Der Helper kann deren Wahrheit nicht prüfen.

Die bestehenden Ask- und Worker-Builder bedienen denselben unmittelbaren Consumer. Das vermeidet
auseinanderlaufende Titel, Einheiten und Modellparameter. Kein neuer Wrapper,
der seinerseits wieder manuell ausgepackt oder bestätigt werden muss.

Diese Erweiterungen sind umgesetzt; eine zusätzliche Ablaufverwaltung wurde nicht eingeführt. Die belegte Modellabweichung beim
Manager und frühere Titelprobleme begründen sie; alle Titel allein wegen
allgemeiner Fehlerangst neu zu implementieren wäre nicht gerechtfertigt.

## Verbundener Modellfall

Luna erhielt die paketierten Instruktionen und einen geordneten Fall:
erster Worker 7 mit drei Steps, überprüfbarer Teilfix mit Handoff,
Managerwechsel mit abweichendem eigenem Modell, Review zu Step 1,
materiale Korrektur durch Worker 8 samt Review, Restarbeit durch Worker 9,
Planabschluss und gewöhnliche Folgefrage. Gegenfälle: generischer Planauftrag,
isolierter Tippfehler und fehlendes Worker-Ergebnis für Review.

Beobachtet: korrekte Titel und Zähler, Manager vor Worker-Nachfolger,
eigener Manager-Modellwert, passender Reviewer-Helper, erhaltene Restarbeit,
keine Wiederholung abgeschlossener Implementierung, kein manueller Ersatz
bei Helperfehler, vollständiger Workflow-Ausstieg.
Grenze: Modellentscheidungen simuliert, kein mehrstündiger produktiver
Mehrchat-Workflow. Tatsächliche Helper-Verbindungen wurden separat ausgeführt.

## Profile und Aufwand

Der Pakettest bestätigt: Codex enthält keine manuellen Plan-Fallbacktexte.
General enthält die getrennten Texte für Auswahl und Profilprüfung, die nur
bei fehlendem Python geladen werden. Ein Helperfehler aktiviert keinen Fallback.
Ask und Workflow haben ausschließlich den Codex-Helperweg.

Der Ask-Helper beseitigt das manuelle Zusammenstellen zweier Regeltexte und
der nativen Startargumente. Das ist weniger wiederholte Agentenarbeit,
aber noch kein gemessener Laufzeit- oder Tokengewinn. Es wurde kein seriöser
Geschwindigkeitsbenchmark durchgeführt. Die Vergleiche belegen konkrete
Verhaltensunterschiede, nicht allgemeine Überlegenheit oder feste Prozentwerte.

Finale Testzahlen, Titelpräzisierungen und Evidenzgrenzen stehen in plan0020-implementation-evidence.md.
