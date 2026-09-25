# Geprüfter Review zur Scoville Suite, 2026-09-25

Grundlage ist das vom Nutzer bereitgestellte Dokument `scoville-fixplan-2026-09-25.md`. Geprüft wurde der tatsächliche Arbeitsbaum bei HEAD `890441e`, einschließlich zahlreicher bereits vorhandener Änderungen und neuer Member. HEAD allein beschreibt diesen Stand nicht. Bestandsplan-Status in diesem Bericht ist eine Momentaufnahme vor dem parallel gesondert beauftragten Abschlussaudit älterer Pläne. Dessen spätere Änderungen sind kein Ergebnis dieses Reviews. Dieser Bericht bewahrt die entscheidenden Ergebnisse, keine Rohprotokolle. Der ausführbare Arbeitsvorrat steht in [PLAN-0011](plans/0011-suite-review-fixes.md).

Der Nutzer bestätigt die im Review ausdrücklich erteilten Freigaben. Er beauftragt die Prüfung und Planung, verlangt eigene Empfehlungen und bestätigt die Richtung: unnötige Komplexität und SHA-256-Vorkehrungen bei Übergaben sollen entfallen. Persönliche Konfiguration muss im jeweiligen Skill-Ordner liegen. Jeder einzelne Befund einschließlich missverständlicher Sprache ist ernsthaft zu prüfen. Der Nutzer priorisiert Einfachheit ausdrücklich vor Absicherung theoretischer Modelländerungen während eines laufenden Auftrags. Im Review ausdrücklich offene Varianten bleiben Vorschläge. Diese Planerstellung führt keine Produkt-, Rechner-, Installations- oder Löschänderungen aus.

## Prüfmaßstab und tatsächliche Nachweise

Kanonische Quellen sind `members/`, `suite.json`, `development/readme/` und der Geschwisterordner `../shared/`. Kopien unter `development/shared/`, Member-READMEs und Pakete werden daraus erzeugt. Die Prüfung umfasst die behaupteten Stellen, ihre direkten Verträge und betroffenen Verbraucher, keine vollständige Sicherheits- oder Veröffentlichungsprüfung.

Unter Windows mit Python 3.14 tatsächlich ausgeführt:

| Prüfung | Ergebnis |
| --- | --- |
| `py -3.14 -B -m unittest discover -s members/scoville-plan/development/tests -p 'test_*.py'` | 78 bestanden |
| Entsprechender Befehl für `members/scoville-ask-for-codex/development/tests` | 17 bestanden |
| Entsprechender Befehl für `members/scoville-workflow-for-codex/development/tests` | 90 bestanden |
| Installierter Plan-Validator gegen die Suite vor neuen Records | gültig; 7 Pläne, 70 Work Items, 22 Decisions |
| `task_lifecycle.py`, Operation `task_title`, Titel mit CJK und Umlaut, `PYTHONIOENCODING=cp1252` | echter `UnicodeEncodeError` in stdout reproduziert |
| Reales `resolve_model_pair.resolve` mit kontrollierter Konfiguration: Startpaar danach aus Tabelle entfernt, Reparatur 2 | `original launched pair is outside the WORK route table` reproduziert |

Bei den Testprozessen war zusätzlich `PYTHONDONTWRITEBYTECODE=1` gesetzt, auch für Kindprozesse. Keine dauerhafte Benutzervariable wurde verändert. Der erste Versuch, eine unbearbeitete Workflow-TOML-Vorlage direkt zu laden, scheiterte erwartbar am Include; das ist kein Produktfehler. Die Eskalationsreproduktion verwendet deshalb kontrollierte Eingaben am echten Resolver.

Nicht ausgeführt: Python 3.10, Linux/macOS, reale Adviser, Netzabflussversuch, echte WordPress-7.2-Oberfläche, Installation/Update, Dropbox-Attribute, Veröffentlichung und neue Modellvergleiche. Grüne Helper-Tests ersetzen diese Nachweise nicht. Die hier verfügbare `create_thread`-Schnittstelle enthält keinen Sandbox- oder Freigabeparameter; das ist eine Aussage über den aktuellen Hostvertrag, nicht über alle Codex-Versionen.

## Einzelprüfung aller 28 Punkte

### F-01: Python 3.10 blockiert Plan-Schreiben — bestätigt, P1

`members/scoville-plan/scoville-plan/references/native-editing.md` verlangt auch in general den Resolver und verbietet bei altem Python den manuellen Weg. `../shared/runtime/resolve_prompt_profile.py::read_config` benötigt tomllib. Die widersprüchliche Aussage zum optionalen Executable steht tatsächlich daneben. Kein Python-3.10-Lauf wurde durchgeführt; die Versionsgrenze ist aus Quelle und Vertrag eindeutig.

Empfehlung: general darf bei ungeeignetem Python die bestehende manuelle Profilroute verwenden; Konfigurations- und Helperfehler bei geeignetem Python bleiben Fehler. codex bleibt 3.11+. Keinen eigenen TOML-Parser schreiben. Der Nutzer verlangt inzwischen ausdrücklich einen deutlich einfacheren Plan-Skill. Empfohlen ist die Entfernung der Plan-Profilauswahl unter gezielter Ablösung des betreffenden ADR-0014-Anteils. Wenn dieser Umbau zuerst erfolgt, entfällt der separate Python-Fallback-Fix. Der berichtete Testfehler 77/78 entstand aus dem unvollständigen Review-Checkout; aktuell 78/78. Debian 11 wird im Review unzutreffend als typisches Python-3.10-System angeführt; diese Verteilungsbehauptung ist für den Fix unnötig.

### F-02: Verschachtelte Markdown-Blöcke — bestätigt als Formatrisiko, P1

`members/scoville-handoff/scoville-handoff/assets/continuation-prompt.md` hat einen äußeren Dreier-Fence. Ein innerer Dreier-Fence kann ihn schließen. Vier Backticks sind nur für Inhalte mit maximal drei ausreichend.

Fix: äußerer Fence länger als jede innere Backtick-Folge; Vorlage mindestens vier. Prüfen mit inneren Dreier- und Vierer-Fences und vollständigem kopierbarem Inhalt. Kein P0-Sicherheitsvorfall und noch kein beobachteter Modellfehler. PLAN-0009 enthält bereits die allgemeine Handoff-Überarbeitung; hier nur diese zusätzliche Regression beheben.

### F-03: WordPress ab 7.2 — Befund richtig, vorgeschlagener Fix zu breit, P2

`members/scoville-ui/scoville-ui/references/wordpress/version-compatibility.md` beschränkt das Beispiel ausdrücklich auf stabile 7.0.x/7.1.x und verlangt neue Prüfung außerhalb dieser Matrix. Die Regex führt auf 7.2 tatsächlich zum Zahlenpfad. Das Dokument behauptet dafür aber keine Unterstützung.

Empfehlung: unbekannte Minor-Version in Beispiel und Ergebnismatrix ausdrücklich als ungeprüft behandeln; keine erfolgreiche Abnahme des Fallbacks. Kein pauschales `>= 7.1`: ein registrierter Handle beweist weder Herkunft noch vorhandene Tokens. Erst nach realem Versions-/Token-Nachweis erweitern. Prüfen: 7.0, 7.1, 7.2, Prerelease, fehlender Handle und fremde Registrierung. Keine Behauptung eines tatsächlich beobachteten 7.2-UI-Defekts.

### F-04: Native Adviser ohne technische Schreibsperre — bestätigt mit Einschränkung, P1

`../shared/runtime/task_lifecycle.py::create` erzeugt lokale Tasks; `references/adviser.md` im Ask-Paket erklärt bereits ausdrücklich, dass keine Sandbox entsteht. Der aktuelle Host bietet den vorgeschlagenen Sandboxparameter nicht an. Read-only ist hier ein Verhaltensvertrag.

Empfehlung: Grenze im Einstieg/README klar benennen; keine neue Hash-Schnappschussmaschine als vermeintlichen Ersatz. Vorher/Nachher-Diffs verhindern keine Schreibvorgänge, können parallele Nutzeränderungen nicht dem Adviser zuordnen und erkennen zurückgenommene Zwischenänderungen nicht. Bei zwingender Isolation einen tatsächlich beschränkten Ausführungspfad verlangen. Optionaler Änderungsbericht darf nur eine Beobachtung heißen. Keine Scheinsicherheit und kein automatisches Zurücksetzen.

### F-05: Read plus Web-Tools — Fähigkeit bestätigt, Exploit nicht nachgewiesen, P1

`scripts/ask_claude.py::READ_ONLY_TOOLS` erlaubt Read/Grep/Glob/WebSearch/WebFetch mit dontAsk. `references/claude.md` erklärt Netzkommunikation schon heute. Daraus folgt ein zusätzlicher Abflusskanal, aber kein hier nachgewiesener erfolgreicher Angriff.

Empfehlung: `claude.web_tools=false` als Default; expliziter Opt-in. Teste Default, Opt-in, Rangfolge und ungültige Werte. Die Modellkommunikation mit Claude bleibt bestehen; weder offline noch vollständige Datenisolation behaupten.

### F-06: Kein CLI-Standardtimeout — bestätigt, P1

`scripts/ask.py::claude` verwendet `request.get('timeout_seconds')`, also standardmäßig None. TimeoutExpired wird in main bereits aufgefangen; der Fehlerpfad fehlt nicht vollständig.

Fix: konfigurierbarer Default von 1800 Sekunden, stabiler Fehlercode `claude_timeout`, kein Retry. Prüfe mit kurz laufendem Fake-Prozess, dass Timeout und Prozessende beobachtet werden; auf Windows auch Wrapper/Kindprozess berücksichtigen. Ein Unit-Mock allein beweist keine Prozessbereinigung.

### F-07: Lokale Pfade und Retention — bestätigt, P1

Die genannten Pfade existieren, unter anderem in Code `development/astra-acceptance-2026-09-12.md`, Plan `development/skillwriter-implementation.md` und Ask `development/test-evidence.md`. Ob jede Datei öffentlich ist oder ein Release sie bindend verlinkt, wurde nicht extern geprüft.

Empfehlung: knappe kanonische Entscheidungen, Pläne und Ergebniszusammenfassungen behalten; rohe Reviewpakete und Transkripte gemäß Retention entfernen. Nicht sämtliche Development-Dokumente ohne Release-Link löschen: Projektwissen ist kein Rohprotokoll. Private Maschinenpfade in veränderlichen Berichten durch brauchbare relative Verweise ersetzen. Terminale Plan-/ADR-Historie nicht beiläufig umschreiben. Veröffentlichungsausgabe mit Ausnahmeliste prüfen, keine pauschale Nulltrefferregel für legitime Pfadbeispiele.

### F-08: Installation und Reponamen — teilweise bestätigt, Entscheidung bereits vorhanden, P1

Ask-README behauptet noch „Partial installation is not supported“, während `suite.json` und die bestandenen Buildtests Standalone erlauben. ADR-0042 hat die Einzelinstallation bereits angenommen. Dafür ist keine neue Nutzerentscheidung nötig.

Fix am kanonischen README-Fragment/Builder. Zwei Repos sind wegen general/codex in ADR-0013 beabsichtigt; nicht blind vereinheitlichen. `members/` bezeichnet Quellen, `packages/` installierbare Pakete. Links gegen ihre jeweilige Distribution prüfen. Reiner Claude-CLI-Pfad benötigt keinen nativen Modellkatalog, bleibt aber eine Nutzung des Codex-Skills und ist nicht offline.

### F-09: UI-Merge — teilweise veraltet, bestehender Besitzer bleibt PLAN-0006

Die alten UI-Quellordner sind im aktuellen Arbeitsbaum bereits weg; Git zeigt ihre Löschungen. `development/ui-evaluation-results.md` enthält inzwischen echte Classic-/React-Interaktionen an Fixtures. Daraus folgt noch kein erfolgreicher Kandidaten-Implementierungsvergleich. PLAN-0006/W-006 ist weiterhin in_progress mit TEST-POLICY.

Die fehlenden Greenfield-/Änderungsnachweise im bestehenden Plan fortsetzen, keine zweite Merge-Aufgabe anlegen. ADR-0044 begrenzte den früheren Lauf ausdrücklich; die alte Zeitfreigabe ist kein unbegrenztes Budget. Vorhandene `development/luna-tests/ui-cases.md` und WordPress-Fälle nutzen. Eine zusätzliche JSON-Datei oder exakt zwölf Fälle sind keine eigenständige Qualitätsgarantie.

### F-10: Ask-Altsource — bestätigt, P1

`../ask-suite-for-codex` existiert weiterhin. `members/scoville-ask-for-codex/development/test-evidence.md` dokumentiert Backup und ausstehende Entfernung. Die 437-Dateien-Angabe wurde hier nicht erneut byteweise geprüft.

Fix: bei Umsetzung Backup und seitdem mögliche Änderungen prüfen, aktive Leser ausschließen, exakten Zielpfad kontrollieren, nur die alte Quelle entfernen. Die mit dem Dokument bestätigte Freigabe bleibt erhalten. Nicht durch einen anderen Löschweg eine erneute Tool-Policy-Sperre umgehen.

### F-11: Handoff-Arbeitsverzeichnis — teilweise bestätigt, P2

Die Vorlage markiert optionale State-Felder nicht einzeln. SKILL.md fordert jedoch bereits anwendbare Fakten, erlaubt benannte Quellen und grenzt bloß zufälliges Host-CWD ab. PLAN-0009 enthält bereits getestete Korrekturen für Gesprächsfakten und Aufgabenorte.

Fix nur für verbleibende Unklarheit: tatsächlich benutzten Repo-Ort als belegte Aufgabeninformation übernehmen; unbekannter Aufgabenort bleibt unknown. Pflichtfelder aus dem bestehenden Vertrag ableiten, keine neuen Pflichtlabels allein nach Reviewvorschlag erfinden. Fall mit bekanntem Task-Repo und abweichendem Host-CWD.

### F-12: Frontmatter und Hostaussagen — bestätigt, P2

Ask und Workflow haben kein compatibility-Feld. Workflow-README nennt Antigravity, obwohl die Ausführung Codex-spezifisch ist. Gleiche Frontmatter-Schlüssel für alle Skills sind keine belegte Anforderung; vorhandene quick_validate-Versionen lehnen compatibility bei anderen Membern gerade ab.

Empfehlung: Aussagen pro Skill sachlich richtig machen, unterstützte und tatsächlich getestete Hosts trennen. Metadaten nur gemäß geklärtem Paketformat ergänzen. Nicht Antigravity pauschal überall hinzufügen oder einen Validator für einen grünen Check verbiegen.

### F-13: Leichter Planweg — sinnvoll, P2, durch Vereinfachungsrichtung gedeckt

P/W/E werden für gewöhnliche Work-Item-Änderungen umfangreich geladen. `native-editing.md` verlangt aber vollständige Mehrdatei-Vorbereitung bereits nur für tatsächlich mehrteilige Änderungen; nicht jede Einzeldatei-Änderung ist heute eine Mehrdatei-Transaktion.

Fix: operationengenaue Lektüre und kurzer Einzeldateiweg mit erneutem Lesen, kontextgebundenem Patch, Diff und Validator. Mehrdatei-Konsistenz bleibt auch für Decision-Übergänge und andere betroffene Beziehungen nötig, nicht nur Aktivierung/Abschluss. Kosten vorher/nachher messen, keine willkürliche 50-Prozent-Abnahme.

### F-14: Evidence mit Komma — bestätigt, P2

`native-plan-format.md` verbietet Kommas/Klammern; `validate_profile.py` parst Inline-Listen durch Trennung an `, `. Das ist ein bewusst enger Vertrag, kein Parserfehler.

Empfehlung: nur Evidence um sauber gequotete/escapte Einträge erweitern, alte Einträge erhalten. Validator, Selector, Decision-Batch-Helper soweit betroffen, manuelle Route und Viewer gemeinsam prüfen. Alte Leser könnten neue Form nicht verstehen; Lesekompatibilität des neuen Readers ist keine beidseitige Kompatibilität. Versions-/Upgradeentscheidung vor Umsetzung.

### F-15: SHA-256 und Guards — unnötigen Aufwand entfernen, pauschalen Ersatz ablehnen, P1

Die genannten Bindungen existieren. Git zeigt Änderungen, verhindert aber weder verlorene Updates noch stale Writer. mtime/Änderungszähler sind ohne vollständigen Schreibbesitz kein gleichwertiger Ersatz für Inhaltsvergleich. Ein Worker-Echo von Scope beweist keine vollständige Promptübertragung.

Beschlossen ist die Vereinfachungsrichtung. Entfernen: vom Modell kopierte/verglichene Hashes, Bytezahlen, Übergabebelege und doppelte Integritätsnachweise. Übergabeprompt direkt als Helper-Ergebnis übergeben. Plan schreibt nach Lesen kontextgebunden; keine Modell-Hashpflicht. Decision-Batches vorzugsweise mit einfacher ID und bestehender Mitgliederliste, statt Batchfunktion zu streichen. Build-/Release-Identität und Backup-Prüfung getrennt beurteilen; sie sind keine Übergabezeremonie. Unsalted Signaturhash ist keine Authentisierung. Der Nutzer legt mit ADR-0052 ausdrücklich Einzelbetrieb fest: keine zusätzliche technische Absicherung gegen parallele Schreiber. Die README erklärt die Bedienregel und den bewusst entfallenen Konfliktschutz.

### F-16: Schreibprofile — Empfehlung zur Vereinfachung, offene Vertragsänderung, P2

Resolver und Imports sind bestätigt; ADR-0014 hat gemeinsame, getrennt konfigurierbare Profile ausdrücklich beschlossen. „Kein Nutzen belegt“ ist kein Nachweis der Nutzlosigkeit.

Empfehlung: Plan verwendet eine kompakte vollständige Schreibregel ohne Modellresolver. Workflow profiliert nur optionale Zusatzanweisungen, falls ein Vergleich einen praktischen Vorteil zeigt. Die konkrete Ausgestaltung bleibt ADR-0048; bei Umsetzung ADR-0014 gezielt ersetzen und nicht still löschen. F-01 nur separat reparieren, wenn dieser kleine Fix tatsächlich vor dem Wegfall des Resolvers benötigt wird.

### F-17: Plattformkompatibilität — konkrete Probleme bestätigt, P1

Ungequotete Pfade, nacktes python und fehlende UTF-8-Streamkonfiguration sind vorhanden. Der CJK-stdout-Fehler in `../shared/runtime/task_lifecycle.py` wurde reproduziert. Umlaute allein sind unter cp1252 häufig darstellbar und kein ausreichender Negativtest. CRLF wird in `validate_profile.py` ausdrücklich abgelehnt.

Fix: einmal geeigneten Interpreter auflösen, Pfade shellgerecht quoten, UTF-8 an tatsächlichen CLI-Grenzen festlegen. Gemeinsame Funktion nur bei mehreren echten Verbrauchern. CRLF-Toleranz braucht eine Formatentscheidung und muss source_text/Bytes, Hashverwendungen und Viewer berücksichtigen. Neue Dateien LF; bestehende Darstellung nicht beiläufig normalisieren. CI für drei Systeme sinnvoll, hier jedoch nur Windows beobachtet. Aktuelle Python-3.14-Defaults verdecken Altcodepage-Probleme teilweise.

### F-18: Workflow-Neuschnitt — Bedarf plausibel, Reviewentwurf nicht unverändert übernehmen, P1

Aktuelle Quellen: 5.459 Bytes SKILL.md, 120.200 Bytes Referenzen, 132.916 Bytes Skripte ohne Cache. Enthaltene Includes bedeuten, dass dies keine Startkontext- oder Tokenmessung ist. Die 90 Tests bestehen; „mehr Fehler als verhindert“ und 75 Prozent Kontextgewinn sind nicht belegt.

Empfehlung: aufrufender Task als Coordinator, direkter Dispatch, keine eigenen Prozent-Rolloverketten, kein Bundling als Default, Archivierungsfehler nicht abnahmeblockierend. Ein Worker und ein späterer Reviewer je Einheit, höchstens drei Reparaturen. Nur aktuelle Einheit, Task und Ergebnis als Arbeitsstand behalten. ADR-0052 schließt zusätzliche Konfliktprotokolle für parallele Bearbeitung aus; Einzelbetrieb wird dokumentierte Voraussetzung. Review per realem Diff, nicht allein changed_paths des Workers. Commit nur innerhalb bestehender Autorisierung.

Fünf vorhandene Routewerte zunächst kompatibel behalten; drei Default-Modellpaare können mehrere Routen abdecken. Ein explizites Modellergebnis nicht im Zuge der Kürzung ersetzen. Bestehenden Rollenresultatvertrag aus ADR-0036 zuerst behalten. Die Akzeptanz prüft neben dem Normalablauf Nutzerstopp und Wiederaufnahme sowie belegte reale Fehler aus der bisherigen Evaluation. Theoretische Randfälle rechtfertigen nicht automatisch zusätzliche Zustände oder Tests. Neuschnitt getrennt freigeben, aktive Runs nicht migrieren.

### F-19: Code-Router — teilweise bereits bearbeitet, kein erneuter Pauschalumbau

PLAN-0010 ist completed; die aktuelle Quelle und `development/skillwriter-fix-evidence.md` enthalten den jüngsten Umbau. Der Vorschlag „reine Klassifikation lädt nichts“ widerspricht im Review selbst „Structural/High lädt immer Change“.

Empfehlung: den aktuellen Stand als Ausgangspunkt nehmen und die benannten sprachlichen Probleme trotzdem erneut prüfen. Verdichtete Begriffe wie „Fixed labels alone trigger no sibling“ durch konkrete Alltagssprache ersetzen; Ausnahmen so ordnen, dass reine Klassifikation und der Risiko-Override zusammen eindeutig bleiben. Ein bestandener früherer Test erledigt Verständlichkeitskritik nicht. Kein pauschaler Neuumbau und keine 20-Prozent-Kürzung als Qualitätsmaßstab. Alte Review-Zeilenangaben sind nicht die aktuelle Quelle.

### F-20: UI-Router — bestätigt als Vereinfachungskandidat, P2

`scoville-ui/SKILL.md` enthält OWNERSHIP-/EVIDENCE-/SOURCE-Ausnahmen, `references/wordpress/routing.md` strukturierte Ausgabewerte. Herauslösen kann nützen.

Fix: Ausgabeformat nur bei angeforderter strukturierter Klassifikation laden; semantische Ausschlüsse und die Entscheidung, welche Referenz nötig ist, müssen vorher verfügbar bleiben. Sonderfälle dürfen nicht bloß in Tests verschwinden. Gleiche Routingantworten für reine Eigentumsfrage, Evidenzurteil, Quellaudit und echte Umsetzung prüfen. Keine starre 9-KB-Grenze.

### F-21: WordPress 6.x — kein bestehender Support, offene Produktwahl, P2

`references/wordpress/adapter.md` sagt ausdrücklich WordPress 7; „older supported“ ist innerhalb der dokumentierten 7.0/7.1-Matrix zu verstehen. 6.5 ist deshalb keine bereits versprochene Kompatibilität.

Empfehlung: Mindestversion und tatsächlich getestete Laufzeit getrennt nennen; 6.x zunächst außerhalb des Adapter-Supports lassen. Bei realem Bedarf eigene Classic-/Core-Components-Matrix freigeben. Kein stilles Aktivieren von 7.x-Tokens auf einem 6.5-Plugin.

### F-22: Greenfield-Fragen — wesentliche Regeln bereits vorhanden

`references/ui-quality.md` verlangt bereits eine Primäraktion pro Entscheidungsbereich, zweckgebundene Regionen und keine Dekoration ohne neue Beziehung. `framework-alignment.md` nennt mehr als nur „name a direction“.

Empfehlung: erst bestehenden Greenfield-Fall praktisch prüfen. Keine zehn ähnlichen Zusatzfragen. Nur eine tatsächlich beobachtete Lücke ergänzen, ohne eine visuelle Richtung durch pauschale Dekorationsverbote zu ersetzen. Besitzer bleibt PLAN-0006.

### F-23: Ask-Präfix und Wegfall der Sidebar-Platzierung — ausdrücklich entschieden

Das alte Verhalten war durch ADR-0042 festgelegt. Der Nutzer korrigiert erst die Reihenfolge zu `ASK <Titel der aufrufenden Aufgabe>` und streicht anschließend die automatische Sidebar-Platzierung zur Komplexitätsreduktion. ADR-0055 enthält den aktuellen Beschluss; ADR-0042 und die Zwischenentscheidung ADR-0054 bleiben als ersetzte Historie erhalten.

W-015 entfernt die Platzierungsoperation samt Aufrufern und Dokumentation vollständig, ohne Opt-in-Einstellung. Ask steht vorne, ohne Adviser-ID, Modellname oder Ask-TAsk-Suffix. Bestehende Aufgaben werden nicht umbenannt oder umsortiert. Task-IDs bleiben Identität; die normale Hostsortierung bestimmt die Position.

### F-24: Git-Zugriff über Bash — Fähigkeit fehlt, vorgeschlagene Freigabe nicht sicher read-only

Claude hat aktuell kein Bash. Git diff/log/show können abhängig von Argumenten und Konfiguration externe Diff-/Textconv-Programme, Pager oder Ausgabedateien verwenden. Toolpräfixe allein garantieren keine Schreibfreiheit.

Empfehlung: vorerst Diff gezielt vom Aufrufer bereitstellen. Nur bei belegtem Bedarf einen engen Adapter mit fester Argumentliste und deaktivierten externen Helfern entwickeln. Kein pauschales Bash(git …:*) als Sicherheitsgarantie einführen.

### F-25: Evaluation — Lücke enger als behauptet, P2

Es gibt bereits `development/luna-tests/run_codex_cli_case.py`, Fallkataloge, Ergebnisberichte und Code/Handoff-Vergleiche. Kein Runner überhaupt ist daher falsch. Ein universeller automatisierter gegeben/erwartet-Vergleich für alle Member ist damit noch nicht vorhanden.

Empfehlung: bestehenden Runner um Baseline/Kandidat/einfachen Prompt und passende Auswertung erweitern. Deterministische Kriterien programmatisch prüfen, Modellurteile nur für tatsächlich semantische Fragen. Gleiche Bedingungen und getrennte Schlussfälle, begrenzte Läufe, beobachtete Kosten. Ein einzelner Lauf mit Bewertungsmodell beweist keine generelle Überlegenheit. Kein neuer Pflicht-Großlauf für jede Wortkorrektur.

### F-26: Größenlimits — Messung sinnvoll, harte Grenzwerte unbegründet, P3

Dateiumfang ist messbar; Wachstum „mit jedem Release“ wurde nicht historisch vermessen. Tatsächlich geladene Referenzen sind relevanter als der gesamte Ordner.

Empfehlung: informative Ausgabe pro Member und pro häufiger Route, kein harter 10-/12-KB-Fehler. Akzeptanz folgt erhaltenem Verhalten und geringerem nachgewiesenem Aufwand. Ausnahmebürokratie würde dem Vereinfachungsziel entgegenwirken.

### F-27: Persönliche Modellkonfiguration — bestätigt, Ort vom Nutzer entschieden, P1

Workflow lädt nur `assets/workflow.toml`; Ask hat bereits `config.default.json` plus `config.json` im Skill-Ordner. Persönliche Datei neben Defaults zu haben beweist allerdings noch nicht, dass ein Installer sie bewahrt.

Entscheidung: je Skill im Installationsordner. Empfehlung: Ask behält `config.json`; Workflow bekommt `assets/workflow.local.toml`; falls Plan-Profile bleiben, `assets/prompting.local.toml`. Rangfolge Anfrage/Step, Projekt, persönliche Datei, Defaults. Distributionen liefern keine persönliche Datei aus; Updates erhalten sie ausdrücklich und scheitern sichtbar bei inkompatibler Konfiguration.

Reparatur 2/3 sucht das ursprüngliche Paar heute in der aktuellen Tabelle; Fehler reproduziert. Nur das Startpaar zu speichern würde den Spezialfall nicht lösen. Der Nutzer verzichtet dafür ausdrücklich auf zusätzliche Technik: Konfiguration zwischen Läufen ändern, während eines laufenden Auftrags unverändert lassen. Kein eingefrorener Reparaturfahrplan, kein Snapshot und keine zusätzliche Versionsbindung. Ein tatsächlich trotzdem geänderter ungültiger Zustand darf den vorhandenen klaren Fehler liefern. Modelle und gewünschtes Reasoning aus Konfiguration laden; gültige API-Werte und historische Testnachweise sind keine verbotenen persönlichen Defaults. Alte Berichte nicht umschreiben, nur um eine globale grep-Regel zu erfüllen.

### F-28: Dropbox — bestätigt, bereits autorisiert, P1

Cacheordner existieren in Ask, Workflow und im echten Geschwisterordner `../shared/`. Viewer node_modules/target sind derzeit nicht vorhanden. Die Root-.gitignore deckt Python-/Node-/Rust-Ausgaben bereits ab; fehlende Member-.gitignore allein ist kein Git-Fehler im Monorepo.

Bei Umsetzung die freigegebenen Rechnermaßnahmen ausführen: bestehendes PYTHONPYCACHEPREFIX prüfen, außerhalb Dropbox erhalten oder passende Benutzervariable setzen, nur benannte Cacheordner löschen, Viewer-Ausgaben vor ihrer Erzeugung ausnehmen, Dokumentation und -B-Befehle ergänzen. Nicht versehentlich nur `<suite>/shared` prüfen, denn der kanonische Besitzer liegt daneben. Dauerhafte Benutzer-Umgebungsvariablen werden von einem Kind eines schon laufenden Prozesses nicht automatisch neu eingelesen; Prüfung mit frisch übernommener Umgebung und nach Neustart unterscheiden. Ignore-Attribut nach npm ci prüfen, da Ordner neu erstellt werden können. Kein absoluter maschinenabhängiger Cargo-Pfad in versionierter Konfiguration.

## Priorität und offene Empfehlungen

Kein Befund wurde hier als aktiver P0-Vorfall reproduziert. Zuerst konkrete Ausführungsfehler und bereits freigegebene Arbeitsumgebung, dann Vereinfachung und Konfigurationsstabilität. Für Plan und Workflow sind weniger Komplexität, weniger Tokens und höhere Ausführungsgeschwindigkeit ausdrückliche Ziele. ADR-0052 hält die akzeptierte Abwägung fest: etwas weniger Fehlbedienungsschutz und dafür normaler Einzelbetrieb ohne parallele Bearbeitung oder laufende Modelländerung. Dies gehört in beide READMEs. Größere Änderungen brauchen keine willkürlichen Prozentziele, sondern gleichwertige Ergebnisse und gemessenen geringeren Aufwand.

| Entscheidung | Empfehlung | Status |
| --- | --- | --- |
| Übergabe-/Plan-Hashes und unnötige Komplexität | Modellbelege und Paralleländerungsabsicherung entfernen; einfachen Einzelbetrieb dokumentieren | angenommen: ADR-0045 und ADR-0052 |
| Persönliche Konfiguration | im jeweiligen Skill-Ordner, vom Update ausdrücklich bewahrt; Änderungen zwischen Läufen | angenommen: ADR-0046 |
| Gemeinsame Projektdatei | `.scoville/config.json` mit vorhandenen Ask-/Workflow-Strukturen; Skillwerte sind Defaults | Vorschlag ADR-0051 |
| Ask-Webzugriff | standardmäßig aus; keine zusätzliche Hash-Sandboxsimulation | Vorschlag ADR-0047 |
| Plan-Schreibprofile und alter Interpreter | direkt Plan ohne Modellprofilresolver; general-Vorabfix nur bei getrenntem Bedarf | Vorschlag ADR-0048 |
| Evidence und Zeilenenden | gequotete Evidence und CRLF-Lesen, mit dokumentierter Grenze für alte Leser | Vorschlag ADR-0049 |
| Workflow-Neuschnitt | schlanke Schleife mit einfachem Arbeitsstand; bestehende Formate vorerst bewahren | Vorschlag ADR-0050 unter angenommenem ADR-0052 |
| WP-Support | 7.0/7.1 präzisieren, 6.x/neuere Minors erst nach gezieltem Nachweis hinzufügen | bestehenden Umfang behalten |
| Ask-Titel/Sidebar | Ask vor dem Aufrufertitel; automatische Platzierung vollständig entfernen | angenommen: ADR-0055; W-015 |
| Git-Bash/Größenlimits | kein Bash-Opt-in ohne Bedarf; Größen nur informativ | vorerst nicht als Pflichtfeature planen |
| Development-Retention | kurze kanonische Records behalten; Rohdaten und private Pfade gezielt bereinigen | bestehende Retentionsregel anwenden |

Für eine einheitliche Projektwahl empfiehlt ADR-0051 genau eine optionale Datei `.scoville/config.json` in der ausgewählten Projektwurzel. Ihre Ask-/Workflow-Bereiche verwenden bestehende Konfigurationsformen. Der Nutzer verlangt Projektkonfiguration; der konkrete Dateipfad und die gemeinsame Ladefunktion sind der hier vorgeschlagene Weg. Keine automatische Dateierzeugung, keine Elternsuche und keine Laufzeitüberwachung.

Vom Nutzer gewählte Reihenfolge steht mit stabilen IDs direkt in PLAN-0011: W-001, W-006, W-003, W-012, danach der neue Ask-Punkt W-015, W-014 (kleine Runner-Vorbereitung), W-002, W-008, W-009, W-005, W-010, W-011, W-004, W-007, W-013. Der aus W-014 getrennte informative Größenbericht W-016 folgt zuletzt. Die Ausgangsmessungen bleiben unmittelbar vor dem jeweiligen Umbau. W-005 hängt von W-002 ab, W-009 von W-008, W-010 von W-002/W-008/W-009/W-005. Die Reihenfolge erteilt keine Annahme der noch vorgeschlagenen Decisions. Vor Aktivierung offene Varianten auswählen; unabhängige noch unbegonnene Arbeit nur durch ausdrückliche Planpflege vorziehen.

Die neuen Vorschläge sind noch nicht angenommen. Der Fixplan ist ein Draft; diese Aufgabe hat die aktive Planroute nicht verändert. Die im geprüften Stand ausstehende UI-Abnahme besitzt PLAN-0006; einen gesondert beauftragten späteren Abschluss anhand seiner eigenen Decisions prüfen. Weder frühere Ergebnisse noch fremde uncommittete Änderungen werden durch dieses Review ersetzt.

## Unabhängiges Astra-Review und Korrekturen

Angefordert: gpt-6-astra mit medium in frischem Kontext. Tatsächliche Modell-/Effort-Telemetrie: unbekannt. Task: `01a0d845-c4df-7142-976b-eb229169ba9c`; Referenz: `scoville-plan-0011-astra-medium-20260925-01`. Nur lesendes Review von Plan, Auswertung und ADR-0045 bis ADR-0052 gegen Originalreview und direkte Quellen. Keine Tests durch den Reviewer.

Astra bestätigte die Einzelbehandlung aller 28 Punkte und meldete drei P2-Planungslücken. Die Gegenprüfung bestätigte sie:

- Die empfohlene Reihenfolge steht jetzt als H3-Reihenfolge mit unveränderten IDs im Plan. Vorhermessung und kleine Fallauswahl stehen vor den Umbauten in W-008/W-010/W-011; W-014 bleibt keine Großtest-Voraussetzung.
- ADR-0048 empfiehlt direkt die Entfernung des Plan-Modellprofilresolvers. Ein alter-Python-Fallback ist nur eine bei eigenem Bedarf wählbare Alternative. Verbleibende Codex-Validator-/Selector-Laufzeiten bleiben separat erhalten.
- ADR-0051 erhält Ask project_config ausdrücklich über der Projektdatei und unter overrides. W-005 prüft den Konfliktfall; bestehende Adviser-/Preset-Merge-Semantik bleibt erhalten.

Das Review ist Quellenprüfung, kein Nachweis künftiger Token-/Zeitersparnis. Die drei Korrekturen wurden vom Verfasser gegen die genannten Quellen geprüft; die native Strukturvalidierung bestand danach ohne Fehler oder Warnungen.

Gezielte Nachprüfung angefordert unter `scoville-plan-0011-astra-medium-20260925-02`, context_mode continued, unverändert gpt-6-astra/medium. Der Host wies die Nachricht ab: Der Reviewer-Task war inzwischen archiviert. Keine Nachprüfung fand statt; keine Entarchivierung, kein Ersatzreview und kein Erfolg behauptet. Das erste Review hatte context_mode fresh. Der genaue Archivierungsgrund ist unbekannt.

## Prüfung der weiteren externen Anmerkungen

Quelle: vom Nutzer bereitgestelltes `review-plan-0011.md`, 2026-09-25. Der externe Reviewer hatte nur den Plantext, nicht die Decisions oder diese Auswertung. Kein neues Modellreview wurde beauftragt. Alle elf Empfehlungen wurden gegen die betroffenen aktuellen Verträge geprüft.

| Nr. | Ergebnis und Behandlung |
| --- | --- |
| 1 | Übernommen: F-01 hat in W-008 und ADR-0048 einen ausdrücklichen general/Python-3.10-Nachweis ohne Writing-Profile-Helper. Kein unnötiger Zwischenumbau. |
| 2 | Zunächst kein sachlich fehlender Befund: F-23 war bewusst gegen ADR-0042 abgegrenzt. Danach entschied der Nutzer neu. W-015/ADR-0055 setzen Ask-Präfix und vollständigen Wegfall der Sidebar-Platzierung um. |
| 3 | Übernommen: zwölfteilige Umfangstabelle in ADR-0050; W-010 liest sie ausdrücklich und gleicht jede Zeile ab. Keine doppelte Volltabelle im Plan. |
| 4 | Gleicher Ordner allein ist keine fachliche Abhängigkeit. Der Nutzer wählte danach ausdrücklich die Reihenfolge: W-005 nach W-002; W-009 nach W-008; W-010 nach W-002/W-008/W-009/W-005. Im Plan gespeichert. |
| 5 | Angepasst übernommen: gezielte Suche plus Einordnung der Treffer für Modellpflichten/Defaults und Befehlsbeispiele. Keine blinde Nulltrefferregel: Adviser-IDs sind keine Modell-IDs; API-Werte, historische Evidenz und echte Vertragsfixtures dürfen bleiben. Referenzumfang vor/nachher wird genannt. |
| 6 | Mechanismus bestätigt: ask.py wartet mit subprocess.run und ask_claude.py kann über PowerShell starten. W-003 verlangt Ende der eigenen CLI-Prozessfamilie plus unbeeinflussten Kontrollprozess. Kein ungezieltes Beenden aller Node-/Claude-Prozesse und keine unbewiesene Festlegung auf taskkill nach schon beendetem Wrapper. Noch kein Prozessbaumtest ausgeführt. |
| 7 | Angepasst: fehlendes Startpaar kann auch durch einen expliziten Override entstehen. W-005 verbessert die Meldung ohne eine Konfigurationsänderung als sichere Ursache zu behaupten. Gemeinsame Projektdatei überschreibt persönliche Defaults auf allen verwendenden Rechnern; README-Hinweis in ADR-0051. |
| 8 | Übernommen als Kommentar unmittelbar an der kopierbaren Verzweigung. Kein neuer Debug-/Laufzeitwarnmechanismus nur für das Beispiel. |
| 9 | Übernommen: zu alte Interpreter und Windows-Store-Alias konkret prüfen, keine pauschale Versionsbehauptung für alle Macs. GitHub-Actions-Matrix mit drei Betriebssystemen; fehlende Läufe bleiben offene Abnahme. |
| 10 | Vom Nutzer gewählte Reihenfolge übernommen: W-014 bereitet früh den vorhandenen Vergleichsweg vor. Eigentliche Ausgangsmessung unmittelbar vor dem jeweiligen Umbau; informativer Größenbericht separat als W-016 am Ende. |
| 11 | Übernommen: vollständige Zuordnung unten. W-001 verweist ausdrücklich auf die dauerhaft festgehaltenen Grenzen und Betriebsbefehle; der temporäre externe Reviewpfad ist keine Ausführungsvoraussetzung. |

PLAN-0006 wurde inzwischen in einem gesonderten Auftrag gemäß ADR-0053 abgeschlossen. Neue Planformulierungen respektieren diesen Abschluss und behaupten keine nachträglich durchgeführten UI-Prüfungen.

## Zuordnung aller 28 Reviewpunkte

Die Detailurteile stehen oben beim jeweiligen F-Punkt. Diese Tabelle ordnet ihre Umsetzung oder bewusste Nichtumsetzung zu.

| Punkt | Behandlung | Besitzer |
| --- | --- | --- |
| F-01 | Geändert: direkte Entfernung der Profilpflicht; general mit Python 3.10 prüfen | W-008; ADR-0048 |
| F-02 | Übernommen mit dynamisch längerem Fence | W-006 |
| F-03 | Geändert: ungeprüfte Version sichtbar, kein pauschales >=7.1 | W-012 |
| F-04 | Geändert: Read-only-Grenze ehrlich erklären, keine Hash-Sandboxsimulation | W-004 |
| F-05 | Übernommen als offener Web-Opt-in-Vorschlag | W-004; ADR-0047 |
| F-06 | Übernommen einschließlich Ende der eigenen Prozessfamilie | W-003 |
| F-07 | Geändert: Rohdaten/Privatpfade gezielt bereinigen, kanonisches Wissen erhalten | W-007 |
| F-08 | Übernommen, Standalone bereits entschieden | W-007; ADR-0055 bewahrt Distribution |
| F-09 | Kein zweiter Mergeauftrag; späterer Abschluss gesondert dokumentiert | PLAN-0006; ADR-0053; Non-goal |
| F-10 | Übernommen, bestätigte Löschgrenzen und Backup beachten | W-013 |
| F-11 | Geändert: nur verbleibende Mehrdeutigkeit bei Taskort/Labels | W-006 |
| F-12 | Geändert: korrekte Hosts und gültige Metadaten statt gleiche Schlüssel erzwingen | W-007 |
| F-13 | Übernommen als deutliche Planvereinfachung | W-008 |
| F-14 | Geändert: Reader-/Upgradegrenzen ausdrücklich prüfen | W-009; ADR-0049 |
| F-15 | Übernommen unter gewähltem Einzelbetrieb; keine Ersatzmaschine | W-008/W-010; ADR-0045/0052 |
| F-16 | Geändert: Planresolver direkt entfernen | W-008; ADR-0048 |
| F-17 | Übernommen; CLI/Plattform und Format getrennt | W-002/W-009 |
| F-18 | Geändert: konkreter Neuschnitt gemäß zwölfteiliger Tabelle | W-010; ADR-0050 |
| F-19 | Aktuellen Stand sprachlich prüfen, nicht alten Umbau wiederholen | W-011 |
| F-20 | Übernommen mit erhaltenen semantischen Ladegrenzen | W-011 |
| F-21 | Supportausweitung abgelehnt; vorhandene Grenze erklären | W-012; Non-goal |
| F-22 | Vorhandene Regeln verständlich machen, nur belegte Lücken ergänzen | W-011 |
| F-23 | Neue Nutzerwahl: Ask vorne, Platzierung vollständig entfernen | W-015; ADR-0055 |
| F-24 | Pauschale Bash-Git-Freigabe nicht übernommen | Non-goal |
| F-25 | Geändert: vorhandenen Runner vorbereiten und gezielte Vergleiche je Umbau | W-014 plus W-008/W-010/W-011 |
| F-26 | Geändert: informative Messung ohne harte KB-Grenzen | W-016 |
| F-27 | Persönliche Skilldatei plus Projektwahl; keine Laufzeit-Snapshots | W-005; ADR-0046/0051/0052 |
| F-28 | Übernommen mit korrektem Shared-Pfad und vorhandener Root-.gitignore | W-001 |

## Ausführungsgrundlage für W-001

Diese Angaben bewahren die vom Nutzer bestätigte F-28-Freigabe. Sie führen hier keine Systemänderung aus.

- Suite bleibt an ihrem Ort. Autorisiert sind der persönliche Python-Cachepfad, die benannten Cachelöschungen und Viewer-Ignore-Einstellungen. Keine weitergehenden System-/Dropbox-Einstellungen oder anderen Ordner.
- Vorhandenes PYTHONPYCACHEPREFIX außerhalb Dropbox erhalten. Bei vorhandenem Wert innerhalb Dropbox vor Änderung den Nutzer fragen. Bei fehlendem Wert den unten genannten persönlichen Cache verwenden und anlegen.
- Vor Löschung die aufgelösten __pycache__-Ziele ausgeben und auf members/ oder den kanonischen Geschwisterordner ../shared/ begrenzen. Ausschließlich diese Cacheordner löschen.
- Viewerziele sind members/scoville-plan/development/viewer/node_modules und members/scoville-plan/development/viewer/src-tauri/target. Vor Build anlegen und ausnehmen; nach einem Build mit Neuerstellung Attribute erneut prüfen.

| System | Persönlicher Python-Cache bei fehlender Einstellung | Ignore setzen / prüfen |
| --- | --- | --- |
| Windows/PowerShell | `[Environment]::SetEnvironmentVariable("PYTHONPYCACHEPREFIX", "$env:LOCALAPPDATA\pycache", "User")` | `Set-Content -LiteralPath "<ordner>" -Stream com.dropbox.ignored -Value 1`; danach `Get-Content -LiteralPath "<ordner>" -Stream com.dropbox.ignored` |
| macOS/zsh | Einmal `export PYTHONPYCACHEPREFIX="$HOME/Library/Caches/pycache"` in ~/.zprofile; vorhandene Einstellung erhalten | `xattr -w com.dropbox.ignored 1 "<ordner>"`; danach `xattr -p com.dropbox.ignored "<ordner>"` |
| Linux | Einmal `export PYTHONPYCACHEPREFIX="$HOME/.cache/pycache"` in ~/.profile; vorhandene Einstellung erhalten | `attr -s com.dropbox.ignored -V 1 "<ordner>"`; danach `attr -g com.dropbox.ignored "<ordner>"` |

Fehlt die Linux-Attributunterstützung, kann target über eine nicht versionierte lokale Cargo-Konfiguration außerhalb Dropbox liegen. Das löst node_modules nicht automatisch: dessen offene Synchronisationsgrenze melden statt erfolgreiche Einrichtung zu behaupten. Keine maschinenabhängigen absoluten Cargo-Pfade versionieren.

Für die Prüfung die geänderte Umgebung ausdrücklich übernehmen oder eine neue Sitzung verwenden; bloßes Starten eines Kindes aus einer alten Sitzung genügt nicht. `sys.pycache_prefix`, Cachebestand und Ignore-Attribute tatsächlich prüfen. Während noch alter Sitzungen zusätzlich Python -B beziehungsweise PYTHONDONTWRITEBYTECODE für Kindprozesse verwenden. Ergebnisse, betroffene Ordner und Neustartbedarf knapp berichten. Eine gelesene Ignore-Markierung allein ist kein plattformübergreifender Live-Nachweis der Dropbox-App.

## Nutzerkorrektur zum Context-Rollover

ADR-0063 ersetzt ADR-0050: Automatischer Context-Rollover für Koordinator und
Worker ist Pflicht und darf nicht durch gespeicherten Stand oder native
Kompaktierung ersetzt werden. Frühere Aussagen dieser Auswertung zum Wegfall
der Prozent-/Nachfolgermechanik sind dadurch überholt. W-010 vereinfacht die
Mechanik bei erhaltener automatischer Übergabe; W-017 macht die vorhandenen
Schwellen über die eine Konfigurationsdatei einstellbar.

## W-009: geprüfter Klartext- und CRLF-Stand

Evidence verwendet nach Nutzerkorrektur ADR-0065 gewöhnlichen Text ohne JSON
oder Escape-Syntax. Alte Listen bleiben wörtlich lesbar. Die neue Syntax beginnt
nicht mit einer öffnenden eckigen Klammer; diese kennzeichnet weiterhin die
bisherige Liste. Konsistentes CRLF ist zusätzlich zu LF lesbar.

Belege: 82 Python-Tests unter Windows/Python 3.14 und Linux/Python 3.12 bestanden.
Die 13 Rust-Tests des tatsächlichen Viewer-Lesecodes bestanden unter Linux mit
Rust 1.98.1 in einer temporären Test-Crate. Nur das Tauri-Command-Attribut wurde
für diesen isolierten Parser-Test entfernt. Das belegt den Lesecode, keinen
vollständigen Tauri-Anwendungsbuild oder Release. Beide gebauten Plan-Pakete
bestehen Linkprüfung und CRLF-Validierung. 90 Workflow-Tests bestehen unter
Windows. Unter Linux bestehen zunächst 89; ein Test benötigt das dort fehlende
Node. Ask besteht dort mit 20 Tests und einem Windows-spezifischen Skip.

Vergleich mit dem gesicherten bisherigen Validator: alte LF-Records bestehen
beide Leser; Klartext-Evidence und CRLF bestehen den neuen Leser, während der
bisherige Reader WORK_LIST_INVALID beziehungsweise FILE_LINE_ENDING_INVALID
meldet. Formatversion 1 bleibt bestehen. Die Erweiterung ist rückwärts lesbar,
aber nicht vorwärts kompatibel mit alten Readern. Die README benennt diese
Grenze. Ein Upgrade vorhandener Records ist nicht erforderlich.

Selector: Ganze Records bewahren die ursprünglichen Zeilenenden. Die explizite
Dispatch-Projektion source_text bleibt gemäß bisherigem Vertrag auf LF mit
einem abschließenden Zeilenumbruch normalisiert. Tests prüfen beide Formen.
Der frühere Batchhelper liest keine Evidence-Syntax und bleibt als nicht mehr
ausgelieferte historische Entwicklungsquelle unberührt.

## W-007: Distribution, Hosts und Metadaten

Ask nennt seine eigenständige Distribution jetzt ausdrücklich auch im
Suite-Kontext. Standalone und Suite bleiben getrennte Buildvarianten. Beide
Ask-Payloads sind mit aufgelösten Links geprüft. Workflow beschreibt die eigene
Codex-Ausführung getrennt von möglichen Hosts anderer Suite-Mitglieder.
README-Projektionen stammen aus dem Builder.

Die [Agent-Skills-Spezifikation](https://agentskills.io/specification) wurde am
25. September 2026 geprüft: compatibility ist optional und auf 500 Zeichen
begrenzt. Die bekannten Frontmatterfelder sowie die Längen von name,
description und compatibility bestanden für alle zehn General-/Codex-Payloads.
Der unveränderte Skill-Creator-Kurzvalidator akzeptiert Ask und Workflow. Bei
acht anderen Payloads lehnt er ausschließlich das laut Spezifikation zulässige
compatibility-Feld ab. Dies ist eine dokumentierte Validatorabweichung, kein
bestandener Kurzvalidatorlauf und kein Nachweis zusätzlicher Hostunterstützung.
Es wird kein Pflichtfeld nur zur Gleichheit aller Skills eingeführt.

Die drei in F-07 benannten Entwicklungsberichte enthalten Ergebnis- und
Entscheidungswissen. Dieses bleibt erhalten. Persönliche Maschinenpfade wurden
durch Workspace-/Codex-Platzhalter beziehungsweise Sitzungs-IDs und
Recordnummern ersetzt. Originaltranskripte bleiben bei ihrem Hostbesitzer;
keine terminalen Plan- oder ADR-Inhalte wurden dafür umgeschrieben. Rohmaterial
wurde nicht neu in die Distribution aufgenommen.


## W-005: Eine Konfigurationsdatei

Ask liest `ask`, Workflow liest `workflow` aus `.scoville/config.json` der
gewählten Wurzel. Der gemeinsame Loader sucht keine Eltern, schreibt nichts
und lädt keine persönliche Datei. Teilwerte überschreiben die importierten
Defaults. Anfrage-/Step-Werte bleiben ungespeichert. Die vorhandene
Adviser-/Preset-Rangfolge bleibt erhalten. Das alte Eingabefeld project_config
wird mit einer konkreten Umstiegsanweisung abgelehnt.

Am 25. September bestanden 21 Ask-Tests, 92 Workflow-Tests und zwei gemeinsame
Schreibprofiltests. Neue Verbraucherfälle prüfen fehlende Datei, partielle
Werte, abgelehnte Fehlwerte, unveränderte gespeicherte Werte bei einem
Aufrufoverride, Änderungen zwischen Läufen und fehlende Elternsuche.
Ask-Einzelpaket und Suitepaket werden durch die Buildtests ausgeführt.
Workflow-Payload (43 Dateien) und Ask-Payload (18) bestehen die Linkprüfung.
Eine zuerst beobachtete lokale Namenskollision im Resolver wurde korrigiert
und der gesamte betroffene Workflow-Testlauf erneut bestanden.

Vorhandene persönliche Abweichung: ask-claude-for-codex/config.json nennt
Fable medium und ein Budget von 50 USD. Das Fable-Preset stimmt bereits,
das aktuelle Claude-Budgetdefault ist 10 USD. Die Altdatei bleibt unverändert.
Keine Projektdatei wurde angelegt und kein Budget ungefragt übernommen.
Der Reparaturfehler nennt ein in der aktuellen execute-Tabelle fehlendes
ursprüngliches Paar, ohne einen Konfigurationswechsel als Ursache zu erfinden.

W-005 und W-010 benötigen die implementierte Portabilitätsbasis aus W-002,
keinen abgeschlossenen fremden CI-Lauf zum Beginn lokaler Änderungen. Ihre
noch unbegonnenen Abhängigkeiten wurden entsprechend präzisiert. Die
vollständige Plattformabnahme bleibt unverändert offen bei W-002.


## W-017: Suite-only Setup

Setup ist ausschließlich im Codex-Suiteprofil enthalten. Der gebaute Skill
verwendet den gemeinsamen Loader sowie die aus Ask und Workflow ausgelagerten
Konfigurationsprüfungen. Er importiert deren Defaults über das Manifest,
liest oder schreibt keine Geschwisterinstallation und hat keine zweite
Ladelogik. show schreibt nichts. set nimmt nur ausdrücklich übergebene
Änderungen an und validiert sie vor dem Schreiben. Fremde gespeicherte Werte
bleiben erhalten. Modellverfügbarkeit bleibt Prüfung des tatsächlichen Hosts
beim Start, nicht eine unbelegte Setup-Zusage.

Die Nutzerdefaults sind jetzt im kanonischen Workflow-Asset 25/75 Prozent.
Setup bearbeitet Ask-Adviser und Presets, Modell/Effort, Claude-Budget,
Persistenz, Customizations, Timeout und Web-Tools sowie Workflow-Modellpaare
und Rollovergrenzen. Entfernte Coordinator-Modelle/Titel und Plan-Schreibprofile
werden nicht als Setup-Felder angeboten. Die noch vorhandenen optionalen
Workflow-Schreibprofile werden beim W-010-Neuschnitt beurteilt.

Zwei Tests des tatsächlich gebauten Setup-Pakets bestehen: Anzeige ohne Datei,
Speicherung, ungültige Werte ohne Veränderung, fremde Werte, Unicode-Pfad und
wirksame Werte im gebauten Ask und Workflow-Checkpoint. Die importierten
Defaultwerte werden dabei geprüft. Weitere 21 Ask-, 92 Workflow- und sechs
Buildertests bestanden nach der Auslagerung. Der Skill-Creator-Kurzvalidator
akzeptiert das gebaute Setup. Die Aussage betrifft den lokalen Helfer und
Paketvertrag, keinen beobachteten Modelllauf oder Workflow-Rollover.

### W-010: Archivierung bleibt erhalten

Der gemeinsame Lifecycle-Helfer und die Workflow-Anweisungen behalten die
Archivierung nach gesichertem Ergebnis und tatsächlichem Aufgabenende bei.
Offene Aufgaben und `needs_user_decision` bleiben offen. Bei Rollover gilt für
alle vier Rollen zusätzlich: Vorgänger beendet und Nachfolger tatsächlich
gestartet. Eine nur vorgemerkte Erstellung reicht nicht. Der letzte Koordinator
bleibt sichtbar. Ask behält seine bisherigen Zustimmungs- und Fehlerregeln.

Archivierung verwendet die gespeicherte Aufgaben-/Host-ID. Nur eine fehlerfreie
Antwort mit derselben ID und booleschem `archived:true` bestätigt Erfolg.
Workflow hält den einmaligen Versuch samt Ergebnis beim Handle fest, meldet
Fehler und wiederholt ihn beim Fortsetzen nicht automatisch. Ein
Archivierungsfehler blockiert keine fachlich bereits angenommene Arbeit.

Am 25. September bestanden 19 gemeinsame Lifecycle-/Titeltests sowie jeweils
19 Tests gegen den Helfer im tatsächlich gebauten Ask- und Workflow-Payload.
Weitere 18 Ask-Verhaltens-/Pakettests bestanden. Geprüft wurden insbesondere
verfrühte Archivierung, fehlende Ergebnissicherung, alle Rolloverrollen,
offene Nutzerentscheidungen, falsche IDs und negative/fehlerhafte Antworten.
Dies belegt den lokalen Vertrag, keine neue reale Host-Archivierung. Der echte
Workflowlauf mit Nachfolgetasks bleibt Teil der offenen W-010-Abnahme.

### W-010: direkter Dispatch und verbleibende Schnittstellen

Der Laufzeitentwurf verwendet jetzt direkten Einheiten-Dispatch, drei
Laufzeitreferenzen und einen Markdown-Laufstand. Guard-, Launcher-, Park- und
Transporthelfer sowie Schreibprofile sind aus dem Workflow-Paket entfernt.
Die README-Fragmente beschreiben Einzelbetrieb, 25/75-Grenzen, neue Titel und
Commitautorität. Das gebaute Paket umfasst 21 Dateien und besteht seine
Linkprüfung. Eine Suche in gebautem SKILL.md und references ergab keine
sha256-/digest-Pflichten; Byte-/Receipt-Erwähnungen erklären deren Wegfall,
Guard-Erwähnungen die Grenze gegenüber alten aktiven Runs.

14 Workflowtests und zwei Setup-Verbrauchertests bestehen. Die Workflowtests
prüfen den erhaltenen Rollenresultatparser einschließlich Fehlformen, aktuelle
Modellrouten und begrenzte Eskalation, den tatsächlichen Plan-Selector samt
Unicode/CRLF/Klartext-Evidence, die unveränderte Projektion im erzeugten Prompt,
Rolleninputs und Context-Defaults/Grenzwerte. Review-Prompts weisen nun
unvollständige Workerresultate zurück. Ein anfänglicher Fixturefehler versuchte,
einen abgeschlossenen statt eines ausführbaren Items zu dispatchen; nach
Korrektur des Testfalls besteht der Selector-Test.

Die alten Tests für entfernte Guard-, Park-, Transport-, Phasen- und
Readinessmechanismen wurden samt vorherigem vollständigem Testbestand
vorübergehend gesichert und aus der aktiven Testsuite entfernt. Der neue
lokale Teststand behauptet ausdrücklich keine gleichwertige reale
Orchestrierungsabnahme. Stopp/Wiederaufnahme, tatsächliche Nachfolgetasks,
Mehr-Einheiten-Lauf und Modellverständnis bleiben offen. Zwei Kandidatenversuche
sind im Vergleichsbericht als fehlgeschlagen dokumentiert.

### W-002: aktuelle Interpreter- und Linux-Prüfung

Nach dem Workflow-Neuschnitt bestehen 14 Tests unter Windows/Python 3.11.15
und Linux/Python 3.12. Der entfernte Node-Transport ist keine aktuelle
Laufzeitabhängigkeit mehr. Ein realer Aufruf des Context-Checkpoints unter
Python 3.10.20 fand zunächst ModuleNotFoundError für tomllib. Der gemeinsame
Workflow-Settingsimport prüft nun die Mindestversion vor diesem Import.
Wiederholte Aufrufe unter Python 3.10.20 und 3.9.25 liefern Exit 1 mit
Python 3.11 or newer is required for Workflow helpers. Der Modellresolver
meldet unter Python 3.9 ebenfalls diese Diagnose. Zwei gebaute
Setup-Verbrauchertests bestehen nach der Korrektur.

Der tatsächlich vorhandene WindowsApps/python.exe-Alias lieferte für
--version Exit 9009, keine Versionsausgabe und den Hinweis, dass Python nicht
gefunden wurde. Er wurde weder installiert noch als Interpreter verwendet.
Die Drei-Plattform-CI einschließlich macOS bleibt mangels beobachteter Läufe
offen. Es erfolgten kein Push und keine Veröffentlichung.

### Laufender Plan im vorhandenen Viewer

Der Nutzer meldete im Plan Viewer invalid inline list für PLAN-0011. Ursache
war die neu geschriebene Klartext-Evidence von W-010; der vorhandene Viewer
verwendet dort noch den bisherigen Listenparser. Die Zeile wurde ohne
Inhaltsverlust auf die unterstützte Klammerliste zurückgestellt. Laufende
Projektpläne behalten bis zum separat erfolgenden Viewer-Update die alte
Schreibweise. Die neue Leserunterstützung im Quellcode bleibt erhalten.

### W-010: Abgleich der zwölf ADR-0064-Bereiche

| Bereich | Quelle im Neuschnitt | Bisheriger Nachweis / offene Grenze |
| --- | --- | --- |
| Launcher/Coordinator-Handshake | SKILL.md Start or resume; launcher.md und coordinator_contract.py entfernt | Fixture startet im aufrufenden Koordinator ohne separaten Launcher |
| Coordinator-Rollover | references/operations-rollover.md Coordinator | Reale Übergabe im Fixture noch in Prüfung |
| Worker-Übergaben | operations-rollover.md Worker; check_context_checkpoint.py | Fixture: frische Messung und neuer Worker mit erhaltener Restarbeit beobachtet; abschließende Hostprüfung folgt |
| Pending-Writer-Aktivierung | operations-dispatch.md; direkter build_dispatch_prompt.py | Direkt erstellte Worker im Fixture, keine Parkaktivierung |
| Guard-Revisionen/Generationen/Capabilities | SKILL.md Markdown-Laufstand; manage_workflow_guard.py entfernt | Arbeit über Taskhandles und eine aktuelle Einheit; keine Sperr-/Signaturfelder im Paket |
| Step-Bundling | select_unit in build_dispatch_prompt.py | Echte Selector-Tests weisen Bereiche zurück; eine Step-Auswahl wird unverändert eingebettet |
| Archivierung | operations.md Archive; gemeinsamer task_lifecycle.py | 19 Lifecycle-/Titeltests je gebautem Verbraucher; tatsächliche Workerarchivierung im Fixture nach Übernahme, Endabgleich folgt |
| Hash-/Transportbelege | build_dispatch_prompt.py; dispatch_transport.js und inspect_dispatch_preflight.py entfernt | Paketprüfung zeigt keine Modell-Hashpflicht; SCOVILLE_RESULT_V1 bleibt |
| Persistente Goals | SKILL.md | Kein zusätzliches Goal im neuen Vertrag; alter Übernahmehelfer entfernt |
| AGENTS.md-Block | references/agents-setup.md | Optionaler Absatz auf ausdrücklichen Auftrag, kein Installations-/Aktivierungszwang |
| Fünf Routeklassen | workflow_settings.py und resolve_model_pair.py; operations-dispatch.md | Tests aller fünf Routen, Overrides und Reparaturen 1 bis 3 bestehen |
| Review-Einstufung | operations.md Einheitenloop und build_dispatch_prompt.py | Tatsächlicher Diff bleibt maßgeblich; unvollständige Ergebnisse werden als Reviewinput abgewiesen; echte Code-Review im Fixture noch offen |

Die Pfade ohne Präfix liegen unter
members/scoville-workflow-for-codex/scoville-workflow-for-codex/.
Diese Zuordnung ist eine Fortschrittsaufnahme, keine abschließende Abnahme.

### W-010: beobachtete native Übergaben, Zwischenstand

Der initiale Koordinator 01a0d8e2-673d-71c1-bf6a-803bf31e6749 hat seinen
Turn tatsächlich beendet. W-001 wurde ausschließlich durch Worker erledigt:
01a0d8e4-42ca-7dd2-9a4d-c78ef04dfdcf hielt mit frischer Messung
30973/258400 und konfigurierter Grenze 1 Prozent vor dem Schreiben an.
Nachfolger 01a0d8e5-e1fb-78c1-a3fa-bcabd6e244c6 führte die verbliebene
Schreibaufgabe aus. Die zusätzliche Zeile steht genau einmal in note.md.
Der Laufstand protokolliert die Archivierung des Vorgängers nach gestartetem
Nachfolger und die spätere Archivierung des abgeschlossenen Nachfolgers.

Nach der W-001-Abnahme lieferte der Koordinator mit frischer Messung
81077/258400 und Grenze 1 Prozent rollover. Er erzeugte den tatsächlichen
Nachfolger 01a0d8e9-85a0-7e00-a019-98110c1d7b7d für denselben Run 1
und beendete sich ohne W-002-Arbeit. Die Beobachtung des Nachfolgers und die
abschließende Host-/Artefaktprüfung laufen noch. Die Testgrenzen waren bewusst
1/1 Prozent. Das ersetzt keinen Live-Beleg der Workergrenze 75 Prozent;
deren Operator und Werte sind durch die separaten Grenzwerttests geprüft.


### W-010: Ursache der vermeintlichen Formatfehler korrigiert

Die tatsächlichen finalen agentMessage-Texte des Workers
01a0d8ec-5760-75b3-9972-eda12d278f59 enthalten in beiden abgeschlossenen
Turns die vorgeschriebenen Zeilenumbrüche. Das read_thread-Ergebnis belegt
dies unmittelbar. Die zuvor als Workerfehler beschriebenen MAGIC_INVALID-
Diagnosen entstanden beim Parsen des verdichteten wait_threads-Snapshots.
Der native Testlauf ist damit weiterhin unvollständig, aber kein Beleg für
zwei fehlerhafte Originalantworten.

operations.md verlangt nun den originalen final_answer-Text aus read_thread
für die genaue Aufgabe und den abgeschlossenen Turn, mit erhaltenen
Zeilenumbrüchen und ausreichender Ausgabelänge. Fehlender oder gekürzter
Originaltext zählt nicht als Formatfehler. Erst der vollständige Originaltext
geht an den unveränderten Rollenparser.

Zusätzlich unterscheidet der Workerauftrag eigene Restarbeit von späterer
Koordinatorabnahme: Nach abgeschlossener Arbeit und eigenen Checks folgt das
normale Rollenresultat ohne weiteren Context-Checkpoint. Executor/Repair
verwenden completed, Reviewer pass oder changes_requested. Damit führt eine
nur noch ausstehende Koordinatorreview nicht zu einem unnötigen Workerwechsel.

Die kanonischen Anweisungen und der Prompt-Builder sind korrigiert; die
README-Projektion ist aktualisiert. Auf Nutzerwunsch wurden danach keine
weiteren Tests oder Modellläufe gestartet. Die erneute Ablaufprüfung bleibt
bis nach dem externen Review offen.


## Fixplan zu beiden Umsetzungsreviews vom 2026-09-25

Verbindlicher Arbeitsplan: [PLAN-0011, W-018 bis W-026](plans/0011-suite-review-fixes.md#w-018-bestehende-pläne-bleiben-im-installierten-viewer-lesbar). Grundlage sind der externe Bericht `review-plan-0011-umsetzung.md` und das zusätzlich im Chat gelieferte unabhängige Review mit drei P2-Befunden. Die folgenden Urteile betreffen die Planung, nicht eine bereits durchgeführte Korrektur oder Abnahme. Der Nutzer verlangt zunächst den Fixplan; Implementierung und neue Modellläufe bleiben angehalten.

Die Nutzerergänzungen ersetzen nur die Empfehlungen zu M6, L4 und L5. Alle übrigen Befunde bleiben berücksichtigt. Reihenfolge nach Wiederaufnahme: W-018 bis W-024, dann die native Abnahme W-026, anschließend W-025. W-010 ist nach ausdrücklicher Nutzerfreigabe cancelled; current_item zeigt auf W-018 mit Status todo. Es läuft keine Umsetzung. W-026 hat keine Freigabesperre und wartet auf W-024.

| Quelle / Befund | Behandlung und Nachweisgrenze | Zuständig |
| --- | --- | --- |
| H1 Evidence-Schreibform | Kompatible Legacy-Listen und LF schreiben; Klartext und CRLF weiterhin lesen. Keine Veröffentlichung als Voraussetzung einschieben. | W-018 |
| H2 Testbasis und CI-Lücken | Veraltete Erwartungen einzeln korrigieren, Ask-Katalog isolieren, doppelte Overrides und USERPROFILE-Zugriff prüfen, CI-Abdeckung ergänzen. Reale GitHub-Matrix bleibt separat unbeobachtet. | W-022; W-002 bleibt offen |
| M1 Letzte Fixes und Ablaufbelege | Originalresultat/Snapshot-Grenze und Lifecycle-Prompt gezielt testen. Kein Texttest als Beweis gegen unnötige Rollover ausgeben. | W-022 und W-026 |
| M2 Koordinator-Pflichtkopf | Rollenmarker am Promptanfang und ausdrücklichen Skillaufruf mit Pfad angeben und am Helper prüfen. | W-019 |
| M3 Lokaler Laufzustand | Workflowdatei und Handoffs niemals committen; Aufräumen erst nach Sicherung und Ende des betreffenden Ablaufs. Projektkonfiguration bleibt versionierbar. Kein Setup-Ausbau allein dafür. | W-019 |
| M4 Interpreterauswahl | Regel in tatsächlich geladene Laufzeittexte aufnehmen; keine pauschale Python-3.11-Pflicht für Plan oder alle Skills. | W-022 |
| M5 Plan noch zu umfangreich | Häufige Planrouten weiter vereinfachen und Verhalten vergleichen; W-008 nicht nachträglich umschreiben. | W-025 |
| M6 Persönliche Altdatei | Nutzerkorrektur: Legacy vollständig entfernen, keine einmalige Warnung und keine Migrationsebene. Exakte alte Dateien vor Entfernung zuordnen. | W-021 |
| M7 CHANGELOGs | Aktuellen Stand unter Unreleased berichtigen, veröffentlichte Historie erhalten. | W-023 |
| L1 Verwaiste Helfer | Manifest und echte Aufrufer entscheiden; keine Löschung allein aufgrund der Reviewerbezeichnung. | W-023 |
| L2 Distribution und Links | Suite-only und selbstständige Nutzbarkeit sprachlich eindeutig erklären; URLs gegen tatsächliche Ziele prüfen. | W-023 |
| L3 Titelvalidierung | Plan-/Einheiten-ID knapp validieren, keine neue Titelverwaltung. | W-019 |
| L4 Reasoning | Nutzerkorrektur: einheitlicher Wortschatz in Plan, Setup, Ask und Workflow; Modellfähigkeit weiterhin prüfen, keine stille Umwandlung. | W-020 |
| L5 CRLF im Paket | Nutzerkorrektur: LF im gebauten Textpaket sicherstellen. Aktuell normalisiert package_bytes bereits CRLF; übrige Ausgabewege und reale Kopien noch prüfen. Binärdaten unverändert lassen. | W-024 |
| L6 Viewer und Batch-IDs | Falsche Verbraucherbehauptung in der aktiven Referenz korrigieren. | W-023 |
| Inline-P2 1: ADR-0066 fehlt im Selector | Fehlende Decision-Verknüpfung bestätigt. W-010 bleibt unverändert als gestartete Historie und wird nicht erneut dispatcht. W-019 und W-026 verknüpfen ADR-0066 regulär; ein Selectorcheck prüft beide Aufträge. | W-019 |
| Inline-P2 2: Erster Manager | Fehlende Erstregistrierung und widersprechendes Umbenennungsverbot bestätigt. Bestehenden aufrufenden Manager als Nummer 1 registrieren und benennen. | W-019 |
| Inline-P2 3: Alte Paketkopien | Vorgesehene installierbare Kopien nach Quellenkorrekturen regenerieren; obsolete generierte Dateien begrenzt entfernen. Die gemeldeten 21 Workflowdateien sind eine Momentaufnahme und kein dauerhaft festgeschriebenes Soll. | W-024 |

### Weitere Aussagen beider Reviews

- **Native Abnahme:** W-026 übernimmt mit ausdrücklicher Nutzerfreigabe die offenen Pflichten von W-010. Der vorhandene Fixturelauf muss nach den Korrekturen die Originaltextübernahme und das Ende unnötiger Worker-Rollover zeigen. Zusätzlich bleiben Review-/Reparaturschleife, Reparaturgrenze, Stopp/Wiederaufnahme sowie unveränderte automatische Manager-/Worker-Übergaben zu belegen. Vorhandene abgeschlossene Arbeit wird nicht blind wiederholt.
- **Archivierung:** Ergebnisse und genaue Task-IDs zuerst sichern; beendete Testaufgaben anschließend archivieren. Rollover-Vorgänger erst archivieren, wenn sie beendet sind und der Nachfolger gestartet ist. Offene Nutzerentscheidungen bleiben sichtbar; Archivierungsfehler werden gemeldet. Diese Anforderung gehört zur W-026-Abnahme.
- **Positive Befunde:** Mehrzeilige Originalantwort, bereits korrigierter Workerauftrag, übereinstimmende Shared-Kopien sowie alte Evidence-Listen bleiben als bestätigter Ausgangsstand erhalten. Frühere Tests gelten nur für ihren damaligen Stand. Das Inline-Review hat keinen erneuten Viewer-Lauf beobachtet.
- **Leistung:** Weniger Paketbytes oder Inputtokens in einem einzelnen Volltextvergleich beweisen keine allgemeine Kosten- oder Laufzeitersparnis. Fehlgeschlagene Referenzauswahl bleibt in der bisherigen Evidence sichtbar.
- **W-001:** Die bestehende Policy-Sperre bleibt bestehen. Kein erneuter oder alternativer Lösch-/Cacheversuch wird aus dem Review abgeleitet.
- **W-002:** Lokale Tests oder eine ergänzte CI-Datei ersetzen keine beobachteten Plattformläufe. Keine Veröffentlichung und kein Push durch diesen Fixplan.
- **W-013:** Der Nutzer hat den Abschluss ausdrücklich als manuelle Batchübergabe akzeptiert. Daher keine Wiederöffnung aufgrund des Reviews und keine Behauptung, die Altquelle sei tatsächlich gelöscht. W-021 betrifft die nun ausdrücklich beauftragte Legacy-Konfiguration; bestehende Löschsperren werden dadurch nicht umgangen.
- **Übrige done-Punkte:** Die positive Gesamtbewertung ist kein neuer Abnahmenachweis. Konkrete Nacharbeiten zu W-005/W-007/W-008/W-009 stehen in den neuen Punkten statt in umgeschriebener Abschlussgeschichte.

Es bestehen keine neuen vorgeschlagenen ADRs. Die drei aktuellen Nutzerkorrekturen sind in W-020, W-021 und W-024 verbindlich festgehalten. Noch zu prüfende technische Details sind keine vorweggenommenen Befunde.


### Nachprüfung des Fixplans durch beide Reviewer

Alle drei Punkte aus Review 1 und alle vier Hauptpunkte sowie fünf Ergänzungen aus Review 2 sind berücksichtigt:

- **Decision-Konflikt:** Keine Ausnahme von der Unveränderlichkeit gestarteter Decisions. W-026 erhält vollständige aktuelle Acceptance und ADR-0066. Der Nutzer hat den endgültigen Abbruch ausdrücklich bestätigt. W-010 wurde mit Verweis auf die übernommene Restarbeit als cancelled geschlossen und USER-W010-REPLACEMENT bei W-026 entfernt. W-026 hängt von W-024 ab; cancelled wird nicht als erfüllte Abhängigkeit verwendet. Die bisherigen Nachweise und gestarteten authored fields bleiben erhalten.
- **Reihenfolge:** current_item ist W-018. W-020 hängt zusätzlich von W-018 ab, W-022 von W-021 und W-025 von W-026. W-026 steht vor W-025 und hängt von W-024 ab.
- **Pfad:** resolve_model_pair.py existiert und ersetzt den falschen Namen in W-020.
- **Eigener Titel:** Die Rückfallregel entfällt auf Nutzerwunsch. Der erste Manager wird als #1 registriert und umbenannt; Wiederaufnahme erhält Nummer und Titel. set_thread_title bestätigte für Aufgabe 01a0d834-d23d-7933-8dc7-f5d9ff5a87a0 den Titel S-MNGR-#1-PLAN-0011. Das belegt die Umbenennung; die Erstregistrierung ist inzwischen im Skill vorgeschrieben.
- **Viewer:** W-018 verlangt delimiterfreie Legacy-Einträge. Gemäß Nutzerergänzung erstellt und validiert der Agent das Testprofil und übergibt Pfad samt kurzer Prüfanleitung. Der Nutzer öffnet es im installierten Viewer und bestätigt die lesbare Anzeige mit Versionsangabe. Bis zur Rückmeldung bleibt die manuelle Abnahme offen; keine Desktopbedienung durch den Agenten voraussetzen.
- **Legacy:** W-021 verlangt vor Entfernung einen Bericht der exakten Ziele und nicht geheimen Wertabweichungen; die Löschung selbst ist noch nicht ausgeführt.
- **Tests:** W-022 verlangt bestandene Läufe mit Plattform und Python-Version; ungestartete CI bleibt unbewiesen.
- **Non-goals:** Der überholte Draft-Aktivierungssatz wurde entfernt. Veröffentlichung und Installation bleiben ausgeschlossen.


## W-018 und W-019: Korrekturen nach dem Umsetzungsreview

W-018 schreibt wieder Legacy-Listen und LF. Windows/Python 3.14: 46 Validator-
und 21 Selectortests bestanden einschließlich Klartext- und CRLF-Lesevertrag.
Das temporäre Viewerprofil ist valide; die manuelle Prüfung im alten Viewer
samt Versionsangabe steht aus.

W-019 schreibt die Erstregistrierung des aufrufenden Managers als #1 mit
Task-/Host-ID und Titelwechsel ausdrücklich vor. Resume erhält Nummer und Titel;
Nachfolger zählen je Rolle weiter. Die Lifecycle-Regel erlaubt diesen eigenen
Titelwechsel; fremde und durch Reconciliation gefundene Aufgaben bleiben geschützt.
Die Titelvalidierung akzeptiert nur kanonische Plan-/Einheiten-IDs.
Windows/Python 3.14: 20 Titel-/Lifecycletests bestanden. Echte Selectoraufrufe
für W-019/step-1 und W-026/step-2 enthalten ADR-0066. Ein Koordinatorprompt mit
Marker an Byte 0 wurde vom Lifecycle-Helper als #2 akzeptiert.
Dies war ein Payloadcheck ohne Taskstart; native Rolloverabnahme bleibt W-026.
Ask-/Workflow-Lifecyclekopien und Shared-Snapshot wurden synchronisiert.
Installierbare Pakete folgen W-024.

W-018: Der Nutzer öffnete das Testprofil erfolgreich im installierten
scoville-plan-viewer-v1.3.2-windows-x64. Sein Screenshot zeigt Plan und alle drei
Evidence-Einträge einschließlich Umlauten und Pfad vollständig. Der erste Versuch
hatte den übergeordneten Ordner gewählt; nach Auswahl von viewer-profile war
die Anzeige korrekt. Damit ist die manuelle Abnahme erfolgt.

W-021: Die einzige über die bekannten Ask-Skillpfade gefundene persönliche
Altdatei <codex-home>/skills/ask-claude-for-codex/config.json wurde nach
Bericht von Fable/medium und 50 USD Budget entfernt. Test-Path meldet False.
Keine Werte wurden übernommen. Die aktive Erhaltungsanweisung entfällt.
Der bestehende Default-/Override-Test besteht unter Windows/Python 3.14:
Lesen legt nichts an; Projektwerte und Aufrufwerte behalten ihre Priorität.
Die ältere Aussage zur damals erhaltenen Altdatei bleibt als Historie bestehen.

W-020: Workflow akzeptiert dieselben acht Syntaxwerte wie Plan. Ask prüft
native Werte gegen den Modellkatalog; Claude behält die CLI-spezifische Prüfung.
Setup setzt nach ADR-0067 nur low/medium/high/xhigh und erhält manuelle
Zusatzwerte bei anderen Änderungen. Windows/Python 3.14: 15 Workflowtests,
2 Setuptests und der Ask-Test aller acht Werte bestanden. Modellkataloge sind
kontrollierte Fixtures; keine neuen Modellaufrufe. Das Plan-README enthält
Reasoning- und Modellbeispiele. Die gestarteten W-020-Felder bleiben historisch;
die nachträgliche Nutzerpräzisierung ist hier und in ADR-0067 festgehalten.

## W-022 und W-023: Portable Prüfungen und bereinigte Quellen

Windows/Python 3.14 und Ubuntu 24.04/Python 3.12.3: Shared 53; Suite 24;
Plan 68; Ask 22; Workflow 16; Setup 2 Tests grün. Ubuntu lässt einen
Windows-spezifischen Test aus. Der finale Linuxlauf verwendet einen isolierten
Quellstand mit lokal initialisiertem Testrepository; keine Projektcommits.
Frühere Fehlversuche durch veraltete Assertions und unvollständige Testumgebung
sowie der während Dokumentationsänderungen ungültige Vergleich sind keine
Abnahmenachweise. Endstand ohne parallele Quelländerungen geprüft.

Der Webtools-Test nutzt einen festen Katalog statt echter App-Server-Abfragen.
Der Runner verwendet Path.home(). CI prüft Shared/Suite/Setup zusätzlich,
mit gebündelten Shared-Quellen als Geschwisterverzeichnis. Keine GitHub-Matrix
ausgelöst oder beobachtet; W-002 bleibt deshalb offen. Laufzeitanweisungen wählen
Python 3.11+ ausdrücklich. Der erzeugte Workerauftrag verwendet den tatsächlich
laufenden Interpreter. Plan bleibt ohne Python nutzbar.

Originalresultat und verdichteter Snapshot sind getrennt geprüft; alle drei
Arbeitsrollen beenden abgeschlossene eigene Arbeit ohne neuen Checkpoint.
Das sind lokale Vertragsprüfungen und keine native W-026-Abnahme.

Unbenutzte compute_decision_batch.py samt Test und die beiden memberlokalen
resolve_prompt_profile.py-Kopien sind entfernt. Manifest und aktive Aufrufer
verwendeten sie nicht. Der weiterhin genutzte Shared-Profilhelper bleibt erhalten.
Der Featurevertrag verweist auf die verbleibenden Batchregeln. Batch-IDs werden
nicht mehr als Viewerfunktion beschrieben. Unreleased und aktuelle Workflowtexte
beschreiben den heutigen Ablauf; veröffentlichte Historie bleibt unverändert.
Die README-Projektionen wurden über den Builder erstellt; Codex-only-Mitglieder
verwenden die Codex-Suite und keine widersprechende Standalone-Aussage.

## W-024: Erzeugte Pakete und Zeilenenden

General- und Codex-Suite wurden unter
<workspace-root>/skills/temp/release/plan-0011-review-fixes gebaut.
Die tatsächlichen packages/-Kopien verwenden für allgemeine Mitglieder das
General-Profil und für Codex-only-Mitglieder das Codex-Profil. Dadurch bleibt
Plan in der allgemeinen Kopie ohne Python verwendbar. Der native Testkandidat
ist das separat vollständig gebaute Codex-Profil.
Alle sieben Paketinventare entsprechen bytegenau ihrem aktuellen Payload;
sämtliche Textdateien sind LF. Der gezielte Buildertest deckt echte CRLF-Quellen,
README-/Fragmentexpansion und Shared-Helper-Ausgaben ab; Binärdateien bleiben
bytegleich. Keine zusätzliche Normalisierung war notwendig.
Obsolete generierte Dateien sowie die zwei abgelösten separaten UI-Paketkopien
wurden nach Zielprüfung entfernt. Quellmitglieder und Git-Historie bleiben erhalten. Keine Installation,
Veröffentlichung oder ausführbare Viewerdatei wurde erstellt.

## W-026: Vorbereitung der nativen Fortsetzung

Der vorhandene Fixturestand wurde mit dem W-024-Codex-Paket abgeglichen.
Die Originalantwort aus read_thread für Aufgabe
01a0d8ec-5760-75b3-9972-eda12d278f59 und Turn
01a0d8ed-252a-7531-a1e5-4f9d7b61493a ist mehrzeilig und wird vom gebauten Parser
akzeptiert. Ihr tatsächlicher Status bleibt context_handoff; er wurde nicht
in completed umgedeutet. Ein erster PowerShell-Pipeversuch fügte eine zusätzliche
Leerzeile hinzu und wurde korrekt abgelehnt; die erneute Byteübergabe bewahrte
den Originaltext und bestand. Das ist ein weiterer Grund die Originalantwort
ohne zusätzliche Ausgabeformatierung weiterzureichen.
Keine neue native Testaufgabe wurde gestartet. Die aktuelle create_thread-
Schnittstelle verlangt einen ausdrücklichen Nutzerauftrag zur Aufgabenerstellung.
Dieser bleibt vor der realen Review-/Reparatur-/Rolloverprüfung zu klären.
W-025 wartet gemäß Abhängigkeit auf W-026. W-001 und W-002 bleiben unverändert offen.

W-026 gestartet: Nutzer genehmigt ausdrücklich neue native Testaufgaben mit
SOL 6 Medium. Koordinator 01a0d933-aef4-77c3-a91a-2bf5bf3fa6e9 auf local
(S-MNGR-#3-PLAN-0001) setzt das vorhandene Fixture mit dem W-024-Paket fort.
Er prüft zuerst die verbleibende W-002-Abnahme und danach aktuellen Manager-
und Worker-Rollover an W-003. Modelle wurden vor Start im Fixture auf
SOL 6 Medium gesetzt; Ein-Prozent-Schwellen sind gezielte Testwerte.
Reparaturgrenze und Stopp/Wiederaufnahme bleiben separate offene Prüfungen.

### Beobachteter Rollover mit dem W-024-Paket

Koordinator #3 (01a0d933-aef4-77c3-a91a-2bf5bf3fa6e9) übernahm das
ursprüngliche mehrzeilige Workerresultat korrekt. Nachfolger-Worker #4
(01a0d936-4344-7040-89f1-6a6982b47c18) bestätigte den vorhandenen Fix und
einen bestandenen Test. Reviewer #1 (01a0d938-42ff-7be0-b9ba-5158e4d6ddec)
prüfte unabhängig und meldete pass ohne Befunde. Alle neuen Aufgaben liefen
mit gpt-6-sol/medium.

Der echte Manager-Checkpoint nach W-002 meldete rollover bei 93720 von
258400 Kontexttokens und absichtlicher Ein-Prozent-Testschwelle. Koordinator
#4 (01a0d93b-c687-7832-9cf6-c2854739c9c8) startete als tatsächlicher
Nachfolger und wartete auf das Ende von #3 vor eigenen Änderungen.
Worker #5 (01a0d93e-f578-76b3-a143-7d129865f6b2) übergab W-003 nach dem
Lesen vor dem Schreiben mit frischer Telemetrie von 28237/258400 Tokens.
Worker #6 (01a0d940-8157-7292-b30b-419e07d8bfc4) erledigte nur den
Restauftrag und meldete completed ohne weiteren Checkpoint. Die erhaltene
Überschrift und beide Sollzeilen kommen jeweils genau einmal vor.

Originalresultate und Task-IDs wurden vor Archivierung gespeichert. Die
nativen Archivierungsantworten für beendete Kinder und Vorgänger wurden
mit archived:true verifiziert; Übergabevorgänger erst nach gestartetem
Nachfolger. Der letzte Manager bleibt sichtbar. Die Rollen nummerierten
getrennt weiter bis Manager #4 und Worker #6. PLAN-0001 des Fixtures ist
abgeschlossen; dessen Validator meldete null Fehler und Warnungen.
Diese Beobachtung belegt die realen Übergaben und Ergebnisübernahme.
Reparaturgrenze und Stopp/Wiederaufnahme sind weiterhin offen.

### Nativer Stopp und Wiederaufnahme

Für Fixturelauf 2 wurden vor Start die Testschwellen auf 99/99 gesetzt.
Der ausdrücklich gesendete Stopp erreichte den aktiven Worker
01a0d946-0bdf-7c71-ac90-609e53df3722 in seiner Beobachtungsphase. Er endete
mit einem gültigen blocked-Originalresultat. Der Manager beobachtete genau
eine erste Zeile und keine zweite Zeile und pausierte W-001. Er startete
weder Review noch Nachfolger oder nächste Einheit. Der Worker blieb sichtbar.
Belegt sind Zustellung und unterbliebener Folgeschreibvorgang; eine sofortige
Unterbrechung des 60-Sekunden-Wartens ist aus dem Hostprotokoll nicht ableitbar.

Die getrennte Resume-Nachricht setzte dieselbe Aufgabe mit derselben Nummer
fort (Turn 01a0d949-3627-7872-8704-8113ae615a67). Sie schrieb nur die zweite
Zeile und gab completed zurück. Worker und Manager zählten unabhängig beide
Zeilen genau einmal; auch die direkte Nachprüfung bestätigte den Dateiinhalt.
Kein zweiter Worker und keine Wiederholung der Wartephase. Die Planprüfung
bestand; der nächste Manager-Checkpoint meldete mit frischer Telemetrie
continue. Die kontrollierte Reparaturprüfung läuft anschließend separat.

### Reparaturschleife und Grenze: native Abnahme

Der Manager beendete den Fortsetzungsturn am vorgesehenen Entscheidungspunkt
nach drei Reparaturen. Alle Aufgaben verwendeten SOL 6 Medium. Die drei Fixer
stellten jeweils die richtige Addition her und bestanden den unveränderten
Test. Erst nach ihrem Ende setzte der Testleiter den bekannten Fehler erneut
ein. Vier frische Reviewer fanden ihn jeweils im tatsächlichen Dateistand.
Das prüft die Schleife bei kontrolliert wiederkehrendem Fehler, nicht drei
spontan fehlgeschlagene Implementierungen.

| Rolle | Native Task-ID |
| --- | --- |
| Executor | 01a0d94b-a2de-7b41-bc67-af9602226022 |
| Reviewer 1 | 01a0d94d-ad45-7342-a3b2-a89324a11d51 |
| Repair 1 | 01a0d94f-d2ba-7321-8d46-c2bff43aba6e |
| Reviewer 2 | 01a0d952-7971-7e01-9d2b-1316996ac0f0 |
| Repair 2 | 01a0d954-8505-7550-841e-9b4287874d7a |
| Reviewer 3 | 01a0d957-0f32-7901-b904-d5f90aa039cc |
| Repair 3 | 01a0d959-778c-7f12-9e05-89442c5cf3d6 |
| Reviewer 4 | 01a0d95b-f82d-7720-b938-442c7307f305 |

Nach dem letzten changes_requested wurde keine vierte Reparatur erzeugt.
Fixture-W-002 bleibt paused und unaccepted; der sichtbare Manager verlangt
Disposition. Das ist der erwartete Testendzustand, kein offener Suitefehler.
Die archivierten Kinder haben gesicherte Originalresultate und geprüfte
Archivierungsantworten. Der Planvalidator bestand mit null Fehlern/Warnungen.
Der Fortsetzungsturn dauerte rund 24 Minuten einschließlich Wiederaufnahme,
Reviews, Reparaturen und Nachweispflege. Kein belastbarer Vorhervergleich
für Geschwindigkeit, Tokenkosten oder Gesamtkosten liegt vor.

### Abschließender Abgleich der zwölf ADR-0064-Bereiche

Die Quellzuordnung der obigen W-010-Tabelle wurde am W-024-Stand erneut
geprüft. Launcher/Handshake, Parkaktivierung, Guard-Generationen, Bundling
und Transportbelege bleiben entfernt. Direkter Dispatch und ein Step pro
Worker wurden real benutzt. SKILL.md erzeugt kein eigenes Goal und macht
den AGENTS-Einrichtungsblock optional. Die fünf Routen sowie Overrides
bleiben durch die vorhandenen Resolver-/Selectorprüfungen abgedeckt.
Reparaturen 1 bis 3 verwendeten im nativen Test den unveränderten konfigurierten
Modellweg. Die drei zuvor offenen Tabellenzeilen Manager-Rollover,
Worker-Übergabe und tatsächliche Code-Review sind durch die oben genannten
Aufgaben belegt. Archivierung erfolgte nach Ergebnisaufbewahrung bzw.
Nachfolgerstart; ein fehlgeschlagener Archivierungsaufruf wurde nicht künstlich
ausgelöst. Sein nicht blockierender Fehlerweg bleibt durch Vertrag und
Lifecycle-Tests belegt. Echte Codeprüfung, reine Textänderung ohne Review und
die Reparaturgrenze wurden beobachtet. Kein Commit wurde autorisiert oder erstellt.

Die bereits bestandenen Kontextprüfungen decken Defaultgrenzen 25/75,
Vergleichsoperatoren, alle Arbeitsrollen, Overrides und fehlende/veraltete
Telemetrie ab. Die nativen Rollover benutzten bewusst ein Prozent; ein
Live-Lauf bis 75 Prozent wird nicht behauptet. W-026 ist damit für den
beschriebenen begrenzten Abnahmeumfang abgeschlossen. W-025 folgt jetzt.

## W-025: Kürzere Plan-Anweisungen mit erhaltenen Ergebnissen

SKILL.md und references/native-work-items.md sind gekürzt. Zuständigkeiten,
Leserouten und Entscheidungsregeln stehen kompakter im Einstieg; Work Items
verweisen für Syntax und Formulierung auf die vorhandenen Besitzer P/G/E.
Warteschlange, explizite Priorität, Rückkehr nach Umleitung, unveränderliche
Historie und die enge Annotation-Ausnahme bleiben beschrieben. Es entstand
keine zusätzliche Datei, Konfigurationsschicht oder Hashpflicht.

Die gleiche Menge an Quelldateien je Vergleichsroute enthält weniger Zeichen
(UTF-8 decodiert; Includes und Profilmarker noch nicht expandiert):

| Operation | Referenzen neben SKILL.md | Vorher | Nachher | Reduktion |
| --- | --- | ---: | ---: | ---: |
| Einfügen | P W E G V | 54794 | 46165 | 15.8 % |
| Fortschreiben | P W E V | 46939 | 38310 | 18.4 % |
| Finaler Abschluss | P W E L V | 53416 | 44787 | 16.2 % |
| Wiederaufnahme | R P W E V | 52782 | 44153 | 16.4 % |

R = read-only.md; P = native-plan-format.md; W = native-work-items.md;
E = native-editing.md; G = planning-granularity.md;
L = native-project-lifecycle.md; V = profile-validation.md.
Die Tabelle misst standardisierte Leserouten, keine beobachteten Tokens.

Zwei frische native Aufgaben mit gpt-6-sol/medium bekamen denselben Auftrag
und identische Ausgangsfixtures. Nur die beiden Anweisungsdateien unterschieden
sich zwischen ihren gebauten Codex-Paketen:

- Vorher: 01a0d960-9591-78a0-9fa9-4f4f921beac4, Turn
  01a0d960-990a-7480-9c09-fe111a319fab.
- Nachher: 01a0d963-a01a-7e33-819a-b8850c7760c0, Turn
  01a0d963-a3e2-7c02-b749-6c28423162e6.

Beide fügten W-003 ein, schrieben W-001 nach dem tatsächlichen Lesen fort,
schlossen W-001 mit beobachteter Validator-Evidence ab und pausierten/resumierten
W-002. Alle fünf gespeicherten Zwischenstände je Fassung bestanden Validator
und Selector mit Exit 0. Die eigene Nachprüfung bestätigte Itemreihenfolge,
Statuswechsel, unveränderte gestartete Inhalte, bytegleiche ADR und Index,
W-003-Abhängigkeit sowie dessen weiterhin offenen Status. Keine Abnahme von
W-002 oder W-003 wurde erfunden. Der Vorherlauf korrigierte einen Escape-Fehler
in seiner temporären Befehlsprotokolldatei; das war kein Planformatfehler.

Die nativen Leseaufrufe zeigen: Vorher wurden SKILL.md und R/P/W/E/V geladen,
nachher zusätzlich G. Der Vorherlauf ließ damit die für neue Ergebnisgrenzen
erforderliche Granularitätsreferenz aus. Beide luden ihre Referenzen vorab für
die gesamte Operationsfolge und verwendeten sie weiter. Einmalig gezählte
Zeichen dieser tatsächlich gelesenen Paketdateien: 50368 vor und 49957 nach
der Kürzung, also 0.8 Prozent weniger trotz zusätzlich geladenem G.
Wiederholte Teil-/Vollreads unterschieden sich ebenfalls. Die beobachteten
220 bzw. 155 Sekunden sind je ein Einzellauf und kein belastbarer Nachweis
allgemeiner Laufzeit-, Kosten- oder Tokenersparnis.

Windows/Python 3.14: alle 68 Plan- und 24 Suite-Tests grün. Beide
Distributionsprofile gebaut. Die installierbare Plan-Kopie entspricht dem
General-Payload mit 20 Dateien; nur die zwei Anweisungsdateien änderten sich,
alle Textdateien bleiben LF. Keine Installation oder Veröffentlichung.
Skill Creators quick_validate lehnt weiterhin das vorhandene compatibility-
Frontmatterfeld ab. Das ist der bekannte W-007-Werkzeugkonflikt, kein neuer
Fehler des Umbaus; dieser Aufruf wird nicht als bestanden ausgegeben.
Die Suite-Buildprüfung und nativen Fälle sind bestanden.

Die letzte Textprüfung präzisierte anschließend nur den Satz zum vollständig
fehlenden Profil: Abwesenheit wird ausschließlich bei drei fehlenden
Profilpfaden gemeldet, ein Teilprofil bleibt ein Stoppgrund. Beide Profile
wurden danach neu gebaut und die Paketkopie aktualisiert. Die nativen
Vergleichspakete bleiben unverändert gespeichert; ihre obigen Messwerte
beziehen sich auf den tatsächlich getesteten Stand.

Beide W-025-Testaufgaben wurden nach Sicherung der Ergebnisse und IDs einmal
archiviert; beide nativen Antworten bestätigten archived:true. Der finale
Workflow-Testmanager bleibt am beabsichtigten Entscheidungspunkt sichtbar.
PLAN-0011 hat nur noch W-001/HOST-POLICY und W-002/CI-PLATFORMS offen.
Die früher abgewiesene Rechner-/Cacheaktion wurde weder wiederholt noch
umgangen. Die Drei-Plattform-GitHub-Matrix wurde nicht gestartet.
