---
format_version: 1
id: PLAN-0002
status: draft
created: 2026-09-24
updated: 2026-09-25
---

# Zwei Scoville Suites mit Schreibprofilen und Scoville Ask

## Goal

Eine gemeinsame Entwicklungsgrundlage erzeugt eine allgemeine Scoville Suite und eine Codex-Suite. Planpunkte und zusätzliche Workflow-Anweisungen verwenden einfache Schreibprofile bei vollständigem Kontext. Scoville Ask ersetzt die bisherigen Ask-Varianten als Codex-Suite-Mitglied und zusätzlich einzeln installierbares Codex-Paket gemäß ADR-0042. Beide Ausgaben erhalten knappe, zutreffende Nutzungs- und Konfigurationshinweise.

**Verbindliche Reihenfolge**

1. Zuerst gemeinsame Schreibgrundlage, Plan und Workflow korrigieren.
2. Danach beide Suite-Ausgaben, Python-Fallback-Trennung und alle aktuellen How-to-use-Abschnitte fertigstellen. Suite-Pakete setzen sämtliche enthaltenen Skills als installiert und aktiviert voraus; nur Standalone-Pakete enthalten Familienblöcke und optionale Geschwister-Behandlung. Diese Ergänzung wird vor den nächsten Tests umgesetzt. Vor vollständiger Prüfung erfolgt kein Release.
3. Erst wenn sämtliche Punkte vor Ask abgearbeitet und die abschließenden Reviews bestanden sind, Plan-/Workflow-Korrekturen und die Codex-Suite veröffentlichen sowie die GitHub-Profilseite aktualisieren. Die allgemeine Ausgabe bleibt Bestandteil der Build-/Exportprüfung.
4. Der Auftrag vom 2026-09-25 erlaubt den unabhängigen Ask-Umbau und SOL-6-Medium-Tests parallel zum UI-Update gemäß ADR-0043. Gemeinsame Dateien werden gegen parallele Änderungen abgeglichen; laufende UI-Arbeit und deren Veröffentlichung bleiben eigenständig.

Die neue read-only Astra-High-Session `01a0d295-31c2-7bd0-9e98-8e1af4f3ddcc` hat die konkrete Umsetzung geprüft; relevante Befunde werden korrigiert und lokal nachgeprüft. Der aktuelle Auftrag verlangt vor W-010 ein Astra-Gesamtreview des finalen Nicht-Ask-Stands einschließlich PLAN-0006 in derselben gültigen Session. Der frühere Reviewverzicht bleibt in W-009 als Historie erhalten. Die frühere Session ist geschlossen und wird nicht wiederverwendet. Ein vorbereiteter Build oder bestandenes Teilreview autorisiert keinen vorgezogenen Release. Ausgenommen ist ausschließlich der Ask-Umbau (W-001/W-002): Er ist gemäß ADR-0043 unabhängig beauftragt und blockiert diese nicht; Ask bleibt read-only.

## Non-goals

- Keine Veröffentlichung, lokale Installation, Aktivierung dieses Entwurfs oder Änderung alter GitHub-Repositories allein durch die Planpflege.
- Keine stillschweigende Modellsubstitution oder manuellen Ersatzwege für erforderliche Python-Helper der Codex-Ausgabe.
- Keine automatische Senkung von Aufgabenrisiko oder Modellanforderungen durch ein Schreibprofil und keine Änderung der laufenden DIVI5-Koordination.
- Keine Änderung von Planpunkten durch den Dispatcher und keine zusätzliche Dispatch-Einheit allein wegen ausführlicherer Anleitung.
- Keine gemeinsam wirksamen Plan-/Workflow-Einstellungen und keine Laufzeitimporte aus Geschwister-Skills oder Entwicklungsverzeichnissen.

## Work items

### W-005 Stufe 1: Gemeinsame Schreibregeln mit einfacher Tier-Auflösung

Status: done
Depends on: []
Blocked by: []
Decisions: [ADR-0014]
Outcome: Ein zentral gepflegter Helper und dieselben drei kurzen Schreibprofile steuern Planschreiben und zusätzliche Kommunikation in Workflow bei unabhängig konfigurierten Einstellungen. Es gibt keinen gesonderten Kommunikations-Helper und keine zweite Sammlung gleichartiger Schreibregeln.
Acceptance: Die einzige reguläre Einstellung ist `profile = auto|low|medium|high`; voreingestellt ist `auto` mit Rückfall `medium`. Eine explizite Profilvorgabe im Auftrag gewinnt, danach die feste Skill-Einstellung. Bei `auto` wird ein bekanntes Zielmodell über die lokale Modellliste aufgelöst; unbekannte Modell-IDs ergeben `medium`. Nur Plan nutzt ohne Zielmodell die bereits für den Arbeitspunkt ermittelte Aufgabenklasse: `ultra_low` und `low` ergeben `low`, `medium` ergibt `medium`, `high` und `ultra_high` ergeben `high`; ohne Klasse gilt `medium`. Dafür entsteht keine zweite Bewertungsskala oder konfigurierbare Klassenmatrix. Workflow nutzt bei `auto` das tatsächliche Empfängermodell. Es gibt keine Modellabfrage, unscharfe Namenserkennung oder zusätzliche Reasoning-Heuristik. Konfigurationsfehler werden diagnostiziert.
Steps:
1. Lege `../shared/prompting/common.md`, `low.md`, `medium.md`, `high.md` und `models.toml` sowie `../shared/runtime/resolve_prompt_profile.py` als kanonische Quellen an. Halte `medium` als Standard und nur die abweichenden Modell-IDs in der Liste: `gpt-6-luna` und `gemini-3.8-flash-high` für `low`; `gpt-6-astra`, `claude-fable-5-1` und `claude-opus-5-5` für `high`. Dokumentiere die Liste als konfigurierbare Startzuordnung.
2. Ergänze nur die notwendige Buildgrundlage: erweitere den vorhandenen Source-Resolver um deklarierte `shared:`-Dateiquellen, bilde `shared_helpers` darauf ab und erfasse Prompting-Quellen im Snapshot samt Wrappern und Quellenhashes. Prüfe den isolierten Paketbuild ohne den späteren Zwei-Profil-Umbau vorauszusetzen. Erzeuge Regeln unter `references/prompting/` und den Helper unter `scripts/` beider Pakete. Erzeuge die unabhängig bearbeitbare Plan-Konfiguration unter `scoville-plan/assets/prompting.toml` und integriere Workflows eigene `[prompting]`-Einstellungen in `scoville-workflow-for-codex/assets/workflow.toml`. Baue die gemeinsame Standard-Modellliste in beide Einstellungen ein; spätere lokale Änderungen wirken nur im jeweiligen Skill. Lege keine globale Konfiguration oder Laufzeitabhängigkeit zwischen den Skills an.
3. Lies in ADR-0014 den Abschnitt Gemeinsame Schreibregeln und übernimm diese Regeln und Profildifferenzen aus den beiden Originalquellen ohne zusätzliche Skillhilfe. `common.md` besitzt alle invarianten Schreibregeln; Profile beschreiben nur die Anleitungstiefe. `../shared/instruction-writing.md` verweist auf diesen Besitzer. Rollen, Risiko, Ergebnisformate und Guards bleiben in ihren bisherigen Verträgen. `models.toml` ist reine Buildquelle; pro Skill gibt es genau eine Runtime-Konfiguration, ohne Rollenmatrix, Umgebungsvariable oder zusätzliche Override-Datei.
4. Prüfe die Auswahlreihenfolge samt explizitem Geltungsumfang und getrennten Einstellungen. Ein unbekanntes vorhandenes Zielmodell ergibt immer `medium`, auch bei hoher Aufgabenklasse. Plan liefert nur ohne Modell die vorhandene Klasse, Workflow das tatsächliche Empfängermodell. Nenne die Python-Mindestversion des Parsers (`tomllib`: 3.11). Der bestehende portable Plan-Paketweg bündelt einen nur bei fehlendem Python geladenen Auswahlersatz; zu altes Python und Helperfehler lösen ihn nicht aus. Workflow nutzt ausschließlich den Helper. Erst W-004 ordnet diese Dateien und Texte general/codex zu.
Evidence: [Shared-Tests r3: 42 bestanden; Auswahlreihenfolge und unabhängige Konfigurationen geprüft, Astra-Review -04 ohne weitere Befunde im geprüften Umfang, Nachweise gelten vor dem Zwei-Profil-Umbau; dessen Abschlussprüfung bleibt W-009]

### W-006 Stufe 2: Plan schreibt jeden Arbeitspunkt passend zum Empfänger

Status: done
Depends on: [W-005]
Blocked by: []
Decisions: [ADR-0014]
Outcome: Plan formuliert unterschiedliche Arbeitspunkte mit passender Anleitungstiefe, ohne verborgenen Kontext oder neue Dispatch-Grenzen.
Acceptance: Explizite Profilangaben wirken nur im genannten Umfang. Sonst bestimmt Plan pro Punkt aus Zielmodell oder vorhandener Aufgabenbewertung das Profil gemäß W-005. Ein Plan kann mehrere Profile enthalten. Alle Profile bewahren Ziel, Umfang, Voraussetzungen, Entscheidungen, Berechtigungen und Abnahmekriterien. Quellen müssen direkt bereitstehen oder eindeutig mit Leseauftrag referenziert sein. Das Autorenmodell ist kein Auswahlgrund. Bestehende Planformate bleiben lesbar; keine neue Pflichtannotation entsteht. Die Aufgabenbewertung beeinflusst das Schreiben, senkt aber keine Workflow-Route. Begonnene Planhistorie bleibt unverändert.
Steps:
1. Passe `members/scoville-plan/scoville-plan/SKILL.md` und die betroffenen Referenzen zu Granularität, Format und Work Items an. Vereinbare die bisher pauschalen Luna-/Lower-Reasoning-Vorgaben in den Projektanweisungen und `../shared/instruction-writing.md` mit den bewusst gewählten Schreibprofilen, ohne Kontextvollständigkeit zu schwächen.
2. Korrigiere die bereits im Arbeitsbaum angepasste `references/read-only.md` endgültig: die manuelle Auswahl steht ausschließlich in der nur ohne Python geladenen Referenz. Ändere die Decision-Lektüre bewusst: IDs und Status vorgeschlagener Entscheidungen bleiben auffindbar; Inhalte und Empfehlungen werden bei Betroffenheit oder Gesamtaudit gelesen und berichtet. Abhängige offene Entscheidungen blockieren weiterhin nur betroffene Arbeiten. Ordne zusätzliche Erläuterungen dem bestehenden Verhaltenseinheitsprinzip unter, damit Low nicht mehr Worker erzeugt.
3. Prüfe einen gemischten Plan und explizite Low-Vorgaben auf erhaltene Anforderungen, klare Reihenfolge, konkrete Prüfung und unveränderte Anzahl fachlich begründeter Arbeitseinheiten. Lade beim Schreiben nur die gemeinsamen Regeln und das benötigte Profil.
Evidence: [Plan-Tests r2: 75 bestanden, Fünf ausgewählte Luna-Fälle r3 protokollseitig und inhaltlich geprüft; Plan-Paket r4 bytegleich, Python fehlt oder ist zu alt sowie Helperfehler korrekt unterschieden, Astra-Review -04 ohne weitere Befunde im geprüften Umfang]

### W-007 Stufe 3: Workflow übergibt Planpunkte unverändert

Status: done
Depends on: [W-005]
Blocked by: []
Decisions: [ADR-0014]
Outcome: Workflow ergänzt passende Empfängeranweisungen, während jeder ausgewählte kanonische Planpunkt vollständig und unverändert übergeben wird.
Acceptance: Nach der Auswahl des tatsächlichen Modells wird nur der Zusatztext für Executor, Reviewer, Reparatur-Worker oder Nachfolgekoordinator profiliert. Ein aus der Übergabe extrahierter Planpunkt stimmt exakt mit dem kanonischen Text überein, unabhängig vom Profil und Modellwechsel. Der Koordinator editiert keine vom Helper gebundenen Payloads nachträglich. Benötigter zusätzlicher Kontext steht getrennt und widerspruchsfrei bereit. Hash-/Guard-Bindungen, Rollen, Berechtigungen und die bisherigen expliziten Workflow-Aktivierungsregeln bleiben gültig. Plan und Workflow funktionieren aus vollständig erzeugten, isolierten Paketen ohne Helperimporte aus installierten Geschwistern.
Steps:
1. Definiere den kanonischen Planpunkt als ausgewählten Step-Quelltext bzw. zusammenhängenden Step-Bereich oder vollständigen Work-Item-Block ohne Steps. Ergänze einen Quelltextwert im bestehenden Kontextobjekt von Plans `scripts/select_context.py`; gleiche `references/read-only.md` und Workflows Promptvalidierung ab. Definiere Ausschnittgrenzen für bestehende einzeilige Steps, zusammenhängende Step-Bereiche und vollständige Work-Item-Blöcke sowie UTF-8/LF-Normalisierung. Übertrage den Ausschnitt danach unverändert; liefere erforderlichen Eltern- und Entscheidungskontext separat. Passe den bisherigen Evidence-Ausschluss für vollständige Items ausdrücklich an.
2. Ergänze Workflows `scripts/build_dispatch_prompt.py` um getrennten `supplemental_context`. Referenzen müssen für den Empfänger lesbar sein; notwendige Inhalte gesperrter Plan-/Decision-Quellen werden direkt geliefert. Stelle Profilzusätze vor der bestehenden Digest-/Guard-Bindung zusammen und binde den aufgelösten Regeltext samt wirksamen Eingaben mit. Ergänze Koordinatorübergaben in `references/operations-rollover.md` am vorhandenen Besitzer mit denselben Schreibregeln; keine neue Workerrolle oder zweiter Helper.
3. Prüfe Executor-, Reviewer-, Reparatur- und Koordinatorübergaben mit unterschiedlichen Empfängerprofilen, fehlender Gesprächshistorie und Modellwechsel. Vergleiche den dekodierten Punkttext mit dem definierten Quellausschnitt und prüfe, dass geänderte wirksame Profilregeln eine andere Bindung erzeugen. Führe doppelte Workflow-Routingregeln an einem vorhandenen Besitzer zusammen; Guard, Lifecycle und Selector behalten ihre unterschiedlichen Aufgaben.
Evidence: [Workflow-Tests r4: 73 bestanden; source_text und Zusatzkontext sowie Digest-Bindung geprüft, Fünf ausgewählte Luna-Fälle r4 protokollseitig bestanden; Abschlussantworten am 2026-09-24 inhaltlich geprüft, Aktivierung und Routing sowie Worker-/Koordinatorübergabe korrekt; Referenzpfad-Präzisierung durch Luna r4 geprüft, Astra-Review -04 ohne weitere Befunde im geprüften Umfang]

### W-003 Stufe 4: Zwei reproduzierbare Suite-Buildprofile

Status: done
Depends on: [W-006, W-007]
Blocked by: []
Decisions: [ADR-0013]
Outcome: Derselbe Quellenstand erzeugt getrennte allgemeine und Codex-spezifische Suite-Ausgaben mit expliziter Mitgliedschaft und Dateiauswahl.
Acceptance: Der Builder und Suite-Exporter wählen über `general` oder `codex` konsistent Namen, Mitglieder, Dateien, Includes, README- und Familienprojektionen sowie Exportquellen aus. Unbekannte Profile und Includes scheitern. Buildnachweise enthalten Profil und Quellenhashes. Zwei Builds desselben Profils sind identisch. Sichtbarkeitsgates bleiben erhalten; der Export kopiert keine ausgeschlossenen Mitglieder nur deshalb, weil sie versioniert sind. Quellkopien werden nicht unabhängig gepflegt.
Steps:
1. Erweitere `../shared/build/build_suite.py`, `export_suite.py`, `sync_suite_sources.py`, ihre Wrapper und `fragments.md`. Ein `suite.json` und eine aufgelöste Manifestansicht pro Profil steuern Paket, Includes, README, Snapshot, Verifikation und Exportmanifest. Nutze zwei einfache Profilobjekte und Auswahlfelder; keine Manifestvererbung oder Ausdruckssprache. Berücksichtige `featured_member` und optionale Familiennachbarn, wenn Workflow in `general` fehlt.
2. Verwende die in W-005 ergänzten gemeinsamen Dateiquellen und Snapshot-Verträge auch für die effektive Profilansicht; führe keine zweite Dateiliste ein. Erzeuge getrennte Profil-Ausgaben ohne gegenseitiges Überschreiben der README-Vorschauen. Prüfe identische Builds und den erneuten isolierten Build beider exportierter Quellen mit ihren effektiven Manifesten. Synchronisiere die erzeugten Werkzeugkopien; Sichtbarkeitsgates gelten auch für exportierte Quellen.
Evidence: [45 Shared-Tests bestanden (shared-profiles-r3); beide Profile reproduzierbar gebaut, Beide exportierten Quellbäume isoliert bytegleich nachgebaut; ausgeschlossene Mitglieder und alte packages ersetzt, Profil in Manifest und Receipts; Sichtbarkeits- und Fehlerprüfungen erhalten]

### W-004 Stufe 5: Python-Fallbacks nur in der allgemeinen Ausgabe

Status: done
Depends on: [W-003]
Blocked by: []
Decisions: [ADR-0013]
Outcome: Allgemeine Skills laden Python-Ersatzwege ausschließlich bei fehlendem Python; Codex-Pakete enthalten ausschließlich die erforderlichen Helper-Verfahren.
Acceptance: Alle Mitglieds-Skills sind auf Python-Ersatzrouten geprüft. Die drei Plan-Referenzen sind nur in `general` enthalten und werden dort nur für die passende Operation ohne Python geladen. Ein fehlender oder fehlerhafter Helper bei vorhandenem Python führt nie zum manuellen Ersatz. Codex enthält keine entsprechenden Dateien, Anweisungen oder optionalen Python-Voraussetzungen. Notwendige Fehlerdiagnosen und fachliche Fallbacks, etwa Darstellung oder Schriftwahl, bleiben erhalten. Der Standard `medium` für unbekannte Modelle ist kein zu entfernender Python-Fallback.
Steps:
1. Bewahre die in W-006 bereits implementierte Trennung in `members/scoville-plan/scoville-plan/references/read-only.md` und prüfe ihre Semantik gegen `select-context-without-python.md`. Erfasse die übrigen Python-Routen in Plan sowie die Pflichthelper in Workflow.
2. Lege vollständige profilabhängige Anweisungsbausteine und Manifest-Dateifilter an. Ersetze reine Fallback-Blöcke in `codex` durch leeren Text, aber vollständige Verzweigungen durch eine gültige Helper-Anweisung. Prüfe beide Paketsätze auf vorhandenes/fehlendes Python und Helperfehler, ohne Fehler in Erfolg umzudeuten.
Evidence: [Alle Skill-Python-Routen inventarisiert; sechs No-Python-Referenzen nur general zugeordnet, General lädt Ersatzrouten nur bei fehlendem Python; Codex-Pakete ohne entsprechende Dateien oder Verweise gebaut, Pflichthelper und Fehlerdiagnosen in Codex erhalten; fachliche Fallbacks unverändert, Paketgrenzen und eigenständige Abhängigkeiten durch Shared-Tests geprüft; finale Modellprüfungen folgen in W-009]

### W-008 Stufe 6: Alle How-to-use-Abschnitte kürzen und Konfiguration erklären

Status: done
Depends on: [W-004]
Blocked by: []
Decisions: [ADR-0013, ADR-0014]
Outcome: Alle aktuellen Skill-Mitglieder erhalten kurze, tatsächlich gültige Aufrufbeispiele und Plan sowie Workflow erklären ihre getrennten Einstellungen.
Acceptance: Jeder aktuelle Skill beider erzeugten Suites hat genau zwei Beispiele: eines mit und eines ohne Skillnamen, jeweils passend zu seinen Aktivierungsregeln. Workflow hat als ausdrückliche Ausnahme genau ein benanntes Beispiel und erklärt, dass allgemeine Planungs- oder Umsetzungsaufträge ihn nicht starten. Andere ausschließlich explizite Aufrufe dürfen durch ein Beispiel nicht stillschweigend erweitert werden; verbleibende Konflikte werden vor einer behaupteten Gültigkeit geklärt. Plan und Workflow erklären zusätzlich Konfigurationspfad, `auto`, feste Profile, Vorrang expliziter Vorgaben, Standard `medium` und lokal bearbeitbare Modellzuordnungen. Beschreibungen stimmen mit den tatsächlich gebauten Profilen überein.
Steps:
1. Inventarisiere die How-to-use-Quellen anhand der aktuellen Mitgliedschaft in `suite.json`. Der spätere neue Ask wird in W-002 nach denselben Regeln dokumentiert und hält diesen Release nicht auf. Kürze die kanonischen Nutzungsfragmente, darunter `development/readme/*/usage.md`, statt erzeugte READMEs separat zu pflegen.
2. Ergänze Plan-/Workflow-Konfiguration und die Workflow-Ausnahme; generiere beide Dokumentationsausgaben und prüfe Beispielzahl, tatsächliche Trigger, Links und profilgerechte Voraussetzungen.
Evidence: [Alle zehn aktuellen Nutzungsfragmente geprüft; neun Skills mit benanntem und unbenanntem gültigem Beispiel, Workflow mit einem ausdrücklich benannten Aufruf; allgemeine Aufträge aktivieren ihn weiterhin nicht, Plan und Workflow erklären getrennte Konfiguration sowie auto und lokale Modellzuordnung, Beide Paketprofile prüfen Beispielzahlen und Codex-Installationsziel in den 45 bestandenen Shared-Tests]

### W-012 Ergänzung vor Abschlussprüfung: Suite-Installation setzt alle Mitglieder voraus

Status: done
Depends on: [W-003, W-004, W-008]
Blocked by: []
Decisions: [ADR-0013]
Outcome: Einzeln installierbare Pakete bleiben unabhängig; beide vollständigen Suite-Ausgaben setzen sämtliche enthaltenen Skills als installiert und aktiviert voraus.
Acceptance: Nur Standalone-Pakete enthalten den Familienblock und Verfügbarkeitsbedingungen für optionale Geschwister-Skills. Suite-Pakete enthalten diese Blöcke und Prüfungen nicht. Suite-READMEs und die knappe gemeinsame Runtime-Anweisung nennen die vollständige Installation und Aktivierung als Voraussetzung; Teilinstallation ist kein unterstützter Suite-Modus. Jedes Mitglied liegt vollständig im Suite-Repository unter packages; die Installation verwendet ausschließlich diese Pakete und lädt niemals Einzelrepositories nach. Fehlende oder inkompatible Mitglieder ergeben einen konkreten Fehler. Fachliche Zuständigkeiten, bedarfsabhängiges Laden von Anweisungen, explizite Aktivierung von Workflow und Nutzer-Ausschlüsse bleiben erhalten. Das gewählte Profil bestimmt die enthaltenen Mitglieder; general setzt weder Workflow noch Ask voraus. Bestehende dynamische Familienprojektionen und gemeinsame Textquellen besitzen die Unterscheidung; keine parallel gepflegten Skill-Kopien. Vor dem nächsten Testlauf sind diese Änderungen umgesetzt und die Paketgrenzen in Tests abgebildet.
Steps:
1. Ergänze den bestehenden Builder und Export um eine eindeutige Standalone-/Suite-Paketprojektion. Nutze den vorhandenen Familienblock-Besitzer für die zentrale Auswahl; bewahre general/codex unabhängig davon als Laufzeitprofil. Erzeuge die eigentlichen Suite-Pakete direkt mit Suite-Vertrag statt Standalone-Pakete unverändert einzusammeln.
2. Inventarisiere Skill-Cores und geladene Referenzen auf Geschwister-Verfügbarkeit und optionale Koordination. Ersetze in Suite-Paketen allein die Installations-/Aktivierungsbedingungen; bewahre fachliche Anwendbarkeit und Autorisierung. Lege gemeinsame README-Textbausteine für beide Installationsverträge an: Suites setzen sämtliche enthaltenen Skills als installiert und aktiviert voraus; Einzel-Skills funktionieren jeweils allein. Passe Suite- und Einzelpaket-READMEs samt Installationsanweisung an; dieselbe Buildauswahl steuert diese Texte und die Runtime-Blöcke.
3. Ergänze vor dem nächsten Lauf Paketprüfungen für vorhandene Familienblöcke in Standalone sowie deren Abwesenheit und vollständige Suite-Voraussetzung in beiden Suites. Baue neue Testpakete; r2-Pakete erfüllen diese neue Anforderung noch nicht. Beziehe diese Änderung in W-009 und die Astra-High-Nachprüfung ein.
Evidence: [Shared 46 Tests und Suite 23 Tests bestanden am 2026-09-24; Layoutgrenzen sowie isolierte Exporte geprüft, Drei aktuelle Paketausgaben unter skills/temp/release gegen kanonische Quellen geprüft; kein Drift, Gemeinsame Installationsblöcke umgesetzt; Suites ohne Familienlisten; Standalone unabhängig; Review -05 Dokumentationsbefunde korrigiert]

### W-013 Ergänzung vor Abschlussprüfung: Ein temporärer Release-Build

Status: done
Depends on: [W-012]
Blocked by: []
Decisions: [ADR-0013]
Outcome: Es gibt genau einen aktuellen Release-Build unter E:/Dropbox/AI Projects/skills/temp/release; alle erzeugten Skill-Ausgaben im regulären Skill-Ordner entsprechen ihrem aktuellen geprüften Build.
Acceptance: Alle Releasepakete und Exporte entstehen im einzigen Stagingbaum skills/temp/release. Neue Kandidaten ersetzen diesen Baum kontrolliert statt weitere release-Datums-/rN-Verzeichnisse anzulegen; laufende Tests dürfen dabei keine Dateien verlieren. Die festen Synchronisationsziele sind skills/public/scoville-suite und skills/public/scoville-suite-for-codex; W-010/W-011 belegen dort den aktuellen vollständig geprüften Build. Nach der Umstellung sind die alten Release- und Korrekturbauten aus dem Skill-Ordner entfernt; Quellen und bestehende Git-Historie bleiben erhalten. Relevante Release-Anweisungen und Tests verwenden den neuen Pfad. Temporäre Testantworten bleiben im vorhandenen Task-Temp; sie sind keine zusätzlichen Release-Builds.
Steps:
1. Aktualisiere Build-/Releaseanweisungen und die betroffenen lokalen Stagingaufrufe auf skills/temp/release. Berücksichtige Suite- und Standalone-Artefakte innerhalb desselben Builds; keine Kandidatenverzeichnisse mit fortlaufenden Suffixen.
2. Erzeuge den aktuellen Build dort. Prüfe vor jeder Entfernung oder Verschiebung die aufgelösten absoluten Zielpfade und laufende Nutzer; entferne nach der Umstellung ausschließlich die inventarisierten alten Release-/Korrekturbauten. Bewahre bestehende Einzelpaket-Kopien bei nötiger Verzeichnisbereinigung außerhalb des Veröffentlichungsordners ohne Änderungen an ihren Repositories.
3. Bereite die vollständige Synchronisation aller erzeugten Skill-Ausgaben einschließlich der festen Suite-Ziele samt Inventar- und Hashvergleich für W-010/W-011 vor. Synchronisiere ausschließlich aus dem geprüften temporären Build und entferne entfallene generierte Dateien; im regulären Skill-Ordner dürfen keine veralteten Builds verbleiben. Quellen und Git-Historie sind keine Build-Ausgaben. Veröffentlichung und endgültiger Abgleich folgen erst nach W-009 und Astra-Gesamtreview.
Evidence: [Einziger Stagingbaum mit drei Paketprojektionen eingerichtet; Refresh und Inventarschutz getestet, Alte Release- und Rollover-Ordner nach manueller Nutzerbereinigung nicht mehr vorhanden; Bestand am 2026-09-24 geprüft, Vollständiger Zielabgleich in development/release-preflight.md vorbereitet; tatsächliche Synchronisierung folgt mit W-010 und W-011]

### W-009 Stufe 7: Beide Ausgaben vollständig prüfen und Release vorbereiten

Status: done
Depends on: [W-013]
Blocked by: []
Decisions: [ADR-0013, ADR-0014]
Outcome: Beide Suite-Ausgaben besitzen nachvollziehbare Build-, Paket- und Verhaltensnachweise als Grundlage einer gesonderten Veröffentlichung.
Acceptance: Beide Profile bauen reproduzierbar mit korrekter Mitgliedschaft, vollständig ersetzten Bausteinen, gültigen Links, eigenständigen Runtime-Abhängigkeiten und überprüften Exportquellen. Die allgemeine Ausgabe besteht die relevanten Ohne-Python-Fälle; die Codex-Ausgabe enthält keine Python-Ersatzwege. Getrennte Einstellungen und identische Helperauflösung sind geprüft. Aufgaben aus allen drei Schreibprofilen erhalten ihre Anforderungen; Workflow übergibt den Punkttext exakt und startet ausschließlich explizit. Vor einer Veröffentlichung gelten die bestehenden betroffenen Release- und Verständlichkeitsgates. Nicht ausgeführte Modelltests, Installationen oder Remote-Prüfungen werden ausdrücklich als offen dokumentiert. Vor W-010 prüft die offene Astra-High-Review-Session das gesamte Nicht-Ask-Update auf Fehler und übersehene Punkte sowie gegen alle einschlägigen Anforderungen dieses Plans. Ein Teilreview genügt nicht; relevante Befunde sind korrigiert und nachgeprüft.
Steps:
1. Prüfe die Integration und den isolierten Wiederaufbau beider Exporte auf dem finalen Quellenstand. Verwende noch gültige Einzelprüfungen der vorherigen Stufen; wiederhole sie nur bei betroffenen Änderungen oder vorgeschriebenen Gates. Prüfe Abschnitte, Dateien, Manifeste und Buildnachweise beider Ausgaben.
2. Erstelle den knapp dokumentierten Veröffentlichungs- und Wechselstand für beide Suites mit betroffenen Zielpfaden, Konfigurationserhalt und noch offenen Freigaben. Führe keine Veröffentlichung oder Repository-Umstellung allein wegen dieses Vorbereitungsschritts aus.
3. Beauftrage die offene Astra-High-Session `01a0d221-82c7-7222-9ba1-4bd8f2737ceb` mit dem vollständigen Nicht-Ask-Quellenstand und diesem Plan. Verlange einen Fehler- und Vollständigkeitsreview samt Anforderungsabgleich; prüfe außerdem gemeinsame High-Schreibregeln gegen die beiden ursprünglichen Prompting-Guides und unnötige Komplexität in Build und Skills. Korrigiere relevante Befunde und lasse die Korrekturen nachprüfen. Dokumentiere Review-Referenz und Ergebnis vor W-010; die Session bleibt offen.
Evidence: [Neues Astra-Gesamtreview scoville-w009-astra-20260924-new-01; alte Session geschlossen; Befunde in development/release-preflight.md, Plan-Default und Helperpflicht präzisiert; Handoff-Redaktion korrigiert; Quellen in allen drei Stagingprojektionen gebaut, 46 Shared und 75 Plan sowie 73 Workflow Tests bestanden; finale vier Distributionstests samt isoliertem Wiederaufbau bestanden, 16 gezielte Korrekturfälle lokal bewertet; 31 native Luna-Medium-Turns samt Hashbindung geprüft; Default-Fixture und frühere Fehlversuche dokumentiert, Nutzer verzichtet ausdrücklich auf erneutes Review; finale Korrekturen lokal geprüft; Release und Installation nicht durchgeführt]

### W-010 Stufe 8: Plan und allgemeine Suite veröffentlichen

Status: cancelled
Depends on: [W-009]
Blocked by: []
Decisions: [ADR-0014, ADR-0016, ADR-0035, ADR-0068]
Outcome: Der korrigierte Plan und die allgemeine Suite sind nach Abschluss aller Nicht-Ask-Implementierungs- und Prüfpunkte veröffentlicht. Workflow wird ausschließlich mit der Codex-Suite in W-011 veröffentlicht; dafür entsteht kein zusätzlicher Releaseweg.
Acceptance: Betroffene Paket-, Selector-, Prompt-, Konfigurations- und Releaseprüfungen sind bestanden. Plan erklärt seine eigene Konfiguration mit zwei gültigen Beispielen; Workflow erklärt seine eigene Konfiguration mit genau einem ausdrücklichen Aufrufbeispiel und seiner Aktivierungsgrenze. Workflow bleibt Suite-only. Veröffentlichungsnachweise nennen Version, Quellrevision, Ziel und Release-URL für Plan und allgemeine Suite. Die Workflow-Veröffentlichung folgt ausschließlich über W-011. Dokumentiere die zusammengehörigen Plan-/Workflow-Versionen. Der neue Workflow meldet einen alten inkompatiblen Selector konkret, ohne manuellen Ersatz; das gemeinsam gebaute Paar besteht den Dispatchcheck. Ein lokaler Build oder eine Releasevorbereitung genügt nicht für done. Alle READMEs der mit Skillwriter überarbeiteten Skills nennen gemäß ADR-0035 die Frontier-Modellvoraussetzung ab Version 5.0; finale Releaseprojektionen sind geprüft und tatsächliche Modellnachweise separat ausgewiesen.
Steps:
1. Schließe zuvor PLAN-0006 vollständig ab. Beauftrage die gültige Astra-High-Session 01a0d295-31c2-7bd0-9e98-8e1af4f3ddcc mit dem finalen gesamten Nicht-Ask-Stand einschließlich der bereinigten Mitgliedschaft und PLAN-0006; korrigiere relevante Befunde und prüfe sie nach. Prüfe die korrigierten Pakete einschließlich fehlender Gesprächshistorie, unverändertem Punkttext und getrennten Einstellungen; aktualisiere die zugehörigen Nutzungsfragmente und erfülle die bestehenden Releasegates.
2. Veröffentliche die Korrekturen im autorisierten Releaseablauf über die vorhandenen zulässigen Ziele und dokumentiere die tatsächlichen Veröffentlichungsnachweise. Der unabhängig beauftragte Ask-Umbau ist bereits umgesetzt; keine Wiederholung dieser Implementierung.
Evidence: [Nutzerauftrag vom 2026-09-25 ersetzt diesen Releasepunkt durch PLAN-0012 nach PLAN-0011 gemäß ADR-0068.]

### W-011 Stufe 9: Reine Codex-Suite veröffentlichen

Status: cancelled
Depends on: [W-009]
Blocked by: []
Decisions: [ADR-0013, ADR-0014, ADR-0016, ADR-0035, ADR-0068]
Outcome: Die Codex-Suite ohne Python-Fallbacks und mit dem gemäß ADR-0042 integrierten Scoville Ask ist veröffentlicht.
Acceptance: Die veröffentlichten Pakete enthalten die bereits freigegebenen Plan-/Workflow-Korrekturen, eigenständige Runtime-Abhängigkeiten und keine Python-Ersatzwege. Release-Version, Quellrevision, Ziel, URL und zugehöriger Buildnachweis sind dokumentiert. Die öffentliche GitHub-Profilseite `benjaminstelzer/BenjaminStelzer` listet die Codex-only Suite genau einmal an der passenden Stelle mit überprüftem Repository-Link und kurzer englischer Beschreibung ihrer Codex-Voraussetzung. Bestehende Einträge bleiben erhalten; der veröffentlichte Profil-README wird nach dem Push geprüft. Die allgemeine Ausgabe ist durch W-010 veröffentlicht und behält ihre geprüften Build-/Exportquellen. Die unabhängig beauftragte ASK-Implementierung ist bereits geprüft und wird nicht erneut gestartet. W-011 veröffentlicht Workflow im Codex-Paket genau einmal; W-010 benötigt dafür keinen vorgezogenen oder doppelten Suite-Release. Alle READMEs der mit Skillwriter überarbeiteten Skills nennen gemäß ADR-0035 die Frontier-Modellvoraussetzung ab Version 5.0; finale Releaseprojektionen sind geprüft und tatsächliche Modellnachweise separat ausgewiesen.
Steps:
1. Prüfe die Codex-Releaseartefakte aus W-009 gegen Profil, Mitgliedschaft und Quellenhashes; erfülle die geltenden Veröffentlichungs- und Sichtbarkeitsgates.
2. Veröffentliche die Codex-Suite im autorisierten Releaseablauf und ergänze oder aktualisiere anschließend ihren Eintrag im kanonischen README des GitHub-Profilrepositories `benjaminstelzer/BenjaminStelzer`. Prüfe den veröffentlichten Link und Inhalt; dokumentiere Suite-Release und Profil-Commit. Beende den Veröffentlichungsauftrag nach vollständigem Nachweis; die gemäß ADR-0043 separat beauftragte ASK-Entwicklung ist bereits abgeschlossen.
Evidence: [Nutzerauftrag vom 2026-09-25 ersetzt diesen Releasepunkt durch PLAN-0012 nach PLAN-0011 gemäß ADR-0068.]

### W-001 Stufe 10: Ein Scoville Ask mit konfigurierbarer Beraterauswahl

Status: done
Depends on: []
Blocked by: []
Decisions: [ADR-0012, ADR-0013, ADR-0016, ADR-0042, ADR-0043]
Outcome: Das gebaute Paket `scoville-ask-for-codex` führt ausschließlich lesende Anfragen an die ausgewählten Berater mit konfiguriertem Modell, Reasoning und Aufrufweg sowie passendem Frage- oder Review-Auftrag aus. Änderungen bleiben beim Ursprungstask; Ask erhält keinen Korrekturmodus.
Acceptance: Die Konfiguration und explizite Nutzerüberschreibungen ergeben für einen, zwei und mindestens drei Berater überprüfbar die ausgewählten Modelle, Reasoning-Stufen und Aufrufwege; gemischte CLI-/Codex-Runden funktionieren. Ein Python-Helper fragt die aktuelle native Codex-Modellliste samt Reasoning-Stufen über `model/list` ab und gibt auswählbare Optionen zurück; für jedes gelistete Modell ist der native Weg konfigurierbar, sofern der Host den Task damit starten kann. Fehlt die Modellauskunft oder schlägt ein Task-Start fehl, meldet der Helper den Fehler ohne Ersatzmodell oder manuellen Fallback. Ein Python-Helper kapselt Claude-CLI-Aufruf, Antwortauswertung und Wiederaufnahme; Skill-Anweisungen enthalten keinen direkten CLI-Ersatzweg. Allgemeine Fragen führen zum festgelegten Expertenrunden-Protokoll; Prüfaufträge geben jedem Berater einen unabhängigen Review-Auftrag. Tests decken mehrdeutige Formulierungen, fehlende Modelle, den Ausfall eines einzelnen Beraters, Python-/Helperfehler, unvollständige Antworten, Follow-ups und Sitzungs-/Task-Handles ab. Neue native ASK-Aufgaben heißen exakt `<Titel der aufrufenden Aufgabe> ASK-TASK`, ohne Nummerierung, Modellnamen oder weitere Zusätze. Gleichnamige Berateraufgaben bleiben über Task-IDs und Handles unterscheidbar. Bei unterstützter Sidebar-Sortierung stehen sie unmittelbar über der aufrufenden Aufgabe; fehlende Unterstützung wird als Einschränkung benannt. Ein isolierter Paketbuild funktioniert ohne installierte Geschwister; keine externe Aktion erfolgt ohne bestehende Nutzer- und Host-Autorisierung.
Steps:
1. Lege die neue kanonische Implementierung unter `members/scoville-ask-for-codex/` dieser Suite an, einschließlich Beraterkonfiguration und Modusvertrag. Übernimm benötigte Quellen aus `../ask-suite-for-codex` als Migration; dort entsteht kein zweiter aktiver Generator. Setze ADR-0012 um: unabhängige Antworten plus Synthese ohne verpflichtende zweite Austauschrunde.
2. Übernimm den Claude-CLI-Adapter, bündele `task_lifecycle` aus `../shared/runtime/` und ergänze die Auswahl-/Validierungsroutine. Prüfe den `model/list`-Datenweg gegen den Codex-Host und bewahre getrennte Antworten, Rückkanäle und Wiederaufnahme-Handles. Modell, Reasoning-Stufe, Aufrufweg und optionaler Name werden je Berater konfiguriert; Ask bleibt read-only. Benannte Presets liefern Astra 6 High, SOL 6 High, Claude Opus 5.5 High und Fable 5.1 Medium. Explizite Anfragen überschreiben Projekteinstellungen, persönliche config.json und zuletzt config.default.json.
3. Ermittle die unterstützten Sidebar-Sortiermöglichkeiten des Codex-Hosts. Implementiere Titelbildung und Zuordnung zur aufrufenden Task-ID im zuständigen Task-Helper; ordne neue ASK-Aufgaben nach Möglichkeit direkt oberhalb dieser Aufgabe ein. Bewahre die relative Reihenfolge fremder Aufgaben und ändere keine globale Sortierpräferenz stillschweigend. Prüfe exakte Titel, mehrere gleichnamige Berateraufgaben und den Fall ohne unterstützte Sortierung.
4. [execute: model=gpt-6-sol; reasoning=medium] Prüfe die funktionalen Helperverträge und realistische Skill-Anwendung mit einem unabhängigen Subagenten; unterscheide simulierte Hostfälle von echten Provideraufrufen.
5. Lasse den finalen Skill mit Astra High abnehmen und prüfe den Claude-CLI-Weg samt Sitzungsfortsetzung tatsächlich. Dokumentiere Provider- oder Anmeldefehler als offene Nachweise; beende keine laufenden Claude-Sitzungen.
Evidence: [Kandidat unter members/scoville-ask-for-codex implementiert; 17 SOL-6-Medium-Tests bestanden; Details in members/scoville-ask-for-codex/development/test-evidence.md, Astra-High-Befunde zur Konfigurationspriorität und Testportabilität korrigiert; Astra-Nachabnahme ohne weitere funktionale Befunde, Claude Code offiziell auf 2.1.282 aktualisiert; reale Claude- sowie SOL-/Astra-Aufrufe und Fortsetzungen erfolgreich; IDs und Grenzen in der Testevidenz, Reale Provider- und Follow-up-Nachweise in members/scoville-ask-for-codex/development/test-evidence.md; Statusdrift geschlossen]

### W-002 Stufe 11: Scoville Ask integrieren und einzeln anbieten

Status: cancelled
Depends on: [W-001]
Blocked by: []
Decisions: [ADR-0012, ADR-0013, ADR-0016, ADR-0042, ADR-0043]
Outcome: `scoville-ask-for-codex` ist Bestandteil der Scoville Codex Suite, zusätzlich einzeln installierbar und ersetzt die bisherigen erzeugten Ask-Varianten mit einem dokumentierten Wechselpfad.
Acceptance: Die beteiligten Manifeste, Build-Prüfungen und README-Quellen nennen genau das neue Paket `scoville-ask-for-codex` als Codex-Suite-Bestandteil und eigenständig installierbares Paket. Die allgemeine Suite-README führt es unter der Scoville Suite mit einem funktionierenden Einzelinstallationsweg und dem sichtbaren Hinweis „Codex online“. Seine Anforderungen sind Python, Codex-Modellauskunft über `model/list` sowie Claude CLI für diesen Aufrufweg. Die Installationsprüfung erkennt fehlendes Python und führt den vorgesehenen autorisierten Installationsschritt aus oder meldet dessen Scheitern. Ein eigenständiger README-Block „How to Ask with Claude Code“ erklärt kurz und in leicht folgenden Schritten Installation, Versionsprüfung und Update, Browser-Anmeldung über claude auth login, Prüfung über claude auth status, eine erste ASK-Anfrage sowie die erneute Anmeldung bei abgelaufenem OAuth. Die READMEs erklären die konfigurierbaren benannten Defaults, persönliche config.json und die Opus-5.5-Voraussetzung Claude Code ab 2.1.280 samt Versionsprüfung und offiziellem claude update ohne Beenden laufender Sitzungen. Die READMEs erklären die ausschließliche Helper-Nutzung ohne Fallback und dass Drittanbieter-Modelle für den nativen Codex-Weg eine passende Provider-Anbindung wie das vom Nutzer genannte EasyCLIProxy voraussetzen; eine sichtbare Modellauswahl allein garantiert keinen erfolgreichen Task-Start. Die bisherigen fünf Pakete werden nicht mehr als aktuelle Varianten generiert. Bestehende Konfigurationswerte werden erhalten und inkompatible Fälle benannt. Das allgemeine Suite-Paket enthält Ask nicht als Laufzeitmitglied oder exportierte Implementierungsquelle; sein README-Katalog darf den Codex-Skill mit Einzelinstallation aufführen. Die Prüfung trennt Katalogsichtbarkeit von Paketmitgliedschaft. Veröffentlichungs- und Installationsnachweise bleiben bis zur gesondert autorisierten Ausführung offen; bestehende Repositories oder Releases werden nicht gelöscht oder umgestellt.
Steps:
1. Deklariere `members/scoville-ask-for-codex/` in diesem `suite.json` als Codex-Suite-Mitglied und passe README-Quellen sowie Paket-/Build-Prüfungen an. Erstelle zwei allgemeine How-to-use-Beispiele mit und ohne Skillnamen sowie die erste Anfrage im eigenen Claude-Code-Einrichtungsblock und prüfe beide Suite-Ausgaben erneut auf die geänderte Mitgliedschaft. Beende im alten Ask-Quellprojekt die Generierung aktueller Varianten mit dokumentierter Migration. Historische Quellen bleiben Migrationsinput; bestehende Veröffentlichungen werden durch diesen Schritt nicht geändert.
2. Ergänze die kanonischen README-Fragmente der allgemeinen Suite um den Scoville-Ask-Eintrag mit „Codex online“ und konkretem Einzelinstallationsbefehl. Ermittle das bestehende geeignete Paket-/Installationsziel, bilde Standalone-Angebot und README-Katalog getrennt von der general-Mitgliedschaft im Manifest und Builder ab und prüfe generierte Links sowie isolierte Einzelinstallation.
3. [execute: model=gpt-6-sol; reasoning=medium] Prüfe mit einem unabhängigen Subagenten isolierte Pakete, Profilgrenzen, README-Projektionen und Migration.
4. Bereite die betroffenen Installations- und GitHub-Ziele mit Versions- und Kompatibilitätsnachweis für eine gesondert autorisierte Veröffentlichung vor.
5. Sichere nach vollständiger Übernahme und bestandenen Prüfungen die Git-Historie sowie lokale Änderungen von ../ask-suite-for-codex unter dem Workspace-Bereich state/. Prüfe verbleibende aktive Verbraucher und entferne den ausdrücklich freigegebenen alten Quellordner erst nach Auflösung seiner Abhängigkeiten.
Evidence: [Drei Paketprojektionen und 46 Shared-Tests bestanden; allgemeiner Katalog bietet ASK einzeln als Codex online an, Benannte Defaults und eigener Claude-Code-Einrichtungsblock in kanonischen README-Quellen und Mitgliedsvorschau ergänzt, Integration und Pakete geprüft; alte Gesamtstufe geschlossen; noch nicht entfernte Altquelle ausschließlich bei PLAN-0011/W-013 gemäß ADR-0053]
