---
format_version: 1
id: PLAN-0018
status: active
created: 2026-09-27
updated: 2026-09-27
current_item: W-006
---

# Workflow und DIVI-Projektvertrag verschlanken

## Goal

Weniger wiederholte Einarbeitung, Reviews, Versionspflege und Testvorbereitung bei gleicher fachlicher Abnahme. Workflow besitzt Rollen und Übergaben, Plan besitzt Arbeitsnachweise, der DIVI-Projektvertrag ergänzt nur projektspezifische Anforderungen. Explizite Nutzer- und Projektvorgaben zum Review-Rhythmus gelten vor Skill-Defaults.

Der Nutzer hat die Umsetzung beauftragt, beginnend mit dem DIVI-Projektvertrag. Suite-Quellen liegen hier, DIVI-Dateien im bereits gespeicherten Projekt DIVI5 Plugin. Auf ausdrückliche Nutzerkorrektur setzt diese Session die DIVI-Vertragsarbeit mit einem zugeordneten Source-Worker um. Der DIVI-Manager bleibt Besitzer von PLAN-0012 und den Produktentscheidungen; er startet währenddessen keine konkurrierenden Vertrags-/Helper-Änderungen. Vorher seinen aktuellen Stand und die bereits beauftragten Astra-Ergebnisse zu Neutral-Reset, Testpreset und M10-Lücken übernehmen.

## Non-goals

Keine Produktfehlerbehebung, neue Workflow-Modi, zusätzlichen Zustandsregister, pauschalen Retries oder Volltestwiederholungen. Keine Änderung der 40/60-Kontextschwellen. Keine rückwirkende Neuerfindung von Abnahmen oder Löschung historischer Nachweise. Kein DIVI-Push, Produktrelease, Remote-Test oder Deployment. Die ausdrücklich beauftragte Skill-Veröffentlichung gehört zu W-006.

## Work items

### W-003 DIVI-Versionierung an geprüfte Kandidaten statt an jeden Edit binden
Status: done
Depends on: []
Blocked by: []
Decisions: []
Outcome: Ein zusammengehöriger Produktstand benötigt einen konsistenten Versionswechsel, ohne bei jedem Bearbeitungsschritt mechanisch Testdaten und Metadaten zu verändern.
Acceptance: Der Vertrag verlangt keinen Versionssprung vor jedem einzelnen Edit. Vor Installation oder Paketbau eines gegenüber dem zuletzt geprüften/installierten Stand geänderten Kandidaten sind Identität, erforderliche Cache-Invalidierung und Metadaten konsistent. Keine unterschiedlichen installierten Kandidaten unter ununterscheidbarer Identität. Verhaltens-Snapshots ändern sich nur bei geändertem erwarteten Verhalten; reine Kandidatenmetadaten werden getrennt behandelt. Erforderliche Produkt-/Import-Metadaten und Übersetzungskonsistenz bleiben geprüft. Eine unerwartete Abweichung wird weiterhin erkannt.
Steps:
1. Im DIVI-Projekt `docs/general-rules/project-workflow-contract.md`, Source-Workflow-Check, Git-Hook, `tools/validation/check-divi5-version-consistency.ps1`, Generatoren und M10-Snapshot-Leser anhand ihrer tatsächlichen Abhängigkeiten abgleichen. Versionierte Cache-Schlüssel und bereits vorhandene Kandidaten-/Quellhash-Nachweise berücksichtigen.
2. Einen Versionswechsel für einen zusammengehörigen Kandidaten vor dessen erstem Build/Installation vorsehen. Weitere Produktkorrekturen nach Installation brauchen erneut eine eindeutig unterscheidbare Kandidatenidentität und korrekte Cache-Invalidierung. Existiert dafür keine geeignete einfache Hash-/Buildbindung, weiterhin die Version erhöhen; kein neues Identitätssystem bauen.
3. `tools/playwright/final-product-test/data/m10-final-preset-snapshots.json` prüfen: `pluginVersion` und `setupResetPresets.generated_from.plugin_version` sind derzeit an die Produktversion gekoppelt. Versions-Provenienz aus Verhaltensvergleichen trennen, ohne erwartete Werte aus dem zu prüfenden Produkt selbst zu erzeugen oder echte Import-/Export-Verträge zu ignorieren.
4. Nachweisen: mehrere Edits desselben noch nicht installierten Kandidaten; neuer Kandidat nach Installation; reine Versionsänderung ohne falschen Verhaltensfehler; absichtlich geänderter Presetwert wird erkannt; kein Wiederverwenden ungültiger Cache- oder alter Testnachweise.
Evidence: ../../../temp/2026-09-27-plan18/version-check-results.json: Identität und Provenienz geprüft; candidate-reader prüft unveränderte Erwartungen. Finalreview folgt in W-005.

### W-004 M10-Vertrag bündeln und nachgewiesen saubere Folgetests beschleunigen
Status: paused
Depends on: [W-003]
Blocked by: []
Decisions: [ADR-0100]
Outcome: Der Projektvertrag nennt die verbindlichen M10-Ergebnisse und verweist für deren Durchführung auf ein einziges Runbook. Folgetests wiederholen keine gültige Erstvorbereitung.
Acceptance: Einmalige Erstvorbereitung und anschließender Reset sind klar getrennt. Ausgewählte Testseiten sind vor Aufbau neuer Testdaten vollständig und kontrolliert bereinigt, einschließlich relevanter gespeicherter Werte und Ownership-Zustände; Überdecken alter Nutzerwerte genügt nicht. Unbeteiligte Seiten bleiben unverändert. Der normale Wirkungsnachweis lautet vollständiges Testpreset laden und erzeugtes CSS plus berechnete Frontend-Styles messen. Builder-Interaktionsprüfungen gelten nur für ihre eigenständigen Kriterien. Bereits gültige Abnahmen bleiben erhalten; nur betroffene Punkte werden erneut geprüft. Detailregeln haben genau einen Besitzer.
Steps:
1. Aktuelles Astra-Medium-Review zu Neutral, vollständigem Testpreset und Lücken übernehmen. Bereits korrigierte Regeln nicht nochmals ändern. Der Neutral-Wechsel allein gilt nur dann als Reset, wenn seine Wirkung nachgewiesen ist; sonst kleinste erforderliche Bereinigung der ausgewählten Testseiten ergänzen.
2. In `docs/general-rules/project-workflow-contract.md` nur Ziele, Zuständigkeit, berechtigte Testsysteme, geschützte Daten, Kandidatenidentität, Editionskonfiguration und Abnahmegrenzen behalten. Ausführungsdetails in `tools/playwright/final-product-test/M10-RUNBOOK.md` bündeln und von Vertrag, README und betroffenen Helfern eindeutig referenzieren. Keine erforderliche Schutzregel ersatzlos streichen.
3. Bestehende Helfer auf einmalige vollständige Vorbereitung, schnelle saubere Folgetests und nötige Abschlusswiederherstellung ausrichten. Ein neuer Prozess oder Worker macht die Erstvorbereitung nicht automatisch ungültig. Echte Zustands-, Fixture- oder Kandidatenänderungen gezielt berücksichtigen; keine zusätzliche Ablaufverwaltung einführen.
4. Repräsentativ auf D4 und D5 nachweisen: verschmutzte Testseite wird vollständig zurückgesetzt; Testwerte wirken im Frontend; unbeteiligte Inhalte bleiben erhalten; Fehler verlassen keinen unklaren Testzustand. Vorhandene erfolgreiche Erstvorbereitung wiederverwenden. Vorbereitungszeiten vor/nach Änderung vergleichen und die tatsächlich betroffenen Reset-/Editionsvarianten abdecken, ohne Gesamtlauf.
Evidence: D4/D5 Reset, D4 Effekt und D5-Recovery bestanden; D5 Importeffekt offen. Bericht: ../../../temp/2026-09-27-plan18/divi-evidence.md.
Next action: D5-Produktimport mit dem Manager klären, dann ausschließlich den fehlenden D5-Wirkungsnachweis abschließen.

### W-001 Review und Worker-Fortsetzung am zusammengehörigen Ergebnis ausrichten
Status: done
Depends on: []
Blocked by: []
Decisions: [ADR-0099]
Outcome: Zusammengehörige Arbeit wird ohne unnötige Rollenwechsel ausgeführt und zum geltenden fachlichen Abschlusszeitpunkt unabhängig geprüft.
Acceptance: Eine Projektregel für ein Review je Planpunkt erzeugt keine zusätzlichen Pflichtreviews je Step oder Step-Gruppe. Zwischenstände dürfen nach ihren gezielten Checks fortgesetzt werden; der Planpunkt bleibt bis zum erforderlichen Review offen. Das Abschlussreview umfasst neue Änderungen, deren Zusammenwirken und offene Abnahme. Bereits akzeptierte unveränderte Teile werden nicht erneut geprüft. Ein ausdrücklich verlangtes Zwischenreview bleibt möglich. Ein Rollover setzt dieselbe Arbeit mit erledigten und offenen Teilen fort. Es gibt keinen zusätzlichen Leichtmodus.
Steps:
1. In `members/scoville-workflow-for-codex/scoville-workflow-for-codex/references/operations.md` und `operations-dispatch.md` Review-Zeitpunkt von Dispatch-Grenzen trennen. Den genehmigten neuen Vertrag vor Umsetzung mit ADR-0093 und betroffenen weiteren Decisions abgleichen und deren Ablösung im vorhandenen ADR-System festhalten.
2. Zusammengehörige Steps weiterhin in Reihenfolge bündeln. Vorhandenen Worker für notwendige Korrekturen weiterverwenden, sofern er verfügbar ist und ausreichenden Kontext besitzt; das unabhängige Review bleibt separat. Bei Kontextbedarf den normalen Rollover nutzen. Rollenauftrag, `build_dispatch_prompt.py` und Tests nur soweit nötig anpassen.
3. Normale Infrastrukturfehler im lokalen Ablaufnachweis behalten. Nur konkrete Blockaden oder Auswirkungen auf die Abnahme in den Plan aufnehmen. Kein erneuter Dispatch bei unklarer Erstellung und keine Reparaturrunde wegen bloßer Formatunterschiede.
4. Fälle prüfen: drei zusammengehörige Steps mit einem Abschlussreview; begründetes Zwischenreview; Korrektur mit anschließend nötigem Review; Rollover ohne Wiederholung; unklarer Dispatch ohne doppelten Worker.
Evidence: Umgesetzt; SOL-Helperfälle und Luna 6 High bestanden; Astra ohne Skill-Findings. development/luna-tests/plan18-results.md.

### W-002 Planänderungen und Evidence ohne Ersatzpunkt-Ketten ermöglichen
Status: done
Depends on: []
Blocked by: []
Decisions: [ADR-0099]
Outcome: Pläne bewahren Ergebnis und Entscheidungen, ohne Chatprotokolle anzusammeln oder für formale Aktualisierungen neue Arbeitspunkte zu erzwingen.
Acceptance: Evidence enthält knapp Ergebnis, entscheidenden Nachweis mit Verweis und gegebenenfalls Commit oder offene Grenze. Ausgelagerte Historie bleibt erreichbar. Bestehende verbindliche Abnahme wird nicht still gelockert. Ein angenommener ADR darf einem gestarteten Punkt mit nachvollziehbarem Änderungsgrund hinzugefügt werden, ohne den Punkt zu ersetzen. Rein formale Korrekturen sind nur bei unverändertem Ergebnis und Prüfungsumfang zulässig. Materiale Änderungen brauchen weiterhin ausdrückliche Entscheidung. Reparaturen innerhalb derselben Ergebnis- und Abnahmegrenze bleiben dort; eigenständige Ergebnisse erhalten eigene Punkte.
Steps:
1. `members/scoville-plan/scoville-plan/references/edit.md`, `planning-granularity.md`, relevante Decision-Regeln und Validatoren abgleichen. Eine kurze Ausnahme für additive angenommene ADR-Verweise und nachgewiesen rein formale Aktualisierungen vorsehen. Abgeschlossene Historie nicht als neue Ausführung umschreiben.
2. Acceptance auf Verhalten und Verträge ausrichten. Versions- oder Zählwerte nur festschreiben, wenn genau der Wert Vertragsbestandteil ist. Tatsächliche Kandidatenidentität im Nachweis erhalten; Gleichheit allein durch dieselbe Versionsnummer nie behaupten.
3. Lange bestehende Evidence bei ausdrücklich beauftragter Bereinigung verlustfrei in einen lokalen Bericht auslagern und knapp verlinken. Keine neue Berichtsdatenbank. Im laufenden DIVI-Plan führt das ausschließlich dessen Coordinator durch.
4. Fälle prüfen: ADR-Ergänzung ohne Ersatzpunkt; formale Versionsreferenz; verweigerte materielle Abnahmelockerung; Testreparatur im selben Punkt; eigenständiger Befund; Wiederaufnahme mit kurzen, erreichbaren Nachweisen.
Evidence: Umgesetzt; SOL-Validatorfälle und Luna 6 High bestanden; Astra ohne Skill-Findings. development/luna-tests/plan18-results.md.

### W-005 Zusammenspiel gezielt prüfen und Änderungen geordnet übergeben
Status: done
Depends on: [W-001, W-002, W-003]
Blocked by: []
Decisions: [ADR-0100]
Outcome: Skill- und Projektregeln führen zu einem konsistenten, kürzeren Ablauf mit ausreichendem Kontext und unveränderter fachlicher Abnahme.
Acceptance: Gezielte realistische Modellfälle und betroffene Helper-Tests bestehen. Übergaben bleiben unmittelbar verwendbar. Kein doppelter Review-Zwang, Ersatzpunkt nur für Metadaten, automatischer Volltest-Neustart oder unnötiger Builder-Eingabeschritt. Gemessene Aufrufe, Übergabeumfang und verfügbare Tokenwerte sind von Schätzungen getrennt. Der offene D5-Produktnachweis bleibt in W-004; lokale Übernahme und Wiederaufnahme durch den Manager werden in W-006 nachgewiesen.
Steps:
1. Betroffene Quellen und installierbare Builds strukturell prüfen. SOL 6 Medium führt die geänderten Workflow-/Plan-Fälle mit realistischen zusammengehörigen Steps, Korrektur, kurzem Nachweis und Rollover aus. Externe Wirkungen simulieren; bestehende Testumgebung und Runner nutzen.
2. Nach allen Änderungen die betroffenen Workflow-/Plan-Fälle gezielt mit GPT-6 Luna High gegen gebaute Pakete prüfen. Tatsächliches Modell und Effort festhalten. Keine neue pauschale 45-Fall-Serie; der Nutzer hat für diesen Abschluss gezielte Tests beauftragt. Fehler ursächlich klären und betroffene Fälle erneut prüfen.
3. Ein unabhängiges Astra-Medium-Review prüft den finalen zusammenhängenden Regelstand einschließlich SOL-/Luna-Befunden auf widersprüchliche Zuständigkeiten, unnötige Prozessschritte und verlorene Schutzwirkung. Findings gezielt korrigieren und nur betroffene Nachweise erneuern. Lokale Installation und Veröffentlichung folgen in W-006.
Evidence: SOL und Luna je sechs Fälle; Astra prüfte Regelstand ohne Blocker. D5-Effekt offen; development/luna-tests/plan18-results.md.

### W-006 Lokale Skills aktualisieren, DIVI fortsetzen und Releases veröffentlichen
Status: in_progress
Depends on: [W-005]
Blocked by: []
Decisions: [ADR-0100]
Outcome: Die geprüften Änderungen sind lokal und auf GitHub verfügbar; der DIVI-Manager führt den beauftragten Prozess mit den aktuellen Regeln fort.
Acceptance: Geänderte lokale Codex-/Claude-Skills stimmen mit den jeweiligen geprüften Builds überein; Workflow bleibt Codex-only. Der DIVI-Manager erhält die genaue Liste geänderter Skills, lädt sie erneut und setzt beim ersten zulässigen offenen Punkt fort. Ungeklärte Produktentscheidungen werden nicht still entschieden. Jede geänderte autorisierte Distribution erhält einen Push und neuen Release mit verifizierten Remote-Dateien, Tags und Assets. Unveränderte Distributionen erhalten keinen neuen Release. Viewer-Assets werden bei unverändertem Viewer nur mit geprüftem Herkunfts-/Hashnachweis wiederverwendet.
Steps:
1. Vor dem Release die Aussage „The Skill requires no network access.“ einschließlich gleichlautender Varianten aus den kanonischen Scoville-README-Fragmenten entfernen und READMEs neu erzeugen. Nach bestandenen gezielten Luna-Tests und finalem Review die betroffenen Skills aus den geprüften Builds lokal installieren und ihre Dateibestände prüfen; aktive DIVI-Aufträge an sicherer Grenze halten.
2. Dem bekannten DIVI-Manager die geänderten Skills und Vertragsregeln nennen, erneutes Laden und Wiederaufnahme ausdrücklich beauftragen. Seine tatsächlich beobachtete Reaktion festhalten, Zustellung allein nicht als Neustart melden. Nur von offenen Entscheidungen unabhängige Arbeit starten.
3. Nach dem GitHub-Skill alle geänderten veröffentlichten Ziele aus den kanonischen Quellen bauen, committen, pushen und mit neuen Releases veröffentlichen. Workflow ausschließlich in der Codex-Suite. Neue Downloads und vollständige Remote-Bäume prüfen, dann abgelöste Releases/Tags bereinigen und lokale öffentliche Projektionen synchronisieren.
Evidence: []
Next action: Geprüfte lokale Installation, Manager-Reload und neue GitHub-Releases ausführen; W-004 bleibt offen.
