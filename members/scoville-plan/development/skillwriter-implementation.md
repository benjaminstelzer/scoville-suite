# PLAN-0008: Umsetzung und Kompatibilitätsnachweise

Stand: 2026-09-25. Die Umsetzung betrifft Scoville Plan; fremde parallele Code-, Handoff- und Workflow-Arbeit sowie der aktive Suite-Index bleiben unverändert. Keine Veröffentlichung oder Installation.

## Änderungen

- Einstieg auf Zuständigkeit, Grenzen und Routenauswahl gekürzt. Granularität besitzt die Step-/Routing-Grenzen, Work Items besitzen Nachrichtenbehandlung und Pre-flight, native Editing besitzt Schreibprofil und Schreibregeln. Wording-Audits laden den Schreibabschnitt ausdrücklich.
- Decision-Beispiel als gültiger Vorschlag; Step-Beispiele folgen Ergebnis- und Abnahmegrenzen. Unnötige feste Item-/Satzanzahlen entfernt. Die bestehende F03-/Autorisierungsgrenze bleibt unverändert.
- README-Voraussetzung für Frontier-LLMs gemäß ADR-0035 ergänzt und die Member-Vorschau aus der kanonischen Quelle erzeugt.
- Drei veraltete Evaluationserwartungen gegen bestehende Verträge korrigiert. Die Routingprüfung folgt den zuständigen Referenzen; der Compatibility-Test prüft Runtime-Parität und Modellvoraussetzung getrennt.

## Lokale Prüfungen

- 75 Plan-Tests bestanden. Der erste Lauf meldete die alte Annahme, der gesamte Compatibility-Abschnitt müsse allein dem Runtime-Frontmatter entsprechen; angepasst ist nur diese Zuständigkeit, beide Anforderungen bleiben geprüft.
- Bestehender Distributionstest für unbekannte Profile, ungültige Includes und unzulässige Layouts bestanden.
- Snapshot des Suite-Profils: 7 Pläne / 69 Work Items / 17 Decisions; historische Member-Akten: 3 Pläne / 9 Work Items / 3 Decisions; ursprüngliches Fixture: 1 Plan / 2 Work Items / 1 Decision. Ausgangs- und Kandidatenvalidator liefern jeweils identische erfolgreiche Ergebnisse, sämtliche Aktenbytes bleiben unverändert.
- Alle vier Python-Helper sind in beiden Profilen bytegleich zur Baseline. Formatversion und Schnittstellen wurden nicht geändert.
- Beide vollständigen Suite-Builds erfolgreich unter `<workspace>/skills/temp/release/plan-0008-plan/`. Finale Plan-Payloads stimmen bytegleich mit `candidate-final` überein. Gegenüber der ersten SOL-Matrix wurde nur das beanstandete Step-Beispiel korrigiert; der gezielte Kandidaten-Nachtest nutzt diese finalen Bytes: general 29 Dateien einschließlich 4 Fallback-Dateien; codex 25 Dateien ohne Python-Fallbacks. Paketlinks und Profilblöcke sind aufgelöst.
- Das Decision-Frontmatter-Beispiel wurde in vollständigen isolierten Projektprofilen mit beiden Paketvalidatoren erfolgreich geprüft.
- Skill Creators `quick_validate.py` scheitert in beiden Profilen am bereits bestehenden Feld `compatibility`, das seine lokale Whitelist nicht unterstützt. Kein grüner Lauf behauptet. YAML, Name, Description-Grenze, bekannte Frontmatter-Felder und aufgelöste Templates wurden zusätzlich geprüft; der Validator wurde nicht verändert.

## SOL-Vergleich

Angefordert: `gpt-6-sol`, Reasoning `medium`, getrennte frische Baseline-/Kandidaten-Agenten. Zusätzlicher Kandidaten-Agent für Neuanlage und Dependency-Proben. Tatsächliche Modell-/Effort-Metadaten waren nicht exponiert. Der Vergleich belegt diese Fälle, keine allgemeine Leistungssteigerung oder vollständige Kompatibilität aller denkbaren Projekte.

| Fall | Baseline | Kandidat | Beobachtung |
| --- | --- | --- | --- |
| Status/Recovery | bestanden | bestanden | Alle Projektbytes unverändert |
| Execute-Ausnahme | bestanden | bestanden | Nur Reasoning des benannten unperformten Steps und Änderungsdatum angepasst |
| todo-Pflege, erster Auftrag | Anforderung erhalten | semantisch abweichend | Kandidat ersetzte die Zusammenfassungsanforderung durch den Marker; kein bestandener Paritätsnachweis |
| todo-Pflege, explizit additive Wiederholung | bestanden | bestanden | Beide behalten die Zusammenfassungsanforderung und ergänzen den Marker; Reihenfolge korrekt, übrige Felder und Projektbytes erhalten |
| Abschluss/Rückkehr | bestanden | bestanden | Exaktes ready-LF beobachtet; W-001 abgeschlossen; W-003 fortgesetzt |
| Additive Warteschlange | bestanden | bestanden | W-005 dauerhaft eingereiht; laufendes W-001 unverändert |
| Blocker/offene Decision | bestanden | bestanden | Keine unautorisierte Fortsetzung; keine Projektänderung |
| Explizite Nachfolgepriorität | bestanden | bestanden | Konflikt benannt; keine falsche Queue-Bestätigung oder Projektänderung |
| Neues Projekt | bestanden | bestanden | Gültiger aktiver Plan mit todo-Item; Umsetzung nicht gestartet |

Die Primärinstanz hat die tatsächlichen Dateien unabhängig geprüft. Ihre erste Bewertung übersah die semantische Abweichung im todo-Fall; Astra deckte sie auf. Die korrigierte Bewertung führt diesen Fall als Abweichung. Zwei frische SOL-Agenten wiederholten anschließend einen ausdrücklich additiven Auftrag mit erhaltener ursprünglicher Anforderung erfolgreich. Das ersetzt den ursprünglichen Befund nicht und beweist keinen kausalen Zusammenhang zwischen Skill-Umbau und Modellabweichung. Der erste Neuanlagevergleich mischte baseline/codex und candidate/general; ein zusätzlicher baseline/general-Lauf stellt jetzt den profilgleichen Vergleich her. Alle schreibenden Fortsetzungsfälle bestanden den nativen Validator. Der erste Versuch hatte einen CRLF-Fehler der erzeugten Testvorlage; er wurde als Harnessfehler verworfen, die korrigierte LF-Vorlage vor dem symmetrischen Wiederholungslauf validiert.

Drei zusätzliche hypothetische Dependency-Proben am Kandidaten: general ohne Python verwendet die vorgesehene manuelle Prüfung; general mit Python und fehlendem Validator meldet die Diagnose ohne Ersatz; codex ohne geeignete Laufzeit blockiert die betroffene Operation. Dies sind Entscheidungsproben, kein Nachweis einer real deinstallierten Pythonumgebung.

## Abnahme

Astra hat die finale Umsetzung im geprüften Scope fachlich angenommen. Beide P2-Befunde sind geschlossen: das Step-Beispiel wahrt eigenständige Abnahmegrenzen; die ursprüngliche todo-Abweichung bleibt transparent dokumentiert und der explizit additive Nachtest erhält die alte Anforderung. Keine offenen relevanten Befunde aus der Nachprüfung. Astra hat die tatsächlichen Diffs und beide finalen Paketpayloads selbst verglichen: general 29/29 und codex 25/25 Dateien bytegleich.

Task `ASK PLAN-0008 Abnahme ASTRA RUN [#1]`, ID `01a0d7da-a1b7-72e1-be4a-73dcef8026a9`. Erste Referenz `plan-0008-acceptance-astra-20260925-01`, Kontext `fresh`; finale Referenz `plan-0008-acceptance-astra-20260925-02`, Kontext `continued`. Angefordert `gpt-6-astra/high`; tatsächliche Modell-/Effort-Metadaten unbekannt. Vollständige Antwort direkt an die Ursprungstask geliefert; Reviewtask bleibt für Rückfragen offen.

Astra hat in der Nachprüfung keine Tests erneut ausgeführt. Die Stichprobengrenzen und der fehlgeschlagene Skill-Creator-Check bleiben bestehen. Fachliche Abnahme und native Lifecycle-Koordination sind getrennt: PLAN-0008 bleibt draft mit verlinkter Umsetzungsevidenz, ohne den aktiven Suite-Plan zu verdrängen. Der aktualisierte native Gesamtbestand wurde erfolgreich validiert: 7 Pläne / 70 Work Items / 18 Decisions; keine Fehler oder Warnungen. Veröffentlichungsgates bleiben unberührt.

Temporäre Rohdaten und isolierte Testbäume bleiben vorerst am Taskpfad; eine frühere automatische Freigabeprüfung hatte rekursive Löschung blockiert. Kein alternativer Löschweg wurde verwendet. Die finalen Builds bleiben im eigenen Release-Staging.

## Identität der geprüften Pakete

SHA-256 über das UTF-8-JSON-Manifest aus sortierten relativen Pfaden und Datei-SHA-256-Werten (kompakt mit `,` und `:`):

- general: 29 Dateien; `cb9f4ee28ef98fc40d3cd3327222fb88daf36db9f68c9f8ff697396a1f268a7d`.
- codex: 25 Dateien; `1233cfb55ac50c72b705e7d334f4680c6c530b147fab9cc0f8c32366bfc55436`.

## Nachtrag: ungestartete Pläne löschen oder umschreiben

Am 2026-09-25 separat beauftragt und umgesetzt. `native-project-lifecycle.md` erlaubt auf Nutzerauftrag die Überarbeitung oder physische Löschung eines noch nicht ausgeführten Plans ohne vorheriges `cancelled`. Aktivierung allein zählt nicht als Ausführung; tatsächliche Arbeit und Evidence haben Vorrang vor veralteten Statusfeldern. Begonnene Historie bleibt geschützt. Die Löschung eines aktiven Plans bereitet den konsistenten Index mit vor; referenzierte Decisions werden nicht mitgelöscht.

Routentabelle und Feature-Vertrag ergänzt. Sieben Verhaltenstestfälle decken Entwurf, aktiven ungestarteten Plan, Überarbeitung, tatsächliche Ausführung trotz draft/todo, gestartete Items, cancelled mit unterschiedlicher Starthistorie und eingehende Referenzen ab. Diese Fälle sind spezifiziert, nicht als neue Modellläufe ausgeführt. Die frühere Astra-Abnahme gilt nicht für diesen Nachtrag.

78 automatisierte Tests bestanden, einschließlich drei neuer Validator-Regressionstests: Entwurf entfernen bei unverändertem aktivem Bestand; letzten ungestarteten aktiven Plan mit idle-Index entfernen und Decisions erhalten; ungültigen verbleibenden Indexverweis ablehnen. Der Validator, die Formatversion und die Helper-Schnittstellen bleiben unverändert.

Beide Builds unter `<workspace>/skills/temp/release/plan-unstarted-deletion/` erfolgreich. Lifecycle-Referenz jeweils bytegleich zur Quelle; keine offenen Templates; general mit vier Python-Fallback-Dateien, codex ohne diese Dateien. Skill Creators quick_validate scheitert unverändert ausschließlich am bestehenden `compatibility`-Feld seiner Whitelist. Keine Installation, Veröffentlichung oder Änderung bestehender Projektpläne und des aktiven Index.

### Astra Medium: Nachprüfung der Löschregel

Fresh-Review `ASK Plan deletion review ASTRA RUN [#1]`, Task `01a0d7f1-c668-7911-a5d1-7adea3a3b186`, Referenz `plan-unstarted-deletion-astra-medium-20260925-02`. Angefordert `gpt-6-astra/medium`; tatsächliche Modell-/Effort-Metadaten unbekannt. Vorherige Reviewtask war archiviert und wurde nicht reaktiviert.

Ein offener P2-Befund: `native-project-lifecycle.md:60–68` erlaubt Überarbeitung anhand bestätigter Nichtausführung, verweist aber auf W. `native-work-items.md:17–19` erlaubt Bearbeitung nur für todo in draft/active; cancelled bleibt terminal. Damit fehlt für einen vor jeder Ausführung abgebrochenen Plan oder ein solches Item eine konsistente Rewrite-Ausnahme. Kleinste Korrektur: eng begrenzte Ausnahme mit ausdrücklichem Rewrite-Auftrag und klarer Statusautorität; bestätigte Nichtausführung voraussetzen, gestartete Historie schützen. Gezielter Modellfall für vor Start cancelled plus Gegenfall mit ausgeführter Arbeit empfohlen. Noch nicht korrigiert.

Astra bestätigt die übrige Löschregel und findet keinen weiteren konkreten Kompatibilitätsdefekt. Direkter Baselinevergleich und Prüfung angrenzender Verträge sowie Paketdateien; keine Tests, Modellfälle oder Builds ausgeführt. Die 78 Tests bleiben strukturelle Evidenz, die sieben neuen Evaluationsfälle ungetestete Spezifikationen. Vollständiges Review direkt in der Ursprungstask zugestellt.

### P2-Korrektur und gezielte Nachprüfung

Die explizite Inhaltsüberarbeitung bestätigt vollständig ungestarteter Pläne umfasst nun auch cancelled-Pläne und deren todo/cancelled-Items. L besitzt die enge Ausnahme mit Vorrang vor W; W verweist darauf. IDs, Referenzen, Evidence, Reihenfolge und Lifecycle-Felder bleiben erhalten. Kein Wiederöffnen, Aktivieren, Starten oder Statuswechsel. Ausgeführte oder unklare Historie schließt die Ausnahme aus. Zwei entsprechende positive/negative Evaluationsfälle ergänzt, nicht als Modellläufe ausgeführt.

78 automatisierte Tests erneut bestanden. Beide Builds unter `<workspace>/skills/temp/release/plan-unstarted-p2/` erfolgreich; beide geänderten Referenzen jeweils bytegleich zur Quelle.

Astra Medium schließt ausschließlich den P2-Befund: keine weiteren Findings im Korrekturpunkt. Referenz `plan-unstarted-deletion-p2-fix-20260925-01`, gleiche Reviewtask `01a0d7f1-c668-7911-a5d1-7adea3a3b186`, Kontext continued, angefordert gpt-6-astra/medium, tatsächliche Metadaten unbekannt. Direkter Vergleich der drei betroffenen Dateien gegen den P2-Snapshot. Textprüfung, keine neue Gesamtabnahme und kein Modell-Verhaltensnachweis. Der zuvor als offen dokumentierte P2 ist damit geschlossen.
