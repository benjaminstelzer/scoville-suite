# PLAN-0062: Quellenprüfung und Fixentscheidungen

Stand: 2026-10-30. Dieser Bericht gehört zum Entwurf von [PLAN-0062](../plans/0062-gemeinsame-qualitaetskriterien-und-helperfixes.md), nicht zur Abnahme seiner Umsetzung. Die Quellenprüfung ersetzt keine Reproduktion oder Modellwirkungsprüfung. Die Laufzahlen und Ausgabegrößen aus dem externen Review wurden hier nicht als eigene Messungen übernommen.

## Quellen und Abgrenzung

Kanonische Quellen sind members/ und das Shared-Geschwisterrepo. Suite-Ausgangspunkt: bb5dd180a89def9ceeec5bbe8848212cec91b4e8. Bereits vorhandene uncommittete Änderungen aus PLAN-0061 sind auf ausdrücklichen Nutzerauftrag übernommen. Bei späterer Umsetzung ist eine Baseline des tatsächlich zu ändernden Stands zu wählen, die diese Änderungen und ihre bereits vorhandenen Belege erfasst. Vorhandene Quellenleistung, neue Korrekturen und noch offene Abnahme bleiben unterscheidbar.

Die Tabellen nennen Dateien relativ zur jeweiligen Skillwurzel oder ausdrücklich Shared. „Bestätigt“ bezeichnet den nachvollzogenen Quellenmechanismus, sofern nicht ausdrücklich ein beobachteter Lauf genannt wird. „Teilweise“ trennt zutreffenden Mechanismus von einer zu weit gehenden Fehler- oder Lösungsaussage. Offene Reproduktionen bleiben Prüfaufgaben.

## Grundauftrag und Kriterienparität

| Punkt | Befund und Quelle | Planmaßnahme |
| --- | --- | --- |
| Umbenennung | Bestätigt: Shared prompting/code-review.md ist über suite.json vier Consumern zugeordnet; Ask- und Dispatchhelper prüfen/verarbeiten den alten Pfad. | W-001: Quelle, Manifest, Helper, aktive Doku und Tests gemeinsam umbenennen; historische Erwähnungen nicht ändern. |
| Ein Kriterienowner | Bestätigt: Code SKILL.md, change-workflow.md und implementation-review.md wiederholen Struktur-/Absicherungskriterien; cost-and-cache.md überschneidet Aufwandsregeln. | Kriterien zusammenführen statt anhängen; weiter nötige Ausführungs- und Ergebnisverträge beim Rollenowner lassen. |
| Frühes Laden | Bestätigt: code-review.md beginnt mit „Before approving“, Code/UI laden die ausführliche Regel überwiegend zur Abnahme. Workflow-Main erhält sie nicht im Main-Auftrag. | W-001: Code/UI und Workflow-Main erreichen den Owner vor Lösungswahl/Implementierung über den vorhandenen Ladeweg; keine wiederholte Einbettung pro Mainloop-Step. Native Ask-Reviews behalten den verpflichtenden Pfadread, Claude-Ask und Workflow-Reviewer die Einbettung. |
| Cache | Bestätigt: Cacheverträge nur in Codes cost-and-cache.md; Validation enthält eigene Nachweisregeln. | Korrektheitskriterien gemeinsam, Nachweise in Validation, allgemeines Cache-Tuning weiter kein Auftrag. |
| Greenfield | Bestätigt: bestehende Entwicklungsabsicht wird vorausgesetzt; Plan authoring.md hat eine bedarfsgerechte Rückfrage. | Rollenneutral: Autor leitet Absicht ab und fragt bei materieller Designwirkung nach; lesender Reviewer meldet ungeklärte materielle Absicht als offene Entscheidung. Neuer Komponenten-Code aktiviert nicht den Layout-Fallback für ein vollständig neues Projekt. |
| Allgemeine Autoren-/Reviewer-Parität | Allgemeiner Intent ausdrücklich beauftragt: „Code … UI Code … Pläne … der schreiber schon die Regeln der Abnahme bzw. der Reviewer kennt“. Keine eigene Asymmetrie in Plan, Skillwriter oder UI-Fachregeln belegt; konkrete Zuordnungslücke nur bei Ask, das jedem Review Code-Regeln einbettet. | Vor Start konkret abgegrenzt: nur Asks fachliche Zuordnung korrigieren. Bestehende gemeinsame Domänenregeln unverändert übernehmen; keine offene Such-/Änderungsrunde für Plan oder Skillwriter. Weitere Vermutungen unter W-007 berichten. |

Bereits nachgewiesene gemeinsame Ladewege: Plan SKILL.md Abschnitt Load only the current route weist Authoring und Review auf dieselben passenden authoring-/progress-/Decision-Feldregeln. Skillwriter SKILL.md lädt Instruction Design vor Schreiben und Review und beschreibt dieselbe bestehende Quellenabnahme unter Check the work. UI SKILL.md Tabelle Concern/Reference lädt ui-quality.md bei Erstellen, Ändern und Beurteilen offener Fachfragen sowie validation.md vor Änderung und Audit. Die spätere Codequalität ist davon getrennt und wird durch W-001 ausdrücklich früher geladen. Ask adviser.md benennt bislang nur actionable findings; build_adviser_prompt.py und ask.py fügen Codequalität für jeden Reviewmodus bei. Dort fehlt die ausdrückliche fachliche Zuordnung, nicht ein bewiesenes strengeres Plan- oder Skillwriterkriterium.

## A: Fehlende und hinzugefügte Absicherung

| ID | Befund und Quelle | Umgang |
| --- | --- | --- |
| A1 | Bestätigt: Code SKILL.md „Failure consequences“ enthält den Kern, der gemeinsame Qualitätsowner nicht. | W-001: ein gemeinsamer Kern; beobachteter Vorfall nicht Voraussetzung, erreichbarer Pfad und tatsächliche Lücke entscheidend. |
| A2 | Bestätigt: Ausführungs-/Validierungsreferenzen zeigen auf Code SKILL.md statt den gemeinsamen Owner. | Kern verschieben, notwendige eigenständige Grenzen erhalten, Verweise aktualisieren. |
| A3 | Bestätigt: build_dispatch_prompt.py sagt „an actual defect returns changes_requested“, adviser.md verlangt „report actionable findings“, ohne die Entscheidung ausdrücklich an denselben Absicherungsmaßstab zu binden. | W-001 Acceptance und Step 3 binden beide Ergebnisverträge ausdrücklich an den Owner. Step 4 prüft mit echten unveränderten Helperaufträgen und gpt-6.1-sol/low korrekt ausgelassene hypothetische Härtung gegen tatsächlich fehlende erforderliche Absicherung; erwartete Workflow-Ergebnisse pass bzw. changes_requested, Ask ohne neue Statusfelder. Kein Erwartungsschlüssel im Empfängerprompt. |

Der vorgeschlagene sechsfache Modellvergleich ist optional und nicht freigegeben. Aktuelle Planberatungen ersetzen ihn nicht.

## B: Workflow

| ID | Befund und Quelle | Umgang |
| --- | --- | --- |
| B1 | Strikte ordinal-Prüfung in resolve_model_pair.py bestätigt; behaupteter aktueller universeller Ausfall durch den vorhandenen eigenen Sessionbeleg widerlegt. Beide Ordinals sind int, Turn-IDs passend und Reihenfolge korrekt. Die eigene Konfiguration enthält execute und keine schema_version oder vollständigen Schema-2-Paare: gewöhnlicher alter Schema-1-Fall, nicht E5s Schema-2-Altfeld-Sackgasse. | Nur vorhandenen Beleg übernehmen: keine neue Messung, B1-Tests oder Codeänderung. Für Workflowtests gültige isolierte Schema-2-Profile nutzen; lokale Migration nur mit eigener Cleanup-Freigabe, keine Abhängigkeit von W-005 für diesen Schema-1-Fall. |
| B2 | Vollständiger unabhängiger Re-Review und evidenzbasierter Wiederholungsstopp sind bestätigt; eine beobachtete nicht konvergierende Schleife ist hier nicht nachgewiesen. operations.md commitet erst nach Pass, daher liegt kein natürlich versioniertes Korrekturdelta vor. | W-002: W-001s gemeinsamer Kriterien-/Absicherungsmaßstab und evidenzbasierter Wiederholungsstopp begrenzen unnötige Kosten. Volle Step-Prüfung und gültige Belege bleiben erhalten. W-007 berichtet ausdrücklich: Bei immer neuen echten Befunden gibt es keine obere Rundenzahl oder garantierte Kostenobergrenze. |
| B3 | Bestätigt: family.contract wird in SKILL.md und operations.md eingebunden. | Ein Einstiegseigentümer, kein wiederholtes Pflichtladen. |
| B4 | Bestätigt: --selector wählt extern, Decision-Funktionen importieren weiterhin den gebündelten select_context. | Kompatibilitätsvertrag präzisieren oder Verhalten minimal vereinheitlichen. Keine Entfernung einer öffentlichen Option allein wegen fehlender Tests/auffindbarer Consumer. |

## C: Checker und Ausgabe

| ID | Befund und Quelle | Umgang |
| --- | --- | --- |
| C1 | Teilweise: output-delivery.md erlaubt bei wiederholbarer Abfrage den zweiten Lauf; für Effekte ist vollständiger Capture bereits Pflicht. | W-003: bei temporärer Schreibbefugnis potentiell große Ausgabe gleich im ersten Lauf sichern. Ohne Schreibrecht zulässigen Kanal nutzen oder Grenze melden; kein unzulässiger zweiter Speicherlauf. |
| C2 | Teilweise: neue POSIX-Kindsession, fehlende Signalweiterleitung und ohne Timeout mögliche offene Enkelpipe sind im Checker nachvollziehbar. Tatsächlicher Hostabbruchweg und Windows-Effekt benötigen Nachweis. | Beherrschbare Abbruch-/Deadlinefälle technisch prüfen. SIGKILL nicht abfangbar; eine native Yield-Zeit ist keine Tötungsfrist. Keine generelle Prozessgarantie behaupten. |
| C3 | Tokenorientierter Vertrag bestätigt; der vorgeschlagene universelle Claude-Zeichenwert ist zu grob. | Effektive Inline-/Read-back-/Fehlergrenze unterscheiden; konservativ nur ein belegtes Limit samt vollständiger Ausgabe/Headern verwenden, Originalcapture erhalten. |
| C4 | Bestätigt: publish_full verwendet os.link und finally entfernt das Tempfile auch nach einem anderen Linkfehler. Der bestehende Fallbackvertrag nennt atomare Veröffentlichung. | Verlustschutz beheben. Fallback muss No-Replace und atomare vollständige Sichtbarkeit erhalten; direktes O_EXCL-Schreiben allein genügt nicht. Ist keine solche Route verfügbar, sichere Fehlerrückgabe mit vollständiger erhaltener eigener Tempdatei und Wiederherstellungspfad; kein Teilinhalt als vollständig und keine stille Abschwächung. |
| C5 | Bestätigt: Kind-Exit und Checkerfehler können beide Prozessstatus 125 liefern; Metadaten unterscheiden sie. | Bestehende Unterscheidung eindeutig dokumentieren, keinen neuen Statusvertrag erfinden. |

Aktuelle offizielle Hostdokumentation: [Claude Code Output limits](https://code.claude.com/docs/en/tools-reference#output-limits), [Environment variables](https://code.claude.com/docs/en/env-vars). BASH_MAX_OUTPUT_LENGTH ist ein Read-back-Fenster; bashOutputMaxChars übersteuert es. Gültige und fehlgeschlagene Ergebnisse haben unterschiedliche Inlinepfade. Bei großen gültigen Ergebnissen kann ein Dateipfad geliefert werden, Fehlerauszüge enthalten diesen nicht generell. Deshalb beweist eine Umrechnung des Variablenwerts allein keinen vollständigen Transport.

## D: Ask

| ID | Befund und Quelle | Umgang |
| --- | --- | --- |
| D1 | Bestätigt: build_adviser_prompt.py gibt vollständigen Auftrag im JSON aus; Workflow hat bereits eine direkte bzw. große Dateiroute. | W-004: zulässigen vorhandenen Mechanismus wiederverwenden, keine Imports installierter Geschwister oder neue Infrastruktur. |
| D2 | Teilweise: ask.py gibt vollständige Claude-Antwort als stdout-JSON zurück; der vorhandene Effekt-Capture kann sie schon sichern. | Zuerst vorhandenen Captureweg im echten Aufruf prüfen; eigenes Ergebnisdateiflag nur, wenn diese Route die konkrete Lücke nicht schließt. |
| D3 Fehler | Bestätigt: raise-Pfade können CLI-Exit/Rohantwort/Sitzungsdaten aus der aufrufbaren Rückgabe verlieren. | Vollständige Originalantwort zulässig lokal behalten; nur nötige sichere Fehler-/Sitzungsfelder anzeigen. Keine große oder möglicherweise geheime Rohantwort im Diagnoseobjekt ausgeben. |
| D3 Modell | Quellen lesen top-level model/effort; in dieser tatsächlichen Opus-Konsultation sind beide reported-Felder null. Das belegt nicht die Form der zugrunde liegenden CLI-Rohantwort. | Vorhandene echte CLI-Evidenz verwenden, eindeutige berichtete Daten von requested unterscheiden. Keine bezahlte Schema-Probe ohne Freigabe. |
| D3 Budget | format(..., 'g') in ask_claude.py bestätigt; Präzisionsverlust erst bei entsprechend genauem Eingabewert. | Konkreten gültigen Gegenfall und vollständigen CLI-Wert prüfen, keine willkürliche neue Genauigkeitsanforderung. |
| D3 BOM | Bestätigt als quellenabgeleiteter Grenzfall: configuration.md erlaubt auch automatisch serialisierte UTF-8-Requests. Derselbe BOM-JSON-Request wird an stdin über utf-8-sig gelesen, bei --input-file über read_utf8/json.loads abgewiesen. Nicht tatsächlich reproduziert. | Eng am JSON-Requestdecoder korrigieren und reproduzieren; kein pauschaler BOM-Eingriff in Frage- oder Quelltextleser. Opus' frühere Prämisse „nur Helperdateien“ genügt nicht zum Verwerfen. |
| D3 Presets | Ganze Konfiguration wird bewusst validiert; ein unbeteiligtes defektes Preset kann daher Auswahl blockieren. | Beabsichtigte Ganzprofilprüfung von einem Fehler trennen. Gespeicherte gültige Anfrage darf nicht still einem anderen Projekt zugeordnet werden; Validierungsumfang nicht ohne belegten Vertragsgrund schwächen. |
| D4 | Feste Aufruferargumente und Adapter zeigen tote Sessionzweige und einen umgewandelten Timeout-Catch. | Entfernbarkeit über alle Aufrufer/Tests prüfen, exakte Resume-ID und bestehende Fehlersemantik erhalten. |
| D5 | Standalone configuration.md erlaubt ausdrückliches Speichern ohne unmittelbar genannten Validierungsaufruf. | Lesenden ask.py --project-root-Aufruf nennen; kein Beraterlauf oder automatische Migration. |

## E: Setup

| ID | Befund und Quelle | Umgang |
| --- | --- | --- |
| E1 | NamedTemporaryFile plus os.replace in setup.py ersetzt den Eintrag; Modus-/Symlinksemantik nicht ausdrücklich behandelt. | W-005: Modus erhalten, Symlink vor Effekten abweisen. POSIX- und Windowsgrenzen getrennt testen. |
| E2 | Cleanup nutzt validate_pair, set zusätzlich validate_setup_choices mit engeren Setup-Stufen. | Neue ausdrücklich gewählte Werte nach Setup-Vertrag prüfen; gültige erhaltene Sonderstufen nicht durch die Presetgrenze entwerten. |
| E3 | Validierung in Temp-Projekt kann Temp-Pfad in Fehler zeigen. | Diagnose auf den tatsächlichen Projekteingang beziehen; atomische Vorbereitung erhalten. |
| E4 | effective wertet Workflow und Ask zusammen aus; Fehler eines Abschnitts stoppt vor dem anderen. Zusätzlich ist eine Kopplung bei der isolierten Workflow-Auflösung quellenbelegt: Shared runtime/scoville_config.py read_config prüft Typen beider Sektionen vor section('workflow'); eine nichtobjektförmige Ask-Sektion blockiert damit auch resolve_model_pair. Inhaltliche Fehler innerhalb eines Ask-Objekts werden auf diesem Weg dagegen nicht geprüft. | W-005 meldet show-Fehler gemeinsam unter ok:false ohne effective-Teilwerte und löst die unberechtigte fremde Typprüfung nur an der lesenden Sektionsgrenze. Global ungültiges JSON, Gesamt-/Speichervalidierung und Ask-Presetprüfung bleiben streng. Gegenfälle mit --show-config und gemeinsamem Konfigurationspfad von --role main bei Umsetzung prüfen; aktuell Quellenbeleg, kein eigener Runtime-Nachweis. |
| E5 | Schema 2 mit Altfeld kann needs_cleanup auslösen; legacy_effective akzeptiert dieses Schema nicht. | Ausdrückliches Cleanup gültiger Schema-2-Paare von tatsächlicher Schema-1-Migration unterscheiden; nur bekannte Altlasten entfernen bzw. konkretes unbekanntes Feld nennen. |
| E6 | Workflow lässt interne Leerzeichen in Modell-ID zu; Ask prüft enger. | Gemeinsame minimale technische ID-Bedingung am vorhandenen Konfigurationsowner, Claude-spezifische Vorgaben separat. |
| E7 | agents/openai.yaml fehlt tatsächlich; fehlende Hostmetadaten allein belegen keine Funktionsstörung. Der Nutzer verlangt die Ergänzung dennoch ausdrücklich. | Über regulären Metadaten-/Manifestweg ergänzen und bisherigen Aktivierungsvertrag erhalten; kein erfundener Laufblocker und keine stille Invocation-Erweiterung. |

## F: Plan

| ID | Befund und Quelle | Umgang |
| --- | --- | --- |
| F1 | Budgetoverflow und gültiges Profil sind unterschiedliche Befunde, kein Widerspruch. Selectordiagnose nennt bereits required_bytes und internen Retry; read-only.md verlangt ausdrückliches Budget. | W-006: Default als internes Budget eindeutig behandeln, begrenzten Retry erlauben, echte bindende Grenze erhalten. Kein pauschales Abschalten. |
| F2 | Unterschiedliche Step-/Frontmatterparser bestätigt: Validator lässt führende Null und leere Werte passieren, Selector strenger. | Gemeinsame begrenzte Grammatik; pro nativem Feld zulässige Leere prüfen, keine pauschale Parserneufassung. |
| F3 | Indexauswahl und explizite --plan-Inspektion laufen durch plan_position; Statusprüfung nicht gleich zur normalen aktiven Auswahl. | Inaktive Indexauswahl ablehnen, erlaubte explizite Draft-/Endplaninspektion erhalten. |
| F4 | Rootpfade mit .. werden unterschiedlich behandelt. | Verantwortlichen Rootvertrag angleichen; Root-Symlinkprüfung weiterhin vor normalisierendem Auflösen. |
| F5 | H2-Titelprüfung und Folgesperre können unsichtbare Leerzeichen als schwer erkennbare Reihenfolgeabweichung melden. | Beobachtete Titel sichtbar/escaped ausgeben, unabhängige nutzbare Diagnosen erhalten; kein neuer Code allein für ein Leerzeichen nötig. |
| F6 | Fehler bei _scan_markdown setzen nicht in jedem Pfad den späteren Parsefehlerstatus; Querprüfungen können mit leerem Bestand weiterlaufen. | Nur unbegründete Folgediagnosen unterdrücken, echte unabhängige Fehler erhalten. |
| F7 | WORK_LIST_INVALID/WORK_FIELD_INVALID in parse_inline_ids, single_field und parse_steps haben keine ausreichenden Item-/Feldorte. Davon getrennt: CURRENT_ITEM_INVALID/WORK_ITEM_MISSING haben eine erfundene Ersatzzeile. | W-006/Step 2 enthält beide Aufgaben: die übernommenen zwei Auswahlcodes UND die eigenständigen F7-Parsingdiagnosen. Die Übernahme ersetzt F7 nicht. |
| F8 | Batch-Datumsregex und reine Leerzeilenbehandlung sind schwächer als die Fallback-Zusage. | Tatsächlichen Formatvertrag angleichen; gültige Inhalte und Zusagen nicht still abschwächen. |
| F9 | Nichtrekursive native Ordner sind bestätigt; verschachtelte Archive sind kein unterstütztes Profilformat. Der Nutzer erlaubt ausdrücklich das Melden. | Nur nichtblockierende Validatorwarnung zu recordbenannten regulären Dateien in unmittelbaren lesbaren Unterordnern; keine Bodyreads, Links verfolgen, weitere Rekursion oder Migration. valid/Exit-Semantik, Selector und Next-ID bleiben unverändert. Keine Behauptung, damit jede ID-Kollision zu verhindern. |
| F10 | Rohe Frontmatterwerte können "null" bleiben; ein nicht regulärer Markdown-Pfad nutzt Verzeichnisdiagnose. | Semantischen Nullwert und tatsächlichen Pfadtyp korrekt ausdrücken, Consumer/Fallback prüfen. |
| F11 | Allgemeiner gleichzeitiger Änderungsvergleich nicht implementiert; Selector verwendet FILE_CHANGED_DURING_READ jedoch in einem Typprüfungs-Sonderfall. | Falsche allgemeine Zusage korrigieren, keinen globalen Änderungswächter bauen oder vorhandenen sinnvollen Fehlerfall versehentlich löschen. |
| F12 | Validator serialisiert mit indent=2; konkrete 50-KB-Messung nicht selbst reproduziert. | Erst kompakt serialisieren und messen. Keine Meldungstabelle mit Schemaänderung; C1 vermeidet unnötigen Zweitlauf. |

## G und weitere Berichtspunkte

| ID | Einordnung | Umsetzung hier |
| --- | --- | --- |
| G1 | Drei Workflowbezüge aus PLAN-0061/W-002 übernommen; zusätzlich modellgebundenes Beispiel „Sol high review performed“ in Plan references/progress.md. Eigenständiger Plan Viewer ist kein Codex-Rest. | Drei General-Bezüge und das nun ausdrücklich beauftragte modellneutrale Beispiel unter W-008/Step 3 korrigieren. Historische Laufbelege bleiben unverändert; Viewername bleibt. |
| G2 | UI-Regel nach optionalem Codeverweis bereits inline vorhanden; die Korrektur aus PLAN-0061/W-002 ist ausdrücklich übernommen. | W-008 entfernt die unnötige Pflichtkopplung ohne zusätzliche Stopregel. |
| G3 | „either layout“ ohne beide sichtbaren Layouts kann unklar sein. | Nur Empfehlung. |
| G4 | „bundled Scoville Plan“ meint Suite-Geschwister, nicht ein Code-Unterpaket. | Nur Empfehlung. |
| G5 | Quelltextsuchtreffer/Diffs sind normalerweise direkt lesbar; eingebettete Log-/JSON-Rohdaten bleiben Maschinendaten. | Nur Empfehlung, keine pauschale Suchausgabe-Ausnahme. |
| R1 | Unabhängiger Review ist Mainloop-Pflicht, sonst Selbstprüfung plus Projektvertrag. Gleiche Kriterien schaffen keine neue unabhängige Reviewphase. | Keine Produktänderung. |
| R2 | Ladeumfang muss bedingte mögliche Referenzen, erzeugte Auftragstexte und tatsächlich beobachtete Reads trennen. Die extern genannten 43/12 KB sind keine eigenen Messwerte. | Nur Bericht; keine pauschale Entfernung des Rohoutputschutzes. |
| R3 | Bei ungültigem UTF-8 bewahrt --publish-full die originalen Bytes als .bin. Ohne Capture kann Ausgabe fehlen; ein Fehlerstatus ist kein Beleg für Verlust im gesicherten Pfad. | Strenge Byte-/Textgrenze erhalten; C1 verbessert den üblichen Captureweg. |

## Übernahme aus PLAN-0061

Der Nutzer hat sämtliche übrigen Fixes in PLAN-0062 übernommen und PLAN-0061 zur Entfernung freigegeben. Der alte Plan wird nicht zusätzlich ausgeführt; sein Indexeintrag entfällt, PLAN-0062 bleibt bis zur Umsetzungs-/Aktivierungsfreigabe draft.

| Bisheriger Umfang | Tatsächlicher Stand bei Übernahme | Zuständigkeit in PLAN-0062 |
| --- | --- | --- |
| W-001 Entwicklungsgeschichte/Profil | Neun Skillgeschichten und beide README-Quellen überarbeitet; Profiländerung 18a0ef5 remote geprüft. Letzte costs.md-Korrektur fehlt noch in generierter Workflow-README. Keine pauschale neue README-Gesamtabnahme daraus ableiten. | W-008/Step 1 vervollständigt Erzeugung/Prüfung; Profilaktion nicht wiederholen. |
| W-002/Step 1 Publikationsnachtrag | ADR-0225 superseded, ADR-0228 accepted und Nachtrag im Bericht vorhanden. ADR-0228 ist weiterhin nie committet (untracked), und der Erstellungsabschluss war in PLAN-0061/W-002/Step 1 noch in_progress. Die Formulierung zu Tags/Releases ist noch zu weit und muss die ausdrückliche Sperre bewahren. | W-008/Step 2 stellt diesen offenen Erstellungsstand unter unveränderter Nutzerwahl kohärent fertig. Falls die Ausgangslage inzwischen abgeschlossen/committet ist, materielle Bindung nur über Supersession und aktualisierte Verweise ändern; PLAN-0060 nicht wiedereröffnen. |
| W-002/Step 2 Restdokumentation | Drei General-Workflowbezüge, UI-Code-Kopplung und falscher Skillwriter-Changelog-Eintrag bestehen noch. Native Warteabschnitte sind bereits begrenzt, kein zusätzlicher Mechanismus belegt. | W-008/Step 3. |
| W-003/Step 1 frühe Main-Unit-Prüfung | Noch nicht implementiert; ganze main-Unit erreicht abhängige Auswahl vor Ablehnung. | W-002/Step 4 mit eigenen positiven/negativen Prüfungen. |
| W-003/Step 2 Selectorort | Noch nicht implementiert; CURRENT_ITEM_INVALID/WORK_ITEM_MISSING nutzen Ersatzzeile 1. | W-006/Step 2, zusätzlich zu den eigenständigen F7-Feld-/Listendiagnosen. |
| W-004 Kandidat/Publikation | Noch offen: aktueller Build/Matrix, Changelogs, vollständige README-/Variantengates, konkrete Freigabe und Remoteprüfung. | W-009 und W-010; alte einmalige Freigabe nicht übertragen. |

Zusätzliche direkte Nutzerergänzung: W-008/Step 4 stellt an der Quelle der Standalone-Code-Familienliste klar, dass nur unabhängig vorhandene aktive Geschwister zuständig sind und keines davon benötigt wird. Shared runtime/skill_composition.md besitzt diese Regel bereits; die Liste braucht die verständliche Einordnung, keinen neuen Mechanismus.

Die historische Testbelegsperre ist als Non-goal übernommen; die Ausnahme ist allein der erkennbare Auslieferungsnachtrag. README-Laufzahlen entfallen nur im beauftragten Entwicklungsabschnitt. Die Neutralisierung der drei General-Verweise ändert deren Verbindlichkeit nicht. Native Warteabschnitte werden ohne unbelegte Schutzmechanismen eingeordnet.

Korrektur der zwischenzeitlichen Stagingeinordnung: Der Helper erlaubt technisch jedes neue Verzeichnis außerhalb des Quellbaums; der verantwortliche Buildablauf in Shared build/fragments.md Abschnitt Runtime build gate verlangt jedoch ausdrücklich `<workspace-root>/skills/temp/release/runtime-ci` unter dem einzigen Release-Stagingbaum. Dieser engere Ownervertrag gilt in W-009; kein beliebiger temporärer Release-/CI-Kandidat. Wegwerfbare isolierte Testfixtures sind davon getrennt.

## Beratung und Freigabe

- Sol: gpt-6.1-sol/xhigh ausdrücklich angefordert. Erste Ausarbeitung an Kapazitätsgrenze unterbrochen, auf demselben Handle fortgesetzt. Vollständige unabhängige Beratung und gegenseitiger Ergebnisaustausch abgeschlossen; zusammengeführten Entwurf samt gezielter letzter Nachprüfung ausdrücklich abgenommen. Der Beraterhost weist Modell/Effort nicht separat aus.
- Opus: claude-opus-5-5/xhigh ausdrücklich angefordert; vollständige unabhängige Beratung und gegenseitiger Ergebnisaustausch abgeschlossen, keine Berechtigungsverweigerung. K1–K7 wurden gezielt korrigiert und der aktuelle Entwurf ausdrücklich abgenommen. Helper meldet tatsächliches Modell/Effort nicht separat; requested ist kein eigener Hostnachweis.
- Konsens der gegenseitigen Prüfung: B2 behält frischen Reviewer und vollständigen unabhängigen Scope; Fokus und gültige Belege steuern Tiefe, nicht Scope. Kein fixer Zweirundenstopp, aber auch keine Konvergenzgarantie. Der im Follow-up angebotene feste Stopp wurde wegen der ausdrücklich fortgeltenden evidenzbasierten Lösung nicht gewählt; der Nutzer kann diese Produktentscheidung ändern. B4 nicht wegen fehlender Tests entfernen. E4 ohne partielle effective-Werte. F1 interner Default mit ausdrücklich erlaubtem begrenztem Retry; F12 kompakt ohne Schematabelle.
- Noch keine Umsetzungs-, CI-Push-, Export- oder Publikationsfreigabe für PLAN-0062. Alle Work Items stehen todo; übernommene vorhandene Quellenleistung bleibt in Evidence erhalten.

Abschluss der ersten Planprüfung: Beide Berater nahmen die damalige zusammengeführte fachliche Fassung ab, ohne offene Planblocker; der Profilvalidator bestand. Das folgende externe Review führte zu den nachstehend abgegrenzten Planänderungen. Die früheren Abnahmen werden nicht als neue Prüfung dieser Änderungen ausgegeben. PLAN-0062 bleibt draft und der Index idle; PLAN-0061 ist nach Übernahme entfernt. Keine Skill-/Helperumsetzung oder Lauf-/Publikationsabnahme.

## Nachtrag zum externen Planreview

| Punkt | Geänderte Felder beziehungsweise begründete Einordnung |
| --- | --- |
| 1 Ergebnisvertrag | W-001 Acceptance und Steps 3/4 nennen die bindende Ergebnisentscheidung und beide gezielten gpt-6.1-sol/low-Fälle. Workflowstatus und Ask-Befundformat bleiben verschieden; keine neue gemeinsame Ergebnisschnittstelle. |
| 2 Kosten | W-002 Acceptance nennt gemeinsame Kriterien und evidenzbasierten Stopp; W-007 Acceptance verlangt den Bericht des fehlenden oberen Limits bei immer neuen echten Befunden. |
| 3 B1 | W-002/Step 1 übernimmt nur den vorhandenen Gegenbeleg; neue Ordinalnachweise, Negativtests und B1-Codeänderung entfallen. Die normale lokale Schema-1-Cleanup-Voraussetzung ist von E5 getrennt. |
| 4 Abhängigkeit | W-002 hängt von W-006 ab; dessen vollständiger Block steht vor W-002. IDs bleiben unverändert. Dispatchchecks laufen damit gegen den korrigierten Selector, ohne spätere technische Änderungen durch vorzeitigen Nachweis zu verdecken. |
| 5 Umfang | Die allgemeine Parität ist durch den direkten Nutzerauftrag belegt. Konkrete bereits gemeinsame Ladewege und die einzige zusätzliche fachliche Zuordnungslücke in Ask sind oben benannt; W-001/Step 4 ist entsprechend begrenzt. Keine weitere Nutzerentscheidung erforderlich. |
| 6 Greenfield | W-001/Step 3 trennt Autorenrückfrage und offene Reviewerentscheidung rollenneutral; keine zusätzliche Befugnis des lesenden Reviewers. |
| 7 Goal/Form | Übernahmehistorie und Berater-/Entwurfsnotizen aus Goal entfernt; README-Ziel nur im zuständigen W-008. Pfadbasis und Profil-README eindeutig benannt. Testmodell heißt im Plan einheitlich gpt-6.1-sol/low. |
| 8 Quellenkriterien | W-009/Step 1 verweist auf AGENTS.md/Project boundaries und Shared readme/README-template.md/Project README contract statt eines Personennamens als Abnahmekriterium. W-008/Step 4 benennt Shared runtime/skill_composition.md als tatsächlichen family.contract-Owner. ADR-0226 bleibt bindend; keine neue private Namensliste oder persönliche Pfade eingeführt. |
| 9 Weitere Punkte | Modellneutrales progress-Beispiel in W-008, PUB-APPROVAL jetzt Blocked by von W-010, Diagnosehandlungen in W-006/Step 2 statt Instructions. E4-Abgrenzung und spätere Gegenfälle in W-005. W-009 nennt fehlende Übertragbarkeit von low auf xhigh und ungeprüftes Claude-Code-Verhalten der General-Varianten. |

Nur Plan und bestehende Befundmatrix überarbeitet; keine Umsetzung, Commits, Pushs oder Exporte. Das vollständige Profil wurde nach der kohärenten Planänderung einmal mit dem installierten Planvalidator geprüft: Exit 0, valid=true, null Diagnosen. Die Auswertung dieses Ergebnisses ergänzt nur den Bericht; sie verändert keine Profilfelder oder Pfade.

## Umsetzungsfreigabe und vorab festgelegte Modellprüfung

Der Nutzer hat die Aktivierung mit W-001 und die Umsetzung bis W-009 einschließlich gewöhnlicher gpt-6.1-sol/low-Verhaltenstests freigegeben. Pushs einschließlich privater CI-Pushs, Quell-Exporte, Synchronisierung öffentlicher Repositories, Veröffentlichung, Tags, Releases und lokale Installation bleiben gesperrt. Der optionale Vorher-nachher-Vergleich ist nicht freigegeben.

W-001/Step 4: zwei Fälle × zwei native Routen (Workflow-Step-Reviewer und Ask-Review) × drei frische Läufe = zwölf gpt-6.1-sol/low-Läufe. Die Fälle unterscheiden korrekt weggelassene rein hypothetische Härtung von fehlender erforderlicher Absicherung; Erwartungen bleiben außerhalb der Helperaufträge. Ergebnisse und beobachtete Verhältnisse werden je Fall/Route berichtet, nicht als Zuverlässigkeitsgarantie. Der Claude-CLI-Pfad wird technisch geprüft, ohne Claude-Modellverhalten zu behaupten.

## Umsetzung: W-001

Code quality ist jetzt der gemeinsame Kriterienowner für Code, UI-Code, Workflow und Ask. Cost-/Cachekriterien und Absicherungsgrundlage sind dorthin verschoben, Modul-Split-Nachweise und Codes Befundformat nach Validation. Die bisherigen Cost-/Cache- und Implementation-review-Dateien sowie deren Manifestziele entfallen. Autoren laden den Owner vor Lösungswahl; native Ask-Reviews behalten ihren verpflichtenden Pfadread, Workflow und Claude-Ask die Einbettung. Rollen- und Ergebnisfelder sind unverändert. Fachfremde Ask-Reviews verwenden ihre zuständigen Autorenkriterien.

Technische Nachweise: 55 Ask-, 85 Workflow- und sechs Shared-Regeltests bestanden. Shared-Tests prüfen die vorgesehenen Verbraucher, identische gemeinsame Inhalte und Paketlinks über General/Codex und Standalone/Suite. Die normale integrierte Abschlussprüfung bleibt W-009. Der installierte Skill-Creator-Validator weist bereits bei Code das vorhandene unterstützte Feld compatibility zurück; dieses wird gemäß Skillwriter nicht entfernt. Das ist eine benannte Grenze dieses Formatvalidators, kein grüner Formatpass oder Grund zur Feldlöschung.

| Native Route | Fall | Erwartung | Beobachtung |
| --- | --- | --- | --- |
| Workflow-Step-Reviewer | Interner Stringhelper hinter unveränderter geprüfter Settings-Grenze | pass ohne zusätzliche hypothetische Härtung | 3/3 pass |
| Workflow-Step-Reviewer | Mapping-Lookup verliert vorgeschriebene Eigentümerprüfung | changes_requested | 3/3 changes_requested; Zugriffslücke und fehlender passender Test erkannt |
| Ask-Review | Interner Stringhelper hinter unveränderter geprüfter Settings-Grenze | Kein blockierender Befund | 3/3 ohne umsetzbaren Befund |
| Ask-Review | Mapping-Lookup verliert vorgeschriebene Eigentümerprüfung | Belegter erforderlicher Befund | 3/3 Zugriffslücke und fehlender passender Test erkannt |

Alle zwölf nativen turn_context-Aufzeichnungen bestätigen gpt-6.1-sol mit effort low. Vollständige Finals und genaue Handles sind im temporären Laufbereich erhalten. Die 48 aufgezeichneten Toolaufrufe enthalten keine erkannten Schreib-/Testaktionen. Native Messageargumente sind im Parent-Record verschlüsselt; ihre vollständige Byteidentität ist nicht unabhängig nachgewiesen, andere erzeugte Erstellungsfelder stimmen bei allen zwölf Aufrufen überein. Keine Promptreparatur oder Erwartungsschlüssel wurde an Empfänger übergeben.

Grenzen: Diese zwölf abgegrenzten Beobachtungen beweisen keine allgemeine Zuverlässigkeit, kein xhigh- oder Claude-Code-Verhalten und keinen Vorher-nachher-Effekt. Zwei Ask-Finals beschreiben die neue unversionierte Testdatei als unverändert beziehungsweise ohne Änderung; diese ungenaue Git-Zustandszuordnung bleibt offen, obwohl die geforderte Reviewentscheidung und Testinhaltsbewertung richtig waren. Kein zusätzlicher Quellenfehler ist daraus belegt und keine neue Regel wurde auf Verdacht ergänzt.

## Umsetzung: W-006

- F1–F4: gemeinsame Step-/Frontmattergrammatik; Defaultbudget als internes Budget mit explizitem einmaligem Retry; kein Erhöhen bindender Caps. Indexposition verlangt aktiven Plan, explizite gültige Draft-/Endplaninspektion bleibt. Rohe `..`-Komponente wird vor Normalisierung abgewiesen; bestehende Link-/Reparse-Grenze bleibt.
- F5–F10: escaped H2-Titel, echte Leerabschnitte, reale Item-/Feld-/Auswahlorte statt Ersatzzeile. Nicht lesbare Inventare/Decisions erzeugen keine unberechtigten Fehlend-Diagnosen; unabhängige Strukturfehler bleiben. Batchdatum ist ein Kalendertag. Unmittelbar verschachtelte reguläre Recorddateien erzeugen nur eine Warnung, ohne Inhaltslektüre, Linkverfolgung oder Rekursion. Semantisches Index-null und regulärer Dateipfadtyp korrigiert. Drei Tests für leere Frontmatterwerte erwarten jetzt den gemeinsamen Syntaxfehler statt einer späteren Felddiagnose; Negativstatus bleibt erhalten.
- F11/F12: kein allgemeiner Stabilitätsvergleich versprochen; vorhandener Selector-Typwechsel-Sonderfall bleibt. JSON-Felder unverändert, kompakte Serialisierung. Aktuelles gültiges Profil: 233 Bytes einschließlich Newline gegenüber 296 Bytes pretty JSON ohne Newline; kein eigener 50-KB-Befund behauptet.
- Technisch: 141 Plan-Tests bestanden, ein echter POSIX-FIFO-Test auf Windows ausgelassen. Darunter 13 neue gezielte Format-/Diagnosefälle mit Korrektur-/Gegenfällen. Aktuelles Profil valid=true, keine Diagnosen. Log: lokales Implementationstemp, w006-plan-tests.log. Kein POSIX-Lauf oder aktueller Actions-Nachweis.

## Umsetzung: W-002

B1 bleibt durch die bereits vorhandenen tatsächlichen nativen Integer-Metadaten widerlegt. Keine neue Messung oder B1-Testserie. Die lokale Schema-1-Konfiguration wird nicht still migriert; gültige Workflow-Testprofile verwenden Schema 2.

- B2–B4 umgesetzt: ein Installationsowner am Einstieg; --selector ersetzt nur Unit-Auswahl, gebündelte Decision-Identität/Projektion bleibt dokumentiert. Main-Ganzitem wird vor Selector/Validator verständlich abgewiesen. Frische Korrekturprüfung behält unabhängigen vollständigen Scope, fokussiert Tiefe auf Änderung/Wirkung/offene Befunde und nutzt gültige Altbelege. Technisch 86 Workflowtests; nach zusätzlichem Transportgegenfall 14 Dispatchtests bestanden. Vollständige Original-Step-, Altbeleg-, neuer Wirkungs- und offener Finaltext bleiben im echten Helperauftrag erhalten. Die abschließenden geänderten Empfängerwege werden in W-009 geprüft; kein neuer Live-Workflow behauptet.

## Umsetzung: W-003

- C1/C4: potentiell große Ausgabe mit temporärer Schreibbefugnis schon beim ersten Lauf vollständig sichern. Atomare No-Replace-Veröffentlichung bleibt; kein direktes Schreiben unter dem endgültigen Namen. Bei Fehler nach vollständigem Schließen bleibt die eigene Tempdatei mit strukturiertem Wiederherstellungspfad erhalten. Keine universelle Wiederherstellungsbehauptung bei vorherigem Speicherausfall.
- C2/C5: gefangene SIGINT/SIGTERM führen durch begrenzte Familienbereinigung; tatsächlicher Kind-Exit 125 bleibt über vollständigen Capture von Checkerfehler 125 unterscheidbar. SIGKILL/Windows TerminateProcess/unkontrollierter Hostabbruch bleiben nicht abfangbar. Windows kann bei bereits beendetem Elternprozess mit offener Enkelpipe keine vollständige Bereinigung bestätigen; status/error/PID benennen das, der Test räumt seinen Enkel gezielt auf.
- Lokale Windows-Nachweise: acht gezielte Runtime-Tests (ein echter POSIX-Signaltest ausgelassen), sechs vorhandene Git-/Dateitests bestanden. Tatsächlicher 431.008-Byte-stdout plus stderr/Exit nach injiziertem nicht unterstütztem Hardlink vollständig nachgelesen, Wirkung genau einmal. Realer Timeout und offene Kindpipes begrenzt geprüft. Lokale Runtimefixture enthält den tatsächlichen Checker; vollständige Paket-/Plattformmatrix bleibt W-009.
- C3: offizielle Claude-Code-Dokumentation am 30.10. erneut geprüft. Effektives bashOutputMaxChars hat Vorrang vor BASH_MAX_OUTPUT_LENGTH; Read-back-Zeichen, gültige Inlineausgabe und Fehlerauszug sind unterschiedliche Grenzen. Keine Umrechnung dieser Variablen allein in ein Tokenlimit oder Fitgarantie; vollständige eigene Erfassung und knapper ausgewerteter Status beziehungsweise vorhandene Komplettdateiroute. Kein beobachteter Claude-Hostlauf behauptet. Quellen: [Output limits](https://code.claude.com/docs/en/tools-reference#output-limits), [Environment variables](https://code.claude.com/docs/en/env-vars).

## Umsetzung: W-004

- D1: Native Spawn-Aufträge über 8 KiB verwenden vorhandene Komplettdateiveröffentlichung in Systemtemp außerhalb des geprüften Projekts; kleine Aufträge bleiben direkt. Kein neuer Helper, keine Geschwisterimporte. Vorhandene Output-Capture-Route bewahrt die vollständige große Ask-Antwort; kein weiterer Antwortdatei-Mechanismus.
- D2: Original-CLI-Streams und Exit werden vor Dekodierung/Parsing privat gesichert. Fehlerpayload nennt Rohdatei, Originalexit und tatsächlich geparste Session, ohne großen/sensitiven stderr-Dump. Timeout bewahrt nur verfügbare Teilbytes und behauptet keine vollständige Antwort. Unbekannte tatsächliche Modell-/Effortdaten bleiben null: ein tatsächlich aufgezeichnetes Claude-Produzentenmodell-Schema fehlt, keine bezahlte Schemasonde. Budgetdarstellung verwendet den unverändert repräsentierbaren Zahlenwert statt sechs signifikanter Stellen.
- D3–D5: BOM nur am JSON-Requestdecoder (stdin/Datei), wörtliche Frage-/Quelltextleser unverändert. Ganzprofil-/Presetvalidierung bleibt. Unaufrufbare fresh/continue/session-name-Zweige und tote Imports entfernt; exakte Resume-ID und Persistence bleiben. Standalone-Doku nennt lesenden Konfigurationscheck.
- Technisch: 59 Ask-Tests bestanden; nach zusätzlichem realem Binärfehlerfall vier Raw-/Timeouttests bestanden. Auth-/Budgetfehler bleiben lokal lesbar, werden nicht als Antwort oder Rohdump ausgegeben. Aufzeichnender lokaler CLI-Platzhalter prüft Prompt/Args/CWD; das ist kein echter Claude-Modelllauf und kein Nachweis jeder PATH/.ps1-Installation.
- Echter großer Empfängerauftrag: 120 Datensätze über den unverändert erzeugten Dateiverweis; Antwort zählt 120, summiert 478 und erhält ID/Unicode-Label des letzten Datensatzes korrekt. Native Turnmetadaten bestätigen gpt-6.1-sol/low. Keine Rückfrage, Promptreparatur oder Projektänderung. Einzelbeobachtung der neuen Transportart, keine allgemeine Zuverlässigkeitsquote; unabhängiger Plaintext-Transportvergleich bleibt bei verschlüsselten nativen Nachrichtenargumenten unbelegt.

## Umsetzung: W-005

- E1/E3: bestehender Dateimodus bleibt am atomaren Ersatz erhalten; Konfigurationsdatei und unmittelbares Konfigurationsverzeichnis werden vor Schreibeffekten und erneut vor Ersetzen auf Link/Reparse geprüft. Eigene Stagingdatei wird auch nach fehlgeschlagenem Read-only-Ersatz bereinigt. Kandidatendiagnosen nennen den tatsächlichen Projekteingang statt des Validierungstempverzeichnisses.
- E2/E5: neue Cleanup-Paare verwenden dieselben engen Setup-Wahlstufen wie set. Gültige unverändert geerbte Sonderstufen bleiben erhalten. Schema 2 mit bekannten Altfeldern kann ausdrücklich bereinigt werden, ohne neue Paare als alte Routentabelle umzudeuten; unbekannte Felder werden nicht still gelöscht.
- E4/E6: Show sammelt beide Abschnittsfehler unter ok:false ohne effective-Teilwerte. Globales read_config bleibt streng; section validiert nur den tatsächlich gelesenen Abschnittstyp. Ungültiger Ask-Typ sperrt gültige Workflow-Auflösung nicht mehr, ungültiges JSON bleibt Fehler. Ask-Ganzprofil-/Presetvalidierung bleibt bestehen. Gemeinsamer Modell-ID-Grundvertrag verbietet sämtlichen Whitespace; Claude-spezifische Einschränkungen bleiben separat.
- E7: Setup agents/openai.yaml über normale Memberdatei/Manifest ergänzt, nur Interface und bestehendes Aufrufziel, keine neue Invocation-Policy. Das frühere Fehlen wird nicht als Runtimeblocker ausgegeben; installierte Discovery wurde nicht geprüft.
- Nachweise: 28 Setup-Tests, vier Shared-Konfigurationstests und zwei weitere reale Link-/Read-only-Tests unter Windows bestanden. Beide Konfigurationsabschnitte negativ, vollständiger Nichtschreibschutz, Modus-/Fremdfelderhalt, Cleanup-Sonderwerte, falsche Modell-IDs und tatsächliche Projektpfade geprüft. --show-config mit ungültigem Ask-Typ löst gültige Workflow-Paare; --role main erreicht danach die unabhängige fehlende native Identität. Das ist kein eigener gültiger Main-Sessionnachweis. POSIX-Modussemantik bleibt bis zur neuen Matrix ungeprüft.

## Abschluss der Berichtspunkte: W-007

| Punkt | Quelle und Bewertung | Umgang / Grenze |
| --- | --- | --- |
| G1/G2 | General-Plan-Referenzen und UI-Validation enthalten die übernommenen konkreten Kopplungen. | Nur die ausdrücklich übernommenen W-008-Korrekturen; keine Viewer-Umbenennung. |
| G3 | ../shared/runtime/skill_composition.md sagt either layout; der vorherige Paketblock beschreibt die jeweilige Standalone-/Suitepflicht. | Nur Formulierungsempfehlung; kein geänderter Laufvertrag oder zusätzlicher Mechanismus. |
| G4 | Code SKILL.md verweist innerhalb package:suite auf Scoville Plan. Der früher beanstandete wörtliche Ausdruck bundled Scoville Plan ist dort aktuell nicht vorhanden. | Kein Code-Unterpaket oder Standalone-Zwang ableiten; kein zusätzlicher Quellenfix. Die ausdrücklich beauftragte optionale Familienlisten-Klarstellung gehört zu W-008. |
| G5 | machine-data.md unterscheidet Inhalt/Zweck. | Suchtreffer/Quell-Diffs bleiben grundsätzlich direkt lesbar; enthaltene Rohberichte erhalten keine pauschale Ausnahme. |
| R1 / Reviewkosten | Workflow operations.md verlangt frische unabhängige Step-/Closure-Prüfungen; Code/sonstige Skills verlangen eigene Prüfung plus Projektvertrag. | Keine weitere unabhängige Reviewphase. Neue echte Befunde können unbegrenzt viele Runden auslösen: Es gibt keine obere Runden- oder Kostenobergrenze. Absicherungsregel und evidenzbasierter Wiederholungsstopp begrenzen unbegründete Arbeit, garantieren keine Konvergenz. |
| R2 / Ladeumfang | Manifest-/Helperpfade bestimmen mögliche Referenzen und erzeugten Auftragstext; native turn_context belegt tatsächliches Paar. | Statischer kompletter Paketumfang ist nicht tatsächliches Laden. Die 43/12-KB-Zahlen des externen Reviews sind hier nicht neu gemessen. W-001 liefert erzeugte Aufgaben und konkrete Empfängerentscheidungen; W-004 zeigt eine tatsächliche Dateiroute mit vollständig verarbeitetem Datensatz. Daraus folgen weder alle möglichen Reads noch abgerechnete Tokens oder xhigh-Wirkung. |
| R3 / UTF-8 | check_text_size.py sichert mit --publish-full Originalbytes vor Dekodierung als .bin. | Ungültiger Text ist unbrauchbar, aber gesicherte Bytes sind nicht verloren. Ohne erlaubten Capture bleiben fehlende Daten offen. C1 verbessert den ersten Lauf, nicht die Rechte schreibgesperrter Rollen. |

Keine zusätzliche materielle Produktentscheidung wurde benötigt. Freigabegrenzen bleiben: optionaler Vorher-nachher-Modellvergleich nicht beauftragt, private CI-Pushs und Quell-Export/Publikation gesperrt. Fehlende POSIX-/Claude-Modellevidenz ist keine erfolgreiche Prüfung.

## Umsetzung: W-008

- Bereits verfasste neun Skillgeschichten und Suite-Geschichte erhalten; General- und Codex-README-Vorschauen über den bestehenden Builder erzeugt und jeweils ohne veraltete Vorschau geprüft. Nur Codex-eigene Membervorschauen zurück an ihren vorgesehenen kanonischen Ort übernommen. Öffentliche Repositories unberührt. Profilaktion nicht wiederholt.
- ADR-0228 war weiterhin untracked/nie committet, ihr offener Erstellungsabschluss wurde unter der unveränderten Nutzerentscheidung fertiggestellt: keine neuen Tags/Releases; allein die belegte einmalige Installations-/Pushfreigabe für PLAN-0060 bleibt Ausnahme. ADR-0225-Verknüpfung und erkennbarer Berichtsnachtrag bleiben. Kein fertiger Plan wiedereröffnet.
- Drei General-Workflowformulierungen neutralisiert, Codex-Vertrag erhalten; modellneutrales Evidence-Beispiel; UI-Stopregel ohne Pflicht auf optionales Code; ausdrücklich falschen ersten Skillwriter-Changelog-Eintrag entfernt. Native Wartevorlage ist schon schrittweise begrenzt und verlangt tatsächlichen Endstatus, keine neue Schleife ergänzt.
- Der exakt beauftragte Standalone-Satz steht in Code an der Familienliste. family.contract / skill_composition.md bleibt der allgemeine Owner; Suite-Installation bleibt vollständig verpflichtend. Standalone-Paket-/Routenprüfung erfolgt mit der Integration, keine installierte Discovery behauptet.

## Integrierter Kandidat vor Veröffentlichungsfreigabe: W-009

- Quellenreview: geänderte kanonische Shared-Qualitäts-/Capture-/Konfigurationsquellen, aktive Consumer in Code/UI/Ask/Workflow/Setup, Plan-Helper samt ursprünglichen Negativgarantien und sämtliche geänderten Instruktions-/README-Routen geprüft. Maßstab sind die Baseline und die ausdrücklich übernommenen Änderungen. Kriterienparität und früher Ladeweg bleiben von Rollenrechten, Freigaben und festen Ergebnisfeldern getrennt. Shared-Snapshots und General-/Codex-README-Vorschauen sind synchron; Changelogs liegen an den zuständigen Quellen. Shared-Quellcommit: 9bd6639b1e1839a611f248b4d04078782c375510; vorheriger Gesamtcheck exit 0. Suite-Zuordnung steht im Commit dieses Berichts, nach eigenem vorgeschriebenem Gate.
- Gesamtcheck: korrigierter check_all.py-Lauf exit 0, zwölf Prüfgruppen bestanden, 522 Python-Tests ausgeführt, acht ausgelassen, zwei Testpfade ohne Python-Tests (Code/Handoff-Modellfälle werden nicht als Python-Tests gezählt). Der erste Gesamtcheck scheiterte an einem älteren Runtime-Test, der den Dateipfad im rohen JSON suchte und das inzwischen ausdrücklich geforderte vollständige Recovery-Tempfile verbot. Der Test dekodiert jetzt die Diagnose und prüft zusätzlich unverändertes Ziel, vollständige Recoverybytes und ausschließlich diese eigene verbleibende Tempdatei. Keine Schutzgarantie abgeschwächt.
- Weitere echte Empfängerbeobachtungen mit gpt-6.1-sol/low: Der neue Korrekturreview berücksichtigt die behobene Eigentümerprüfung samt neuem Einzeltest und erkennt unabhängig den Rückgabeverlust durch strip(), ohne alte Tests als aktuellen Gesamtpass auszugeben oder neue Tests auszuführen. Der Closure-Reviewer prüft beide Originalsteps, erkennt im zweiten Step den None-zu-Leerstring-Adapterfehler samt fehlender Adapterprüfung und hält die volle Acceptance offen. Standalone Code liest seine eigenen Planungs-/Qualitätsreferenzen, liefert einen begrenzten Vorschlag ohne Geschwister-Skill oder neuen Plan und ordnet Fortsetzungsfakten dem vorhandenen README zu. Zusammen mit W-001 und W-004 sind dies 16 native Einzelbeobachtungen; kein zusätzliches 3+3-A/B-Experiment.
- Grenzen: Keine vollständige Korrektur-Review-Commit-Lifecycleabnahme oder produktive Workflowfreigabe. Der große Ask-Dateiauftrag wurde zunächst einschließlich Datenteil vollständig gelesen und danach im Code ausgewertet: das belegt vollständigen Transport und richtige Verarbeitung, keine sparsame Datendarstellung oder allgemeine Rohdump-Regelbefolgung. Unabhängige Plaintext-Transportidentität bleibt wegen verschlüsselter nativer Nachrichtenargumente unbelegt. W-001s zwei ungenauen Git-Zuordnungsformulierungen bleiben sichtbar. Keine General-Claude-Modellwirkung, kein xhigh-Wirkungsbeweis, keine installierte Discovery und keine native POSIX-Codex-Ausführung.
- Runtime-CI: aktueller Kandidat unter skills/temp/release/runtime-ci für General/Codex × Standalone/Suite vorbereitet. Veraltetes runtime-current liegt als obsoleter disponibler Artefaktbaum im Implementationstemp, nicht als zweiter Releasekandidat. Neue private Actions-Matrix ist wegen veränderter Python-Eingaben erforderlich und mangels Pushfreigabe offen; alte Nachweise werden nicht wiederverwendet. Paketbuild/Export/Publicationsgates werden nicht als bestanden behauptet.
- Neue/geänderte öffentliche Records: Index, PLAN-0062, dessen Befundmatrix, ADR-0228/0229, ADR-0225-Verweis und erkennbarer PLAN-0060-Nachtrag geprüft. Keine Treffer für geschützte Namen, persönliche Absolutpfade oder die geprüften Credentialmuster. Das ist eine konkrete Quellprüfung, kein vollständiger historischer Geheimnisaudit. Öffentliche Produkt-/Modellnamen sind für die beschriebenen Schnittstellen notwendig. Keine Quell-Exporte erzeugt.

### Konkreter noch gesperrter Umfang

1. Nächste Freigabe: den vorbereiteten unveränderten Runtime-CI-Kandidaten ausschließlich auf main im privaten Repo benjaminstelzer/scoville-runtime-ci committen/pushen und seine sechs Windows/macOS/Linux × Python-3.11/aktuell-Jobs auswerten. Eingangsmanifest und Kandidat liegen im vorgeschriebenen einzigen Release-Stagingbaum. Das umfasst noch keine öffentliche Synchronisierung.
2. Nach gültigem Matrixnachweis wäre der bestehende Build-/Exportweg für scoville-suite und scoville-suite-for-codex-mainloop sowie die sechs Einzel-Skills Code, Plan, UI, Handoff, Project Context Cleanup und Skillwriter betroffen. Jeweils nur main, mit ihren Changelogs und vorgesehenen Paketvarianten. Neue öffentliche Records sind PLAN-0062 samt verlinkter Befundmatrix und ADR-0228/0229; die genannten bestehenden Recordkorrekturen kommen mit. Die privaten Quellen-/Namenslisten und unverbundenen Modelllaufartefakte bleiben privat.
3. Quell-Exporte, öffentliche Synchronisierung und sämtliche Pushs bleiben bis zur konkreten jeweiligen Freigabe gesperrt. Keine Installation, neuen Tags oder Releases. W-010 bleibt PUB-APPROVAL-blockiert; PLAN-0062 bleibt aktiv.

Temporäre Bereinigung: Automatische Checks konnten gesperrte eigene Tempverzeichnisse teilweise weder löschen noch vollständig verschieben. Verbleibende Workspace-Teile werden nach dem Ende ihrer Leser reversibel in Desktop/_delete verschoben; konkrete Restpfade sind nötigenfalls in der Abschlussantwort benannt. Kanonische Quellen und Testbelege wurden dabei nicht verändert.

## Veröffentlichungsfreigabe und geprüfte Matrix

Der Nutzer hat nach Vorlage des lokalen Kandidaten mit „Alles pushen“ die private CI und die vorgesehenen öffentlichen Exporte, Synchronisierungen und Pushs freigegeben. Installation, neue Tags und Releases bleiben ausgeschlossen. Die vorherige Pushsperre ist damit für diese Auslieferung aufgehoben, nicht allgemein für andere Aufträge.

Die zuvor genannte Einzelrepo-Liste war an einer Stelle falsch: Das Manifest deklariert Ask als Standalone und Project Context Cleanup nur innerhalb der Suites. Korrekt sind scoville-suite, scoville-suite-for-codex-mainloop, scoville-code, scoville-handoff, scoville-plan, scoville-ui, scoville-ask-for-codex und scoville-skillwriter. Alle acht bestehenden Ziele sind öffentlich, nicht archiviert, auf main und ohne lokale/Remote-Divergenz geprüft. Keine Sichtbarkeitsänderung und kein neues Repository.

Private CI: Commit 24120a23f725c4ef408d6eba2b6b3e43de20111a, [Runtime helpers 41056288278](https://github.com/benjaminstelzer/scoville-runtime-ci/actions/runs/41056288278). Alle sechs Jobs auf Windows, macOS und Linux mit Python 3.11/aktuell erfolgreich. Der neue Modus-/Sektionsgrenztest läuft dort auf den jeweiligen Betriebssystemen. Native POSIX-Codex-Ausführung und Claude-Modellverhalten bleiben weiterhin ungeprüft.

Vor dem Build wurden ausschließlich drei neue englische Changelog-Sätze im Wortlaut geglättet. Keine Skill-Instruktion und kein Python-Input geändert. Die Matrix bleibt für identische Python-Eingaben gültig, aktuelle Nicht-Python-Deltas werden vom vorhandenen Builder separat an den Kandidaten gebunden.

## Auslieferung und Abschluss: W-010

- Quellkandidat 03aea7753b605e8e0deba094c5fd63076a0f4824 aus sauberem main gebaut. Vier Paketansichten (General/Codex × Suite/Standalone), bestehende Release-Belege und Publikationsgates bestanden. 22 Paketstrukturen samt YAML-Frontmatter geprüft; eigenständige Cleanup-Distribution weiterhin ausgeschlossen.
- Zwei Quell-Exportprofile mit Planvalidator und Links erfolgreich geprüft. Der vorhandene Exportweg prüft private Namen und Ausschlüsse. Unterschiedliche README-Gesamtvarianten einschließlich Installationspfaden, Kompatibilität und allgemeiner Entwicklungsgeschichte gelesen; identische Textteile nur einmal. Changelogs aus den kanonischen Quellen mitgeliefert.
- Acht normale main-Pushs, keine neuen Tags, Releases oder Installation. Vorher saubere, nicht divergierende Distributionscheckouts; vollständiger Index gegen Exportdateien und danach vollständiger Remote-Gitbaum gegen Kandidatenbaum geprüft. Alle acht Ziele bleiben öffentlich, nicht archiviert und auf main. Sechs zusätzliche Live-Publikations-/Strukturaudits der Einzelskills bestanden.

| Repository | Geprüfter funktionaler Auslieferungscommit | Remote-Dateibaum |
| --- | --- | --- |
| scoville-suite | 8a534bbf52b29920b9fb7ac5407064f4742d7a9d | vollständig identisch |
| scoville-suite-for-codex-mainloop | 45b2241b323a83544295a37f18d20f474be1899c | vollständig identisch |
| scoville-code | 40c9badaa0d86f910637a4ec95a75c78f41884c6 | vollständig identisch |
| scoville-handoff | 78437f87002a23e4209be914ff285a3576bf708f | vollständig identisch |
| scoville-plan | b56b531896402a0bb7fd08a6929f83f13084b849 | vollständig identisch |
| scoville-ui | 05fc26921e173def42f5854accb6eb9b8deaa919 | vollständig identisch |
| scoville-skillwriter | dfd021137f828512ac3ccaab38fae129af057bc6 | vollständig identisch |
| scoville-ask-for-codex | 4d18f278b78ac8a3b568500940b56580b8e3f834 | vollständig identisch |

Diese Tabelle nennt den funktionalen Export vor dem Abschlussrecord. Die abschließende Dokumentationslieferung enthält nur diesen Bericht, den abgeschlossenen Plan und den leeren Aktivzeiger; sie verändert keine Skill-/Helperbytes. Auch sie folgt dem bestehenden Build-/Export-/Remote-Abgleich.

Ergebniszuordnung: W-001 bis W-006 und W-008 umgesetzt, W-007 als Quellenanalyse abgeschlossen, W-009 technisch und mit begrenzten Empfängerbeobachtungen geprüft, W-010 ausgeliefert. B1 blieb belegt unverändert; Berichtsempfehlungen G3–G5 wurden nicht ungefragt umgesetzt. Die oben dokumentierten Grenzen bleiben erhalten: kein Claude-Modell-/xhigh-/Produktivwirkungsbeweis, keine native POSIX-Codex-Ausführung, keine installierte Discovery und keine vollständige Korrektur-Review-Commit-Lifecycleabnahme. Die sechs CI-Jobs belegen die Python-Runtimepfade auf den dortigen Plattformen, nicht diese fehlenden Modell-/Hostnachweise.
