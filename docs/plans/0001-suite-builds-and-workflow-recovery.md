---
format_version: 1
id: PLAN-0001
status: active
created: 2026-09-21
updated: 2026-09-22
current_item: W-025
---

# Suite-Builds und zuverlässige Workflow-Übergaben

## Goal

Scoville und Ask werden in getrennten Suite-Quellen unter `E:/Dropbox/AI Projects` gepflegt und als eigenständig installierbare Einzel-Skills gebaut. Gemeinsame Helper reduzieren mechanische Modellarbeit. Der Scoville-Workflow kann nach einer gültigen Übergabe trotz unvollständiger Aufgabenliste sicher fortfahren.

## Non-goals

- Workflow-Veröffentlichung nur als Suite-Bestandteil mit Beta-Kennzeichnung gemäß ADR-0009.
- Keine Änderung des fachlichen DIVI5-Plans oder seiner Akzeptanzkriterien.
- Keine Änderung der bestehenden Pollingregeln.
- Keine Task-Identifikation allein über Titel oder Titelpräfixe.

## Work items

### W-001 Zwei Suite-Quellen mit reproduzierbaren Einzelpaketen

Status: done
Depends on: []
Blocked by: []
Decisions: []
Outcome: `scoville-suite` und `ask-suite-for-codex` ersetzen die einzelnen Entwicklungs-Checkouts; Einzel-Repos erhalten ausschließlich gebaute Pakete und Nutzerdokumentation.
Acceptance: Alle 13 übernommenen Mitglieder sind gegen die Originale geprüft; Git-Historien und lokale Änderungen bleiben erhalten; reproduzierbare Builds enthalten keine Development-Dateien; öffentliche Builds schließen den Workflow aus; zusammengesetzte READMEs erhalten die Inhalte und nennen die Codex-only-Ausnahme; der GitHub-Skill verwendet den Build-Vertrag.
Steps:
1. Prüfe die bereits nach `members/` und in die benachbarte Ask-Suite kopierten Quellen einschließlich Workflow-Änderungen und die Git-Bundles unter dem neuen Workspace-Root; sichere weitere lokale Zustände vor Entfernung alter Checkouts.
2. Ergänze `development/build_suite.py` und ein Suite-Manifest um geprüfte Paketgrenzen sowie gemeinsame und mitgliedsspezifische README-Bausteine; erzeuge die Ask-Variante ohne gegenseitige Laufzeitabhängigkeit.
3. Passe den benjaminstelzer-github-Skill und dessen Strukturprüfungen an Suite-Quellen und generierte Distributions-Repos an; erhalte bisherige Installationspfade und Sichtbarkeiten.
4. Prüfe Builds und betroffene Mitgliedstests am neuen Root und konsolidiere erst danach die alten lokalen Checkouts ohne Verlust ihrer Historie oder Änderungen.
Evidence: [374 Quelldateien bytegleich übernommen und 13 Git-Bundles geprüft, README-Bausteine in beiden Suites zusammengesetzt, 8 Buildtests und 263 ausführbare Mitgliedstests bestanden, 46 GitHub-Skill-Tests und beide Distributionsabgleiche bestanden, Scribe-Routingfehler unverändert auch im Original reproduziert, Originalcheckouts vollständig unter Z:/Projekts/AI/state/suite-source-archives-2026-09-21 erhalten]

### W-002 Gemeinsame Helper mit eigenständigen Skill-Paketen

Status: done
Depends on: [W-001]
Blocked by: []
Decisions: []
Outcome: Wiederkehrende Task-Lifecycle-Operationen werden aus der kanonischen Quelle `E:/Dropbox/AI Projects/skills/private/shared` gebaut; beide Suites verwenden diese Quelle und jeder betroffene Skill enthält seine benötigte Kopie ohne installierte Laufzeitabhängigkeit vom Shared-Ordner.
Acceptance: Tests prüfen Erstellungspayloads und Rollenmarker; ready und pending IDs; eindeutige Rückgabezuordnung; Schutz vor Doppelstarts; unterschiedliche Ask- und Workflow-Archivierungsregeln; isolierte Nutzung jedes Pakets ohne installierte Geschwister; Drift-Erkennung der generierten Kopien.
Steps:
1. Ermittle die gemeinsamen mechanischen Verträge in Workflow-Prompt-Builder und Ask-Skills; trenne native App-Aufrufe von deterministischer Parameterbildung und Rückgabeprüfung.
2. Implementiere die gemeinsame Helper-Quelle und deren Build-Zuordnung; bewahre rollenspezifische Freigaben sowie die offene Fortsetzung erfolgreicher Ask-Tasks.
3. Integriere die Helper in die Skill-Anweisungen und prüfe die tatsächlich gebauten Einzelpakete einschließlich Fehler- und Wiederaufnahmefällen.
Evidence: [Gemeinsamer Helper unter ../shared/runtime/task_lifecycle.py mit vier Buildverbrauchern integriert, 11 Shared-Tests inklusive isolierter Paketaufrufe und tatsächlicher Drift-Erkennung bestanden, Native Listenfelder id und kind gegen list_threads geprüft und im Helper berücksichtigt, 50 Workflow- und 52 betroffene Ask-Mitgliedstests bestanden; keine Live-Aufgabe erzeugt oder archiviert]

### W-003 Nachträglich angefordert: Sichtbarkeitsblocker nach Koordinator-Übergabe beheben

Status: done
Depends on: [W-002]
Blocked by: []
Decisions: []
Outcome: Ein per exakter ID erreichbarer und im Guard gültig aktivierter Nachfolger kann nach bestätigtem Vorgängerabschluss weiterarbeiten; eine unvollständige Aufgabenliste allein blockiert nur die Archivierung.
Acceptance: Regressionstests bilden den DIVI5-Fall mit fehlendem Listeneintrag und erfolgreicher Exact-ID-Erreichbarkeit ab; gültige Guard-Identität und Generation bleiben erforderlich; falsche IDs und unbestätigter Vorgängerabschluss blockieren; fehlender Sichtbarkeitsnachweis lässt den Vorgänger offen; kein Doppelkoordinator oder zusätzlicher Executor entsteht; Sichtbarkeit wird nicht aus Titelpräfixen oder Listenabwesenheit abgeleitet.
Steps:
1. Prüfe `members/scoville-workflow-codex/scoville-workflow-codex/references/operations.md` beim Rollover-Schritt 9 und den bestehenden Lifecycle-Helper gegen den beobachteten Exact-ID-/Listenwiderspruch.
2. Trenne Fortsetzungsberechtigung und Archivierungsfreigabe im Helper und Operationsvertrag; behalte den Vorgänger bei unbekannter Sichtbarkeit als offenen Rückverweis und erhalte den Guard als alleinige Schreibberechtigungsquelle.
3. Ergänze Verhaltens- und Vertragsprüfungen unter `members/scoville-workflow-codex/development/tests/`; baue und installiere den geprüften Fix ohne laufende DIVI5-Worker neu zu starten.
Evidence: [54 Workflow-Tests einschließlich test_rollover_readiness.py und 11 Shared-Tests bestanden, Privater Build workflow-rollover-fix erstellt; fünf installierte Dateien per SHA256 abgeglichen, Vorheriger Skill unter E:/Dropbox/AI Projects/state/skill-install-backups/2026-09-21-lifecycle-rollover gesichert; keine laufenden Tasks neu gestartet]

### W-007 Native-Context-Gate-Abbruch und verfrühte Startmeldung prüfen und beheben

Status: done
Depends on: [W-001, W-002]
Blocked by: []
Decisions: []
Outcome: Der Workflow behandelt den beobachteten Gate-Abbruch bei W-013/step-4 korrekt und unterscheidet eine versandte Aufgabe von tatsächlich begonnener Ausführung.
Acceptance: Die Ursache wird aus vollständigem Dispatch, Gate-Aufruf oder dessen Ausbleiben und Rollenresultat belegt; ein Regressionstest deckt die bestätigte Fehlerursache ab; ein erforderliches Gate wird weder übersprungen noch bei Fehler als erfolgreich gewertet; Statusmeldungen behaupten keinen Projektstart allein aufgrund des Dispatchs; Fix und Tests liegen in der neuen Suite-Quelle und werden in das Einzelpaket gebaut.
Steps:
1. Lies bei Bearbeitung dieses Punktes die vollständigen Nachrichten zur Delivery-Referenz `g2-w013-step4-executor-a1-turn1-d83a6c15` aus den zugeordneten Tasks; vergleiche den tatsächlichen Dispatch mit `members/scoville-workflow-codex/scoville-workflow-codex/scripts/build_dispatch_prompt.py` und den Gate-Regeln in `references/operations.md` desselben Pakets.
2. Reproduziere den belegten Fehler entlang Prompt, `scripts/inspect_native_context.py`, verfügbarer Laufzeit und Rückgabevalidierung; unterscheide einen unterlassenen Aufruf von einem fehlgeschlagenen Aufruf oder einem korrekt blockierenden Gate.
3. Korrigiere die bestätigte Ursache und die verfrühte Startmeldung im jeweiligen kanonischen Owner innerhalb der neuen Suite; erhalte Read-only-Grenzen, eindeutige Ergebniszuordnung und Schutz vor doppeltem Retry.
4. Ergänze Regressionstests unter `members/scoville-workflow-codex/development/tests/` und prüfe das gebaute Paket; installiere den Fix ohne laufende Worker oder Projektdateien eigenmächtig neu zu starten beziehungsweise zu ändern.
Evidence: [Exact-ID-Lesung 01a0c2f7-fadb-70f3-b931-d52e71f41485 vollständig: kein Gate-Aufruf im Aktivierungsturn, Executor deutete finale Zustellungsform als Beschränkung des nächsten Tool-Aufrufs; kein technischer Gate-Fehler belegt, Prompt trennt Gate und Arbeitsaufrufe von finaler Zustellung; Vorabmeldungen nennen Versand statt Arbeitsbeginn, 54 Workflow-Tests bestanden; Luna ordnete fünf simulierte Ablaufzweige ohne Live-Effekte zu, Privater Build workflow-gate-fix installiert und SHA256-geprüft; Sicherung state/skill-install-backups/2026-09-21-gate-prompt am Workspace-Root]

### W-009 Ignorierte Codex-Einstellung features.thread_tools bereinigen

Status: paused
Depends on: []
Blocked by: [HOST-FLAGOWNER]
Decisions: []
Outcome: Die im Codex-Einstellungsdialog gemeldete unbekannte Einstellung `session-flags: features.thread_tools` ist an ihrer tatsächlichen Quelle korrigiert, ohne unbelegte Änderungen an Task-Funktionen vorzunehmen.
Acceptance: Der Ursprung des Flags ist belegt; aktuelle offizielle Codex-Dokumentation oder die konkrete Host-Diagnose begründet Entfernung oder Ersatz; relevante Konfiguration ist vor Änderungen gesichert; keine andere Einstellung wird verändert; ein erneuter Konfigurationscheck oder sichtbarer App-Nachweis bestätigt die beseitigte Warnung; nicht ausführbare Reload-Prüfung bleibt ausdrücklich offen.
Steps:
1. Prüfe bei Bearbeitung dieses Punktes aktuelle Codex-Konfigurationsdokumentation und den lokalen Ursprung von `features.thread_tools`; unterscheide Benutzerkonfiguration, Projektkonfiguration und injizierte Session-Flags.
2. Korrigiere ausschließlich die belegte ungültige Einstellung an ihrem Owner; verwende keinen geratenen Ersatz und behaupte keinen Zusammenhang mit dem Rollover-Sichtbarkeitsfehler ohne unabhängigen Nachweis.
3. Prüfe die Warnung erneut ohne laufende DIVI5-Tasks unautorisiert abzubrechen; falls ein App-Neustart erforderlich ist, benenne diesen verbleibenden Schritt statt dessen Erfolg zu behaupten.
Evidence: [Offizielle Referenz https://learn.chatgpt.com/docs/config-file/config-reference enthält weder thread_tools noch session-flags, Kein Treffer in geprüften Benutzer- und Projektkonfigurationen sowie globalem App-Zustand oder codex.exe-Startargumenten, App 26.915.4065.0 verwendet thread_tools intern als defaultFeatureOverrides; CLI 0.155.0-alpha.9.2 listet es nicht unter features list, Ursprung der konkreten Session-Injektion nicht abschließend belegt; keine Konfiguration oder App-Datei geändert]
Next action: Nutzer hat Zurückstellung zugunsten W-010 erlaubt. Bei neuer Host-Evidenz die tatsächliche Flag-Quelle prüfen; keine Binäränderung oder Unterbrechung laufender Tasks.

### W-010 Deferred after W-009: Familienverweise deterministisch erzeugen

Status: done
Depends on: [W-001]
Blocked by: []
Decisions: []
Outcome: Alle gepflegten Familienauflistungen und daraus abgeleiteten Verweise entstehen aus einer kanonischen Definition statt aus unabhängig gepflegten Kopien.
Acceptance: Hinzufügen eines Testmitglieds aktualisiert alle betroffenen Listen in stabiler Reihenfolge; absichtlich abweichende Kopien werden erkannt; eigenständige Builds enthalten vollständige Listen ohne Shared-Laufzeitabhängigkeit; private Mitglieder und historische Belege werden nicht versehentlich veröffentlicht oder umgeschrieben.
Steps:
1. Inventarisiere familienbezogene Elemente in Skills und README-Bausteinen beider Suites sowie deren Build- und GitHub-Prüfungen. Unterscheide vollständige Mitgliederlisten von absichtlich begrenzten Rollenverweisen und historischen Belegen.
2. Ergänze die kanonische Mitgliedsdefinition in suite.json und den Builder unter ../shared/build/build_suite.py um geordnete Familienbausteine und explizite Teilmengen. Ersetze manuell gepflegte Kopien einschließlich Family owners durch generierte Inhalte.
3. Prüfe Erweiterung und Drift mit einem Testmitglied sowie Paketgrenzen und bestehenden Rollenunterschieden. Dokumentiere den einzigen Pflegeweg knapp in den Projektregeln.
Evidence: [suite.json besitzt Familienmetadaten und explizite Nachbarteilmengen; shared/build/build_suite.py expandiert alle Listen vor Export, 15 Shared-Tests und je 4 Suite-Buildtests sowie 32 Design-Tests bestanden, Testmitglied erweitert vollständige Scoville- und Ask-Listen; Teilmengen bleiben begrenzt; manipulierte Paketkopie wird erkannt, Öffentliche Builds beider Suites gegen aktuelle Quellen und GitHub-Paketprüfung erfolgreich; Workflow nicht exportiert, README-Checks ohne Drift; historische Mitgliederunterlagen unverändert, quick_validate scheitert am vorhandenen compatibility-Feld und bei Plan zusätzlich am Windows-Decoding; keine Gesamtvalidierung behauptet]

### W-004 Einheitliche SCW- und ASK-Titel für neue Tasks

Status: done
Depends on: [W-002]
Blocked by: []
Decisions: []
Outcome: Neue Workflow-Tasks verwenden das Präfix `SCW` statt `Scoville-Workflow-Codex`; Arbeitsdurchläufe heißen `SCW <PLANPUNKT> WORK RUN [#<N>]`, `SCW <PLANPUNKT> REVIEW RUN [#<N>]` oder `SCW <PLANPUNKT> REPAIR RUN [#<N>]`. Neue Ask-Tasks verwenden ein entsprechendes eigenständiges ASK-Schema. N ist die numerische Versuchsnummer; das Wort ATTEMPT erscheint nicht im Titel.
Acceptance: Erstellungsaufrufe und angezeigte Durchlaufbezeichnungen verwenden dieselben deterministisch erzeugten Titel; Planpunkt und Versuch sind eindeutig; Koordinatoren beginnen mit SCW; Ask-Titel kennzeichnen Beratungsgegenstand und Berater; RUN bezeichnet den Durchlauf und behauptet keinen erfolgreichen Befund; vorhandene Tasks bleiben unverändert; Identitäts-, Pending- und Rollover-Abgleiche bleiben korrekt und verwenden Titel nicht als Ersatz für bestätigte Task-IDs.
Steps:
1. Inventarisiere die Titelbildung in `members/scoville-workflow-codex/scoville-workflow-codex/SKILL.md`, `references/operations.md` und `assets/workflow.toml` innerhalb desselben Pakets sowie in den vier Ask-Mitgliedern der benachbarten Suite; prüfe die Verbindung zwischen Titel, Versuchszähler und Pending-Reconciliation.
2. Ergänze den gemeinsamen Lifecycle-Helper um SCW-Titel für Koordinatoren und das vorgegebene Schema für WORK, REVIEW und REPAIR; erhalte benötigte Workflow- und Generationskennungen im Koordinatortitel und bestätigte Task-IDs als Identitätsquelle.
3. Ergänze für neue native Ask-Tasks das analoge Schema `ASK <GEGENSTAND> <BERATER> RUN [#<N>]`; berücksichtige Astra und SOL sowie zugehörige Claude-Durchlaufbezeichnungen ohne zusätzliche Claude-Tasks zu erzeugen oder bestehende Follow-up-Tasks umzubenennen.
4. Prüfe Titelgrenzen, Planpunktdarstellung, Versuchszählung, Rollenunterscheidung und unveränderte Wiederaufnahme mit den gebauten Einzelpaketen; aktualisiere die zugehörigen README-Bausteine und Beispiele.
Evidence: [Gemeinsamer task_title-Formatter erzeugt SCW-/ASK-Namen; create und gespeicherter Handle verwenden exakt denselben Titel, 20 Shared-Tests einschließlich isolierter Einzelpakete und Vorgänger-Ausschluss bestanden; 54 Workflow-Tests bestanden, Je 4 Suite-Buildtests bestanden; README-Beispiele generiert; bestehende Task-IDs und installierte Pakete unverändert]

### W-008 Workflow-Paket umbenennen und SCW-Kurzaufruf ermöglichen

Status: done
Depends on: [W-001, W-002, W-004]
Blocked by: []
Decisions: []
Outcome: Der kanonische Workflow-Skill heißt `scoville-workflow-for-codex` und ist über `$scoville-workflow-for-codex` sowie, soweit vom Host unterstützt, `$scw` aufrufbar.
Acceptance: Paketname, Frontmatter, Manifest, Installationshinweise und aktive Verweise verwenden den neuen Namen konsistent; beide Aufrufe führen zur selben Workflow-Implementierung und erzeugen nicht doppelte Koordinatoren; Alias-Unterstützung ist am Host belegt oder die verbleibende Einschränkung ausdrücklich berichtet; Sichtbarkeit bleibt privat; laufende Tasks behalten ihre funktionsfähigen bisherigen Pfade, bis ihre Umstellung sicher möglich ist.
Steps:
1. Prüfe die aktuelle offizielle Codex-Dokumentation und verfügbare Host-Funktionen auf native Skill-Aliase; verwende andernfalls nur bei belegter Unterstützung einen minimalen `scw`-Weiterleitungs-Skill ohne kopierte Workflow-Logik.
2. Benenne die kanonische Quelle und Builddefinition in der neuen Suite um; aktualisiere Frontmatter, Loader, Helper-Pfade, README-Bausteine, Tests und GitHub-Zielzuordnung unter Erhalt der privaten Sichtbarkeit und bisheriger Git-Historie.
3. Prüfe beide Aufrufe und die eindeutige Rollen-/Launcher-Erkennung mit gebauten Paketen; plane einen konfliktfreien Installationswechsel, der laufende Tasks nicht durch entfernte Pfade unterbricht und keine zwei automatisch konkurrierenden Workflow-Skills hinterlässt.
Evidence: [Kanonische Quelle und privater Build heißen scoville-workflow-for-codex; alte Installation unverändert, 54 Workflow-Tests sowie 20 Shared-Tests und 4 Suite-Buildtests bestanden; neuer privater Build stimmt mit Quellen überein, Offizielle Build-skills-Dokumentation geprüft; kein nativer Alias belegt; scw nur im geladenen Core erkannt und nicht als Host-Discovery behauptet, development/workflow-rename.md dokumentiert Alias-Einschränkung und sicheren späteren Installationswechsel; kein Live-Launch oder Remote-Rename]

### W-005 Ask SOL und gemeinsame Quellen für die Ask-Buildvarianten

Status: done
Depends on: [W-001, W-002, W-004]
Blocked by: []
Decisions: []
Outcome: `ask-suite-for-codex` erzeugt fünf eigenständig installierbare Skills. Der neue `ask-sol-for-review-for-codex` teilt seine gepflegte Basis mit Ask Astra und verwendet standardmäßig SOL mit Very High. Ask Claude and SOL und Ask Claude and Astra entstehen als zwei Builds derselben kombinierten Basis.
Acceptance: Der SOL-Einzelskill verwendet ohne Override `gpt-5.6-sol` und `xhigh` für Very High; explizite Einstellungen behalten Vorrang; Astra- und bestehende kombinierte Defaults ändern sich nicht unbeabsichtigt; alle fünf Pakete haben eindeutige Namen und Trigger; Einzel- und Doppelberatung bleiben getrennt; alle Pakete funktionieren ohne installierte Geschwister; generierte Varianten enthalten keine separat gepflegten Kopien gemeinsamer Logik oder README-Bausteine.
Steps:
1. Vergleiche in der benachbarten `ask-suite-for-codex` die Quellen unter `members/ask-astra-for-review-for-codex`, `members/ask-claude-and-sol-for-codex` und `members/ask-claude-and-astra-for-codex`; trenne gemeinsame Rollen- und Lifecycle-Verträge von Beraterkennung, Defaults, Metadaten und belegten Verhaltensunterschieden.
2. Ergänze die Suite-Builddefinition um eine gemeinsame Einzelberater-Basis mit Astra- und SOL-Varianten; übernimm SOL und Very High als Default ausschließlich für den neu angeforderten SOL-Einzelskill und prüfe die technische Effort-Zuordnung vor Auslieferung.
3. Erzeuge die beiden kombinierten Claude-Skills aus einer gemeinsamen Basis mit variantenabhängigen Beraterdaten; erhalte bestehende Konfigurationspräzedenz, Read-only-Grenzen, unabhängige Beratung, Rücklieferung, Follow-ups und Archivierungsregeln.
4. Ergänze Manifest, README-Bausteine, ASK-RUN-Titel und Paketprüfungen für fünf Ask-Skills; prüfe Triggerausschlüsse, Overrides, Variantenunterschiede und isolierte Installierbarkeit ohne reale Beratungen auszulösen.
Evidence: [Gemeinsame single/paired-Templates und fünf Manifestvarianten in ../ask-suite-for-codex; Defaults und Grenzen in development/variants.md dokumentiert, 2026-09-21: check-sources und check-readmes ohne Abweichung; check-packages für ask-five-variants valid:true, 2026-09-21: 7 Suite-Tests + 26 Astra-Paar-Tests + 23 SOL-Paar-Tests + 3 Astra-Einzeltests + 20 Claude-Tests + 20 Shared-Tests bestanden, Pakettests starten Adapter isoliert ohne Provideraufrufe; keine Live-Beratung oder Installation behauptet]

### W-011 Deferred after W-005: Vorgänger nach Koordinator-Rollover zuverlässig archivieren

Status: done
Depends on: [W-002, W-003]
Blocked by: []
Decisions: []
Outcome: Nach erfolgreicher Koordinator-Übergabe wird der abgeschlossene Vorgänger sicher archiviert; zunächst zurückgestellte Archivierung bleibt nachvollziehbar und wird bei erfüllten Voraussetzungen nachgeholt.
Acceptance: Der aktuelle DIVI5-Fall ist mit exakten Vorgänger-/Nachfolger-IDs und Archivierungsbedingungen nachvollzogen; Tests decken sofortige und zunächst blockierte Archivierung sowie spätere Wiederaufnahme ab; nur der bestätigte abgeschlossene Vorgänger wird archiviert; exakte archived:true-Rückgabe wird geprüft; unvollständige Listen blockieren keine gültige Fortsetzung und erzeugen weder Doppelstarts noch zusätzliche Pollingschleifen.
Steps:
1. Prüfe bei Bearbeitung den DIVI5-Wechsel von 01a0c308-ad05-7f03-82df-fbc11672cea1 zu 01a0c346-f731-7c90-8ec1-189692fe948b und den tatsächlich geladenen installierten Stand; trenne fehlende Freigabe, unterlassenen Aufruf, fehlgeschlagenen Aufruf und fehlende Nachholung.
2. Korrigiere die belegte Ursache in members/scoville-workflow-for-codex/scoville-workflow-for-codex/references/operations.md und bei Bedarf ../shared/runtime/task_lifecycle.py sowie ../shared/runtime/rollover_readiness.md; erhalte Guard-Identität, Vorgängerabschluss und Exact-ID-Nachweis.
3. Ergänze Regressionstests in members/scoville-workflow-for-codex/development/tests/test_rollover_readiness.py und ../shared/tests/; prüfe das gebaute Paket und dokumentiere den sicheren Rollout ohne Eingriff in laufende DIVI5-Aufgaben.
Evidence: [DIVI5 G3/G4 per Exact-ID geprüft: Vorgängerturn completed; Nachfolger aktiv aber nicht gelistet; kein Archivierungsaufruf im gelesenen Aktivierungsturn, Nachholung über geprüfte Übergabeketten und exakte Archivierungsbelege implementiert; Sichtbarkeitsschutz bleibt erhalten, 58 Workflow- und 20 Shared-Tests bestanden; privater Build workflow-archive-recovery-final stimmt mit Quellen überein, development/archive-recovery.md dokumentiert Ursache und Rollout; kein Live-Eingriff oder Installationsnachweis; dauerhafte Listenlücke bleibt sichtbarer Archivierungsblocker]

### W-012 Deferred after W-011: Ask-Einzelskills ausschließlich im Build erzeugen

Status: done
Depends on: [W-005]
Blocked by: []
Decisions: []
Outcome: Die Ask-Suite pflegt unter members nur gemeinsame Templates und notwendige variantenspezifische Quellen; vollständige Einzel-Skills entstehen ausschließlich im externen Build-Ziel.
Acceptance: Unter members liegen keine generierten Paketvorschauen; fünf eigenständige Pakete entstehen reproduzierbar aus den Quellen; Mitgliedstests prüfen gebaute Pakete statt Quellkopien; Defaults und Verhaltensgrenzen bleiben erhalten; Entwicklungshistorien und lokale Änderungen sind separat erhalten; gemeinsame README-Bausteine werden nicht dupliziert.
Steps:
1. Ordne in ../ask-suite-for-codex die bisherigen development/templates und members-Dateien nach gemeinsamer Quelle, Variantenwert, Entwicklungshistorie und generierter Vorschau; prüfe suite.json und alle betroffenen Testpfade vor der Verschiebung.
2. Konsolidiere die gepflegten Templates unter members und passe suite.json sowie bei Bedarf ../shared/build/build_suite.py an; erhalte historische Unterlagen separat und entferne ausschließlich nachgewiesen regenerierbare Vorschauen mit gesichertem Vorzustand.
3. Stelle die Tests unter ../ask-suite-for-codex/development/tests und die bisherigen Mitgliedstests auf isolierte Builds um; passe AGENTS.md, development/variants.md und betroffene GitHub-Buildprüfungen an und prüfe alle fünf Pakete ohne Provideraufrufe.
Evidence: [members enthält nur single/paired/claude; member_previews:false verhindert erzeugte Mitgliedskopien; Historien separat unter development/history, 64 vorherige Mitgliedsdateien SHA256-gesichert; Originale unter state/suite-migration-2026-09-21/ask-layout-before-w012 am Workspace-Root erhalten, 72 Mitgliedstests gegen isolierte Builds + 8 Ask-Suite-Tests + 20 Shared-Tests + 4 Scoville-Buildtests bestanden, Fünfer-Build ask-source-only und check-packages erfolgreich; Quellregeln und README aktualisiert; keine Installation oder Veröffentlichung]

### W-013 Deferred after W-012: Gemeinsame README-Templates unter shared verwenden

Status: done
Depends on: [W-001, W-010, W-012]
Blocked by: []
Decisions: []
Outcome: Wiederkehrende README-Inhalte beider Suites entstehen aus gemeinsamen Templates unter ../shared; Installation und Familienübersichten verwenden Manifestdaten statt separat gepflegter Kopien.
Acceptance: Alle README-Bausteine beider Suites sind auf gemeinsame Bedeutung geprüft; tatsächlich gleiche Inhalte haben eine gemeinsame Quelle; Namen, Links und Familienlisten werden deterministisch eingesetzt; Unterschiede bei Host-Kompatibilität, Sichtbarkeit und Installation bleiben erhalten; fertige READMEs enthalten keine Platzhalter oder Shared-Laufzeitabhängigkeit; Tests erkennen fehlende Variablen und Drift und verhindern private Workflow-Inhalte in öffentlichen Paketen.
Steps:
1. Inventarisiere die README-Quellen aus beiden suite.json-Dateien; identifiziere gemeinsame Installationstexte, Familienabschnitte und weitere bedeutungsgleiche Bausteine sowie notwendige Varianten.
2. Lege die gemeinsamen Templates unter ../shared/readme an und integriere deren explizite Auflösung in ../shared/build/build_suite.py; nutze bestehende Familienprojektionen aus ../shared/build/fragments.md und Manifestdaten als einzige Listenquelle. Der Abschnitt „Install the complete Scoville suite“ erhält genau einen manifestgesteuerten Link zum Suite-Monorepo statt Einzel-Skill-Installationslinks; prüfe Ziel und tatsächliche Installierbarkeit und kennzeichne private Zugangsvoraussetzungen ohne Veröffentlichungsfreigabe.
3. Ersetze duplizierte aktive README-Quellen durch Template-Verweise; erhalte Ersetzungstags für Familienblöcke auch in SKILL.md und Referenzen; lasse den gemeinsamen Helper sie ausschließlich aus suite.json erzeugen. Prüfe mit einem zusätzlichen Testmitglied die automatische Aktualisierung aller vollständigen Familienblöcke beim Build sowie private Paketgrenzen; explizite Nachbarschaftsauswahlen bleiben manifestgesteuert.
Evidence: [Gemeinsame Lizenz- und Familienblöcke sowie Suite-Mitgliederübersicht unter ../shared/readme eingebunden; beide Manifeste verwenden shared:-Referenzen, Builder prüft Shared-Pfadgrenzen und hält konsumierte Mitglieds-README-Templates im Buildbeleg fest; 22 Shared- und 12 Suite-Buildtests bestanden, Acht öffentliche Scoville-Installationsabschnitte aus einem Template bei unverändertem README-Ergebnis; vier native Ask-Varianten teilen Installationstemplate, Nach Ask-Umstellung: 72 Pakettests + 8 Ask-Suite-Tests + 22 Shared-Tests bestanden; danach vier gezielte README-Tests inklusive fehlender Variable und Konfigurationserhalt bestanden, Nutzer bestätigt finalen Monorepo-Link vor gemeinsamer Veröffentlichung; fehlendes Remote blockiert lokale Templates nicht, Finaler Stand: 26 Shared- und 4 Scoville-Buildtests bestanden; scoville-final-link und ask-shared-readmes gegen Quellen validiert, development/readme-templates.md hält Grenze fest: keine Remote-Erstellung oder Online-Installation nachgewiesen]

### W-015 Deferred after W-013: Skill-Beschreibungen in der Suite-README zusammensetzen

Status: done
Depends on: [W-013]
Blocked by: []
Decisions: []
Outcome: Die gemeinsame Scoville-Suite-README beschreibt jeden Skill aus dessen kanonischer Einzelbeschreibung ohne separat gepflegte Kopie.
Acceptance: Alle laut Manifest für die jeweilige Ausgabe vorgesehenen Mitglieder erscheinen in stabiler Reihenfolge mit ihrer eigenen Beschreibung; eine Änderung am Beschreibungsbaustein aktualisiert Einzel- und Suite-README beim Build. Neue Mitglieder werden automatisch berücksichtigt; fehlende Beschreibungen führen zu einem klaren Buildfehler. Workflow-Kompatibilität nur mit Codex und bestehende Sichtbarkeitsgrenzen bleiben ausdrücklich erhalten.
Steps:
1. Prüfe suite.json sowie development/readme und die README-Zusammensetzung in ../shared/build/build_suite.py; bestimme pro Mitglied den vorhandenen kanonischen Beschreibungsbaustein und trenne Beschreibung von Installations- und Entwicklungstext.
2. Ergänze eine manifestgesteuerte Suite-Projektion dieser Beschreibungen und verwende sie in der Suite-README-Quelle; pflege jeden Beschreibungstext nur einmal und erhalte gültige Links im jeweiligen Ausgabepfad.
3. Prüfe Vollständigkeit, Reihenfolge, Beschreibungsänderung, zusätzliches Testmitglied und fehlenden Baustein sowie private Ausgabegrenzen; regeneriere die README-Vorschauen und prüfe sie gegen die Quellen.
Evidence: [suite.descriptions übernimmt erste Mitgliedsfragmente; featured_member setzt Workflow zuerst; alle neun Beschreibungen in README geprüft, 28 Shared-Tests und 4 Suite-Tests bestanden; README-Check ohne Drift; öffentlicher Build scoville-descriptions-public gegen Quellen validiert, Tests prüfen Reihenfolge und neue Beschreibung sowie Quelländerung und fehlenden Inhalt; relative Links und Verwendung in Einzelpaketen werden abgewiesen, Workflow-Sonderrolle gemäß ADR-0001 dokumentiert; Scribe-Plan-Ausnahme an aktuellen Skill-Vertrag angeglichen; keine Veröffentlichung]

### W-016 Deferred after W-015: Workflow ausschließlich mit der Suite ausliefern

Status: done
Depends on: [W-015]
Blocked by: []
Decisions: [ADR-0001]
Outcome: Scoville Workflow hat kein Einzelrepository-Ziel und wird ausschließlich innerhalb der Scoville Suite gebaut und später ausgeliefert.
Acceptance: Manifest und gemeinsamer Builder unterscheiden Suite-only-Mitglieder von Einzelrepository-Paketen; GitHub-Prüfungen erzeugen oder verlangen kein Workflow-Einzelrepository. Aktive Links verweisen auf die Suite. Workflow bleibt Codex-only; laufende Installationen und historische Belege bleiben unverändert. Release-Testpfad ist der echte Suite-Auslieferungspfad.
Steps:
1. Prüfe suite.json, ../shared/build/build_suite.py und den benachbarten GitHub-Skill auf Einzelrepository-Annahmen und bestimme den Suite-Auslieferungspfad ohne neue Veröffentlichung.
2. Passe Manifest, Buildlogik, aktive README-Verweise und GitHub-Prüfungen an die Suite-only-Zuordnung an; erhalte die eigenständig installierbaren übrigen Skills und die aktuelle private Workflow-Grenze bis zur Freigabe.
3. Prüfe Suite-Build, fehlendes Einzelrepository-Ziel und gültige Links; konkretisiere W-014 mit dem belegten Suite-Release-Pfad für Workflow.
Evidence: [Manifest und Builder verwenden distribution:suite sowie scoville-suite/packages/scoville-workflow-for-codex; kein Einzelrepository-Ziel, 28 Shared- und 4 Suite-Tests bestanden; 2 GitHub-Belegtests prüfen Suite-Ziel und Pfad sowie private Sperre, Frischer Build workflow-suite-only mit GitHub-Paketprüfung und Quellenvergleich validiert; Installationslink zeigt Suite-Unterpfad, Skill-Creator-Validator lehnt vorhandenes compatibility-Feld ab; keine vollständige Skill-Validierung oder Online-Installation behauptet, Abschließende Pfadprüfung: suite-only family.install korrigiert; 29 Shared- und 4 Suite-Tests bestanden; Ask-README ohne Drift]

### W-006 Alle Skills auf gemeinsame Helper und Textbausteine prüfen

Status: done
Depends on: [W-005]
Blocked by: []
Decisions: []
Outcome: Alle Skills beider Suites sind auf gemeinsame Helper und verallgemeinerbare Textelemente geprüft. Empfehlungen benennen eine gemeinsame Quelle je Baustein und erhalten notwendige Skill-Unterschiede.
Acceptance: Die Prüfung erfasst alle Suite-Mitglieder einschließlich Plan und Workflow; Helper-Kandidaten nennen Aufrufer sowie Ein- und Ausgaben; Textkandidaten nennen Verbraucher sowie gemeinsame und abweichende Regeln; jeder Kandidat nennt kanonische Quelle und Einbindung beim Build sowie Nutzen und Fehlerrisiko; Risikoeinstufungen wie low/medium/high werden ausdrücklich verglichen; bestehende Helper und Fragmente werden berücksichtigt; ungeeignete Vereinheitlichungen werden begründet ausgeschlossen; keine Untersuchung vor diesem Planpunkt und keine zusätzliche Implementierung allein aufgrund dieser Prüfung.
Steps:
1. Inventarisiere nach W-013 alle Mitglieder aus beiden suite.json-Dateien und prüfe deren Skill-Anweisungen, Referenzen, Vorlagen und Skripte auf wiederkehrende Mechanik und verallgemeinerbare Textelemente; berücksichtige vorhandene gemeinsame Quellen.
2. Vergleiche insbesondere Risikoeinstufungen von Plan und Workflow sowie weitere wiederholte Regeln aller Skills; trenne identische Bedeutung von nur ähnlicher Formulierung und erhalte skill-spezifische Zuständigkeiten und Grenzen.
3. Halte priorisierte Empfehlungen in der zugehörigen Suite-Entwicklungsdokumentation fest; benenne je gemeinsamem Baustein eine Quelle unter ../shared, Verbraucher und deterministische Build-Einbindung in eigenständige Pakete; trenne mechanische Helper von Textbausteinen und fachlicher Bewertung.
Evidence: [development/shared-candidates.md enthält Abdeckung aller neun Scoville-Mitglieder und fünf Ask-Varianten aus drei Basen, 102 exportierte Markdown-/Python-/JavaScript-Quellen auf Duplikate geprüft; relevante Verträge und Adapter semantisch verglichen, Kandidaten nennen gemeinsame Owner und Build-Einbindung sowie Nutzen und Risiken; Plan-/Workflow-Routing von Code-Risiko getrennt, Vollständige Claude-Runner und universelle Beleg-/Handoff-Verträge begründet ausgeschlossen; keine Kandidaten implementiert]

### W-014 Prioritized after W-006: Luna-Verständnistest als Veröffentlichungssperre

Status: cancelled
Depends on: [W-006]
Blocked by: []
Decisions: [ADR-0001]
Outcome: Jeder Scoville-Skill und ein Vertreter jeder Ask-Templatebasis ist vor Veröffentlichung mit 25 verschiedenen zunehmend schwierigen theoretischen Aufgaben auf LUNA Medium geprüft.
Acceptance: Der auftraggebende Agent schreibt Aufgaben und Soll-Ergebnisse vor Testbeginn. Ein SOL-Medium-Koordinator führt die Tests mit LUNA Medium aus und protokolliert die Ist-Ergebnisse getrennt davon. Jeder Fall bewertet Trigger und Nicht-Trigger sowie zuständiges Routing, fachliche Bewertungen und Verständnis der Skill-Regeln anhand vorab festgelegter Kriterien. Keine offenen Fehlbefunde oder fehlenden Fälle; Korrekturen sind erneut getestet. Belege nennen Paket-Hashes, tatsächliche Modell-IDs, Reasoning und Fallresultate; theoretische Tests gelten nicht als Live-Funktionsnachweis.
Steps:
1. Ermittle nach W-006 den finalen Testumfang aus beiden suite.json-Dateien; berücksichtige alle Scoville-Mitglieder einschließlich Workflow sowie je einen Vertreter aus ../ask-suite-for-codex/members/single, paired und claude. Verankere die Veröffentlichungssperre in gemeinsamen Projektregeln und im GitHub-Veröffentlichungsweg.
2. Erzeuge zuerst die zur Veröffentlichung bestimmten Einzelpakete unter E:/Dropbox/AI Projects/skills/public/<skill-name> aus den Suite-Manifesten; prüfe vorhandene Zielverzeichnisse und erhalte fremde oder uncommittete Änderungen. Prüfe vollständige Runtime-Abhängigkeiten und fehlende Entwicklungsdateien; erfasse Paketpfade und Datei-Hashes. Teste ausschließlich diese Release-Pakete ohne Zugriff auf private Templates oder gemeinsame Quellverzeichnisse. Ein noch nicht zur Veröffentlichung freigegebenes Mitglied bleibt separat privat testbar und wird nicht allein für diesen Test öffentlich gestaged. Workflow ist kein Einzelrepository: teste den Suite-Unterpfad scoville-suite/packages/scoville-workflow-for-codex/scoville-workflow-for-codex aus einem getrennten privaten Build bis zur Freigabe; danach liegt derselbe relative Pfad unter skills/public.
3. Erstelle als auftraggebender Agent je Testobjekt 25 geordnete Fälle von einfachen Positiv-/Negativfällen bis zu mehrdeutigen Grenz-, Konflikt- und Fehlerfällen; schreibe Soll-Ergebnisse mit Begründung aus den Skill-Regeln und eindeutigen Prüfkriterien getrennt von den Testprompts. Halte Aufgaben, Soll-Ergebnisse und Testanleitung unter development fest; verwende keine nachträglich an Modellantworten angepassten Soll-Ergebnisse.
4. [execute: model=gpt-5.6-sol; reasoning=medium] Führe als Koordinator die vorbereiteten Tests ausschließlich mit gpt-5.6-luna und reasoning=medium aus; bestätige zuerst deren tatsächliche Verfügbarkeit und starte andernfalls keinen Ersatzmodell-Test. Lade je Fall das Paket aus dem erfassten Release-Pfad und prüfe seine Hashes; gib LUNA nötigen Aufgabenkontext ohne Soll-Ergebnisse oder frühere Antworten. Simuliere externe Aktionen ohne echte Provideraufrufe oder Zustandsänderungen. Erfasse Antworten und bewerte sie gegen die vorgegebenen Kriterien; protokolliere Abweichungen statt Erfolge zu erfinden.
5. Prüfe als auftraggebender Agent SOLs Ergebnisbericht gegen die Testbelege; behebe belegte Skill-Fehler ausschließlich im jeweiligen Quell-Owner und baue betroffene Release-Pakete im public-Ziel neu. Lasse SOL betroffene Fälle sowie relevante Regressionen erneut mit LUNA Medium gegen diesen neuen Stand prüfen. Halte die knappe Ergebnismatrix bei der Suite und Rohdaten unter dem Workspace-temp-Ziel; Änderungen an getesteten Artefakten entwerten betroffene Testbelege. Veröffentliche später nur hashidentische geprüfte Pakete. Gib Veröffentlichung erst bei vollständigem fehlerfreiem Nachweis frei; dieser Testpunkt veröffentlicht selbst nichts.
Evidence: [development/luna-tests enthält zwölf Fall-/Soll-Dateipaare mit 300 Fällen, Alle 24 Testdateien enthalten geprüft genau die geordneten IDs 01 bis 25, development/luna-tests/author-review.md dokumentiert Autorenprüfung aller zwölf Testsätze gegen gebaute Verträge und korrigierte Testvoraussetzungen, development/luna-tests/results.md: Pilot code-01 bestanden und vom Autor bestätigt; native Laufzeit gpt-5.6-luna / medium geprüft, development/luna-tests/evaluation-manifest.json fixiert geprüfte Paket- und Testhashes, Nutzer ersetzt LUNA durch Gemini Flash Medium gemäß ADR-0002; W-017 übernimmt den Testumfang; ursprüngliche Befunde bleiben erhalten]

### W-017 Gemini-Verständnistest als Veröffentlichungssperre

Status: cancelled
Depends on: [W-006]
Blocked by: []
Decisions: [ADR-0001, ADR-0002]
Outcome: Alle Suite-Skills und je ein Vertreter jeder Ask-Templatebasis sind mit Gemini 3.8 Flash Medium anhand von 300 vorab geschriebenen theoretischen Fällen geprüft.
Acceptance: SOL Medium führt 25 zunehmend schwierige Fälle je Scoville-Skill und je Ask-Templatebasis mit gemini-3.8-flash-medium und medium aus. Getestet werden gebaute Pakete im public-Ziel sowie der private Suite-Pfad des Workflows. Der Autor prüft SOLs Bewertung gegen feste Soll-Ergebnisse. Modell/Effort, Paket-Hashes, Routing, Bewertungen und Verständnis sind belegt; keine fehlenden Fälle oder offenen Fehlbefunde. Simulierte Aktionen verändern keinen Live-Zustand. Dies ist kein Live-Integrationsnachweis und keine Veröffentlichung.
Steps:
1. Prüfe den bestehenden Antigravity-Transport in Z:/Projekts/AI/skills/private/gemini-worker und agy.exe; verwende keine automatische Tool-Freigabe oder Implementierungsberechtigung. Verifiziere sichere Testgrenzen und Modell-/Effort-Belege vor Fallausführung.
2. Übernimm development/luna-tests als unveränderte Aufgaben-/Soll-Basis und erhalte alte Läufe. Passe ../shared/luna-release-gate.md und den Veröffentlichungsweg an ADR-0002 an. Baue die Code-Quellkorrektur neu; prüfe Pakete und erfasse neue Hashes getrennt vom alten evaluation-manifest.json.
3. Führe unter SOL Medium zuerst einen isolierten Gemini-Piloten und danach alle 300 Fälle mit frischem Kontext je Fall aus. Verberge Soll-Ergebnisse und frühere Antworten; protokolliere Rohdaten unter Workspace-temp und kompakte Resultate in der Suite.
4. Prüfe Antworten und tatsächliche Aktionen unabhängig; korrigiere belegte Fehler im Quell-Owner, baue neu und wiederhole betroffene Fälle und Regressionen. Bestätige nur vollständig geprüfte unveränderte Pakete.
Evidence: [development/luna-tests/gemini-preflight.md dokumentiert verweigerten Sentinel-Schreibzugriff und Grenzen der Isolation, development/luna-tests/gemini-evaluation-manifest.json fixiert 206 geprüfte Paketdateien und unveränderte Aufgaben/Soll-Dateien, Code-Paket im public-Ziel neu gebaut; Altstand unter temp/2026-09-21-suite-gemini-evaluation/luna-code-baseline gesichert, development/luna-tests/gemini-results.md: code-01 vom Autor geprüft; korrekte Nicht-Aktivierung ohne Tools, Shared-Veröffentlichungssperre und GitHub-Veröffentlichungsweg auf ADR-0002 umgestellt, Nutzer ersetzt Gemini durch Codex CLI mit LUNA Medium; W-018 übernimmt; 14 Gemini-Fälle bestätigt und code-15 nach verweigertem Tool-Aufruf gestoppt]

### W-018 LUNA-Verständnistest über Codex CLI

Status: done
Depends on: [W-006]
Blocked by: []
Decisions: [ADR-0001, ADR-0003]
Outcome: Alle 300 festgelegten theoretischen Fälle sind mit LUNA Medium über Codex CLI unter SOL-Medium-Koordination gegen die gebauten Suite-Pakete geprüft.
Acceptance: Alle 25 Fälle je Scoville-Skill und Ask-Templatebasis bestehen gegen unveränderte Soll-Ergebnisse; der Autor bestätigt SOLs Bewertungen. Belege nennen aktuelle Paket-Hashes und tatsächliches gpt-5.6-luna mit medium. Toolzugriff und Live-Mutationen sind vor Tests nachweislich unterbunden. Kein Ersatzmodell und keine Veröffentlichung; Gemini-Belege zählen nicht als LUNA-Nachweis.
Steps:
1. Prüfe die vorhandene Codex CLI und per-run Konfiguration anhand development/luna-tests/isolation-check.md; bestätige Toolgrenzen sowie native Modell-/Effort-Belege ohne globale Konfigurationsänderungen oder erneuten Zugriff auf verweigerte Ressourcen.
2. Stelle ../shared/luna-release-gate.md und den GitHub-Veröffentlichungsweg auf ADR-0003 um. Erfasse aktuelle public-Pakete und den privaten Workflow-Suite-Pfad mit neuen Hashbelegen; bewahre alle früheren Manifeste und Läufe.
3. Führe unter SOL Medium zuerst einen begrenzten CLI-Piloten und danach die festen 300 Fälle aus development/luna-tests mit frischem Kontext je Fall aus; halte Soll-Dateien und frühere Antworten vom Tester fern. Liefere erforderliche Pakettexte kontrolliert; simuliere Projektaktionen ohne Tools.
4. Prüfe als Autor Antworten und native Laufzeitbelege; korrigiere nachgewiesene Fehler im Quell-Owner, baue betroffene Pakete neu und wiederhole betroffene Fälle sowie Regressionen. Halte Ergebnisse bei der Suite und Rohdaten unter Workspace-temp.
Evidence: [Nutzer verlangt Rückkehr zu Codex CLI mit LUNA; SOL Medium bleibt Koordinator, development/luna-tests/codex-cli-preflight.md: lokaler Request mit festem Katalog bestätigt tools leer und LUNA Medium; kein Backend-Nachweis, Veröffentlichungssperre und GitHub-Vertrag verwenden ADR-0003; Gemini-Belege bleiben historisch, Nutzer verlangt nach qualifiziertem Testweg eine detaillierte exakt wiederverwendbare Anleitung samt geprüftem Starter im Suite-Development, 64 ausgewählte Fälle gemäß ADR-0008 durch SOL und Autor bestätigt; development/luna-tests/codex-cli-results.md und codex-cli-execution.md, Astra high auf Nutzerwunsch ohne neue Modelltests; nur theoretische Prüfung und keine Veröffentlichung]

### W-019 Deferred after W-018: Reine Ergebnisprojektion automatisch abfangen

Status: done
Depends on: []
Blocked by: []
Decisions: [ADR-0004]
Outcome: Nachweislich reine Byte-/Darstellungsfehler zwischen Ergebniszustellung und Host-Projektion führen automatisch zur Darstellungskorrektur oder gültigen Übernahme ohne erneute Nutzerfrage.
Acceptance: Beide gemeldeten Reviewer-Ergebnisse sind anhand verfügbarer Originaldaten verglichen; md:grid und md:w-1/2 sind abgedeckt. Automatische Fortsetzung setzt belegte Identität des Ergebnisses und ausschließlich transportbedingte Darstellung voraus. Echte Inhaltsabweichungen und fachliche Fehler bleiben erkennbar und werden nicht als pass übernommen; fehlende Originalbytes bleiben Beleglücken. Negative Integritätsfälle und erneute Tests geänderter Pakete bestehen. Keine DIVI5-Projektänderungen oder Live-Task-Mutationen.
Steps:
1. Lies die gemeldeten Ergebnisquellen der Reviewer 01a0c3fa-53e2-73a1-9f9e-a5a1be803249 und 01a0c486-ce2b-7442-a7da-8885fa15658c im Workflow 01a0c128-2f34-7903-a601-43c6dec5c151; vergleiche Delivery und finale Projektion ohne weitere Zustellung oder Task-Neustart.
2. Ermittle im Workflow-Mitglied und seinen gemeinsamen Helpern den Owner des bytegenauen Ergebnisvergleichs; grenze Host-Darstellung gegen Inhaltsänderung ab und bestimme eine unveränderte verlässliche Belegquelle für die automatische Behandlung.
3. Implementiere die belegte Darstellungskorrektur oder Ergebnisübernahme am kanonischen Owner gemäß ADR-0004; bewahre Originalbytes und Ergebnisstatus, ohne fachliche Befunde zu überschreiben.
4. Prüfe echte Inhaltskonflikte und fehlende Belege als Negativfälle sowie die gemeldeten Projektionen als Positivfälle; baue betroffene private Pakete neu und wiederhole deren betroffene Verständnistests und Regressionen.
Evidence: [Meldung aus Aufgabe 01a0c3d1-11a6-7ad2-8f01-dabf6713f211, Delivery g8-w015-step3-reviewer-a1-turn1-result und g8-w015-step3-reviewer-a2-turn1-result, Nutzerentscheidung zur automatischen Behandlung im Ursprungschat read_thread bestätigt; ADR-0004, Beide ursprünglichen Wait-Projektionen weichen bei passenden IDs von identischen Source-/Delivery-Bytes ab; development/result-projection-recovery.md, Operations erlaubt begrenzte Wiederherstellung; privater Build workflow-projection-recovery-final besteht Paketabgleich, Zwei fokussierte Vertragsprüfungen und Luna projection-01 durch SOL und Autor bestätigt; development/result-projection-recovery.md]

### W-020 Deferred after W-018: Letzte zehn DIVI5-Durchgänge auf Übergaben und Tokenverlauf prüfen

Status: done
Depends on: []
Blocked by: []
Decisions: []
Outcome: Die letzten zehn abgeschlossenen DIVI5-Workflow-Durchgänge sind auf übergroße Übergaben und den Tokenverlauf ihrer Sessions untersucht; die vom Nutzer beobachtete Stabilität wird anhand belegter Laufdaten eingeordnet.
Acceptance: Ein kompakter Bericht unter development/divi5-workflow-ten-runs.md nennt Erhebungszeitpunkt und Auswahlregel sowie die zehn Durchgänge mit exakten Task-IDs und zugehörigen Koordinatoren. Er vergleicht Übergabeumfang und notwendige Inhalte; trennt Kontextbelegung von kumulativer Nutzung sowie Input und Cache und Output; vermeidet Doppelzählung fortgesetzter Sessions. Spitzen und Verlauf werden mit Modell-Kontextfenster und wirksamen Thresholds eingeordnet. Fehlende Telemetrie bleibt unbekannt; keine erfundenen Tokenkosten oder pauschale Stabilitätsbehauptung. Konkrete Auffälligkeiten erhalten Beleg und Empfehlung. Keine Änderungen an DIVI5-Dateien oder Live-Aufgaben.
Steps:
1. Ermittle beim Analysebeginn read-only die aktuelle DIVI5-Workflow-Kette und ihre letzten zehn abgeschlossenen Durchgänge; ordne exakte Task- und Turn-IDs sowie Rollen und Versuche zu und dokumentiere Auswahlgrenze und laufende ausgeschlossene Durchgänge.
2. Vergleiche deren Dispatch- und Rollover-Übergaben mit den erforderlichen Inhalten; ermittle verfügbare Tokenwerte oder kennzeichne Byte-/Zeichenumfang als Ersatzmaß. Benenne unnötige Wiederholungen und übertragene Altinformationen ohne notwendige Vertragsdaten als Ballast zu werten.
3. Werte vorhandene native Nutzung und Kontextbelegung je beteiligter Session chronologisch aus; prüfe Zählersemantik und Resume-Überlappung vor Aggregation sowie Threshold- und Rollover-Ereignisse. Keine zusätzlichen Modellläufe zur Messung.
4. Halte belegten Verlauf und Ausreißer sowie Unsicherheiten und priorisierte Empfehlungen in development/divi5-workflow-ten-runs.md fest; Rohdaten nur unter Workspace-temp. Führe vorgeschlagene Korrekturen nicht im Rahmen dieser Analyse aus.
Evidence: [development/divi5-workflow-ten-runs.md belegt zehn akzeptierte Einheiten mit zehn Koordinatoren und 23 Kindern; exakte IDs und Zählerabgleich, Alle zehn Boundary-Checks verlangen Rollover; Schwelle 33 Prozent ist kein harter Kontextdeckel; Peaks bis 81 Prozent, Zwei identische zusätzliche Dispatch-Ausgaben in G15 belegt; Empfehlungen ohne Live-Änderung; W-009 bleibt nutzerpausiert]

### W-021 Phase 1: Dispatch-Payload einmal erzeugen und ohne Vollausgabe weiterreichen

Status: done
Depends on: [W-020]
Blocked by: []
Decisions: []
Outcome: Ein Dispatch wird einmal erzeugt und bytegleich durch Prüfung und Versand geführt; der Koordinator erhält im Normalfall nur eine kompakte Bestätigung statt mehrfacher Prompt-Vollausgaben.
Acceptance: Ein isolierter Test belegt genau eine Erzeugung und einen Versandversuch mit identischen Payload-Bytes. Die Bestätigung nennt Ziel-ID, Rolle, Dispatch-Referenz, Länge und Hash. Abgeschnittene Anzeige löst weder Neuerzeugung noch Doppelversand aus; geänderte Eingaben und veraltete Guard-Daten werden erkannt. Unbekannter Versandstatus blockiert Wiederholung. Plan-/Decision-Inhalte, Berechtigungen und Ergebniszustellung bleiben erhalten. Tests unterscheiden tatsächliche Host-Integration von Simulation; keine Live-DIVI5-Aufgabe, Installation oder Veröffentlichung.
Steps:
1. Prüfe in members/scoville-workflow-for-codex/scoville-workflow-for-codex/scripts/build_dispatch_prompt.py und ../shared/runtime/task_lifecycle.py den Datenweg vom Builder über message bis zum Host-Aufruf. Belege, ob der vorhandene Ausführungskontext den vollständigen Payload ohne Modellausgabe halten und weiterreichen kann; führe keinen echten Dispatch zur Erkundung aus.
2. Implementiere am bestehenden Owner den belegten Übergabeweg und kompakte Erfolgsausgaben. Falls speicherinterne Weitergabe nicht möglich ist, bestimme vor Umsetzung einer kurzlebigen Payload-Datei deren zulässigen Ort, Identitäts-/Hashbindung und Wiederaufnahmegrenzen; verwende keine ungesicherte Dateifallback-Lösung. Volltextdiagnose bleibt explizit und darf keinen Versand auslösen.
3. Passe die Dispatch-Anweisungen in members/scoville-workflow-for-codex/scoville-workflow-for-codex/references/operations.md an. Ergänze fokussierte Tests im zugehörigen development/tests und bei Änderungen am Shared-Vertrag in ../shared/tests; prüfe alle betroffenen Buildverbraucher isoliert und erzeuge einen neuen privaten Workflow-Build.
Evidence: [Builder und dispatch_transport.js halten Payload und kompakten Beleg getrennt; einmaliger Versandversuch mit Vorab-Sperre, test_dispatch_transport.py besteht mit echtem Builder und Lifecycle sowie Mock-Sender; Integrität und Negativpfade geprüft, Privater Build temp/2026-09-21-workflow-context-fix/w021 besteht Paketabgleich; kein Live-Dispatch]

### W-022 Phase 2: Koordinator-Regeln vollständig nach Arbeitsphase laden

Status: done
Depends on: [W-021]
Blocked by: []
Decisions: []
Outcome: Der Koordinator lädt einen kurzen Pflichtkern und die eindeutig zugeordneten Regeln seiner aktuellen Phase statt bei jedem Start den gesamten Operationsvertrag.
Acceptance: Jede bisherige verbindliche Regel hat genau einen gepflegten Owner und bleibt von ihrem Ausführungspunkt erreichbar. Die Lesetabelle deckt Aktivierung, Dispatch, Ergebnisprüfung, Review/Repair, Abschluss und Rollover sowie Fehler-/Wiederaufnahmewege ab. Kein Pfad überspringt Guard, Freigaben, Ergebnisintegrität oder Archivierungsbedingungen. Pflichtkern und benötigte Phasenreferenzen sind vollständig in eigenständigen Builds enthalten; keine pauschale Volllektüre oder abgeschnittene Pflichtregel ersetzt das Routing. Alte installierte Pfade und laufende Aufgaben bleiben unverändert.
Steps:
1. Ordne die Regeln aus members/scoville-workflow-for-codex/scoville-workflow-for-codex/SKILL.md und references/operations.md desselben Pakets den Phasen und übergreifenden Invarianten zu. Erfasse Querabhängigkeiten einschließlich Projektionserholung, Checkpoints und Wiederaufnahme; vergleiche gegen die W-021-Anweisungen.
2. Teile den Operationsvertrag an diesen Verantwortungsgrenzen in kurze Phasenreferenzen auf und ersetze die Volllektürepflicht im SKILL.md durch eine eindeutige Lesetabelle. Behalte nur phasenübergreifende Regeln im Pflichtkern; aktualisiere suite.json und alle betroffenen Verweise ohne doppelte Regelpflege.
3. Passe members/scoville-workflow-for-codex/development/tests/test_contract.py und betroffene Paketprüfungen an. Prüfe normale und fehlerhafte Phasenwechsel gegen den bisherigen Vertrag und baue das private Paket neu; eine geringere Textmenge allein gilt nicht als Verhaltensnachweis.
Evidence: [12 Phasenreferenzen mit Pflichtkern und Lesetabelle; vollständiger Absatzvergleich gegen W-021 ohne Regelverlust, 46 Workflow-Vertragstests bestehen nach Anpassung an Phasenowner und bereits bestehenden W-019-Recoveryvertrag, Privater Build temp/2026-09-21-workflow-context-fix/w022 besteht Paketabgleich; installierte Skills unverändert]

### W-023 Phase 3: Wiederholtes Erzeugen und Lesen mit klaren Wiederaufnahmeregeln verhindern

Status: done
Depends on: [W-022]
Blocked by: []
Decisions: []
Outcome: Der Skill verwendet unveränderte Payloads und bereits vollständig verfügbare Phasenregeln wieder, ohne nach Kontextverlust auf fehlendes Wissen zu vertrauen oder unbekannte Zustellungen zu wiederholen.
Acceptance: Normaler Ablauf erzeugt keinen identischen Dispatch erneut und lädt unveränderte vollständig verfügbare Phasenregeln nicht erneut. Kontextverlust oder Compaction verlangt die aktuell benötigten Regeln; eine frühere Gelesen-Markierung genügt nicht. Geänderte Quellen und unvollständige Reads lösen gezieltes Nachladen aus. Wiederaufnahme verwendet erhaltene Identitäts-/Versandbelege und erfindet keinen Zustellstatus. Fokussierte Terra-Medium-Fälle gegen den privaten Build prüfen Routing und Wiederaufnahme mit vorab festgelegten Soll-Ergebnissen und unabhängiger Autorenprüfung. Vergleichbare deterministische Abläufe belegen weniger unnötige Ausgaben ohne verlorene Pflichten; Zeichen- und Tokenmessungen bleiben getrennt. Thresholds 33/66 und Pollingregeln bleiben unverändert.
Steps:
1. Ergänze im Pflichtkern und den in W-022 entstandenen Phasenreferenzen knappe Regeln für Payload-Wiederverwendung, abgeschnittene Anzeige, verfügbare unveränderte Regeltexte, Quellenänderung und Kontextverlust. Nutze den W-021-Datenweg; erzeuge kein zweites Zustellungsjournal oder paralleles Regelregister.
2. Ergänze fokussierte Fälle für unveränderten Ablauf, verkürzte Anzeige, geänderte Eingaben, fehlenden Payload, unbekannten Versandstatus und Compaction in den bestehenden Workflow-Tests. Vergleiche Builder-Aufrufe und tatsächlich ausgegebene Inhalte mit dem W-020-Duplikationsbefund; behaupte keine Tokenersparnis allein aus Zeichenlängen.
3. Baue das private Paket und teste nur die betroffenen Routing-/Wiederaufnahmefälle mit gpt-5.6-terra und medium über das bestehende isolierte Codex-CLI-Verfahren unter development/luna-tests. Halte feste Soll-Ergebnisse vorab fest und bestätige tatsächliches Modell, Effort, Paket-Hashes sowie Autorenbewertung; keine Wiederholung aller 64 Fälle und keine Installation während laufender DIVI5-Arbeit. Die Terra-Auswahl gilt nur für diesen Fix-Test und ändert nicht die allgemeine Veröffentlichungssperre.
Evidence: [development/workflow-context-fix.md: 61 deterministische Workflow-Tests und 16 CLI-Tests bestanden, Drei Terra-Medium-Fälle mit 15 Varianten und gezielter Ergänzung decken Routing und Wiederaufnahme ab; alle neun nativen Modell-/Effort-Kontexte bestätigt, Privater final-Build mit Receipt e185f88b955a003e4e704fb27faafe87ddfe02841bea24533cf95b1981ebd4e1 verifiziert; keine Live-Installation, Testweg in development/luna-tests/workflow-context-execution.md; 33/66 und Polling unverändert; W-009 bleibt pausiert]

### W-024 WordPress-Backend-Skill in die Scoville Suite integrieren und mit fünf Aufgaben testen

Status: done
Depends on: []
Blocked by: []
Decisions: []
Outcome: scoville-wordpress-ui-backend-anti-ai-slop ist ein einheitliches Suite-Mitglied mit eigenständigem Build und geprüftem Routing sowie Skill-Verständnis.
Acceptance: Quellen, Manifest, generierte Familienverweise und Suite-README enthalten das neue Mitglied ohne manuell duplizierte Familienlisten. Andere Skill-Namen und Links bleiben unverändert; Workflow bleibt im Suite-README zuerst. Fünf unterschiedliche Aufgaben am gebauten Paket bestehen unter SOL-Medium-Koordination mit LUNA Medium als Ausführer; tatsächliches Modell, Effort, Paket-Hashes und unabhängige Autorenprüfung sind belegt. Fehler werden korrigiert und betroffene Fälle wiederholt; keine ungeprüfte Veröffentlichung.
Steps:
1. Ermittle die maßgebliche Quelle von benjaminstelzer/wordpress-backend-ui-skill und sichere vorhandene Änderungen und Historie beim Import nach members/scoville-wordpress-ui-backend-anti-ai-slop/. Vereinheitliche Skill-Identität und interne Verweise; die Umbenennung dieses GitHub-Repositories ist erlaubt, die anderer Repositories nicht. Aktualisiere bei Umbenennung die kanonischen Links statt auf Weiterleitungen zu vertrauen.
2. Integriere das Mitglied in suite.json, Build-Exporte und generierte Family-Tags; ersetze seine bisherige externe Nachbarrolle. Verfasse unter development/readme/ eine Beschreibung nach dem Muster von scoville-ui-anti-ai-slop, spezialisiert auf plugin-eigene WordPress-wp-admin-Oberflächen und in Benjamins Ton. Nutze gemeinsame README-Bausteine und suite.descriptions für das Gesamt-README.
3. Prüfe betroffene Routing-Verweise und Buildverträge; erzeuge alle lokalen Suite-Pakete in einem neuen externen Buildordner und validiere sie mit development/build_suite.py --check-packages. Überschreibe weder installierte Skills noch bestehende Checkouts.
4. Erstelle vor Testbeginn fünf zunehmend anspruchsvolle Aufgaben mit getrennt gehaltenen Soll-Ergebnissen nach development/luna-tests/codex-cli-execution.md. Decke einfache Backend-UI, komplexe Zustände, Accessibility/Internationalisierung, Abgrenzung zu allgemeiner UI und Ablehnung nicht unterstützter Frontend-/Editor-Flächen ab. Prüfe Routing, Regelanwendung und Verständnis; fünf verschiedene Fälle statt identischer Wiederholungen.
5. [execute: model=gpt-5.6-sol; reasoning=medium] Koordiniere und bewerte die fünf isolierten Codex-CLI-Läufe mit gpt-5.6-luna / medium gegen das gebaute Paket. Halte Soll-Ergebnisse vor dem Ausführer verborgen; bestätige Modell, Effort und Paket-Hashes aus Laufbelegen. Bei fehlendem Modellzugriff stoppen, nicht substituieren; kein erneuter vollständiger 64-Fälle-Test.
6. Prüfe als Testautor die Ergebnisse unabhängig und dokumentiere Fälle, Befunde, Korrekturen und Wiederholungen knapp unter development/luna-tests/. Rohdaten bleiben in Workspace-temp; halte den exakt wiederholbaren Testaufruf und das getestete Paket fest. Bestehende UI-Ausschlusstests gelten nicht als Verständnistest dieses WordPress-Skills.
7. Vergleiche nach bestandenen Tests README, Beschreibung und öffentliche Texte mit den übrigen Suite-Mitgliedern und korrigiere Abweichungen an den Fragment-Ownern. Aktualisiere das GitHub-Profil benjaminstelzer mit Scoville Family oben und Ask Family darunter; entferne den separaten WordPress-Skills-Punkt und führe den Skill unter Scoville. Bewahre andere Profileinträge und prüfe veröffentlichte Links.
Evidence: [development/wordpress-suite-integration.md belegt Import sowie Build und Präsentationsabgleich, build-r1 mit zehn Paketen und 189 Dateien verifiziert; fünf Buildtests und 16 CLI-Tests bestanden, Fünf LUNA-Medium-Fälle unter SOL Medium bestanden und unabhängig bestätigt; wordpress-sol-results.md, Spacing-Fokus wp-01 und wp-02 bestanden; elf native Modellkontexte und 19 Referenzlieferungen geprüft, Profil f9a915c3da5ad020b1004b31c986678cc0339089 live verifiziert; endgültige Ziel-Links im Releaseentwurf vorbereitet, Keine Installation oder Skill-Veröffentlichung; W-009 bleibt pausiert]

### W-025 Autorisierten Suite-Release mit Beta-Workflow veröffentlichen

Status: in_progress
Depends on: []
Blocked by: []
Decisions: [ADR-0009, ADR-0010]
Outcome: Beide Suites und ihre Einzelpakete sind veröffentlicht; Workflow ist ausschließlich in der Suite als Beta verfügbar und Scoville Plan behält seine Viewer-Downloads.
Acceptance: Finale Pakete erfüllen das Luna-Gate und entsprechen den Remote-Dateien. Beide Suite-Quellen bauen ohne privaten Nachbarordner. Je autorisiertem Releaseziel verbleiben ein aktuelles Release und ein Release-Versionstag; operative Tags bleiben erhalten. Plan-Viewer-Assets entsprechen Buildmatrix und README mit belegter Herkunft und Hashes. Profil und Installationslinks zeigen auf erreichbare Ziele. Fehlende Nachfolger verhindern Bereinigung.
Steps:
1. Prüfe vorhandene Luna-Evidenz gegen aktuelle Laufzeitdateien und ergänze nur betroffene Fälle unter SOL Medium mit Luna Medium. Übernehme WordPress nach ADR-0010 und die ausdrücklich testbefreite Astra-high-Änderung mit belegter Bytezuordnung.
2. Ergänze generierte gemeinsame Build-Dateien in beiden Suite-Quellen, ohne den kanonischen Owner ../shared aufzugeben. Prüfe isolierte Builds, Beta-Projektion, README-Ziele und Paketgrenzen; bereite saubere geprüfte Quellcommits und finale Pakete unter skills/public vor.
3. Prüfe die Live-Releases und Tags aller autorisierten Ziele. Wende die GitHub-Verträge references/release-and-publication.md und references/suite-build-publication.md an. Prüfe Plan-Viewer-Assets gegen Buildmatrix, README, Herkunft und SHA-256.
4. Veröffentliche die beiden Suites und 14 Einzelpakete ohne separates Workflow-Repo. Bewahre Historien, benenne das WordPress-Ziel wie autorisiert um und prüfe komplette Remote-Bestände. Verifiziere neue Releases und Asset-Nachfolger vor dem Entfernen abgedeckter älterer Releases und Release-Versionstags.
5. Veröffentliche E:/Dropbox/AI Projects/projects/BenjaminStelzer/README.md mit Scoville oben und Ask darunter; prüfe finale Installationslinks, Topics, Releases und Tags. Historische Belege bleiben unverändert.
Evidence: [Plan-Viewer-Asset-Gate in der kanonischen GitHub-Skill-Quelle ergänzt, 37 gemeinsame sowie 21 Scoville- und acht Ask-Tests bestanden; lokale Quellen committed, Vollständige Suite-Exporte unter temp/2026-09-22-suite-release/r2 isoliert geprüft; öffentliche Pakete unter skills/public/release-2026-09-22 verifiziert, SOL führt fünf feste Workflow-Fälle mit Luna Medium gegen unveränderte öffentliche Buildpakete aus, development/release-preflight.md belegt Workflow und WordPress sowie Handoff/UI; Code-Nachtest besteht; Design-Nachtest und Plan-Gate laufen, Isolierte r4-Builds liefern 238 bytegleiche Paketdateien; 38 gemeinsame Tests bestehen; Viewer-Dateien entsprechen elf CI-Artefakten, RELEASE-HISTORY: Entscheidung zum Nachtragen sieben belegter veröffentlichter Versionen angefragt; keine Remote-Mutation]
Next action: Finale Quellcommits und öffentliche Pakete erstellen; Laufzeitdateien der bestandenen Luna-Fälle exakt zuordnen. Danach Remote-Bestände und Releases veröffentlichen. Der Workflow-Nachtest ist bestanden; sieben belegte historische Changelog-Einträge sind ergänzt. Nachweise stehen in development/luna-tests/workflow-archive-results.md und development/release-preflight.md.

### W-029 Deferred after W-025: Release-Ablauf wiederverwendbar automatisieren

Status: todo
Depends on: [W-025]
Blocked by: []
Decisions: []
Outcome: Ein gemeinsames Release-Script führt den belegten Suite-Ablauf mit überprüfbarer Wiederaufnahme aus; der GitHub-Skill nennt den genauen Aufruf.
Acceptance: Tests belegen frische und unterbrochene Läufe ohne doppelte Veröffentlichung sowie Ablehnung geänderter Eingaben und fehlender Gates. Remote-Dateien und Plan-Viewer-Assets werden vor Bereinigung geprüft. Dokumentierte Befehle decken Start, Status, Wiederaufnahme und Fehlerfälle ab; gespeicherte Zustände ersetzen keine frische Remote-Prüfung oder Freigabe.
Steps:
1. Überführe den tatsächlich geprüften W-025-Ablauf in ../shared/build/ mit festen Eingaben für Quellen, Pakete, Versionen, Ziele, Autorisierung und Testbelege. Bewahre Versionshistorien und eigenständige Pakete.
2. Implementiere nachvollziehbare Schritte für Buildprüfung, Veröffentlichung, Remote-Verifikation und nachgelagerte Release-Bereinigung. Speichere bestätigte Ergebnisse mit Eingabehashes; gleiche unbekannte Ergebnisse vor Wiederaufnahme mit GitHub ab. Bewahre fremde Drafts und operative Tags.
3. Teste Unterbrechungen vor und nach externen Änderungen sowie fehlende Assets, Drift und mehrdeutige Remote-Ergebnisse ohne Live-Schreibzugriffe. Dokumentiere den belegten Aufruf und passe den kanonischen GitHub-Skill an; synchronisiere gemeinsame Suite-Kopien.
Evidence: []
Next action: Nach W-025 dessen verifizierte Release-Schritte und Eingaben für den gemeinsamen Ablauf übernehmen.

### W-026 Entwicklungslinks nach README-Ziel generieren

Status: done
Depends on: []
Blocked by: []
Decisions: []
Outcome: Suite-READMEs enthalten einen gemeinsamen kompakten Entwicklungsblock. Einzelpakete enthalten weder diesen Block noch Entwicklungsdateien oder unerfüllbare lokale Dateiverweise.
Acceptance: Beide Suites bauen mit zielabhängigen README-Bausteinen. Entwicklungslinks entstehen aus suite.json und zeigen auf vorhandene Suite-Quellen. Tests belegen fehlende Entwicklungsblöcke in allen Einzelpaketen sowie Buildabbrüche bei ungültigen lokalen Links und ausgeschlossenen Dateien. Skill-Laufzeitdateien bleiben unverändert.
Steps:
1. Ergänze ../shared/build/build_suite.py und ../shared/readme/ um zielabhängige Bausteine und kompakte Entwicklungslinks aus den Mitgliedsmetadaten beider suite.json-Dateien. Bewahre die templatebasierten Ask-Quellen ohne zusätzliche Mitgliedskopien.
2. Entferne aktuelle Entwicklungslinks aus Release-Bausteinen und korrigiere betroffene Paketverweise. Ergänze im gemeinsamen Builder eine Prüfung lokaler Markdown-Dateilinks gegen das tatsächliche Paket und dokumentiere die Pflege in ../shared/build/fragments.md.
3. Teste beide Ausgabeziele und Fehlerpfade unter ../shared/tests. Erzeuge Suite-Vorschauen und isolierte Builds beider Suites, prüfe Paketbestand und unveränderte Laufzeitdateien. Keine Installation oder Veröffentlichung.
Evidence: [development/readme-build-targets.md: 26 fokussierte Tests bestanden und beide README-Projektionen aktuell, 15 Pakete gebaut; 223 Nicht-README-Dateien unverändert; keine Installation oder Veröffentlichung]

### W-027 README-Sprachaudit und verbleibende Entwicklungsbeschreibungen abschließen

Status: done
Depends on: [W-026]
Blocked by: []
Decisions: []
Outcome: Aktuelle README-Texte beider Suites sind knapp und verständlich in Benjamins Ton und beschreiben die gemeinsame Quellbasis korrekt.
Acceptance: Aktive README-Bausteine und verbleibende aktuelle Entwicklungs-READMEs sind geprüft. Redundanzen und veraltete Beschreibungen sind an ihren Quellen korrigiert. Einschränkungen und historische Belege bleiben korrekt. Generierte READMEs und Pakete bestehen die W-026-Prüfungen ohne Laufzeitänderungen.
Steps:
1. Prüfe die bereits festgestellten Textbefunde in development/readme/scoville-plan/ und development/readme/scoville-workflow-codex/. Kürze interne Regelwiederholungen und aktualisiere die Workflow-Beschreibung auf Pflichtkern und Phasenreferenzen ohne stärkere Testbehauptungen.
2. Prüfe die aktiven Fragmente aus beiden suite.json-Dateien sowie die aktuellen Suite-Einstiege und Entwicklungsbeschreibungen. Kläre Ask-Auswahl und Hostgrenzen aus den Quellen; erhalte gute trockene Formulierungen ohne erzwungene Witze. Historische Importtexte bleiben unverändert.
3. Regeneriere README-Vorschauen und isolierte Pakete. Prüfe Textfakten und Zielgruppen sowie Buildtests und unveränderte Laufzeitdateien; veröffentliche nichts.
Evidence: [development/readme-style-audit.md dokumentiert Stilprüfung und Quellenkorrekturen, 26 README- und Buildtests bestanden; 15 Pakete verifiziert; 223 Nicht-README-Dateien unverändert, Keine Installation oder Veröffentlichung]

### W-028 Lokale Skills aktualisieren und DIVI5 sicher fortsetzen

Status: done
Depends on: []
Blocked by: []
Decisions: []
Outcome: Codex und Claude verwenden die aktuellen kompatiblen Skill-Builds; DIVI5 läuft unter einem neuen Koordinator weiter.
Acceptance: Sicherer Stopp ohne aktive Kinder belegt; Altinstallationen wiederherstellbar gesichert; alter WordPress-Skill entfernt; installierte Dateien gegen Builds geprüft und persönliche Konfiguration erhalten; bestehende DIVI5-Übergabe aktiviert genau einen Nachfolger.
Steps:
1. Bestätige den sicheren DIVI5-Stopp am bestehenden Guard ohne zweite Übergabekette.
2. Sichere die betroffenen Installationen außerhalb der Skill-Verzeichnisse. Installiere die lokalen Suite-Builds in Codex und kompatible Skills in Claude sowie die gepflegten privaten GitHub- und Voice-Skills; bewahre persönliche Konfiguration und fremde Skills.
3. Prüfe Paketdateien und lasse den bisherigen Guard-Eigentümer die bestehende Übergabe mit dem neuen Workflow abschließen. Verifiziere Nachfolger und Fortsetzung; kehre danach zu W-025 zurück.
Evidence: [development/local-skill-update.md: 17 Codex- und 11 Claude-Installationen verifiziert; Sicherungen und persönliche Konfiguration erhalten, G27 01a0c725-88d5-70e3-84e7-bdf9632feceb aktiv bei Guard Revision 329; G26-Turn abgeschlossen]
