# W-016: Projektregelprüfung

Zunächst ausschließlich Review. Danach hat der Nutzer die vier Findings ausdrücklich zur Korrektur freigegeben; der Stand folgt unten.
Geprüft: kanonische Skill-Einstiege von Workflow, Plan und Ask; Workflow operations, dispatch und rollover; Builder-Auftrag; Ask native und native-delivery; Plan edit und Validator-Evidence-Pfad. Maßstab: workspace/skills/AGENTS.md sowie private/AGENTS.md und Suite-Regeln. Ergänzend geprüft: Ask configuration, Claude und adviser; Plan read-only, lifecycle, granularity und Decision-Regeln; Workflow-Modellauflösung und Checkpoint-Vertrag; Paketmanifest und angebotene native Toolverträge. Die Prüfung betrifft Anweisungen und dokumentierte Laufzeitpfade, keinen vollständigen Code-Sicherheitsaudit.

## Findings

1. Workflow- und Ask-SKILL.md nennen unter Windows zuerst py -3.11. Die Luna- und SOL-Evidenzen zeigen wiederholtes Scheitern dieses Aufrufs trotz installiertem Python 3.14.3. Kleinste Korrektur: vorhandenen Interpreter wiederverwenden; sonst py -3 versuchen und die Mindestversion prüfen. Kein neuer Suchhelper.
2. Workflow operations.md verlangt Feldreihenfolge und mehrere exakte Zeichenlimits und erlaubt bei reinem Formatfehler eine zusätzliche Restatement-Runde. Ohne Runtime-Parser können sachlich eindeutige Ergebnisse dadurch unnötige Nachrichten erzeugen. Kleinste mögliche Korrektur: Pflichtinformationen, Status und knappe Länge erhalten, aber rein kosmetische Abweichungen tolerieren. Das ist ein Vertragsvorschlag, kein belegter Formatfehler des aktuellen zweiten Laufs: dessen erster Worker lieferte tatsächlich vier Zeilen; die native Statusansicht hatte sie nur zusammengezogen.
3. Plan edit.md verlangt kompatible Evidence-Listen ohne Kommas oder Klammern, obwohl dieselbe Anleitung und der Validator bereits einzeiligen Klartext erlauben. Diese zusätzliche Schreibbeschränkung widerspricht dem Ziel, unnötige Formatkorrekturen zu vermeiden. Kleinste mögliche Korrektur: unterstützten Klartext für neue Evidence zulassen; vor Freigabe noch prüfen, welche tatsächlich unterstützten Verbraucher die alte Listenkompatibilität benötigen.
4. Der Builder nennt Assigned point und gesamte Work-Item-Acceptance gemeinsam den vollständigen Auftrag. Im zweiten nativen Test erledigte Worker 1 für Step 1 auch test_names.py und ein Beispiel, obwohl Tests und Nutzungsdoku eigene Steps sind. Die übergreifende Acceptance ist eine plausible Mitursache, nicht abschließend bewiesen. Kleinste Korrektur: Assigned point als Arbeitsumfang und Outcome/Acceptance als übergreifende Bedingungen unterscheiden, die den Umfang nicht erweitern. Kein zusätzlicher Scope-Validator.

## Bereits passend

Workflow und Ask verwenden native create_thread, send_message_to_thread und set_thread_archived direkt. Konfigurationsauflösung und Planprojektion schließen konkrete lokale Datenlücken; die verfügbaren nativen Chat-Tools ersetzen diese fachlichen Daten nicht. Es gibt keine native Lifecycle-Wrapper-Pflicht mehr. Archivierung benötigt keine Bestätigung oder Nachprüfung. Absenderprüfung und Wiederaufnahme anhand bekannter IDs vermeiden falsche Ergebnisannahme oder doppelte schreibende Worker mit wenigen Regeln.

## Testgrenze

Die 1%-Worker-Kontextschwelle der Fixture löste mehrere künstliche Rollover desselben Steps aus. Nach beobachtetem Handoff wurde der Coordinator angewiesen, an einer sicheren Grenze zum normalen Workerwert 75 zurückzukehren. Diese Teststeuerung ist kein Quellfix und muss bei Kostenvergleichen getrennt bleiben.

## Ergebnis der ergänzenden Prüfung

Keine weiteren konkreten Regelabweichungen in den ergänzend geprüften Pfaden. Die vier Findings oben bleiben bestehen. Claude ist die ausdrücklich beibehaltene CLI-Ausnahme; dessen JSON-Verarbeitung und Prozessdeadline sind kein unerlaubter Nachbau nativer Codex-Chats. Die vorhandenen nativen Tools stellen Chat-Lifecycle und Modelleinstellungen bereit, aber keinen Selector für dieses Repository-Planformat und keinen aktuellen Kontextfüllstand des einzelnen Chats. get_usage_limits beschreibt Accountlimits und ersetzt den Context-Checkpoint nicht. Deshalb sind diese verbleibenden fachlichen Helper nicht allein wegen ihrer Existenz ein Finding.

Fundstellen: Workflow SKILL.md:15; Ask SKILL.md:29; Workflow operations.md:35-39 und :96-97; Plan edit.md:88-93 mit validate_profile.py:791; Workflow build_dispatch_prompt.py:95. Beobachtete Fälle sind in luna/evidence.md, sol-plan-setup/evidence.md, sol-native/evidence.md und den run-2-worker-1-Handoffdateien der nativen Fixture gesichert.

Die Korrektur verwendet das bereits von Selector und Validator unterstützte Klartext-Evidenceformat; alte Listen werden nicht migriert.

## Freigegebene Korrekturen

Auf die ausdrückliche Aufforderung des Nutzers, diese vier Probleme zu beheben:

- Workflow/Ask verwenden bekannte Interpreter weiter und ermitteln fehlende lokal ohne Rückfrage.
- Ergebnisinformationen bleiben Pflicht; Feldreihenfolge, Zäune und rein kosmetische Abweichungen lösen keine Restatement-Runde aus. Mehrere exakte Zeichenlimits entfallen. Eindeutiges finding=none verlangt keine Reparatur.
- Plan empfiehlt unterstützte Klartext-Evidence mit Kommas/Klammern statt eingeschränkter Listen. Die bestehende skalare Grenze von 200 Zeichen und der Validator bleiben unverändert; längere Nachweise werden verlinkt.
- Assigned point definiert allein den Arbeitsumfang. Übergreifende Acceptance weist keine weiteren Steps oder zusätzlichen Liefergegenstände zu.

Vorherige Dateien: temp/2026-09-26-private-helper-tests/before-approved-rule-fixes. Gebauter Teststand: candidate-rule-fixes. 16 Workflowtests bestanden; eine obsolete wortgleiche Assertion wurde entfernt, diagnostische Parserprüfungen bleiben. Paketprüfung gültig. SOL-6-Medium-Verbraucherprüfung unter sol-rule-fixes läuft. Keine reguläre Installation oder Veröffentlichung.

Nutzerpräzisierung zur Step-Grenze: Vorweggenommene Tests können Korrekturen am aktuellen Step erzwingen, obwohl dessen Worker den späteren Kontext nicht kennt. Der Builder verbietet deshalb ausdrücklich Tests auf angenommene Anforderungen anderer Steps sowie Anpassungen des aktuellen Steps für zukünftiges Verhalten. Eigene erforderliche Verhaltensprüfungen bleiben erlaubt. Diese Präzisierung folgt nach dem Build candidate-rule-fixes und benötigt den entsprechenden Nachtest.

Weitere Nutzerpräzisierung: Die Scope-Regel verweist nicht auf unbekannte spätere Steps. Assigned point ist der vollständige Arbeitsumfang; nur dessen ausdrücklich verlangtes Verhalten wird implementiert und geprüft. Outcome/Acceptance begrenzen diese Arbeit und sind keine Zusatzaufträge. Das bestehende Verbot, Plan oder weitere Planpunkte nachzuladen, bleibt. Der Stand candidate-step-scope enthält noch die vorherige Formulierung.

## Zusätzliche Kontextprüfung auf Nutzerfrage: noch keine Änderungsfreigabe

Arbeitsumfang und Verständniskontext müssen getrennt bleiben. Der Worker benötigt nicht den ganzen Plan, aber den Zweck seiner Arbeit, zugehörige Anforderungen, geltende Grenzen und relevante bereits feststehende Ergebnisse.

Belegte aktuelle Projektion:

- select_context.py liefert Plan Goal/Non-goals. build_dispatch_prompt.py verwendet context.plan nicht. Vorgaben, die ausschließlich dort stehen, fehlen ohne gesonderten Zusatzkontext.
- Direkte Abhängigkeiten liefern nur ID und Status. Fertige Schnittstellen oder andere tatsächlich benötigte Ergebnisse müssen vom Coordinator gezielt ergänzt werden; Status done ersetzt sie nicht.
- Der Builder überträgt für jede verknüpfte ADR nur ID und Decision-Abschnitt. Status, scope und superseded_by gehen verloren. Dadurch ist aus dem Auftrag allein nicht erkennbar, ob eine Entscheidung nur vorgeschlagen oder bereits ersetzt ist. Der Coordinator muss wirksame Vorgaben bestimmen; kein zusätzliches ADR-Nachladen durch den Worker.
- Outcome/Acceptance werden vollständig übertragen. Sie liefern nützliche Anforderungen, enthalten aber unter Umständen weitere Liefergegenstände. Die Formulierung 'only the behavior it explicitly requires' kann andererseits zu eng sein, wenn ein knapper Step seine fachliche Definition erst aus der Acceptance erhält.

Kleinste sinnvolle Richtung: Der Coordinator liefert vor dem Builder den ausgewählten Schritt, einen kurzen Zweck, die dazugehörigen Anforderungen/Prüfkriterien sowie nur die wirksamen Einschränkungen und benötigten Abhängigkeitsergebnisse. Der Builder stellt diese vorbereiteten Inhalte zusammen; er soll keine semantische Relevanzmaschine werden. Kein vollständiger Plan, keine ADR-Historie und keine Vorgängerchats. Die klare Trennung muss auch im Reviewer-Auftrag gelten. Diese Ergänzungen sind neue Reviewbefunde, noch nicht umgesetzt.

## Abschließende Nutzerentscheidung zur Arbeitseinheit

ADR-0093 hält die freigegebene Variante fest: zusammenhängende Step-Gruppen, verbindliche Reihenfolge, vollständiger Work Item als Kontext und vom Coordinator ausgewählte nötige Goals/Non-goals sowie geltende Vorgaben. Gruppierung spart wiederholte Einarbeitung und Übergaben, muss aber ein zusammenhängendes umsetzbares und prüfbares Ergebnis bilden. Keine zusätzliche Gruppierungsstruktur. Die zwischenzeitliche Variante eines obligatorischen Workers für den gesamten Work Item wurde nicht beibehalten.

Aktueller Build: candidate-grouped. 31 Suite-, 21 Ask-, 21 Selector- und 17 Workflowtests bestanden; Paketprüfung gültig. Der native SOL-6-Medium-Test läuft im bestehenden gespeicherten workflow-e2e-Projekt als PLAN-0003. Frühere Scope-Proben beziehen sich auf ihre benannten Paketstände und werden nicht als finale Gruppenabnahme ausgegeben.

### Checkable grouping choice (2026-09-26)

Plan and Workflow now ask what repeated setup a group saves and what concrete
result its final checks prove. Unclear answers call for revising the grouping.
SOL 6 Medium applied both source references read-only: it selected Steps 1-4
(library behavior and unit tests) followed by Steps 5-6 (complex CLI integration,
CLI tests and documentation). It identified shared setup and a checkable result
for both groups. Relevant acceptance and Plan constraints still belong in the
dispatch context. This proves wording application only, not native execution or
measured savings. No helper ran and no test input needed repair. git diff --check
passed. Agent: /root/sol_grouping_criterion.

Setup enthielt noch dieselbe py-3.11-Vorgabe wie die bereits korrigierten
Ask-/Workflow-Einstiege. Die freigegebene lokale Interpreterwahl gilt nun auch
dort. SOL 6 Medium verwendete candidate-grouping-criterion erfolgreich für
show, serialisiertes set und tatsächliche Workflow-Resolver-Verwendung:
temp/2026-09-26-private-helper-tests/sol-setup-final/evidence.md. Kein Helper-
Ergebnis benötigte Reparatur, keine reguläre Installation wurde geändert.
