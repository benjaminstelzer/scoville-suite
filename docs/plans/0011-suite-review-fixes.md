---
format_version: 1
id: PLAN-0011
status: draft
created: 2026-09-25
updated: 2026-09-25
---

# Scoville Suite nach geprüftem Review vereinfachen und korrigieren

## Goal

Die Suite behebt die bestätigten Reviewprobleme und wird deutlich einfacher verständlich und bedienbar. Jeder der 28 Punkte einschließlich sprachlicher Mehrdeutigkeiten wird einzeln berücksichtigt. Für Plan und Workflow sind weniger Komplexität und Tokens sowie schnellere Ausführung ausdrückliche Ziele. Der Nutzer akzeptiert dafür geringfügig weniger Fehlbedienungsschutz: Ein Auftrag läuft ohne parallele Bearbeitung betroffener Dateien oder laufende Modelländerungen bis zum Abschluss. Geordnete Pläne und nachvollziehbare Ergebnisse bleiben erhalten; unnötige Übergabe-Hashes, Belege und theoretische Absicherungen entfallen. Grundlage und Einzelurteile stehen in [der geprüften Reviewauswertung](../suite-review-pruefung-2026-09-25.md).

## Non-goals

- Keine blinde Übernahme von Reviewvorschlägen, Prozentzielen oder unbelegten Sicherheits-/Leistungsbehauptungen.
- Keine Umschaltung auf PLAN-0006, Veröffentlichung oder Installation durch die Planpflege.
- Keine automatische Supportausweitung auf WordPress 6.x/ungeprüfte Minors und kein neuer Bash-Git-Zugang für Adviser.
- Keine Wiederöffnung des nach ADR-0053 abgeschlossenen PLAN-0006. F-09 und frühere praktische UI-Nachweise bleiben dort dokumentiert; bekannte Grenzen werden nicht zu bestandenen Tests umgedeutet.
- Keine automatische ASK-Sidebar-Platzierung oder neue Platzierungseinstellung. F-23 wird gemäß ADR-0055 mit ASK-Präfix und vollständigem Wegfall der Platzierungslogik umgesetzt.
- Keine Wiederholung bereits abgeschlossener PLAN-0010-Arbeit. F-19 prüft konkrete verbleibende Sprachprobleme am aktuellen Stand.

## Work items

### W-001 Dropbox-Arbeitsumgebung erzeugt keine synchronisierten Caches

Status: paused
Depends on: []
Blocked by: [HOST-POLICY]
Decisions: []
Outcome: Die in F-28 freigegebenen Rechnermaßnahmen vermeiden Python-, Node- und Rust-Buildlast im Dropbox-Quellbaum.
Acceptance: Bestehender externer Cachepfad bleibt erhalten. Ein neuer Prozess mit aktualisierter Umgebung und eine neue Sitzung bestätigen den Cacheort. Nur freigegebene Cacheverzeichnisse wurden entfernt; Ignore-Attribute bleiben auch nach dem jeweiligen Build wirksam. Dokumentation nennt tatsächliche Ergebnisse und Neustartbedarf.
Steps:
1. Prüfe die vorhandene Benutzer- und Prozessvariable PYTHONPYCACHEPREFIX sowie die tatsächlichen Cachepfade in members/ und ../shared/. Setze den freigegebenen externen Benutzerpfad nur nach den Freigabegrenzen und Betriebssystembefehlen im Abschnitt „Ausführungsgrundlage für W-001“ der verlinkten Reviewauswertung. Bestehendes externes Ziel erhalten; bei bestehendem Ziel innerhalb Dropbox vor Änderung fragen. Andere Systemeinstellungen und Ordner sind ausgeschlossen.
2. Prüfe die aufgelösten Löschziele und entferne ausschließlich die benannten __pycache__-Ordner. Richte die freigegebenen Ignore-Attribute für members/scoville-plan/development/viewer/node_modules und src-tauri/target ein; prüfe ihre Haltbarkeit bei Neuerstellung.
3. Ergänze die kanonische Entwicklungsdokumentation um plattformspezifische Einrichtung und Python -B. Nutze die vorhandene Root-.gitignore; zusätzliche Member-Dateien nur für echte Distributionsanforderungen.
Evidence: [2026-09-25: Sieben Cacheordner gefunden; System-/Cachebefehl vor Ausführung mit blocked by policy abgewiesen., 2026-09-25: Benutzervariable auf %LOCALAPPDATA%\pycache gesetzt; neuer Kindprozess meldet denselben externen sys.pycache_prefix., 2026-09-25: Viewer node_modules behielt com.dropbox.ignored=1 nach npm ci; src-tauri/target trägt denselben Wert., 2026-09-25: Einzeln geprüfte Löschung eines der sieben Cacheordner erneut mit blocked by policy abgewiesen; alle sieben bleiben bestehen., 2026-09-25: README-Quelle und generierte Suite-README dokumentieren Plattformwerte Python -B Ignore-Attribute und Neustartbedarf.]
Next action: Nach Freigabe durch Host-Policy ausschließlich die sieben benannten Cacheordner entfernen; danach neue Sitzung und Ignore-Attribut nach Cargo-Build prüfen.

### W-006 Handoff-Vorlage bleibt eindeutig und vollständig kopierbar

Status: done
Depends on: []
Blocked by: []
Decisions: [ADR-0045]
Outcome: Die zusätzlichen F-02/F-11-Befunde sind in Vorlage und Sprache behoben, ohne die bereits umgesetzte PLAN-0009-Überarbeitung zu wiederholen.
Acceptance: Innere Dreier- und Vierer-Fences zerstören den äußeren Block nicht. Ein belegtes Aufgabenrepo wird übernommen, zufälliges Host-CWD nicht. Pflichtangaben und optionale State-Labels sind widerspruchsfrei erklärt. Vier Abschnitte, Autorität, Redaktion und Fortsetzungsgrenzen bleiben erhalten.
Steps:
1. Passe members/scoville-handoff/scoville-handoff/assets/continuation-prompt.md und die Kompositionsregel in SKILL.md an: äußerer Fence länger als innere Folgen.
2. Präzisiere nur die noch mehrdeutigen Aussagen über Task-Arbeitsort und optionale Labels. Ergänze gezielte Fälle in development/tests/evaluation-cases.json und bewahre vorhandene Recoveryfälle.
Evidence: [2026-09-25: Fence-/Ordner-/Labelregeln am vollständigen Vertrag geprüft; drei Fälle ergänzt; beide Paketprofile samt Links geprüft., quick_validate lehnt das bestehende compatibility-Feld ab; bekannter Konflikt in W-007. Kein neuer Modelltest.]

### W-003 Claude-Aufrufe haben eine nachvollziehbare Zeitgrenze

Status: done
Depends on: []
Blocked by: []
Decisions: []
Outcome: Ask beendet einen festhängenden CLI-Aufruf mit konfigurierbarem Timeout und eindeutiger Fehlermeldung.
Acceptance: Default 1800 Sekunden, expliziter Override und ungültige Werte sind geprüft. Ein Fake-CLI überschreitet eine kurze Frist und liefert claude_timeout ohne Retry; Prozessende des tatsächlich gestarteten Wrappers und seiner CLI-Kindprozesse ist beobachtet. Ein Test mit länger laufendem Kindprozess bestätigt, dass nach dem Timeout kein Prozess dieses Aufrufs weiterläuft; ein unabhängiger Kontrollprozess bleibt unberührt.
Steps:
1. Ergänze den Default in members/scoville-ask-for-codex/scoville-ask-for-codex/config.default.json und die Auflösung in scripts/ask.py.
2. Erhalte den vorhandenen Fehlerpfad und ergänze den stabilen Code. Beende bei Timeout die zu diesem Aufruf gehörenden Prozesse, unter Windows einschließlich PowerShell-/Node-Kindern, unter POSIX mittels einer für den Aufruf angelegten Prozessgruppe. Wähle einen vorhandenen einfachen Prozessmechanismus; bloßes subprocess.run(timeout=...) reicht für Wrapperkinder nicht. Prüfe echtes Timeoutverhalten und verständliche Ausgabe. Aktualisiere die betroffene CLI-/Konfigurationsanleitung.
Evidence: [2026-09-25: Nutzerkorrektur berücksichtigt lange Fable-Reviews; Standard wird auf 3600 Sekunden statt der ursprünglichen 1800 gesetzt., 2026-09-25: 20 Ask-Tests bestanden inklusive echtem Windows-Prozessbaum und unberührtem Kontrollprozess; POSIX hier nicht ausgeführt.]

### W-012 WordPress-Beispiele zeigen ihre tatsächliche Versionsgrenze

Status: done
Depends on: []
Blocked by: []
Decisions: []
Outcome: F-03/F-21 sind ohne unbelegte Supportausweitung verständlich beschrieben.
Acceptance: 7.0-/7.1-Beispiele und unbekannte Minor-/Prerelease-Versionen sind eindeutig getrennt. Ein unbekannter Fallback gilt nicht als erfolgreiche Tokenabnahme. Mindestversion des Plugins und getestete Laufzeit werden separat erfasst. Keine automatische 6.x- oder >=7.1-Zusage.
Steps:
1. Präzisiere members/scoville-ui/scoville-ui/references/wordpress/version-compatibility.md und adapter.md am bestehenden 7.0/7.1-Support. Ergänze die fehlende unbekannt-Version-Zeile und einen Kommentar unmittelbar an der kopierbaren Verzweigung: Andere Versionen sind ungeprüft, der Zahlenpfad ist kein Supportnachweis. Keine neue Debug-Warnung oder Laufzeitdiagnose allein für das Dokumentationsbeispiel.
2. Prüfe die Verzweigung für 7.0, 7.1, 7.2, Prerelease und fehlenden/fremden Handle. Reale neue Versionen nur nach gesondertem Versionsnachweis als unterstützt nennen.
Evidence: [2026-09-25: 12 PHP-Version-/Handlefälle bestanden; unbekannte Version im Kommentar und in Matrix benannt; Mindestversion getrennt. Kein neuer gerenderter Supportnachweis.]

### W-015 Ask steht im Titel vorne und verzichtet auf Sidebar-Platzierung

Status: done
Depends on: []
Blocked by: []
Decisions: [ADR-0060]
Outcome: Neue native Ask-Aufgaben heißen exakt Ask <Modell> · gefolgt von einem Leerzeichen und dem unveränderten Aufrufertitel; <Modell> ist die tatsächlich ausgewählte Modell-ID. Automatische Sidebar-Platzierung entfällt vollständig.
Acceptance: Kurze, lange und Unicode-Titel liefern Ask <Modell> · <Aufrufertitel> ohne Ask-TAsk-Suffix oder weitere Kennungen. Der Ask-Ablauf ruft keine Platzierungsoperation und keine allein dafür nötigen Host-Aufrufe auf. Task-ID-Zuordnung und Fortsetzung bleiben erhalten; bestehende Aufgaben werden weder umbenannt noch umsortiert.
Steps:
1. Übergebe das tatsächlich ausgewählte Modell vom Ask-Aufrufer an die Titelerzeugung und setze die neue Ask-Titelform in ../shared/runtime/task_lifecycle.py und seiner kanonischen Anleitung um. Workflow-Titel bleiben unverändert.
2. Entferne die Sidebar-Operation und ihre Aufrufer aus members/scoville-ask-for-codex/scoville-ask-for-codex/scripts/ask.py, den betroffenen Referenzen und README-Fragmenten. Keine Opt-in-Einstellung oder Ersatzsortierung einführen.
3. Passe Titel-/Ablauftests an, erzeuge betroffene Shared-Kopien und Pakete über den bestehenden Buildweg und prüfe Titel, fehlende Platzierungsaufrufe und erhaltene ID-Zuordnung.
Evidence: [2026-09-25: 20 Ask-Tests samt gebautem Einzel-/Suitepaket und sechs gemeinsame Titeltests bestanden; Platzierungsoperation entfernt; aktive Aufrufer-/Dokumentationssuche ohne Treffer.]

### W-014 Vorhandener Runner ist für die gezielten Vergleiche vorbereitet

Status: done
Depends on: []
Blocked by: []
Decisions: [ADR-0045]
Outcome: Der vorhandene Vergleichsweg ist vor den Umbauten für F-25 nutzbar. Baseline, Kandidat und einfacher Zielprompt werden unter nachvollziehbar gleichen Bedingungen ausgewertet.
Acceptance: Eine kleine Probe mit development/luna-tests/run_codex_cli_case.py oder seinem vorhandenen Ergebnisformat belegt, dass Variante, Fall, Modell/Host/Effort, Ergebnis, geladene Referenzen und verfügbare Kosten getrennt erfasst werden. Fehlende Tokenmetrik bleibt als nicht verfügbar markiert. Kein zweiter Runner und kein vollständiger Suite-Modelllauf werden zur Voraussetzung.
Steps:
1. Prüfe den vorhandenen Runner und seine Ergebnisformate für die ausgewählten Vergleichsfälle. Ergänze nur eine tatsächlich fehlende kleine Funktion oder verwende eine knappe gemeinsame Auswertungsvorlage. Halte Fallauswahl, gleiche Bedingungen und getrennte Schlussfälle vor Läufen fest.
2. Prüfe an einer vorhandenen Ausgabe die Auswertbarkeit; eine neue begrenzte Probe nur bei fehlendem Nachweis. Die echten Ausgangsmessungen vor Änderungen bleiben Bestandteil von W-008, W-010 und W-011.
Evidence: [2026-09-25: Vorhandenes Ergebnisformat geprüft; 18 Runner-Tests bestanden. Gemeinsame Auswertung in development/luna-tests/suite-simplification-comparison.md; echte Messungen folgen vor Umbauten.]

### W-002 Helper verarbeiten Unicode und Pfade portabel

Status: paused
Depends on: []
Blocked by: [CI-PLATFORMS]
Decisions: []
Outcome: Die in F-17 bestätigten Interpreter-, Pfad- und Streamprobleme sind behoben, ohne das Planformat zu ändern.
Acceptance: CLI-Aufrufe mit Leerzeichen im Skill-/Projektpfad und CJK/Umlauten funktionieren unter geeigneten Interpretern. stdin/stdout verwenden nachvollziehbar UTF-8, ungültige Daten liefern klare Fehler. Die GitHub-Actions-Matrix windows-latest, macos-latest und ubuntu-latest prüft Python 3.11 und die bei Umsetzung aktuelle stabile Version. Ausstehende Plattformläufe bleiben offene Abnahme. Ein zu alter Interpreter liefert eine Versionsdiagnose; ein Windows-Store-Alias wird nicht als funktionsfähiger Interpreter behandelt. Eine Suche der aktiven Befehlsbeispiele plus Sichtprüfung bestätigt gequotete Pfadargumente und Bezug zur einmaligen Interpreterauswahl.
Steps:
1. Korrigiere die CLI-Grenzen in ../shared/runtime/task_lifecycle.py und den betroffenen Plan-/Workflow-Helpern. Verwende vorhandene Streamkonfiguration oder eine kleine gemeinsame Funktion nur bei tatsächlicher Mehrfachnutzung.
2. Ersetze uneindeutige Interpreter-/Pfadbeispiele an ihren kanonischen Fragmenten und Referenzen durch eine einmal erklärte Auswahl und korrekt gequotete Aufrufe. Prüfe echte Versionsausgabe statt Dateiname: Windows-Store-Alias ohne nutzbaren Interpreter überspringen; vorhandenes Python 3.9/3.10 bei einem 3.11+-Helper als zu alt melden. Keine feste Python-Version aller macOS-Installationen behaupten.
3. Prüfe betroffene gebaute Pakete und die relevanten Verbraucher von shared. Ergänze die genannte GitHub-Actions-Matrix im vorhandenen Testaufbau; Veröffentlichung oder Push ist durch diesen Planpunkt nicht automatisch erlaubt. CRLF-Vertragsänderungen gehören ausschließlich zu W-009.
Evidence: [Linux Python 3.12: Plan 82 bestanden; Ask 20 mit einem Windows-Skip; Workflow 89 bestanden und ein Test wegen fehlendem Node nicht ausgefuehrt, 2026-09-25: Python 3.11 lokal zusätzlich geprüft; Plan 78 und Ask 20 Tests bestanden., 2026-09-25: Ask 20 und Workflow 90 sowie Plan 78 Tests bestanden; sieben Titeltests inklusive UTF-8/cp1252 und ungültiger Eingabe bestanden., Befehlsbeispiele auf unquotierte Platzhalter geprüft; README-Prüfung und beide Git-Diffprüfungen fehlerfrei. CI-Matrix für drei Systeme und Python 3.11/aktuell vorbereitet; Läufe offen., Aktueller Workflow: 14 Tests Windows 3.11 und Linux 3.12 bestanden; Python 3.9/3.10 liefern Versionsdiagnose; Store-Alias Exit 9009 erkannt; Details im Pruefbericht]
Next action: Drei-Plattform-CI einschliesslich macOS ausfuehren, sobald die externe Ausfuehrung verfuegbar und autorisiert ist. Keine Veroeffentlichung erfolgt.

### W-008 Plan wird ein deutlich einfacheres System für geordnete Arbeit

Status: done
Depends on: []
Blocked by: []
Decisions: [ADR-0045, ADR-0048, ADR-0052]
Outcome: Plan beschreibt Ziele, geordnete Arbeit, Abnahme und nächste Schritte kompakt. Gewöhnliche Pflege benötigt keine Modellprofile, Hashbelege oder verstreuten Sonderfallrouten, soweit die angenommene Ausgestaltung dies festlegt.
Acceptance: Einfügen, Umordnen unbegonnener Arbeit, Next action, Evidence, Abschluss und Wiederaufnahme bleiben verständlich und zuverlässig. Bestehende gültige Records behalten Bedeutung und Autorität. Hash-/Bytebelege verschwinden aus Modellanweisungen. Nur tatsächliche Mehrdateiänderungen brauchen gemeinsame Konsistenzprüfung. F-01 ist ausdrücklich abgedeckt: Im gebauten general-Profil gelingt eine Planänderung mit Python 3.10 ohne Writing-Profile-Helper bis zur erfolgreichen Validatorprüfung. Codex behält seine separat geltende Laufzeitgrenze. Für Einfügen, Next action, Evidence und Abschluss sind geladene Referenzen, Ergebnis und Kosten vor/nachher festgehalten. Eine Suche nach sha256, digest und Byte-Belegen in gebauten SKILL.md/references samt Bewertung der Treffer bestätigt, dass keine Modellpflicht übrig bleibt; Negativbeschreibungen sind keine Fehler. Kosten und reale Ergebnisse werden statt Prozentziele berichtet.
Steps:
1. Sichere den tatsächlichen Ausgangsstand von Plan samt verwendeten Imports vor Änderungen temporär. Lege wenige gleiche Fälle für Einfügen, Next action, Evidence und Abschluss fest und erfasse Ergebnis, Tokens soweit verfügbar, Tool-Aufrufe und Dauer vor dem Umbau. Nutze vorhandene Vergleichswerkzeuge; Verwende den zuvor in W-014 geprüften Vergleichsweg; keine zusätzliche große Runnerentwicklung.
2. Gleiche SKILL.md und references/native-editing.md, native-work-items.md, native-project-lifecycle.md und planning-granularity.md unter members/scoville-plan/scoville-plan/ mit den häufigen Handlungen ab. Ordne jede benötigte Regel genau einem vor der Handlung verfügbaren Besitzer zu.
3. Entferne die Modell-Hashpflicht und zusätzliche Konfliktabsicherung für parallele Bearbeitung gemäß ADR-0052. Vereinfache den Einzeldateiweg auf Lesen, kontextgebundenes Ändern und passende Ergebnisprüfung. Reduziere geladenen Text nach Handlung, ohne Pflichtfakten nur in unzugängliche Tests zu verschieben. Erkläre den Einzelbetrieb und seine Grenzen in den kanonischen Plan-README-Fragmenten.
4. Behebe F-01 durch direkte Entfernung der Plan-Modellprofilpflicht gemäß angenommener ADR-0048; prüfe den general-Endzustand unter Python 3.10. Setze die Profilvereinfachung um und bereinige Imports/Manifest nur für entfallene Planabhängigkeiten. Workflow-Verbraucher des gemeinsamen Helpers getrennt erhalten.
5. Vereinfache Decision-Batch-Identität auf eine gewöhnliche ID mit bestehender Mitgliederliste, sofern die Consumerprüfung v1-Bestandskompatibilität bestätigt. Alte Hash-IDs weiter lesen; keine neue Ersatzmaschine schaffen.
6. Prüfe typische Planhandlungen, Mehrdateiabschluss und Wiederaufnahme gegen bestehenden Validator/Selector und tatsächliche Consumer. Ergänze nur fehlende entscheidende Fälle und beobachte einen begrenzten Verständlichkeitsvergleich.
Evidence: [78 Plan-Tests und finale General-/Codex-Pakete bestanden; Wiederaufnahme unter Python 3.10 validiert, General-Paket nach Next-action-Edit unter Python 3.10.20 validiert, Vergleich in development/luna-tests/suite-simplification-comparison.md; kein belegter Kosten- oder Geschwindigkeitsgewinn]

### W-009 Evidence und Windows-Zeilenenden werden ohne Informationsverlust gelesen

Status: done
Depends on: [W-008]
Blocked by: []
Decisions: [ADR-0049]
Outcome: Die angenommene Formaterweiterung beseitigt F-14 und den CRLF-Teil von F-17 bei klaren Upgradegrenzen.
Acceptance: Alte Fixtures bleiben gültig. Neue Evidence mit Sonderzeichen und CRLF werden von Validator, Selector und Viewer konsistent verarbeitet. source_text-Vertrag bleibt belegt; kein unbeabsichtigtes Normalisieren. Verhalten alter Reader ist dokumentiert.
Steps:
1. Prüfe alle Parser und Formatverbraucher unter members/scoville-plan/ einschließlich Viewer und betroffener Batchlogik. Entscheide anhand veröffentlichter Reader, ob format_version 1 erweiterbar ist.
2. Setze erst nach Annahme die gemeinsame Evidence-/Zeilenendenregel im Parser und in den manuellen Formatreferenzen um. Prüfe Daten aus alten und neuen Profilen sowie die bestehenden Workflow-Consumer. W-010 übernimmt anschließend diesen geprüften Formatstand.
Evidence: [ADR-0065 konkretisiert Nutzerkorrektur: Klartext-Evidence ohne JSON; historischer ADR-0049-Verweis bleibt erhalten, 82 Python-Tests bestanden; alte Syntax unveraendert lesbar; alter Reader lehnt Erweiterungen erwartungsgemaess ab, 13 Viewer-Parser-Rust-Tests unter Linux bestanden; Pakete und 90 Windows-Workflowtests bestanden; Details in docs/suite-review-pruefung-2026-09-25.md]

### W-005 Eine Konfigurationsdatei überschreibt importierte Skill-Defaults

Status: done
Depends on: []
Blocked by: []
Decisions: [ADR-0052, ADR-0061]
Outcome: Ask und Workflow lesen .scoville/config.json vor ihren importierten Defaults. Es gibt keine zusätzliche persönliche Konfigurationsebene.
Acceptance: Ohne Datei und bei fehlenden Werten gelten die Skill-Defaults. Teilweise Overrides und ungültige Werte sind über die tatsächlichen Verbraucher geprüft. Lesen und Workflowstart erzeugen keine Datei. Einmalige Anfrage-/Step-Parameter bleiben wirksam und ungespeichert. Alte persönliche Dateien bleiben erhalten; ihre Abweichungen werden beim Übergang benannt statt heimlich weiter geladen. Das fehlende ursprüngliche Modellpaar bei Reparatur 2/3 wird ohne erfundene Ursache erklärt. Keine Snapshots oder Überwachung. Aktive Anleitungen importieren Defaults statt sie zu duplizieren.
Steps:
1. Prüfe vorhandene Ask config.json und den bisherigen Workflow-Konfigurationsweg auf zu übernehmende Abweichungen. Entferne die persönliche Ladeebene ohne Dateien zu löschen; führe keine workflow.local.toml ein.
2. Implementiere den kleinen gemeinsamen Loader für .scoville/config.json in ../shared/runtime/ und binde ihn über suite.json in Ask und Workflow ein. Bewahre deren Einstellungsstrukturen und Adviser-Mergeverhalten. Prüfe bestehende explizite Aufrufparameter getrennt von gespeicherter Konfiguration.
3. Prüfe fehlende Datei, partielle Overrides, ungültige Werte und Modelle zwischen Läufen. Präzisiere die Reparaturfehlermeldung. Dokumentiere nur Datei vor Default und unveränderte Einstellungen während eines Laufs.
Evidence: [Eine Datei vor Defaults ohne persoenliche Ladeebene umgesetzt; 21 Ask- und 92 Workflowtests sowie zwei Schreibprofiltests bestanden, Teilwerte und einmalige Overrides ueber echte Verbraucher geprueft; Lesen legt keine Datei an; Details in docs/suite-review-pruefung-2026-09-25.md, W-002-Plattformabnahme bleibt offen; vorhandenes persoenliches Claude-Budget 50 statt Default 10 USD benannt und nicht ungefragt uebernommen]

### W-017 Prioritized after W-005: Scoville Setup verwaltet die Konfigurationsdatei

Status: done
Depends on: [W-005]
Blocked by: []
Decisions: [ADR-0061, ADR-0064]
Outcome: Ein ausschließlich mit der Suite ausgelieferter optionaler Setup-Skill zeigt wirksame Einstellungen an und speichert ausdrücklich beauftragte Werte in .scoville/config.json.
Acceptance: Setup hat keine eigenständige Distribution. Anzeigen ohne Projektdatei erzeugt keine Datei. Setup kann claude.timeout_seconds in der Konfigurationsdatei speichern; Default 3600 Sekunden und positive endliche Werte prüfen. Die Datei überschreibt importierte Skill-Defaults; es gibt keine weitere persönliche Ebene. Bestehende Einstellungen bleiben erhalten und ungültige Werte werden erklärt. Einmalige Overrides werden nicht dauerhaft gespeichert. Ask und Workflow funktionieren ohne Setup-Aufruf. Keine zusätzliche Konfigurationsdatei, eigene Ladelogik, Installation, Updates oder Überwachung entstehen.
Steps:
1. Prüfe nach W-005 die bestehenden Ask-/Workflow-Ladeverträge und ihre Validierung. Prüfe als Setup-Felder Ask-Adviserauswahl und Presets einschließlich Modell/Effort sowie Claude-Budget, Sitzungspersistenz, Customizations und die durch W-003/W-004 hinzukommenden Timeout-/Web-Einstellungen. Für Workflow bleiben Executor-/Reviewer-Modellpaare je Route. Übernimm die Context-Thresholds für Koordinator und Worker aus den importierten Defaults gemäß ADR-0064 als konfigurierbare Werte; prüfe erlaubte Prozentwerte. Entfernte Coordinator-Modell-/Titelsettings und Plan-Schreibprofile nicht wieder einführen. Optionale Workflow-Schreibprofile erst nach W-010 auf verbleibenden Nutzen prüfen. Verwende bestehende Verträge für Rangfolge und Prüfung; verwende ausschließlich die Konfigurationsdatei vor den Skill-Defaults.
2. Erstelle den eng begrenzten Skill unter members/scoville-setup/scoville-setup/ und registriere ihn über suite.json ausschließlich als Suite-Bestandteil; keine eigenständige Distribution. Pflege Dokumentation in development/readme/scoville-setup/; verwende den vorhandenen Buildweg für Projektionen und Paketprüfung.
3. Prüfe Anzeigen ohne Datei, gezielte Speicherung in der Konfigurationsdatei, Erhalt fremder Werte und ungültige Eingaben. Prüfe anhand tatsächlicher Ask-/Workflowverbraucher die wirksamen Werte und den Start ohne Setup.
Evidence: [Setup ist nur im Codex-Suitepaket; gemeinsame Verbraucherpruefung und importierte Defaults statt zweiter Ladelogik, Zwei gebaute Setup-Verbrauchertests bestanden; 21 Ask- und 92 Workflowtests sowie sechs Buildertests bestanden; Kurzvalidator akzeptiert Setup, Anzeige ohne Dateierzeugung und Erhalt fremder Werte geprueft; Defaults 25/75 umgesetzt; Details in docs/suite-review-pruefung-2026-09-25.md]

### W-010 Workflow führt mit weniger Zuständen und Übergabeaufwand aus

Status: cancelled
Depends on: [W-008, W-009, W-005]
Blocked by: []
Decisions: [ADR-0045, ADR-0064, ADR-0052, ADR-0061]
Outcome: Der nach ADR-0064 vereinfachte Workflow führt geordnete Planeinheiten mit Worker, Reviewer, begrenzter Reparatur und automatischem Context-Rollover für Koordinator und Worker aus.
Acceptance: Automatische Übergabe an einen neuen Koordinator und Nachfolgeworker ist bei den konfigurierten Kontextschwellen belegt; bloße Speicherung oder native Kompaktierung genügt nicht. Grenzfälle und fehlende/veraltete Telemetrie sind geprüft. Unvollständige Arbeit und aktueller Run bleiben erhalten; Vorgänger und Nachfolger schreiben nicht gleichzeitig weiter. Workflow-Anzeigen verwenden SCW MNGR · RUN <Nummer> · <Aufrufertitel>, SCW WORK · RUN <Nummer> · <Aufrufertitel> und SCW REVW · RUN <Nummer> · <Aufrufertitel>. Die sichtbare Runnummer beginnt bei 1 und bezeichnet denselben Workflowlauf für Manager und zugehörige Worker/Reviewer; sie ist keine Task-ID oder Reparaturnummer. MNGR ersetzt COORD im sichtbaren Titel; technische Rollen bleiben davon getrennt. Die Hashanzeige ist auf tatsächliche Verbraucher geprüft und entfällt ohne belegten Bedarf. Taskidentität bleibt über IDs erhalten. Die angenommene Schleife bewahrt Planhoheit, autorisierte Änderungen, Nutzerstopp und klare Fehler. Übergabebelege und unnötige SHA-256-Prüfungen sind entfernt. Keine Modellkonfigurations-Snapshots. Jede Zeile der zwölfteiligen Umfangstabelle in ADR-0064 wird im Endstand mit Quellstelle oder entfallenem Pfad sowie passendem Ablaufergebnis abgeglichen. Eine Suche nach sha256, digest und Byte-Belegen in gebauten SKILL.md/references samt Bewertung der Treffer bestätigt den Wegfall der Modellpflicht. Relevante Simulationen und ein begrenzter realer Lauf belegen die Änderung; reine Textgröße beweist sie nicht.
Steps:
1. Sichere den tatsächlichen Ausgangsstand von Workflow samt verwendeten Imports vor Änderungen temporär. Wähle einen begrenzten normalen Mehr-Einheiten-Lauf und belegte bisherige Fehlerfälle; erfasse dieselben Ergebnisse und Kosten vor dem Umbau mit vorhandenen Werkzeugen. Verwende den zuvor in W-014 geprüften Vergleichsweg; keine zusätzliche große Runnerentwicklung.
2. Lies die vollständige Umfangstabelle in ADR-0064; sie ist die Abnahmecheckliste dieses Umbaus. Ordne die tatsächlich konsumierten Regeln in members/scoville-workflow-for-codex/scoville-workflow-for-codex/ und ../shared/runtime/ dem Kernablauf zu. Ersetze betroffene bestehende Decisions gezielt nach Annahme, statt alle historischen ADRs pauschal aufzuheben.
3. Baue direkten Dispatch und einen kleinen Datensatz für aktuelle Einheit, Task und Ergebnis. Entferne zusätzliche Konfliktabsicherung für parallele Schreiber sowie unnötige Park-/Generations-/Transportzeremonien entsprechend ADR-0064 und ADR-0052. Erkläre den Einzelbetrieb in den kanonischen Workflow-README-Fragmenten. Erhalte check_context_checkpoint.py und die tatsächlich benötigte Übergabe an Nachfolgetasks für Koordinator und Worker. Verwende die vereinfachte Handoff-Struktur mit Arbeitsstand, offenen Punkten und nächstem Schritt; keine Hash-/Empfangsbelege. Defaults sind Koordinator ab 25 Prozent und Worker über 75 Prozent. Rollover-Schwellen kommen aus .scoville/config.json oder bei fehlendem Wert aus den importierten Skill-Defaults. Vereinfache den Ablauf ohne Rollover abzuschaffen. Bewahre zunächst Resultatformat und Routewerte, damit keine unnötige zweite Migration entsteht.
4. Setze die beauftragten Titel in ../shared/runtime/task_lifecycle.py und den Workflow-Aufrufern um; übergib den unveränderten Aufrufertitel und die laufende Runnummer aus dem Workflowstand. Bewahre den ursprünglichen Titel ohne wiederholte SCW-Präfixe. Prüfe die bisher sichtbare Hash-/Run-Kennung auf tatsächliche Verbraucher und entferne unnötige Ausgabe samt Anweisungen. Erzeuge keinen zusätzlichen Manager-Task allein für dessen Titel; ADR-0064 behält den aufrufenden Task als Koordinator. Prüfe Titel und weiterhin eindeutige ID-Zuordnung.
5. Prüfe tatsächlichen Diff vor Review/Commit, nutze vorhandene Commitautorität und melde Archivierungsfehler ohne fachliche Blockade. Teste Normalablauf, Reparaturgrenze, automatischen Koordinator-/Worker-Rollover, Stopp/Wiederaufnahme und belegte vorherige Fehler.
Evidence: [Neues Titelschema gemaess ADR-0066; 19 Lifecycle-/Titeltests bestanden, Nativer Rollover erfolgt; Snapshot-Verwechslung bei Ergebnisuebernahme korrigiert; Wiederholungspruefung nach externem Review offen. Details im Pruefbericht, Nutzer genehmigt Abbruch und Uebertragung aller offenen Abnahmepflichten an W-026; bisherige Nachweise bleiben erhalten]

### W-011 Code- und UI-Sprache führt zu eindeutigen Handlungen

Status: done
Depends on: []
Blocked by: []
Decisions: [ADR-0045]
Outcome: F-19/F-20 und die Sprachhinweise aller übrigen Punkte sind gegen den aktuellen Stand geprüft und konkrete Mehrdeutigkeiten behoben.
Acceptance: Code unterscheidet Handlung, Klassifikation und Risikooverride eindeutig. UI lädt benötigte semantische Grenzen, ohne Testausgabeformate immer mitzuladen. Begriffe, Pflicht/Optional und Fehlerfolgen sind für Menschen und Modelle gleich verständlich. Bestandene frühere Tests ersetzen die Sprachprüfung nicht.
Steps:
1. Sichere die aktuellen Code-/UI-Texte samt geladenen Imports vor Änderungen temporär. Lege wenige Routing- und Verständlichkeitsfälle einschließlich korrekter Bestandsfälle fest; prüfe sie vor und nach der Überarbeitung unter gleichen Bedingungen mit vorhandenen Werkzeugen. Verwende den zuvor in W-014 geprüften Vergleichsweg; keine zusätzliche große Runnerentwicklung.
2. Prüfe die im Review benannten verdichteten Sätze, Ausnahmefolgen und Beispiele in Code und UI gegen ihre vollständigen aktuellen Regeln. Formuliere jede verbleibende Mehrdeutigkeit als konkreten Vorher/nachher-Fall.
3. Vereinfache Code SKILL.md auf klare Handlungen und geordnete Bedingungen; bewahre den aktuellen PLAN-0010-Vertrag. Verschiebe in UI nur ausdrücklich strukturierte Ausgabeformate in bedarfsweise geladene Referenzen.
4. Prüfe betroffene Routingfälle und typische Leserfragen. Für F-22 die bereits vorhandenen Greenfield-Regeln auf Verständlichkeit prüfen; zusätzliche Regeln nur bei benannter Lücke. Frühere praktische UI-Nachweise und ihre Grenzen bleiben beim nach ADR-0053 abgeschlossenen PLAN-0006; keine Wiederöffnung.
Evidence: [Code-/UI-Routing im Luna-Vergleich geprueft; zwei konkrete WordPress-Mehrdeutigkeiten im Schlussfall behoben, Finale strukturierte Klassifikation mit sechs Feldern und fuenf Verboten korrekt; General-/Codex-Paketlinks bestanden, Details und Fehlversuche in development/luna-tests/suite-simplification-comparison.md; keine belegte Geschwindigkeitsersparnis]

### W-004 Ask benennt und begrenzt seine tatsächlichen Fähigkeiten

Status: done
Depends on: []
Blocked by: []
Decisions: [ADR-0047]
Outcome: Ask erklärt vertragliches Read-only korrekt und aktiviert Webwerkzeuge gemäß angenommener Einstellung.
Acceptance: Default und Opt-in entsprechen der angenommenen Decision. Kein Dokument behauptet native Sandboxisolierung oder Offlinebetrieb. Keine zusätzliche Hash-Schnappschussmaschine und kein pauschaler Bash-Git-Zugang wurden eingeführt.
Steps:
1. Setze nach Annahme ADR-0047 in scripts/ask_claude.py, scripts/ask.py, config.default.json und references/claude.md um.
2. Präzisiere Einstieg und kanonische README-Fragmente: Native Adviser erhalten einen Read-only-Auftrag, aber keine technische Schreibsperre durch den aktuellen Host. Bestehende Adviser- und Fehlerverträge erhalten.
Evidence: [21 Ask-Tests bestanden; Default und Opt-in erreichen beide CLI-Toolflags; ungueltige Werte abgelehnt; beide Codex-Layouts geprueft, Native Read-only als Auftrag ohne technische Schreibsperre dokumentiert; keine Live-Modellabfrage fuer diese Adapterpruefung]

### W-007 Dokumentation beschreibt Distribution und Unterstützung korrekt

Status: done
Depends on: []
Blocked by: []
Decisions: [ADR-0060]
Outcome: F-07/F-08/F-12 sind an ihren kanonischen Dokumentationsbesitzern korrigiert, ohne neue Distributions- oder Hostzusagen.
Acceptance: Ask-Standalone ist korrekt erklärt. General/Codex und Quell-/Paketlinks bleiben sachlich getrennt. Hostangaben nennen nur belegte Unterstützung. Kurze kanonische Records bleiben erhalten; persönliche Pfade und Rohmaterial werden nach Retention behandelt. Paketmetadaten folgen einem belegten Formatvertrag.
Steps:
1. Korrigiere die Ask-Installation in development/readme/scoville-ask-for-codex/ und den zuständigen Shared-README-Fragmenten; erzeuge Member-/Release-Projektionen über den Builder.
2. Prüfe compatibility-Feld und Hostformulierungen anhand des tatsächlich verwendeten Paketvalidators. Kläre den bekannten quick_validate-Konflikt, ohne dessen Prüfung für grüne Ausgabe umzuschreiben.
3. Prüfe die in F-07 benannten Berichte auf kanonisches Wissen, Rohdaten und Releasebindung. Bereinige veränderliche Berichte und Exporte gezielt; terminale Plan-/Decision-Historie nicht als Nebenwirkung umschreiben.
Evidence: [Ask-Standalone und Workflow-Hostangaben korrigiert; README-Projektionen durch Builder erzeugt; sechs Buildtests bestanden, Zehn Payloads auf Spezifikationsfelder und Feldlaengen geprueft; quick_validate-Abweichung zu compatibility mit offizieller Quelle dokumentiert, Drei benannte Ergebnisberichte von persoenlichen Maschinenpfaden bereinigt; kanonisches Wissen und terminale Historie erhalten]

### W-013 Ask hat nur noch eine gepflegte Quelle

Status: done
Depends on: []
Blocked by: []
Decisions: []
Outcome: Die freigegebene Restmigration F-10 entfernt ausschließlich die veraltete Ask-Quelle bei erhaltenem Backup.
Acceptance: Backup und seitdem mögliche Änderungen sind abgeglichen. Der exakte alte Quellordner ist entfernt und kein aktiver Leser verwendet ihn. Standalone-/Suite-Builds nutzen nur den konsolidierten Member. Keine Veröffentlichung erfolgt.
Steps:
1. Prüfe den in members/scoville-ask-for-codex/development/test-evidence.md bezeichneten Backupbestand und aktuellen Zustand von ../ask-suite-for-codex. Sichere neue relevante Änderungen vor Entfernung.
2. Prüfe Zielgrenze und aktive Leser, entferne nur den autorisierten Altordner und dokumentiere einen knappen migrationsbezogenen Nachweis. Eine neue Policy-Sperre melden, nicht umgehen.
Evidence: [Nutzer erlaubt ausdruecklich Abschluss von W-013 mit einer Desktop-Batchdatei zur manuellen Loeschung statt automatischer Entfernung, 437 Altquellen- und Backupdateien aktuell bytegleich; Git sauber und HEAD 59d50932b02e024f85a4bf7d68716dbb37d48297 unveraendert, Desktop/Scoville-Altquelle-loeschen.bat erstellt und nur syntaktisch geprueft; Altordner wurde durch den Agenten nicht geloescht]

### W-016 Größenberichte machen den Ladeumfang sichtbar

Status: done
Depends on: []
Blocked by: []
Decisions: [ADR-0045]
Outcome: F-26 ergänzt informative Datei- und Ladeumfangsberichte im vorhandenen Buildreport.
Acceptance: Der Report nennt Größen pro Member und geladener Route. Warnungen blockieren keine korrekte Änderung allein wegen willkürlicher KB-Grenzen. Kein zweiter Runner entsteht.
Steps:
1. Ergänze informative Größen-/Ladeumfangsausgabe im vorhandenen Buildreport; unterscheide komplette Pakete und für typische Handlungen tatsächlich geladene Dateien.
2. Vergleiche eine Berichtsausgabe mit den gemessenen Dateien.
Evidence: [Builder meldet Datei- und Paketbytes sowie beobachtete Referenzrouten; sechs Buildtests bestanden, Reale Kandidatenspur mit aktuellen Dateigroessen verglichen; geaenderte Dateien korrekt als nicht mehr exakt gemessen gekennzeichnet, Anleitung in development/luna-tests/build-evidence.md; keine Groessensperre oder Tokenschaetzung]


### W-018 Bestehende Pläne bleiben im installierten Viewer lesbar

Status: done
Depends on: []
Blocked by: []
Decisions: [ADR-0065]
Outcome: Neue Evidence-Einträge bleiben mit dem vorhandenen Viewer kompatibel; erweiterte Leser behalten Klartext- und CRLF-Unterstützung.
Acceptance: Schreibanleitung verlangt vorerst Legacy-Listen und LF; einzelne Einträge enthalten weder Kommas noch eckige Klammern. Das Testprofil besteht den aktuellen Validator; der Nutzer bestätigt die fehlerfreie Anzeige im installierten alten Viewer mit Versionsangabe. Neue Klartext-/CRLF-Fixtures bleiben im aktuellen Reader gültig. Keine Viewer-Veröffentlichung ist erforderlich.
Steps:
1. Korrigiere die voreilige Klartext-Schreibvorgabe in members/scoville-plan/scoville-plan/references/native-plan-format.md und ihren direkten Schreibreferenzen; erhalte die neue Lesefunktion.
2. Erstelle ein temporäres Testprofil mit mehreren Legacy-Evidence-Einträgen und prüfe es mit dem aktuellen Validator sowie Klartext-/CRLF-Fixtures mit dem aktuellen Reader. Übergib dem Nutzer den absoluten Profilpfad und eine kurze Prüfanleitung: Profil im installierten Viewer öffnen und bestätigen dass Plan und sämtliche Evidence-Einträge ohne Fehlermeldung lesbar sind; Viewer-Version angeben. Der Nutzer führt diese Desktopprüfung aus. Halte seine Rückmeldung als Abnahmenachweis fest; bis dahin bleibt nur diese manuelle Abnahme offen und Parsertests ersetzen sie nicht.
Evidence: [Schreibregel auf Legacy-Listen und LF korrigiert, Windows Python 3.14: 46 Validator- und 21 Selectortests bestanden, Testprofil temp/2026-09-25-plan-0011-fixes/viewer-profile valide; Viewer v1.3.2 Anzeige per Nutzer-Screenshot bestätigt]

### W-019 Workflow startet und übergibt mit eindeutiger Identität

Status: done
Depends on: []
Blocked by: []
Decisions: [ADR-0066, ADR-0064]
Outcome: Aufrufender Manager und Nachfolger erhalten korrekte Rollenzähler und Titel; Übergabeprompts erfüllen den tatsächlich verwendeten Helper-Vertrag.
Acceptance: Erster bestehender Manager wird als #1 registriert und einmal in S-MNGR-#1-PLAN-0011 umbenannt; sein Nachfolger erhält #2. Bei Wiederaufnahme derselben Aufgabe bleiben Nummer und Titel erhalten. Fortsetzung derselben Aufgabe erhöht nichts. WORK/REVW/FIXR zählen getrennt. Ungültige Plan-/Einheiten-IDs werden abgelehnt. Ein echter Selector-Aufruf für die Titelarbeit liefert ADR-0066. Der Koordinator-Übergabeprompt wird vom Lifecycle-Helper akzeptiert. Laufzustand und Handoffs sind ausdrücklich lokal; config.json bleibt versionierbar.
Steps:
1. Richte in members/scoville-workflow-for-codex/scoville-workflow-for-codex/SKILL.md die bestehende aufrufende Aufgabe ausdrücklich als Manager Nummer 1 ein; begrenze das Umbenennungsverbot in ../shared/runtime/task_lifecycle.md auf fremde oder durch Reconciliation gefundene Aufgaben. Speichere Nummer und Task-ID im bestehenden Laufdatensatz. Ergänze in task_lifecycle.py nur die notwendige ID-Formatprüfung.
2. Prüfe mit dem echten Selector dass W-019 und der Abnahmenachfolger W-026 ADR-0066 liefern. Dispatch erfolgt nur aus diesen aktuellen Aufträgen; W-010 wird nicht erneut dispatcht und seine gestarteten Decisions/Steps/Acceptance werden nicht geändert.
3. Ergänze in references/operations-rollover.md den Pflichtkopf scoville_role=coordinator ab Byte 0 und den ausdrücklichen Skillaufruf mit Pfad. Beschreibe in references/operations.md lokalen Laufzustand und gezieltes Aufräumen erst nach Ergebnissicherung und abgeschlossener Übergabe; keine neue Setup-Funktion.
Evidence: [Windows Python 3.14: 20 Titel- und Lifecycletests grün, Echte Selector-Aufrufe für W-019 und W-026 liefern ADR-0066, Koordinator-Prompt durch Lifecycle akzeptiert; Host-Titelwechsel bestätigt, Details docs/suite-review-pruefung-2026-09-25.md]

### W-020 Reasoning-Stufen gelten einheitlich für Plan und Ausführung

Status: done
Depends on: [W-018]
Blocked by: []
Decisions: []
Outcome: Plan-Annotation, Setup, Ask und Workflow verwenden denselben Wortschatz für Reasoning; gültige Werte scheitern nicht an widersprüchlichen lokalen Listen.
Acceptance: none/minimal/low/medium/high/xhigh/max/ultra werden syntaktisch einheitlich verarbeitet. Die tatsächliche Modellunterstützung entscheidet über Ausführbarkeit; nicht unterstützte Paare werden verständlich abgelehnt und niemals still umgeschrieben. Tests führen eine Plan-Annotation über Selector und Dispatch bis zur Modellprüfung und prüfen Setup-Overrides.
Steps:
1. Gleiche members/scoville-plan/scoville-plan/scripts/select_context.py und validate_profile.py sowie members/scoville-workflow-for-codex/scoville-workflow-for-codex/scripts/workflow_settings.py und resolve_model_pair.py mit Ask- und Setup-Verbrauchern ab.
2. Vereinheitliche die zulässigen Werte in deren bestehendem Konfigurations-/Validierungsweg und den zugehörigen Referenzen. Bewahre eigenständig installierbare Pakete; keine neue Laufzeitabhängigkeit zwischen Skills.
Evidence: [Windows Python 3.14: 15 Workflowtests und 2 Setuptests grün, Ask-Modellprüfung für alle acht Werte bestanden, Nutzerpräzisierung ADR-0067 umgesetzt; Plan-README erklärt Annotationen und reguläre Auswahl]

### W-021 Ask verwendet keinerlei Legacy-Konfiguration mehr

Status: done
Depends on: []
Blocked by: []
Decisions: []
Outcome: Nur .scoville/config.json vor importierten Defaults bleibt als gespeicherte Konfiguration erhalten; Legacy-Dateien und ihre aktive Dokumentation entfallen gemäß Nutzerkorrektur.
Acceptance: Keine Legacy-Erkennung, Warnung, Ladeebene oder automatische Migration bleibt aktiv. Exakt zugeordnete alte Konfigurationsdateien sind entfernt; aktuelle Projektkonfiguration und Defaults bleiben erhalten. Ohne Projektdatei gelten Defaults und Lesen erzeugt nichts. Historische Nachweise bleiben wahrheitsgemäß erhalten.
Steps:
1. Ermittle ausschließlich die alten persönlichen Ask-Konfigurationsdateien und ihre aktiven Verweise über members/scoville-ask-for-codex/scoville-ask-for-codex/references/configuration.md und scripts/ask.py. Prüfe Zielpfade und Inhalt vor Entfernung. Berichte dem Nutzer vor dem Löschen die exakten Pfade und vom Default abweichende nicht geheime Werte einschließlich des bekannten 50-USD-Budgets; keine Zugangsdaten ausgeben. Bestehende Policy-Sperren nicht umgehen.
2. Entferne die bestätigten Legacy-Dateien und aktive Erhaltungs-/Migrationsanweisungen. Übernimm alte Werte wie das 50-USD-Budget nicht ungefragt in .scoville/config.json und baue keinen Warnmechanismus ein.
Evidence: [Altdatei C:/Users/benja/.codex/skills/ask-claude-for-codex/config.json nach Wertbericht entfernt; Abwesenheit geprüft, Windows Python 3.14: Default-/Override-Test bestanden; Lesen erzeugt keine Datei]

### W-022 Tests und Laufzeitaufrufe funktionieren ohne lokale Sonderumgebung

Status: done
Depends on: [W-019, W-020, W-021]
Blocked by: []
Decisions: [ADR-0067]
Outcome: Die betroffenen Tests sind isoliert und portabel; Laufzeitanweisungen wählen einen geeigneten Python-Interpreter.
Acceptance: Shared-, Suite-, Plan-, Ask-, Workflow- und Setup-Tests bestehen grün ohne unbeabsichtigten Modell-/App-Server-Aufruf; für jeden Lauf werden Plattform und Python-Version angegeben. Unix-Pfade benötigen kein USERPROFILE. CI enthält die betroffenen Tests. Lokale Ergebnisse und ungestartete GitHub-Matrix bleiben getrennt ausgewiesen; W-002 bleibt ohne reale CI-Beobachtung offen. Originales mehrzeiliges Ergebnis wird akzeptiert und verdichteter Snapshot nicht als Original verwendet.
Steps:
1. Aktualisiere belegbar veraltete Erwartungen in ../shared/tests/test_description_contract.py, test_readme_templates.py und test_distribution_profiles.py. Isoliere den Webtools-Test in members/scoville-ask-for-codex/development/tests/test_ask_behavior.py mit festem Katalog und beseitige doppelte Override-Schlüssel.
2. Korrigiere die Home-Verwendung in development/luna-tests/run_codex_cli_case.py und ergänze .github/workflows/python-portability.yml um Shared-, Suite- und Setup-Abdeckung ohne Push oder CI-Start.
3. Verankere die Interpreterwahl in den tatsächlich geladenen Ask-/Workflow-/Setup-Laufzeitreferenzen. Verlange Python 3.11 nur bei Verbrauchern die es brauchen; Plan bleibt ohne Python nutzbar und seine optionalen Helfer behalten belegte Unterstützung.
4. Ergänze gezielte Regressionen für Originalresultat statt Snapshot und den gültigen Koordinator-Übergabeprompt. Prüfe die Rückgaberegel aller drei Arbeitsrollen; Textprüfungen ersetzen nicht den späteren nativen Ablauf unter W-026.
Evidence: [Windows 3.14 und Ubuntu 3.12.3: Shared 53 Suite 24 Plan 68 Ask 22 Workflow 16 Setup 2 grün; Ubuntu 1 Windows-Test ausgelassen, Details docs/suite-review-pruefung-2026-09-25.md]

### W-023 Aktive Dokumentation und Quellbestand beschreiben nur den gültigen Betrieb

Status: done
Depends on: [W-021]
Blocked by: []
Decisions: []
Outcome: README, Unreleased-Einträge und aktive Planreferenzen widersprechen weder Distribution noch aktuellem Verhalten; ungenutzte Helfer entfallen.
Acceptance: Workflow ist klar als suite-only beschrieben. Links zeigen auf belegte Distributionsziele. Unreleased beschreibt den Umbau ohne historische Releaseeinträge umzuschreiben. Nur nachweislich ungenutzte Helfer und ihre obsoleten Tests werden entfernt; keine aktive Funktion geht verloren. Viewer wird nicht fälschlich als Verbraucher von Decision-Batch-IDs bezeichnet.
Steps:
1. Korrigiere M7/L2 in development/readme/scoville-workflow-codex/, development/readme/scoville-ask-for-codex/ und den Plan-/Workflow-CHANGELOGs. Erzeuge README-Projektionen über den Builder und erhalte Änderungen der separaten Release-Session.
2. Prüfe die in L1 genannten compute_decision_batch.py- und resolve_prompt_profile.py-Kopien samt Tests gegen suite.json und tatsächliche Aufrufer. Entferne nur tote Pfade; korrigiere L6 in members/scoville-plan/scoville-plan/references/native-decision-batches.md.
Evidence: [Aktuelle READMEs und Unreleased korrigiert; 4 ungenutzte Helper-/Testdateien entfernt; historische Releases erhalten, Details docs/suite-review-pruefung-2026-09-25.md]

### W-024 Installierbare Pakete entsprechen den Quellen und verwenden LF

Status: done
Depends on: [W-018, W-019, W-020, W-021, W-022, W-023]
Blocked by: []
Decisions: [ADR-0067]
Outcome: Die vorgesehenen Paketkopien enthalten die korrigierten Quellen ohne obsolete Workflowdateien und mit einheitlichen Textzeilenenden.
Acceptance: Alle erzeugten Textdateien sind LF-normalisiert unabhängig von CRLF im Arbeitsbaum; Binärdateien bleiben bytegleich. README-, Fragment- und Shared-Helper-Ausgaben sind einbezogen. Installierbare Kopien stimmen mit dem aktuellen Manifest/Payload überein. Der Workflow enthält beide letzten Ergebnis-/Checkpointkorrekturen und die Titelkorrekturen. Keine Installation oder Veröffentlichung findet statt.
Steps:
1. Prüfe ../shared/build/build_suite.py: package_bytes normalisiert bereits CRLF. Sichere alle weiteren Textausgabewege einschließlich README und Fragmentexpansion mit einem gezielten Buildtest ab; ergänze nur fehlende Normalisierung.
2. Synchronisiere kanonische Shared-Quellen und erzeuge Pakete mit development/build_suite.py im vorgeschriebenen Release-Temporärverzeichnis. Gleiche anschließend packages/ mit dem vorgesehenen Build ab und entferne nur obsolete generierte Dateien nach Prüfung der Zielgrenze.
3. Prüfe die tatsächlichen Ausgabebytes und Paketinventare; erhalte den CRLF-Lesevertrag vorhandener Planrecords. Stelle den geprüften Paketstand für den anschließenden nativen W-026-Lauf bereit.
Evidence: [Beide Distributionsprofile gebaut; 7 Paketkopien und 113 Dateien entsprechen Payload, Alle erzeugten Textbytes LF; Binärvertrag geprüft, Aktueller Workflow enthält Ergebnis-/Checkpoint-/Titelkorrekturen]

### W-026 Workflow erfüllt die aktuelle native Abnahme

Status: done
Depends on: [W-024]
Blocked by: []
Decisions: [ADR-0045, ADR-0064, ADR-0052, ADR-0061, ADR-0066, ADR-0067]
Outcome: Der vereinfachte Workflow führt Planeinheiten mit Review und begrenzter Reparatur aus und übergibt unvollständige Arbeit bei Context-Rollover zuverlässig an Nachfolgeaufgaben.
Acceptance: Ein begrenzter nativer Mehr-Einheiten-Lauf belegt Originaltextübernahme aus read_thread mit erhaltenen Zeilenumbrüchen sowie keinen weiteren Worker-Checkpoint nach abgeschlossener eigener Arbeit. Review-/Reparaturschleife und Reparaturgrenze sowie Stopp/Wiederaufnahme sind beobachtet. Automatischer Manager- und Worker-Rollover übergibt Auftrag und Restarbeit an tatsächlich gestartete Nachfolger ohne gleichzeitiges Weiterschreiben; Speicherung oder Kompaktierung allein genügt nicht. Defaults ab 25 Prozent für Manager und über 75 Prozent für Arbeitsrollen sowie Overrides und fehlende/veraltete Telemetrie bleiben geprüft. Titel folgen ADR-0066 mit getrennten Rollenzählern und der in W-019 festgelegten Erstregistrierung; Fortsetzung derselben Aufgabe erhöht nichts. Ergebnisse und Task-IDs werden vor Archivierung gesichert; Vorgänger erst nach Ende und gestartetem Nachfolger archiviert. Archivierungsfehler werden gemeldet und offene Nutzerentscheidungen bleiben sichtbar. Jede Zeile der zwölfteiligen ADR-0064-Umfangstabelle ist mit Quellstelle oder entfallenem Pfad und passendem Nachweis abgeglichen. Unnötige Übergabe-Hashes und Modellkonfigurations-Snapshots bleiben entfernt; reale Diffs bestimmen die Review und Commitautorität wird nicht erweitert. Keine allgemeine Kosten- oder Geschwindigkeitsersparnis ohne entsprechenden Beleg.
Steps:
1. Gleiche den unter docs/suite-review-pruefung-2026-09-25.md dokumentierten Fixturestand mit dem nach W-024 gebauten Paket ab. Übernimm weiterhin gültige W-010-Nachweise mit genauer Standangabe und führe abgeschlossene Arbeit nicht blind erneut aus.
2. Setze den unterbrochenen nativen Ablauf mit Originaltextübernahme fort und prüfe die noch unbeobachteten Review-/Reparatur-, Rollover- und Stopp-/Wiederaufnahmefälle. Verwende das bestehende Fixture und die vorhandenen Werkzeuge statt eines neuen Runners.
3. Sichere knappe Ergebnisse und Task-IDs im vorhandenen Prüfbericht, prüfe die erforderliche Archivierung und gleiche die ADR-0064-Umfangstabelle sowie aktuelle Titel gegen tatsächliches Verhalten ab. Benenne offene Grenzen statt sie mit Helpertests als bestanden auszugeben.
Evidence: [SOL 6 Medium: Originalresultate und reale Manager-/Worker-Rollover bestanden, Nativer Stopp und Wiederaufnahme derselben Aufgabe ohne doppelte Effekte bestanden, Drei Reparaturen mit kontrollierter Fehlerrückkehr; keine vierte; Entscheidungsstopp beobachtet, Archivierung und zwölf ADR-0064-Bereiche geprüft; Details im Prüfbericht]

### W-025 Plan lädt für gewöhnliche Änderungen weniger Regeln

Status: done
Depends on: [W-024, W-026]
Blocked by: []
Decisions: [ADR-0045, ADR-0048]
Outcome: Gewöhnliche Planänderungen benötigen weniger wiederholte Regeln bei erhaltener direkter Bearbeitung und zuverlässiger Fortsetzung.
Acceptance: Vorher/nachher-Vergleich benennt tatsächlich geladene Dateien für Einfügen, Fortschreiben, Abschluss und Wiederaufnahme. Redundante Regeln sind entfernt oder nur bei Bedarf geladen. Dieselben konkreten Fälle bestehen Validator und Selector; Entscheidungen, Historie und offene Arbeit bleiben erhalten. Kein bloßes Verschieben von Text oder unbelegtes Versprechen zu Tokens, Kosten und Laufzeit.
Steps:
1. Prüfe M5 in members/scoville-plan/scoville-plan/SKILL.md und references/native-work-items.md auf doppelte und selten benötigte Regeln; berücksichtige die bereits gekürzte native-editing.md.
2. Kürze die häufigen Routen und synchronisiere betroffene Referenzen ohne neue Profile, Hashpflichten oder Planverwaltungsschicht. Prüfe die genannten Fälle und aktualisiere anschließend die betroffenen Pakete über den vorhandenen Buildweg.
Evidence: [Vier Standardleserouten enthalten 15.8 bis 18.4 Prozent weniger Quelltext; tatsächliche Lesewege separat gemessen, Zwei SOL-6-Medium-Läufe bestanden fünf Zwischenstände; ADR und gestartete Inhalte erhalten, Windows Python 3.14: Plan 68 und Suite 24 grün; beide Profile gebaut; Plan-Paket synchronisiert, Umfang und Messgrenzen stehen im Prüfbericht]
