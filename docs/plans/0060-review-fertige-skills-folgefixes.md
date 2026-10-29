---
format_version: 1
id: PLAN-0060
status: active
created: 2026-10-29
updated: 2026-10-29
current_item: W-009
---

# Folgefixes aus dem Review der ausgelieferten Skills

## Goal

Die zwölf Befunde und optionalen Vorschläge des externen Reviews vom 2026-10-29 gegen die kanonischen Quellen prüfen und bestätigte Lücken mit der einfachsten tragfähigen Lösung beheben. Das Review untersuchte die zuletzt veröffentlichten acht Repositories statisch; es enthält keine ausgeführten Helper- oder Modelltests. Behauptete Laufdefekte vor ihrer Korrektur isoliert reproduzieren. Fachliche Abnahmen, Rollenrechte, vollständige notwendige Inhalte und Schutz vor Rohdumps bleiben erhalten.

Owner sind `members/` in der Suite und `../shared/`; daraus entstehen General, Mainloop und die Einzelpakete mit derselben fachlichen Basis und begründeten Profilunterschieden. Gemeinsame Quellen haben jeweils einen Editor; unabhängige Memberarbeiten haben keine fachliche Reihenfolgeabhängigkeit. Maßstab für Texte ist `../shared/prompting/instruction-design.md`. Modellprüfungen verwenden ausschließlich `gpt-6.1-sol` / `low` und bewerten tatsächliche Aktionen und Ergebnisse. Der Claude-Pfad erhält nach ADR-0227 einen Transportnachweis mit aufzeichnendem CLI-Platzhalter; Claude-Verhalten bleibt ungeprüft.

Quelländerungen erfolgen ausschließlich in dieser kanonischen lokalen Struktur. Öffentliches `members/` ist je Suite profilaufgelöst; `development/shared/` ist ein generierter Snapshot. Diese Online-Kopien ersetzen weder die ursprünglichen Profilblöcke noch das Shared-Geschwisterrepo oder private Testdaten.

ADR-0225 verlangt die Freigabe des konkreten geprüften Veröffentlichungsstands; ADR-0226 schützt private Namen.

Zur Umsetzung gehört bei benötigten Plattformnachweisen der Testkandidaten-Push auf main ausschließlich in das bestehende private Repository `benjaminstelzer/scoville-runtime-ci`. Dieser Testweg liegt vor der öffentlichen Veröffentlichungsfreigabe; er veröffentlicht keine Skills.

## Non-goals

- Keine pauschale Neuformulierung aller Skills, neue Helper-Infrastruktur oder zweite Parserarchitektur.
- Keine feste Zahl erlaubter Korrekturrunden, globalen Zeitbudgets oder Ausnahme für kleine Rohdumps.
- Keine ungeprüfte Behauptung zusätzlicher Tokenkosten, allgemeiner Modellzuverlässigkeit oder Claude-Wirkung.
- Keine Änderungen fremder Projekteinstellungen, Historien, Tags oder Releases.
- Keine Bearbeitung der offenen externen Klärung aus PLAN-0059.
- Keine eigenmächtige Lifecycleumstellung von PLAN-0059 oder dessen W-004 beim Wechsel des aktiven Plans.

## Work items

### W-001 Plan-Grenzen und Diagnosen konsistent machen

Status: done
Depends on: []
Blocked by: []
Decisions: []
Outcome: Validator und Selector verwenden denselben dokumentierten Strukturvertrag und führen bei ungültigen Eingaben zur tatsächlichen Korrektur.
Acceptance: Unterschiedliche Layoutannahmen von Validator und Selector sowie fehlende oder irreführende Plan-Diagnosen sind reproduziert oder begründet verworfen. Für dieselben Strukturgrenzen widersprechen sich gültige Validator- und Selector-Ergebnisse nicht; Diagnose nennt betroffene Stelle und nächsten Schritt. Gültiger Originalinhalt und Fence-Behandlung bleiben erhalten, Folgefehler verdecken keine eigentliche Parseursache.
Instructions: []
Steps:
1. [status: done] `members/scoville-plan/scoville-plan/scripts/{select_context.py,validate_profile.py,markdown_structure.py}` und den nativen Formatvertrag abgleichen. Gegenfälle für Einleitung nach H1, Leerzeilen, Unterüberschriften und Text vor dem ersten Work Item erstellen. Fertig, wenn echte Vertragsverletzung von unnötiger Formatstrenge unterschieden und ein gemeinsamer Sollvertrag begründet ist; keine Verschärfung allein zur Anpassung an den strengeren Parser.
2. [status: done] Kleinste Korrektur am bestehenden Struktur-/Diagnoseowner umsetzen und vorhandene Plan-Tests erweitern. Primärfehler statt irreführender Lifecycle-Folgefehler prüfen. Prüfen, ob Next-ID abweichend benannte Dateien bei der nächsten ID nicht mitzählt und dadurch trotz vorhandener Kollisionsdiagnose IDs übersehen kann; nur eine belegte Lücke beheben. Fertig bei bestandenen positiven und negativen Fällen für betroffene Selector-Modi sowie Validator.
Evidence: Fünf Abweichungen reproduziert; gemeinsamer Strukturvertrag korrigiert. 128 Plan-Tests (1 POSIX-Skip) und 7 Diagnose-Gegenfälle bestanden; Next-ID blendet fehlerhafte Recordnamen nicht aus.

### W-002 Workflow-Pfade und Helper-Eingaben berichtigen

Status: done
Depends on: []
Blocked by: []
Decisions: [ADR-0224]
Outcome: Workflow-Aufträge lösen Decisions auch unter einem verlinkten Workspace-Vorfahren korrekt auf und melden Eingabefehler direkt.
Acceptance: Die behauptete fehlschlagende Decision-Auflösung bei verlinktem Workspace-Vorfahren ist isoliert nachgestellt und behoben oder anhand geprüfter Quellen und Laufbelege begründet verworfen; direkte Root und Root unter einem verlinkten Vorfahren liefern dieselbe autorisierte Auswahl. Root selbst als Symlink oder Reparse-Point bleibt vor Normalisierung entsprechend dem Selectorvertrag mit ROOT_INVALID abgewiesen. Tatsächliche Pfadausbrüche und unzulässig verlinkte Recorddateien bleiben abgewiesen. Belegte Argument-/Dokumentationslücken sind am Helpervertrag korrigiert.
Instructions: []
Steps:
1. [status: done] `members/scoville-workflow-for-codex/scoville-workflow-for-codex/scripts/build_dispatch_prompt.py`, `decision_sources` und die Plan-Pfadprüfung zusammen prüfen; einen bestätigten Normalisierungsfehler am zuständigen Eingang unter Erhalt der Eingangssperren beheben. Fertig nach Fällen für direkte Root, verlinkten Vorfahren, Root selbst als Link und tatsächlichen Pfadausbruch; eingeschränkte Symlinktests als Skip ausweisen, nicht als Widerlegung des Befunds.
2. [status: done] Einfache Argumentfehler vor abhängigen Validator-/Selector-Aufrufen behandeln und tatsächlich angebotene Optionen in `references/operations-dispatch.md` erläutern. Lebensdauer temporärer Aufträge nur bei bestätigtem Problem korrigieren; keine Datei entfernen, die ein Empfänger noch braucht. Fertig bei passenden Helpertests und unverändertem Einzelstep-/Decision-/Rollenvertrag.
Evidence: Verlinkter Vorfahr unter Windows reproduziert und korrigiert; Root-/Recordlinks weiter gesperrt. 85 Workflow-Tests bestanden; frühe Argumentprüfung und Helperoptionen abgeglichen.

### W-003 Capture-Ausgaben auch bei Hängern und Encodingfehlern erhalten

Status: done
Depends on: []
Blocked by: []
Decisions: [ADR-0204]
Outcome: Capture behält ursprüngliche Ergebnisse und gibt bei begrenztem Warten kontrolliert die Steuerung zurück.
Acceptance: Unbegrenztes Warten, geerbtes stdin und Verlust ungültiger UTF-8-Ausgabe des Python-Helpers sind mit isolierten Kindprozessen auf POSIX und Windows geprüft. Nichtinteraktive Capture wartet nicht auf geerbte Eingabe. Ungültiges UTF-8 eines Einmaleffekts bleibt bei beauftragtem Speichern als Originalbytes mit Exitstatus erhalten, ohne als gültiger Text oder Erfolg zu gelten. Die native JavaScript-Vorlage ist auf dem verfügbaren Codex-Host geprüft; ohne POSIX-Codex-Host bleibt ihre native POSIX-Ausführung ausdrücklich ungeprüft. Python-CI ersetzt keinen Hostnachweis. Laufende Prozesse und unvollständige Ausgaben bleiben eindeutig erkennbar; kein automatischer Neustart.
Instructions: []
Steps:
1. [status: done] `../shared/runtime/check_text_size.py` mit EOF-/Eingabe-, langsamem Prozess-, ungültigem UTF-8- und Einmaleffektgegenfall prüfen. Native Begrenzung zuerst nutzen, Helper-Timeout nur für eine konkrete verbleibende Lücke; POSIX-/Windows-Abbruchmechanik in Ask `scripts/ask_claude.py` als Referenz nutzen, ohne Geschwisterpaket-Abhängigkeit. Windows lokal und fehlendes POSIX über die private Runtime-Matrix auf Linux/macOS prüfen. Vor deren erstem Lauf die Python-3.10-Mindestversionsstufe in `../shared/runtime-tests/runtime-helpers.yml` entfernen und ihre erforderlichen Fälle in der gültigen 3.11-Matrix erhalten. Gegenfälle in `../shared/runtime-tests/test_runtime_helpers.py` ergänzen; Kandidat mit `development/build_suite.py --prepare-runtime-ci <neues Verzeichnis außerhalb des Quellbaums>` erzeugen und in die private CI pushen. Hänger-Fixtures besitzen eigene kurze Limits unter dem Joblimit. Fertig bei erfolgreichen Helper-Plattformläufen mit erhaltenen Streams, Exitstatus und Prozesszustand; fehlende Nachweise halten das Item offen. Abbruch erlaubt keine Wiederholung.
2. [status: done] `../shared/runtime/native_output.md` und `../shared/prompting/output-delivery.md` angleichen: keine unbegrenzte Pollschleife innerhalb eines äußeren Aufrufs, offenes Handle beim Ende eines Warteabschnitts bewahren. Den bestehenden Speicherweg für rohe Fehlerbytes und minimale Vertragsanpassungen konsistent dokumentieren. Die native Vorlage tatsächlich auf dem verfügbaren Codex-Host für Erfolg, Fehler und Pending ausführen. Fertig, wenn Ergebnisse, Host und erhaltene Handles belegt sind; native POSIX-Ausführung ohne entsprechenden Codex-Host als Grenze ausweisen, nicht durch Python-CI als bestanden erklären.
Evidence: 25 lokale Runtime-Tests und CI 40952453745 (6/6) bestanden; Windows-Codex: Erfolg/Exit 7/Pending mit Handle geprüft. Native POSIX-Vorlage ungeprüft.

### W-004 Quelltext und Maschinenausgaben eindeutig abgrenzen

Status: done
Depends on: []
Blocked by: []
Decisions: [ADR-0089, ADR-0153]
Outcome: Agenten können nötigen Quelltext direkt vollständig lesen und halten Diagnose-/Berichtsdaten trotzdem aus dem Kontext heraus.
Acceptance: Die Grenze zwischen benötigtem Quelltext, direkter Klartextdiagnose und auszuwertenden Maschinendaten ist ohne Dateityp-Helper und pauschale Größenausnahme geklärt. JSON/YAML als benötigter Quellvertrag ist von Ergebnisdaten unterscheidbar. Strukturierte Berichte und eingebettete Dumps bleiben vor Anzeige ausgewertet; notwendige Prosa und vollständige Aufträge gehen nicht verloren. Beide Ask-Wege verwenden dieselbe Adviser-Regelquelle; Nutzerfragen, Zitate, technische Schnittstellen und verborgene Erwartungsschlüssel werden auch beim Aufrufer nicht stilistisch umgeschrieben. Aufrufer und Berater erreichen die jeweils für sie geltende Regel vor ihrer Operation.
Instructions: []
Steps:
1. [status: done] Den bestehenden Geltungsbereich in `../shared/prompting/{machine-data.md,common.md,output-delivery.md}` kompakt nach Inhalt und Operation präzisieren. Benötigter Quelltext, gezielte Statusinformation und Klartextdiagnose dürfen direkt gelesen werden; Umbenennen oder Bearbeiten macht einen Rohbericht nicht zu Quelltext. Fertig nach Quellenreview mit Beispielen für package.json, Konfiguration, Git-Status, kurzen Fehlertext und großen Bericht desselben Dateityps.
2. [status: done] Ask-spezifische Regeln aus `common.md` nach Zuständigkeit verorten: Auftragsframing und Schutz wörtlicher Fragen, Zitate, technischer Daten und Erwartungsschlüssel für den Aufrufer in Asks `SKILL.md`, Abschnitt „Ask and collect“; Regeln für Beraterantworten in `adviser.md`, das beide Builder verwenden. Allgemeine Literal- und Autoritätsgarantien erhalten und nur unnötige Ladewege verkürzen. Fertig, wenn der Aufrufer die nötige Regel vor dem Framing liest, beide Beraterpfade ihren Vertrag behalten und keine notwendige Lektüre durch eine Zusammenfassung ersetzt wird.
Evidence: Inhalts-/Operationsgrenze geklärt; package.json, Konfiguration, Git-Status, Diagnose und Bericht abgeglichen. Literalregel am Ask-Aufrufer und in Adviser-Quelle erreichbar.

### W-005 Native Ask-Aufträge schlanker und unverändert zustellen

Status: done
Depends on: [W-003, W-004]
Blocked by: []
Decisions: [ADR-0061, ADR-0089, ADR-0120, ADR-0136, ADR-0153, ADR-0227]
Outcome: Native Berater erhalten einen vollständigen eindeutigen Auftrag ohne vermeidbare Textkopie oder unnötig eingebettete Regeln.
Acceptance: Der Aufwand eingebetteter nativer Ask-Aufträge ist nach Buildergröße, tatsächlich modellseitig ausgegebenem Inhalt und reiner Tooltrace-Darstellung unterschieden. Eine Änderung verringert belegten Aufwand und erhält Empfängerauftrag, Rollenrechte, unabhängige Beratung und exakte Frage. Keine automatisch übernommene 8-KiB-Pflicht, Ersatzberater oder Änderung der Ask-Claude-Schnittstelle.
Instructions: []
Steps:
1. [status: done] `members/scoville-ask-for-codex/scoville-ask-for-codex/scripts/build_adviser_prompt.py` und `references/native.md` am tatsächlich verfügbaren Hosttransport prüfen. Erst unnötige Einbettung durch eindeutige bedingte Pfade reduzieren; bestehenden Dateiweg nur verwenden, wenn dadurch ein konkretes Transportproblem entfällt. Fertig bei gemessenem Ausgangs-/Kandidatenumfang und belegter Übergabe ohne manuelle Reparatur; aufgeklappte Tooltraces allein beweisen keine doppelten Tokenkosten.
2. [status: done] Unbegrenztes Sammeln wie in W-003 in kontrollierte Warteabschnitte mit erhaltenen Handles übersetzen. Den optional beanstandeten `sol`-Default in `config.default.json` als Vorschlag auf gpt-6.1-sol prüfen; vorhandene Nutzer-Overrides und Claude-Einstellungen erhalten. Fehlende Konfigurationsdatei und Teil-Overrides über echte Verbraucher prüfen. Fertig nach Helper-/Empfängertests und begründeter Entscheidung zum Default, ohne ungetestete Verfügbarkeitsaussage.
Evidence: 55 Ask-Tests bestanden; Startnachricht 9840/11872 auf 5127/5294 Bytes; exakte Frage/Fehler erhalten. Sol-Default 6.1; bestehende Overrides und begrenzte native Sammlung geprüft.

### W-006 Korrekturschleifen und UI-Overflow gezielt korrigieren

Status: done
Depends on: []
Blocked by: []
Decisions: []
Outcome: Workflow und UI setzen nur belegbar sinnvolle Korrekturen fort und prüfen Dokumentüberlauf gegen die tatsächliche Inhaltsbreite.
Acceptance: Workflow und UI besitzen einen Ausgang bei fehlendem gestütztem Lösungsansatz. Ein nach belegter Widerlegung ohne neue Belege oder geänderte Bedingungen wiederkehrender Reviewbefund beendet die erfolglose Wiederholung; der betroffene Step bleibt offen und eine fehlende Voraussetzung blockiert das Work Item. Eine notwendige Nutzerentscheidung wird konkret erfragt; bloße Wiederholung widerlegt keine Fakten. Neue Belege erlauben auch nach mehreren Runden eine weitere Korrektur. Der Overflow-Check erfasst kleinen Überlauf trotz sichtbarer klassischer Scrollbar. Frische unabhängige Reviews, vollständiger zuständiger Diff und erforderliche Reviewpflicht bleiben erhalten.
Instructions: []
Steps:
1. [status: done] Die vorhandene Code-Regel „Stop repetition“ mit Workflow `SKILL.md`/`references/operations.md` und UI `references/validation.md` abgleichen. Bestehende Tabellen und Mermaid-Ausgänge für belegten Fortschritt, widerlegt wiederholten Befund und fehlende Voraussetzung korrigieren; Blocker am Work Item abbilden, keine pauschale Zwei-Runden-Grenze oder neue Zählerverwaltung. Fertig bei konsistenten Diagrammen und Gegenfällen für berechtigte weitere Korrektur sowie Stillstand; Audit bleibt lesend.
2. [status: done] In `members/scoville-ui/scoville-ui/references/wordpress/responsive.md` die nutzbare Dokumentbreite verwenden. Den Gegenfall mit nachweisbar sichtbarer klassischer Scrollbar herstellen: innerWidth ist größer als clientWidth, scrollWidth liegt dazwischen. Fertig, wenn der alte Vergleich den Überlauf übersieht, der neue ihn erkennt und der zulässige lokale Zweiachsen-Container weiterhin besteht; Headless ohne diese Breitenbedingung ist kein Gegenbeleg. Screenshot und Interaktionsnachweis bleiben getrennte Aussagen.
Evidence: Windows Edge: 800/785/792 px reproduzieren alten Fehlpass; clientWidth erkennt Überlauf, lokaler Scrollcontainer besteht. Workflow/UI unterscheiden belegte Fortsetzung und Stillstand.

### W-007 Fallbacks und Profiltexte an ihren Vertrag angleichen

Status: done
Depends on: [W-001, W-003, W-004]
Blocked by: []
Decisions: [ADR-0148, ADR-0224]
Outcome: General-Fallbacks, Profile und Diagnosen beschreiben die tatsächlich verfügbare Operation ohne fachliche Abweichung.
Acceptance: Widersprüche zwischen Fallbacks und Skripten, Setup-Diagnosen mit Typ statt Wert sowie Workflow-/Ask-spezifische Generalformulierungen sind nachvollzogen und korrigiert oder begründet verworfen. Idle-Verhalten und Evidence-Format sind je Helpervertrag korrekt. ADR-0148s Regelorte und Nutzerentscheidung bei gleichrangigen Regelkonflikten sowie ADR-0224s Markierung neuer Decisions bleiben in den zutreffenden Profilen erhalten. Geheimnisredaktion, Schreibrechte und Git-Ausnahme für temporäre Dateien bleiben gewahrt.
Instructions: []
Steps:
1. [status: done] Plan-Fallbacks mit den festgelegten Helperfällen vergleichen; NUL-Prüfung und Evidence-Form unterscheiden. Leere Evidence als zulässiges [] von einem ungültigen leeren Feldwert abgrenzen. Shared `runtime/check_text_size-fallback.md` einschließlich temporärer .gitignore an W-003 angleichen und Setup-Diagnose in `validate_setup_choices` am vorhandenen `diagnostic_value`-Owner korrigieren. Fertig nach positiven und negativen Vertragsfällen einschließlich geschützter Werte; Fehlermeldungen dürfen keine Secrets offenlegen.
2. [status: done] Workflow-exklusive Planformulierungen in General neutralisieren oder bedingt ausliefern; neue Decisions behalten `Binding sections: complete` nach ADR-0224. Viewer als eigenständigen Scoville Plan Viewer benennen. Doppelungen in Workflow, Standalone-Code und UI sowie Setup ohne `agents/openai.yaml`, uneinheitliche Helper-Platzhalter/`-X utf8` und die mögliche Plan-Aktivierung ohne Profil durch „durable work across interruptions“ in der Beschreibung bewerten. Die fehlende Mainloop-Code-Konfliktregel gegen ADR-0148 abgleichen: Nutzerentscheidung bei gleichrangigem Widerspruch bleibt, Codex berücksichtigt nur AGENTS.md. Fertig nach begründeter Entscheidung je Kandidat und Profil-/Pakettests ohne Regelverlust; fehlende openai.yaml allein ist kein Defekt.
Evidence: 20 Setup-Tests und 128 Plan-Tests (1 POSIX-Skip) bestanden. Diagnosewert/Nested-Redaktion, Fallbacks, Generaltexte und Mainloop-Konfliktregel korrigiert; optionale Metadatenlücken verworfen.

### W-008 Änderungen mit tatsächlichen Empfängern abnehmen

Status: done
Depends on: [W-002, W-005, W-006, W-007]
Blocked by: []
Decisions: [ADR-0153, ADR-0227]
Outcome: Geänderte Verträge und Texte haben gezielte technische und beobachtete Verhaltensnachweise mit ausgewiesenen Grenzen.
Acceptance: Für geänderte native Adviser-Aufträge, Dispatch-Aufträge, Capture-Ausgaben und per Complete-File-Route (--publish-full) abgelegte Dateien ist je Ausgabeart die unveränderte Übergabe an einen frischen gpt-6.1-sol/low-Empfänger ohne Promptreparatur belegt. Für den Claude-Pfad belegt der vorhandene aufzeichnende CLI-Platzhalter die unveränderte Promptübergabe nach ADR-0227 ab ersetzter Befehlsauflösung; PATH-Suche, .ps1-Behandlung und Claude-Modellverhalten bleiben ausdrücklich ungeprüft. Modell-/Effortnachweis, tatsächliche Aktionen, Ergebnis und Grenzen sind je Fall festgehalten; reine Formulierungsidentität ist keine Abnahmebedingung. Am finalen Stand bestehen die erforderlichen technischen Prüfungen und Reviews; unverändert gültige Ergebnisse werden wiederverwendet.
Instructions: Kein echter Claude-Modelllauf; den begrenzten Transportnachweis nicht als Claude-Verhaltensabnahme ausgeben.
Steps:
1. [status: done] Je geänderter Ausgabeart vollständige Belege wiederverwenden oder fehlende Tests ausführen: native Ask-/Dispatch-Aufträge, Capture-Ausgabe und per Complete-File-Route abgelegte Datei an Sol/low-Empfänger. Dispatch-Paare über .scoville/config.json eines isolierten Testprojekts setzen, ohne Produktkonfigurationen oder feste Paare per Flags zu umgehen. Claude-Transport über den bestehenden aufzeichnenden Platzhalter in `members/scoville-ask-for-codex/development/tests/test_claude_recipe.py` prüfen; ersetzte Befehlsauflösung, ungeprüfte PATH-Suche und .ps1-Behandlung und fehlenden Modelllauf ausweisen. Aufrufer-Framing einschließlich wörtlicher Fragen und Erwartungsschlüssel prüfen. An passenden Aufgaben Quell-JSON gegenüber Berichtsdaten, große Dumps, notwendige Langtexte und Stillstand gegenüber berechtigter Fortsetzung prüfen. Fertig nach unabhängig geprüften Artefakten/Aktionen mit unveränderten Nutzdaten; keine neue Harness-Infrastruktur.
2. [status: done] Vorliegende technische Tests und erforderliche Step-/Closure- beziehungsweise Quellenreviews am finalen Stand zusammenführen. Nur fehlende Integrationsprüfungen oder durch Änderungen/Fails ungültige Nachweise nachholen; keine zusätzliche Reviewrunde für bereits abgenommenen unveränderten Inhalt. Fertig, wenn bestätigte Lücken am Owner geschlossen oder Grenzen benannt sind und die Texte ohne begründeten Bedarf nicht wachsen.
Evidence: 5 Sol-6.1/low-Empfänger, Quellenreview und gezielte Fixabnahme; 26 lokale Runtime-Tests, finale CI 6/6. Grenzen in [Abnahme](../testing/0060-fertige-skills-folgefixes.md).

### W-009 Aktuelle Pakete bauen und Veröffentlichung vorlegen

Status: in_progress
Depends on: [W-008]
Blocked by: []
Decisions: [ADR-0144, ADR-0199, ADR-0204, ADR-0225, ADR-0226, ADR-0227]
Outcome: Geprüfte aktuelle Pakete und zutreffende Veröffentlichungstexte stehen zur Freigabe bereit und werden nur im genehmigten Umfang veröffentlicht.
Acceptance: Gemeinsame Basis in Einzelpaketen und beiden Suites stimmt mit den Ownern überein; Hostunterschiede sind begründet. Build, Paket-/README-Prüfungen, beide Planprofile und check_all.py bestehen. PLAN-0060 und seine verknüpften Decisions einschließlich ADR-0227 sind in beiden öffentlichen Suite-Exporten enthalten und ihre Verweise auflösbar. Geändertes paketiertes Python erhält die erforderliche Runtime-Matrix. Changelogs und README-Quellen beschreiben nur beobachtete Ergebnisse. Öffentlicher Export enthält weder private Namen noch private Audits. Der ausdrücklich freigegebene Stand ist auf main veröffentlicht und gegen den Remote verifiziert.
Instructions: Aktuelle Nutzerfreigabe: geprüften Auftragsstand bauen, auf GitHub pushen und lokal aktualisieren. Je Repository die aktuell verifizierte Remote-main-Historie verwenden; kein Force-Push, keine neuen Tags oder Releases. Der echte Workflowtest nutzt einen eigenen Hauptthread mit gpt-6.1-sol/low für alle Rollen; offene Testgrenzen bleiben ausgewiesen.
Steps:
1. [status: in_progress] Betroffene README-Quellen anpassen, generierte Gesamttexte vollständig lesen und beide Profile bauen. Shared-Snapshots und zentralen Build regenerieren; passende private Runtime-Nachweise aus W-003 wiederverwenden und nur bei später geänderten Python-/CI-Testinputs aktualisieren. Transportprüfung, Modellverhalten und native Host-/Plattformgrenzen getrennt und zutreffend beschreiben. Fertig nach bestehenden technischen Prüfungen und einmaligem Paketvergleich aller betroffenen Consumer; keine neue Sicherungs-, Hash- oder Prosa-Prüfinfrastruktur.
2. [status: todo] Konkrete Diffs, Ergebnisse, Grenzen und betroffene Repos vorlegen; gemäß aktueller Nutzerfreigabe ausschließlich main pushen, den Remote verifizieren und die vorhandenen lokalen Skills auf den veröffentlichten Stand aktualisieren. Fertig nach belegtem Remoteabgleich und Prüfung der lokalen Paketstände; tatsächliche Blocker bleiben offen.
Evidence: Quellen und Empfängertests abgenommen; finale Runtime-CI 40955452986 besteht 6/6. Pakete und Veröffentlichungsunterlagen werden vorbereitet.
