---
format_version: 1
id: PLAN-0034
status: completed
created: 2026-10-04
updated: 2026-10-05
---

# Intention, Sprache und Wirkung der Scoville-Skills

## Goal

Jeder Skill vermittelt seine Intention klar, wird passend aktiviert und erzielt
durch befolgte Regeln das gewünschte Ergebnis. Beschreibungen und dichte Prosa
werden verbessert, ungenutzte Schreibprofile entfernt und gemeinsame Regeln aus
einer kanonischen Quelle gebaut. Alle bestehenden Bedeutungen, Zuständigkeiten,
Rangfolgen, Ausnahmen und Schutzregeln bleiben erhalten, außer den ausdrücklich
beschlossenen Änderungen am Schreibregelwerk und an AGENTS.md/CLAUDE.md.
Sinngleiche Regeln zusammenzuführen erlaubt selbst keine Verhaltensänderung.

ADR-0165 beauftragt nun die Ausführung des gesamten
Plans nach unabhängigem Astra-high-Review und bestätigten Korrekturen.
Der vollständig unbegonnene W-015 wurde gemäß ADR-0176 nach PLAN-0035
übertragen und gehört nicht mehr zum verbleibenden Umfang dieses Plans.
Die offene finale Restabnahme von W-014 wurde nach ADR-0177 an PLAN-0035/W-009
übertragen. PLAN-0034 endet als Umsetzung mit erhaltenen Teilergebnissen;
die vollständige Skill-Abnahme bleibt dort offen.

Der Plan übernimmt den Nutzerprompt vom 04.10.2026 und die gebilligten
Präzisierungen (ADR-0154). ADR-0156 und ADR-0157 beauftragen die Umsetzung
von W-002 bis W-013 mit Astra-high-Review nach jedem Arbeitspunkt und Stopp
vor W-001. ADR-0160 erlaubt anschließend die modellfreie Vorbereitung von W-001.
Modelltests laufen erst nach allen Skill-Änderungen, nie am
Ausgangsstand, und brauchen ihre gesonderten Budget- und Live-Freigaben.
Plan-Review, Umgang mit Befunden und offene Entscheidungen stehen im
[Review-Bericht](../../development/plan-evidence/0034-plan-review.md), die
[Laufbudgetschätzung](../../development/plan-evidence/0034-run-budget.md) ist
keine Ausführungsfreigabe.

**Arbeitsvertrag**

**Quellen, Varianten und Ausgangsstand**

Kanonische Quellen sind dieses Repository mit members/ und suite.json sowie das
eigene Nachbar-Repository ../shared/. development/shared/ ist generiert.
Vor Beginn Git-Zustände und relevante Ausgangsbehauptungen im
[Quellennachweis](../../development/plan-evidence/0034-source-context.md) erneut
prüfen. Uncommittete Ausgangsänderungen gegebenenfalls zusätzlich in Workspace-Temp
sichern. Generierte Kopien nicht unabhängig bearbeiten.

Nach Shared-Änderungen entfallene Dateien auch in development/shared/ entfernen,
dann `python ../shared/build/sync_suite_sources.py --root .` und `--check`.
Der Sync verweigert überzählige Dateien. Nur auf geprüfte betroffene Pfade löschen.

Build-Profil bedeutet general oder codex, Layout standalone oder suite.
Paketvarianten: general standalone, general suite, codex suite und Ask codex
standalone. General enthält Code, Plan, UI, Handoff und Cleanup; Codex alle acht.
Skill-Verzeichnis bedeutet <member>/<member>/ im Paket, ohne README/CHANGELOG
an der Paketwurzel. Planungsprofile bleiben; low/medium/high-Schreibprofile entfallen.

Testkandidaten über build() aus development/build_suite.py im Testprojekt nach
<Desktop>/test/plan0034/ bauen (ADR-0152). Ihr
runtime_validation bleibt pending. Die verifizierte CLI mit --output braucht für
Helper-Pakete den passenden privaten Runtime-CI-Lauf; auch Textänderungen
invalidieren ihn. Statische Vergleiche von Paketbytes und Routenkosten beziehen
sich auf den Ausgangsstand Suite 6621fa3 mit Shared 3d013c9 und brauchen keine Modellläufe.
Exporttests nutzen eine Temp-Kopie mit lokalem Temp-Commit und aktuellem Snapshot
nach ../shared/tests/test_distribution_profiles.py. Echte Quellen bleiben uncommittet.

**Erhaltene Semantik und Sprache**

Für jede entfernte, verschobene oder zusammengeführte Regel eine Semantik-Diff-Liste
führen: alte Regel → neue Regel → kanonischer Ort → betroffene Verbraucher/Cases.
Die Evidence verlinkt diese Liste. Gleichartige Regeln nur dann gemeinsam halten,
wenn Geltungsbereich, Rangfolge und Ausnahmen übereinstimmen. ADR-0142 bleibt bindend:
notwendige Schutzregeln dürfen in Regeldatei und ausgelagertem Verfahren stehen.

Alle ausgelieferten Skill-Dateien einschließlich Frontmatter, references/, assets/,
agents/openai.yaml und Skripttexten mit eigenen Meldungen sind Englisch.
Laufzeitdokumente und übernommene Nutzerdaten folgen weiterhin Nutzer-/Projektsprache.
Deutsche Aktivierung muss ohne deutsche Description-Wörter funktionieren.
Deutsche Testanfragen und Rohantworten bleiben außerhalb des öffentlich exportierten
development/-Baums im Testprojekt unter <Desktop>/test/plan0034/ (ADR-0152).

Im Profil general sollen Skill-Verweise auf AGENTS.md auch CLAUDE.md abdecken;
codex nennt weiterhin nur AGENTS.md. Lesen, Bearbeiten, Konflikte und Neuanlage
werden vor W-006 in ADR-0148 entschieden. Bestehende Profilblöcke verwenden;
openai.yaml und Python lösen keine Blöcke auf. Betroffene README-Stellen nur melden.

**Überarbeitung je Skill**

W-008 bis W-013 ändern Texte ohne Modelltests; die Skill-Abnahme prüft W-014.
Frontmatter-Description, openai.yaml short_description und default_prompt
folgen dem Regelwerk und nennen nur Nutzerwörter, für die der Skill zuständig ist.
compatibility nennt Umgebungsanforderungen; technische Modellanforderungen wie
bei Ask bleiben, Modellempfehlungen stehen nur im README. Dichte Dateien aus dem
Quellennachweis zuerst entdichten; in anderen Dateien nur Regelverstöße wie
Slash-Ketten beheben. Wort-, Byte- und Token-Delta je Datei und Route statisch
festhalten, Semantik-Diff ergänzen und alle Paketvarianten bauen.
Bestehende Tests mit exakten Formulierungen in jedem Work Item nur wegen einer
gewollten Änderung anpassen und in Evidence begründen.

**Testvertrag und Abnahme**

ADR-0166 begrenzt die nachstehende ursprüngliche Vollmatrix auf eine gezielte,
vor Ausführung festgelegte Auswahl mit insgesamt höchstens 300 Testversuchen.
Auslassungen und nicht qualifizierte Wege bleiben ausdrücklich unverifiziert.
Die übrigen fachlichen Kriterien und technischen Nachweise gelten weiterhin.

Modelltests laufen erst nach allen Skill-Änderungen und vor jeder
Veröffentlichung; es gibt keine Baseline-Läufe (ADR-0154). Builds,
Paketvergleiche, Unit- und modellfreie Helper-Consumer-Tests bleiben bei den
Änderungen. Tests mit tatsächlichen modellgestützten Verbrauchern, insbesondere
nativen Workflow-/Ask-Agenten, gehören zu W-014 (ADR-0155). Lokale Prüfungen
nachgebildeter Aufrufsignaturen ersetzen diesen Nachweis nicht.
W-002 legt Cases und erwartete Ergebnisse vor der ersten Skill-Änderung ohne Läufe fest.

Aktivierung, Verständnis, Befolgung, Wirkung und Kosten getrennt prüfen.
Je Trigger-Case erforderliche, zulässige und unzulässige Skills angeben.
Fachlich richtige gemeinsame Aktivierung ist keine Nachbar-Verwechslung.
Alle Trigger-Läufe installieren die vollständige jeweils gültige Suite; im
Standalone-Layout alle für diesen Host zulässigen Pakete. Codex-only-Skills
werden nicht als Claude/General-Pflichtfälle gewertet.

Alle Luna-Läufe nutzen gpt-6-luna mit high. Luna prüft die Codex-Suite, bei
abweichendem Profiltext auch General. Claude-Aufrufe für die fünf General-Skills
sind erlaubt (ADR-0159); unabhängige Nutzerprüfungen bleiben möglich. Budget und
Live-Testfreigaben gelten weiterhin. Externe Ergebnisse bleiben bis zu ihrer
belegten Übernahme unverifiziert.
Abweichender Layouttext wird in beiden Layouts geprüft. Identische Varianten
nicht künstlich vervielfachen; begründete Matrix je Case vor Ausführung festlegen.

Jeder Case startet mit drei Läufen je Modell und anwendbarer Variante. Bei
uneinheitlicher Bewertung auf fünf Läufe ergänzen; bisherige Läufe zählen mit.
Die Mehrheit entscheidet den Pass, und jeder anwendbare Case muss bestehen.
Einen Fehlschlag zuerst auf seine Ursache prüfen (Skilltext, Case, Runner,
Transport), nicht automatisch Prosa ändern und nie den Schlüssel an Antworten
anpassen. Keine Läufe über das freigegebene Budget. Transportfehler gesondert behandeln.

Wirkung benötigt reale Aufgaben und vorab definierte Ergebnisse. Für Workflow
und Ask gelten ohne eigens freigegebene Desktop-Live-Probe nur Trigger-,
Verständnis- und modellfreie Helper-Consumer-Nachweise; Wirkung und native
Verbraucherprüfungen bleiben ausdrücklich unverifiziert.
Setup ist separat mit Konfigurations-Fixtures und seinen tatsächlichen Consumern
zu prüfen; seine Desktop-Pfade brauchen eine geeignete isolierte Umgebung.
Keine vollständige Skill-Abnahme mit nur technischem Teilnachweis behaupten.

Cases und erwartete Ergebnisse nach W-002 einfrieren.
Verständnis-Cases bleiben hypothetisch; ihre Übertragung in reale Fixtures darf
den bestehenden Given/Expect-Vertrag nicht verändern. Nach ADR-0161 erhält ein
unabhängiger Sol-6.1-high-Bewerter gesammelte Testgruppen mit verborgenen
Erwartungen und anonymisierten Ergebnissen,
keine Änderungsbegründung. Alle Versuche und ungeprüften Wege ausweisen.
Eine Korrektur invalidiert betroffene Nachweise, auch wenn der konsumierende
Skill unverändert ist.

Ein Skill ist angenommen, wenn alle anwendbaren Testarten bestehen und seine
Routen nicht länger sind als im Ausgangsstand oder jedes Plus begründet ist.
Byte-, Wort- und Tokenkosten je Datei/Route statisch gegen den Ausgangsstand
sowie die Lauf-Usage messen. Nicht vergleichbare Tokenizer getrennt ausweisen.
Scheitert die Abnahme eines Skills nach drei Überarbeitungsrunden in W-014,
den Skill als nicht angenommen melden und die übrigen Skills weiter prüfen.
Das schwächt keine Acceptance; W-014 und der Plan bleiben offen, solange
Acceptance unerfüllt ist. Fehlende Freigaben erlauben keine zusätzlichen
Versuche und lassen die betroffenen Wege unverifiziert.

## Non-goals

Keine Veröffentlichung, Installation, Änderung von skills/public/ oder
skills/temp/release/, kein Commit im echten Repository und kein Push ohne
gesonderte Freigabe. Ein lokaler Temp-Commit für den Exporttest ist erlaubt.
Keine Arbeit in packages/, exportierten Bäumen oder scoville-agent-dev als Quelle.
Keine Erweiterung des Profilmechanismus; diese gehört PLAN-0019 W-002.
Keine Modellläufe am Ausgangsstand und keine Luna-Efforts außer high.
READMEs und CHANGELOGs werden nicht redaktionell geändert; einzige Ausnahme ist
der Satz zur niedrigsten getesteten Basis in W-014 (ADR-0154). Die Luna-high-Basis
ändert keine Laufzeit-Defaults wie Workflows execute.ultra_low.
Harte Suite-Kopplung, Family-Projektionen und explizite Aktivierungsgates
bleiben erhalten. Keine neuen Release-Gates auf exakte Prosa oder einen festen
Modell-Case-Katalog.

## Work items

### W-002 Eingefrorene Cases mit vorab festgelegten Erwartungen

Status: done
Depends on: []
Blocked by: []
Decisions: [ADR-0148, ADR-0150, ADR-0152, ADR-0154, ADR-0156, ADR-0157, ADR-0158]
Outcome: Ein genehmigter, reproduzierbarer Case-Katalog mit vorab festgelegten Erwartungen deckt die geforderten Verhaltensdimensionen und Varianten ab.
Acceptance: Vor der ersten Skill-Änderung hat jeder anwendbare Case Erwartungen, Matrix und Wiederholungszahl, und der Katalog ist eingefroren. Es fanden keine Modellläufe statt.
Instructions: Katalog nach externem Review korrigieren und erneut mit Astra high prüfen; dann bis W-013 fortsetzen, vor W-001 stoppen (ADR-0157).
Steps:
1. [status: done] Bestehende 164 Given/Expect- und Recovery-Cases von Plan, Code und Handoff unverändert übernehmen, ihre Eignung je Testart festhalten und reale Fixtures separat ableiten.
2. [status: done] Verständnis-/Befolgungs-Cases für UI/Cleanup anlegen und repository-relative portable Testeinstiege unter development.tests in suite.json registrieren. Private deutsche Case-Daten separat anbinden, nie externe Maschinenpfade ins Manifest schreiben.
3. [status: done] Dichte Passagen und jede zusammenzuführende Regel im Quellennachweis abdecken; UI-Sonderfall-Cases aus Regeln rekonstruieren und so kennzeichnen. AGENTS.md/CLAUDE.md nach ADR-0148 abdecken.
4. [status: done] Je Skill etwa 10–15 Trigger-Cases, mindestens ein Drittel deutsch, mit erforderlichen/zulässigen/verbotenen Aktivierungen anlegen. Paare: Plan/Handoff, Code/Plan, Code/UI, Cleanup/Plan bei PROJECT_INDEX.md, Workflow/Plan, Ask/Code bei Reviews. Explizites Workflow-Gate, gewöhnliche Fragen an Ask und „Füge das den Projektregeln hinzu“ abdecken.
5. [status: done] Je Skill 3–5 realistische Wirkungsaufgaben mit Erfolgskriterien definieren; Workflow/Ask/Setup gemäß Testvertrag behandeln. Fortführung von Plan oder Handoff ohne fehlenden Kontext prüfen, berechtigte Rückfragen nicht pauschal als Fehler werten.
6. [status: done] Typische Routen je Skill und Variante sowie die begründete Matrix je Case festlegen und das Laufbudget präzisieren. Katalog und Datenidentitäten einfrieren; spätere Case-Änderungen begründen.
Evidence: v7: 342 Cases, 105 Hashes, 17 Consumer-Checks; Astra bestätigt Korrekturen zum Opus-Review. Keine Modelltests. development/plan-evidence/0034-w002-result.md.

### W-003 Sprachprüfung meldet deutsche Paketinhalte

Status: done
Depends on: []
Blocked by: []
Decisions: []
Outcome: Alle gebauten Skill-Verzeichnisse werden auf bekannte deutsche Inhalte geprüft, ohne die Tests mit vollständiger Sprachvalidierung zu verwechseln.
Acceptance: Der Test meldet das aktuelle „(Projektregeln)“, erfasst Skripte und openai.yaml und lässt nur begründete Ausnahmen zu. Der befristete Eintrag verweist auf W-012.
Instructions: README/CHANGELOG liegen außerhalb der Sprachregel dieses Plans; deutsches README-Beispiel nur zur Entscheidung melden.
Steps:
1. [status: done] In ../shared/tests/ einen Package-Test für alle Paketvarianten ergänzen: Umlaute/ß und kuratierte eindeutig deutsche Wörter mit enger Allowlist, keine allgemeine Wortliste mit englischen Kollisionen.
2. [status: done] Positiv-/Negativfälle und den Fund „(Projektregeln)“ belegen; diesen bis W-012 befristet erlauben. Finale Sichtprüfung als eigenen Nachweis vorsehen.
3. [status: done] development/readme/scoville-project-context-cleanup/usage.md melden, Shared-Kopie synchronisieren und bestehende Pakettests ausführen.
Evidence: Vier Sprach-, vier Export-/Profil- und zwei Bytetests bestanden; Astra ohne Befund. development/plan-evidence/0034-w003-result.md.

### W-004 Ungenutzte Schreibprofile sind ohne Paketänderung entfernt

Status: done
Depends on: [W-003]
Blocked by: []
Decisions: []
Outcome: Unbenutzte Schreibprofile und ihre Build-Unterstützung entfallen, während jedes ausgelieferte Paket bytegleich bleibt.
Acceptance: members[].files der Receipts sind vor und nach W-004 für alle Paketvarianten identisch; Sync und betroffene Tests bestehen.
Instructions: prompting/common.md bleibt bis W-007 einschließlich seines veralteten Schreibprofil-Satzes unverändert.
Steps:
1. [status: done] Unmittelbaren Vorher-Build sichern. ../shared/prompting/{low,medium,high}.md, models.toml, runtime/resolve_prompt_profile.py und tests/test_prompt_profile.py nach erneuter Nutzungsprüfung entfernen.
2. [status: done] prompting.defaults-Unterstützung aus expand_fragments() und Receipt-Erzeugung im kanonischen ../shared/build/build_suite.py entfernen. Profilverweise in beiden AGENTS.md, instruction-writing.md und fragments.md bereinigen.
3. [status: done] Entfallene generierte Dateien entfernen, synchronisieren, Nachher-Builds erstellen und vollständige Paketdatei-Hashes vergleichen; Regelverlagerungen in der Semantik-Diff-Liste erfassen.
Evidence: 275 Paketdateien in vier Varianten bytegleich; 11 betroffene Tests und Sync bestanden; Astra ohne Befund. development/plan-evidence/0034-w004-result.md.

### W-005 Gemeinsame Regeln haben eine kanonische Quelle

Status: done
Depends on: [W-002, W-004]
Blocked by: []
Decisions: [ADR-0149]
Outcome: Wirklich gemeinsame Opt-out-, Autoritäts- und Python-Regeln werden ohne Bedeutungsänderung geteilt; Code-Planungsregeln folgen der beschlossenen Zuständigkeit.
Acceptance: Jede Zusammenführung hat gleichen Geltungsbereich, gleiche Rangfolge und Ausnahmen und steht in der Semantik-Diff-Liste; alle Paketvarianten bauen, geladene Routen sind statisch gemessen. Nicht sicher vereinheitlichbare Regeln bleiben begründet getrennt.
Instructions: family.contract nur für alle acht Skills betreffende Regeln verwenden; designspezifische UI-Rangfolge und ausdrückliche Handoff-Aktivierung erhalten.
Steps:
1. [status: done] Opt-out-Regeln von Code/UI/Plan/Cleanup, allgemeine Autoritätsregeln von Code/Plan/UI und identische Codex-Python-Erkennung von Ask/Setup abgleichen.
2. [status: done] Passende Quellen unter ../shared/ anlegen, neue Include-Schlüssel nur bei Bedarf. Python-Regel alternativ im Codex-Zweig von helper.policy. Betroffene Verbraucher explizit binden, neue Quellen in Receipt/Export-Provenienz berücksichtigen.
3. [status: done] Code references/planning-and-decisions.md gemäß ADR-0149 in suite auf passende Plan-/Handoff-Texte verweisen lassen; standalone behält eine knappe vollständige Fassung. Zusätzliche Referenz-Tokens mitzählen.
4. [status: done] Synchronisieren, Semantik-Diff ergänzen und alle Paketvarianten bauen. Zusammenführungen, deren Cases in W-014 scheitern, nimmt W-014 zurück und meldet sie.
Evidence: Gemeinsame Regeln, Semantik-Diff und 47 Routen geprüft; 19 Tests, alle Varianten und Astra-Review bestanden. development/plan-evidence/0034-w005-result.md.

### W-006 Projektregeldateien folgen dem Build-Profil

Status: done
Depends on: [W-005]
Blocked by: []
Decisions: [ADR-0147, ADR-0148]
Outcome: General berücksichtigt CLAUDE.md entsprechend der beschlossenen Dateisemantik, Codex behält AGENTS.md.
Acceptance: Alle sieben Ausgangsfundstellen und alle weiteren Skill-Verweise sind je Paketvariante korrekt und durch den Build-Test belegt. Die Konflikt-, Neuanlage- und Konventions-Cases prüft W-014.
Instructions: READMEs nicht ändern; neue general-Blöcke für PLAN-0019 dokumentieren. Kein neuer Profilmechanismus.
Steps:
1. [status: done] Die Fundstellen in Code SKILL.md, Code references/project-conventions.md und Cleanup SKILL.md mittels bestehender general/codex-Blöcke und ADR-0148 anpassen.
2. [status: done] Profilblock im Package-Block an Codes suite-Stelle durch Build-Test absichern und die zu weit gefasste Verschachtelungsaussage in ../shared/build/fragments.md präzisieren; weiterhin ungültige gleichartige Verschachtelungen ablehnen.
3. [status: done] Alle Varianten bauen, Verweise je Variante prüfen und README-Fundstellen einschließlich Codes configuration.md sowie neue Profilblöcke im Bericht festhalten.
Evidence: ADR-0148 projiziert; alle sieben Stellen getestet, Codex bytegleich; sechs Tests und Astra-Nachreview bestanden. development/plan-evidence/0034-w006-result.md.

### W-007 Ein gemeinsames Schreibregelwerk erreicht alle Verbraucher

Status: done
Depends on: [W-006]
Blocked by: []
Decisions: [ADR-0153, ADR-0155]
Outcome: Allgemeine Schreibregeln haben einen ausgelieferten Laufzeitteil und einen ergänzenden Autorenteil unter ../shared/; alle betroffenen Texte und Helper verwenden ihre kanonische Quelle.
Acceptance: Keine allgemeine Schreibregel hat zwei unabhängig gepflegte Quellen. Alle geänderten Helper bestehen lokale modellfreie Funktions-, Diagnose- und Schnittstellentests mit gültigen, ungültigen und korrigierten Aufrufen; vorhandene modellfreie Verbraucher werden direkt geprüft. Betroffene Semantik und Kosten sind geprüft. Modellgestützte Verbraucher prüft W-014.
Instructions: README-Stilregeln und ADR-0144 bleiben; Ergebnis-/Formatverträge wie adviser.md und Workflow-Statusmeldungen bleiben beim jeweiligen Skill.
Steps:
1. [status: done] Regeln aus instruction-writing.md, prompting/common.md, Suite-AGENTS.md, Plan/Handoff SKILL.md, Workflow operations.md und build_dispatch_prompt.py abgleichen und Widersprüche auflösen, ohne fremde Verhaltensregeln still zu verändern.
2. [status: done] Laufzeitteil für Pläne, Decisions, Übergaben, Anweisungen, Agentenkommunikation, Adviser-Prompts, Reviews und Berichte erstellen. Autorenteil ergänzt Skill-/Description-Regeln und Englischpflicht ohne gemeinsame Regeln zu duplizieren.
3. [status: done] Maßstab verankern: kürzeste beim ersten Lesen für Luna eindeutige Fassung, notwendige Fakten und Schutzregeln erhalten, ganze Sätze mit Verb/Imperativ, keine Slash-Ketten in Prosa, ein Begriff je Bedeutung, Klartext vor Fachbegriff. Sonderfälle in bedingt geladene Referenzen, außer Routing oder Regression erfordert sie im Body. Technische Syntax und Formatverträge bleiben gültig.
4. [status: done] Description-Regel: erst Fähigkeit, dann Anlass in englischen Nutzerwörtern und eine relevante Geschwistergrenze; etwa 500 Zeichen als Richtgröße ohne Gate. Laufzeitteil über shared:-Einträge an schreibende Skills ausliefern und beim Schreiben laden; Einbindung nach tatsächlichen Routenkosten wählen.
5. [status: done] build_dispatch_prompt.py ersetzt den festen String; ask.py und build_adviser_prompt.py verwenden dieselbe ausgelieferte Datei gemäß ADR-0153; build_manager_handoff.py nennt deren Pfad. Registry/Provenienz und Consumer-Verträge erhalten, Fehlerdiagnosen samt korrigiertem Aufruf testen.
6. [status: done] Alte allgemeine Schreibstellen entfernen oder verweisen lassen; instruction-writing.md behält ergänzende Autorenregeln. common.md ersetzen/bereinigen, Cleanups Bytegleichheitstest nur wegen dieser gewollten Änderung anpassen und begründen. Synchronisieren und alle Paketvarianten bauen.
Evidence: development/plan-evidence/0034-w007-result.md; Astra PLAN-0034-W007-1 ohne materielle Befunde.

### W-008 Code vermittelt Auftrag und Grenzen verständlich

Status: done
Depends on: [W-007]
Blocked by: []
Decisions: [ADR-0149, ADR-0154]
Outcome: Code beschreibt seine Aufgaben in Nutzerwörtern und erhält seine Regeln mit weniger schwer verständlicher Prosa.
Acceptance: Description, Metadaten und Prosa folgen dem Regelwerk; Semantik-Diff und Datei-/Routendeltas liegen vor, alle Paketvarianten bauen. Die Skill-Abnahme prüft W-014.
Instructions: Überarbeitungsvertrag aus dem Arbeitsvertrag anwenden.
Steps:
1. [status: done] Description mit bug, fix, debug, refactor, failing test und code review präzisieren, „engineering Plan entries“ auflösen und Zuständigkeiten zu UI/Plan ohne falsche Exklusivität klären. default_prompt von Jargon befreien und vorhandene short_description angleichen.
2. [status: done] SKILL.md entdichten; core in den Referenzen ersetzen oder einmal definieren.
Evidence: development/plan-evidence/0034-w008-result.md; Astra PLAN-0034-W008-2 ohne Restbefunde.

### W-009 UI trennt allgemeine Regeln und Adapterdetails klar

Status: done
Depends on: [W-007]
Blocked by: []
Decisions: [ADR-0154]
Outcome: UI beschreibt seinen allgemeinen Auftrag und den WordPress-Adapter verständlich; Sonderfälle bleiben auffindbar und wirksam.
Acceptance: Description und Prosa folgen dem Regelwerk, Sonderfälle bleiben auffindbar, Semantik-Diff und Deltas liegen vor. Die Skill-Abnahme mit Fixture-App und Browser prüft W-014.
Instructions: Nach Code bearbeiten; Überarbeitungsvertrag aus dem Arbeitsvertrag anwenden.
Steps:
1. [status: done] WordPress-Scope in der Description in einen Satz fassen. Adapter-Ausschlüsse in references/wordpress/routing.md erhalten, Triggergrenze zu nicht-UI-Backend und interfacefremder Prosa erhalten.
2. [status: done] SKILL.md und references/validation.md entdichten; owner je tatsächlicher Bedeutung präzisieren. OWNERSHIP-ONLY, EVIDENCE-ONLY und SOURCE-ONLY AUDIT nach Regelwerk verorten, Herkunft nicht erfinden.
3. [status: done] Regelverstöße in weiteren dichten WordPress-Dateien einschließlich routing.md und classification-output.md beheben.
Evidence: development/plan-evidence/0034-w009-result.md; Astra PLAN-0034-W009-2 ohne Restbefunde.

### W-010 Plan bleibt präzise aktiviert und ausführbar

Status: done
Depends on: [W-007]
Blocked by: []
Decisions: [ADR-0154]
Outcome: Plans Beschreibung und Anweisungen sind verständlicher, ohne Aktivierung, Lebenszyklus oder Kontextbedarf zu verändern.
Acceptance: Description und Prosa folgen dem Regelwerk; bestehende Datensatzverträge bleiben gültig, Validator und Plan-Tests bestehen. Die Skill-Abnahme einschließlich activation-distinguishes-instruction-from-pure-question prüft W-014.
Instructions: Nach UI bearbeiten; Überarbeitungsvertrag aus dem Arbeitsvertrag anwenden.
Steps:
1. [status: done] hand off aus der Description entfernen, format-version-1 projects verständlich ersetzen und messages during active planned work präzisieren statt streichen.
2. [status: done] SKILL.md, edit.md, repair.md und native-project-lifecycle.md entdichten; Kompaktregel nur aus dem gemeinsamen Regelwerk beziehen. Planungsprofil und Maschinenfelder unverändert erhalten.
3. [status: done] Bestehende Plan-Tests und den Validator ausführen.
Evidence: development/plan-evidence/0034-w010-result.md; Astra PLAN-0034-W010-1 ohne Befunde.

### W-011 Handoff hat einen klaren Übergabeauftrag

Status: done
Depends on: [W-007]
Blocked by: []
Decisions: [ADR-0149, ADR-0154]
Outcome: Handoff grenzt explizit angeforderte Übertragung gegen Planpflege ab und erhält vollständige Fortsetzungskontexte.
Acceptance: Die Description grenzt gegen Plan ab, die Kompaktregel stammt aus dem Regelwerk; Aktivierungsgrenzen und erforderliche Inhalte bleiben unverändert. Handoff- und Recovery-Cases prüft W-014.
Instructions: Nach Plan bearbeiten; Überarbeitungsvertrag aus dem Arbeitsvertrag anwenden.
Steps:
1. [status: done] Description gegenüber Plan präzisieren, Kompaktregel aus gemeinsamer Quelle beziehen und vorhandene Metadaten konsistent halten.
Evidence: development/plan-evidence/0034-w011-result.md; Astra PLAN-0034-W011-1 ohne Befunde.

### W-012 Cleanup triggert deutsch mit englischen Skill-Inhalten

Status: done
Depends on: [W-007]
Blocked by: []
Decisions: [ADR-0148, ADR-0154]
Outcome: Cleanup hat eine englische Description ohne Modellempfehlung in compatibility und versteht weiter deutsche Projektregelaufträge.
Acceptance: Description ohne deutsche Wörter, compatibility ohne Modellempfehlung; der Sprachtest besteht ohne befristeten Projektregeln-Eintrag, Schutzregeln nach ADR-0142 bleiben erhalten. Die Skill-Abnahme mit Luna high und Claude prüft W-014.
Instructions: Nach Handoff bearbeiten; Überarbeitungsvertrag aus dem Arbeitsvertrag anwenden.
Steps:
1. [status: done] (Projektregeln) aus der Description und den befristeten W-003-Allowlist-Eintrag entfernen; Modellempfehlung aus compatibility entfernen, vorhandene README-Information erhalten.
2. [status: done] Allgemeine Regelwerksverstöße gezielt beheben und Schutzregeln nach ADR-0142 erhalten.
Evidence: development/plan-evidence/0034-w012-result.md; Astra PLAN-0034-W012-1 ohne Befunde.

### W-013 Workflow, Ask und Setup übernehmen nur die gemeinsamen Änderungen

Status: done
Depends on: [W-007]
Blocked by: []
Decisions: [ADR-0153, ADR-0155]
Outcome: Die drei Codex-Skills verwenden gemeinsame Regeln und behalten ihre übrige Prosa und Verhaltensgrenzen.
Acceptance: Gemeinsame Regeln sind übernommen, die übrige Prosa ist unverändert; geänderte Helper bestehen ihre lokalen modellfreien Funktions-, Diagnose- und Schnittstellentests. Trigger-, Verständnis-, modellgestützte Verbraucher- und Live-Nachweise prüft W-014.
Instructions: Nach Cleanup bearbeiten; außerhalb W-005/W-007 keine Prosa ändern. Setup hat keine openai.yaml.
Steps:
1. [status: done] Gemeinsame Regeln und beide Ask-Adviser-Pfade übernehmen; übrige Prosa unverändert lassen.
2. [status: done] Alle betroffenen Helper lokal ohne Modellaufrufe mit gültigen, ungültigen und korrigierten Eingaben prüfen; modellfreie Verbraucher direkt verwenden. Erforderliche modellgestützte Verbraucherprüfungen für W-014 festhalten.
Evidence: development/plan-evidence/0034-w013-result.md; Astra PLAN-0034-W013-1 ohne Befunde; Stopp vor W-001.

### W-001 Verlässliche Testwerkzeuge für die erforderlichen Hosts

Status: done
Depends on: [W-002, W-008, W-009, W-010, W-011, W-012, W-013]
Blocked by: []
Decisions: [ADR-0147, ADR-0150, ADR-0154, ADR-0159, ADR-0160, ADR-0161, ADR-0162, ADR-0163, ADR-0164, ADR-0165, ADR-0166]
Outcome: Isolierte Runner und Bewertungswege unterscheiden Aktivierung, Verständnis, Befolgung und Wirkung mit nachvollziehbarer Identität und Kosten.
Acceptance: Jeder Runner besteht einen bekannt guten und einen bekannt schlechten Kontrollfall. Host, Modell, Effort, Paket, Referenzen und Runner sind protokolliert; Transportfehler bleiben getrennt. Nicht verfügbare Fähigkeiten sind unverifiziert, nicht bestanden.
Instructions: ADR-0166 begrenzt W-001 auf die ausgewählten Verständniswege. Weitere Ausführung von Schritt 3 und 4 entfällt; vorhandene Vorbereitungen und unverifizierte Grenzen bleiben erhalten.
Steps:
1. [status: done] Hostfähigkeiten gegen development/claude-code/capabilities.md und development/luna-tests/codex-cli-execution.md prüfen; Risiko der nutzerweit installierten Skills und externer Tools ausschließen.
2. [status: done] development/luna-tests/run_codex_cli_case.py mit comprehension-instructions.md um Suite-Paketwurzeln erweitern; Luna läuft nur mit high. Claude-Headless-Verständnis ohne native Tools und Pakettext nur auf Anforderung gleichwertig bereitstellen oder als unverifiziert kennzeichnen.
3. [status: cancelled] Trigger-Runner mit isoliertem Home/Host-Konfiguration und aktiver Skill-Suche bauen. Codex exec --json läuft read-only mit Shell; beobachtetes Lesen von SKILL.md als Ladesignal validieren. Bei Claude Hooks/Transcript prüfen. Nicht zuverlässig erkennbare Aktivierung als unverifiziert melden.
4. [status: cancelled] Befolgungs-/Wirkungs-Fixtures aus Plan-Fixtures, Cleanup-Testberichten und UI-Linden-Brief im Projekt Desktop/test bereitstellen; UI-App mit Browserzugriff. Für Setup isolierte Konfiguration und Consumer verwenden, Workflow/Ask nach dem Testvertrag begrenzen.
5. [status: done] Verblindete Sol-6.1-high-Bewertung gesammelter Testgruppen (ADR-0161), getrennte Erwartungen, vollständige Versuchsaufzeichnung und Budgetzählung prüfen. Bei jedem Resume alle erforderlichen Sandbox-/Tool-Einschränkungen erneut setzen; keine echten Projekt- oder Kontomutationen.
Evidence: development/plan-evidence/0034-astra-full-result.md und 0034-selected-300.md: drei Befunde korrigiert, Verständnis-Hostkontrollen bestanden; nicht gewählte Wege nach ADR-0166 ausgeschlossen.

### W-014 Gezielte Tests vor Veröffentlichung belegen den gewählten Umfang

Status: cancelled
Depends on: [W-001]
Blocked by: []
Decisions: [ADR-0147, ADR-0149, ADR-0150, ADR-0151, ADR-0152, ADR-0154, ADR-0155, ADR-0159, ADR-0161, ADR-0165, ADR-0166, ADR-0167, ADR-0168, ADR-0169, ADR-0170, ADR-0171, ADR-0172, ADR-0173, ADR-0177]
Outcome: Der geänderte Stand besteht die vorab begründete gezielte Auswahl innerhalb von 300 Testläufen; Auslassungen und Grenzen sind belegt.
Acceptance: Alle vorab ausgewählten Cases bestehen am endgültigen Stand nach dem Testvertrag innerhalb von insgesamt 300 Versuchen. Ausgelassene Cases und nicht qualifizierte Testarten sind ausdrücklich unverifiziert. Erforderliche lokale Helper-, Sprach-, Build- und Portabilitätsprüfungen sowie der verifizierte Runtime-CI-Build bestehen. Semantik-Diff, unveränderte W-004-Pakete und statischer Kostenvergleich sind belegt. Keine vollständige Aktivierungs- oder Wirkungsabnahme aus der Auswahl ableiten.
Instructions: Nach W-016 hier mit erhaltenem Schrittstand fortsetzen (ADR-0172). ADR-0168 erlaubt 200 zusätzliche Korrekturversuche ab Zähler 391, insgesamt höchstens 591 ohne getrennte Poolgrenzen. Vollständige Workflow-Funktionstests mit 15/15-Prozent-Schwellen und die Runner-Benachrichtigungsprobe bleiben beauftragt. ADR-0170 erlaubt private CI-Pushes für korrigierte Testsnapshots. Fehlgeschlagene oder unverifizierte Pflichtprüfungen erlauben keinen Abschluss von W-014. Claude-Aufrufe sind erlaubt (ADR-0159). Keine Installation oder Veröffentlichung. Auf Nutzerauftrag vom 05.10.2026 ist die Restabnahme nach PLAN-0035/W-009 übertragen; dieser Punkt endet ohne vollständige Abnahme cancelled.
Steps:
1. [status: cancelled] Die vorab festgelegte Auswahl aus W-002 nach ADR-0166 am geänderten Stand ausführen und verblindet in vollständigen Gruppen bewerten. Nicht ausgewählte Testwege bleiben unverifiziert. Erfolgreiche Ausgaben der in W-007/W-013 geänderten Helper unverändert an die tatsächlichen modellgestützten Verbraucher übergeben und deren Ergebnis prüfen. Native Workflow-/Ask-Proben nur nach eigener Freigabe (ADR-0150); fehlende Freigabe lässt diesen Pflichtnachweis offen.
2. [status: cancelled] Fehlschläge je Skill auf Ursache prüfen und in höchstens drei Überarbeitungsrunden beheben. Descriptions von Workflow, Ask und Setup nur bei belegtem Triggerproblem ändern; bei impliziter Workflow-Aktivierung allow_implicit_invocation: false nur, wenn alle expliziten Aktivierungsformen weiter funktionieren. Zusammenführungen aus W-005 mit scheiternden Cases zurücknehmen und melden. Invalidierte Nachweise erneuern.
3. [status: cancelled] Hat sich nach dem ersten Triggerlauf eine Description geändert, alle Trigger-Cases gemeinsam am endgültigen Stand wiederholen.
4. [status: cancelled] Den Satz zur niedrigsten getesteten Basis in den README-Compatibility-Fragmenten und ../shared/readme/suite-requirements.md auf Luna High setzen, je Skill erst nach bestandenen Luna-high-Tests (ADR-0154); README-Vorschauen mit --write-readmes erzeugen.
5. [status: cancelled] Alle Paketvarianten als Kandidaten bauen, beide Suiten aus einer Temp-Kopie exportieren und bestehende Tests, run_portability.py, Sprachtest plus sprachliche Sichtprüfung ausführen. Verifizierten CLI-Build nur mit separat freigegebenem privaten Runtime-CI-Push; sonst pending/unverifiziert berichten und skills/temp/release/ nie still verändern.
6. [status: done] Alle AGENTS.md-Verweise, neue general-Profilblöcke für PLAN-0019, Semantik-Diff und Datei-/Routenkosten gegen den Ausgangsstand vergleichen; jedes Kostenplus begründen.
7. [status: cancelled] Abschlussbericht je Skill nach Testart, Sprache, Modell/Effort, Runden und Kosten erstellen. Nicht angenommene Skills, externe Case-Hindernisse, unverifizierte Wege, getrennt gebliebene Regeln, README-Beispiel und README-Dateiregelstellen nennen. Offene Befunde vorzulegen bedeutet nicht, dass deren Abnahme bestanden ist.
Evidence: Teilnachweise: development/plan-evidence/0034-w014-test-corrections.md; finale Restabnahme nach ADR-0177 an PLAN-0035/W-009 übertragen. Kein vollständiger PASS.




### W-016 Verbleibende dichte Skilltexte werden verständlich

Status: done
Depends on: [W-013]
Blocked by: []
Decisions: [ADR-0172]
Outcome: Die 19 konkret benannten Reviewpunkte sind korrigiert; Luna erhält klare Anweisungen mit erhaltenen Verträgen.
Acceptance: Alle Punkte sind gegen ihre Baseline geprüft und je Datei im Semantik-Diff samt Datei-/Routendeltas erfasst. Profilblöcke und technische Literale bleiben erhalten, außer den zwei ausdrücklich beschlossenen Funktionskorrekturen. Workflow-, Plan-, Ask-, Setup-, gemeinsame und Build-Tests sowie Sync-, README-, Sprach- und vier Paketprüfungen bestehen. Unabhängiges Astra-high-Review enthält keine bestätigten Restbefunde. Modellnachweise gehören danach zu W-014.
Instructions: Vor neuen Modellläufen bearbeiten; nur kanonische Suite- und Shared-Quellen ändern. Nach Abschluss W-014 an seinen erhaltenen Schritten fortsetzen. Bestehende Daten und Nachweise bleiben historisch erhalten; keine Installation oder Veröffentlichung.
Steps:
1. [status: done] Plan-Passagen aus Reviewpunkten 1–7 verständlich formulieren und Bedeutung erhalten.
2. [status: done] UI-Bedingungen sowie Ask- und Setup-Felder aus Punkten 8–10 gliedern.
3. [status: done] Workflow-Passagen aus Punkten 11–16 gliedern und reine Prosa-Slashketten auflösen.
4. [status: done] Child-Recovery und frische Create-Dispatches aus Punkten 17–18 korrigieren und tatsächliche Helper-Verbraucher prüfen.
5. [status: done] Gemeinsamen Satz aus Punkt 19 klarstellen, Quellen synchronisieren und geänderte Pakete lokal prüfen.
6. [status: done] Semantikvergleich, Deltas und Bericht für alle Punkte erstellen; Astra-high-Review einholen und bestätigte Fehler beheben.
Evidence: development/plan-evidence/0034-opus-v5-corrections.md: alle zwölf Nachkorrekturen geprüft; frisches Astra W016-2 ohne Quellbefund. Aktuelle Modell- und CI-Nachweise bleiben W-014.
