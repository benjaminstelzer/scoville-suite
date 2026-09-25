# Audit: gemeinsamer Unterbau für Scoville UI und WordPress UI

Stand: 2026-09-24. Ergebnis: **Beide Skills erhalten einen gemeinsam gepflegten Qualitäts- und Prüfunterbau. Scoville UI ermittelt das Framework; WordPress UI konkretisiert denselben Vertrag für unterstützte plugin-eigene wp-admin-Seiten.** Das ist die empfohlene Ausgestaltung der gewünschten gemeinsamen Grundlage, noch keine Umsetzung.

Der [Fixplan PLAN-0006](plans/0006-shared-ui-foundation.md) enthält Reihenfolge, Eigentümer und Abnahme. [ADR-0015](decisions/0015-shared-ui-foundation.md) hält die vorgeschlagene technische Ausgestaltung fest. Der aktive Suite-Plan bleibt unverändert.

## Umfang und Aussagegrenze

Geprüft wurden beide kanonischen Member-Cores, ihre insgesamt 15 Referenzen, Beispiele, Testdefinitionen, relevante Entwicklungsnachweise sowie Manifest und gemeinsame Buildmechanik. Ausgangspunkt ist der veränderte Arbeitsbaum bei Commit `c89641a6d73b0ecdfb32f057663261a4aa1dd972`, nicht allein dieser Commit. Während des Audits änderten sich UI-Core und zwei UI-Referenzen durch parallele Suite-Arbeit; die betroffenen Stellen wurden erneut gelesen. Dieser Audit änderte keine Skill-Implementierung.

Die Marktübersicht nutzt am Stichtag abgerufene öffentliche Primärquellen und ausgewählte öffentliche Fehlerberichte. Sie ist keine vollständige Rangliste. Die ergänzende Recherche zu Informationsaufbau, Kommunikationsdesign und Usability erfolgte auf ausdrücklichen Wunsch ohne Recherche-Skill, direkt anhand der unten genannten Quellen. Private Skill-Texte wurden nicht in externe Suchanfragen übertragen.

Keine neuen Modellläufe, Browser-Regressionen oder Nutzertests wurden ausgeführt. Aussagen über vorhandene Testergebnisse sind als gelesene Projektberichte einzuordnen. Ob die Skills die Qualität moderner LLM-Ergebnisse messbar verbessern, weiß ich auf dieser Grundlage nicht.

## Was bereits gut abgedeckt ist

- **Beide:** kanonische Komponenten statt paralleler Gestaltungssysteme; echte Zustände und Wiederherstellung; Erhalt nativer Unterschiede; Trennung von Quellcode, gemessener Geometrie, angesehenem Render und Interaktion; begrenzte Audit-Autorität.
- **UI:** Framework-Klassifikation, unterstützte Themes, reduzierte Bewegung und Eingabewechsel als Prüfauslöser; gezielte Referenzwahl; keine pauschalen Farb-, Schrift- oder Abstandsrezepte.
- **WordPress:** Classic/Core Components/WPDS/Hybrid getrennt; tatsächlicher Portal- und Tokenbesitzer; PHP-/JS-i18n mit Trennung zwischen Übersetzbarkeit und Übersetzungslieferung; native CSS-Einheiten; explizite Versionsgrenzen und echte Ladeprüfung.
- **Informationsgestaltung ist schon vorhanden:** UI `references/ui-quality.md` behandelt Aufgabe, Hierarchie, Gruppierung, Lesbarkeit und Zustände. WordPress `references/ui-guidance.md` behandelt Navigation, Handlungen, Formulare und Feedback. Es fehlt kein vollständiges UX-Kapitel, sondern eine einheitliche, konkreter prüfbare Fassung dieser Regeln.

Die WordPress-7.1-Kernaussagen wurden erneut anhand des Dev Notes, des gepinnten `script-loader.php` und des öffentlichen Theme-Exports geprüft: `wp-theme` als Stylesheet und öffentlicher `ThemeProvider` sind belegt [W1–W3]. Stichproben für Absatzmargin, `.wrap`, Seitentitel und Button-Mindesthöhe stimmen mit dem gepinnten Core-CSS überein [W4]. Das bestätigt Quellverträge, keine geladene Plugin-Oberfläche. Nicht jede historische Token-/Paketangabe wurde neu validiert.

## Aktueller Stand öffentlich verfügbarer UI-Skills

Die folgenden Ansätze sind am abgerufenen Quellstand sichtbar; ihre Wirksamkeit wurde hier nicht experimentell verglichen.

| Ansatz | Beobachteter Mechanismus | Konsequenz für Scoville |
| --- | --- | --- |
| Anthropic `frontend-design` [S1] | Fachgebiet und Zielgruppe prägen Hierarchie, Typografie und Gestaltung; Plan, Umsetzung und Selbstkritik. | Konkreter Aufgabenbezug ist sinnvoll. Art Direction bleibt ein eigener Auftrag; keine Übernahme fremder Stilvorlieben. |
| Vercel Web Interface Guidelines [S2] | Konkrete Checks für Formulare, Fokus, Navigation, Medien, Performance und Hydration. | Fehlmechanismen als bedingte Checks übernehmen, keine komplette Fremd-Checkliste. Der Skill lädt mutable Remote-Regeln; Scovilles lokale, versionierbare Quellen sind hier vorzuziehen. |
| shadcn-Skill [S3] | Projektkontext, tatsächliche Komponenten, Varianten und konkrete API-/Kompositionsregeln. | Bestätigt den Ansatz gemeinsamer Qualitätsziele plus Framework-Adapter. Kein Grund, shadcn-Muster für WordPress vorzuschreiben. |
| Impeccable [S4] | Aufgabenbezogene Playbooks, Unterschied zwischen operativen und werbenden Oberflächen, gebündelte Prüfung; Hardening für Fehler, Lokalisierung und Randfälle. | Kontext und reale Zustände stärken. Kein zusätzlicher Befehlskatalog nötig. |
| UI/UX Pro Max [S5] | Suchbare Regeln, Stack-Erkennung, aufgabenbezogene Suchauswahl und Design-System-Ausgabe. | Retrieval kann Umfang begrenzen; ein Stil-/Palettenkatalog löst die hier belegten Lücken nicht. Numerische Standardrezepte nicht pauschal übernehmen. |
| WordPress `wpds` und `wp-plugin-development` [W5] | WPDS-Dokumentation über MCP; separat Plugin-Architektur, Settings API und Sicherheit. | Unser Spezialist ist bei Classic, i18n und Rendernachweisen spezifischer. Kein obligatorischer MCP-Zugang und keine allgemeine React-Annahme erforderlich. Backend-Sicherheit bleibt eigener Engineering-Vertrag. |

Gegenproben verhindern unkritische Übernahme: Impeccable-Issue 805 berichtet über nach visuellen Prüfungen unerkannte Touch-Probleme, enthält aber keine reproduzierbaren historischen Agententraces [S6]. UI/UX-Pro-Max-PR 434 dokumentiert einen inzwischen gemergten Fix für widersprüchliche Dark-Mode-Empfehlungen [S7]. Beides sind konkrete Warnungen vor falscher Sicherheit, kein Beleg allgemeiner Unterlegenheit. Die offene Vercel-PR 317 schlägt selbst das Pinnen der Remote-Regeln vor [S8].

## Priorisierte Befunde

Prioritäten bewerten den Verbesserungsbedarf des Skill-Vertrags. Eine fehlende konkrete Regel beweist noch keinen Fehler jeder damit erzeugten Oberfläche.

### F1 · P1 · Praktische Wirksamkeit bleibt für beide unbewiesen

**Beleg:** `development/luna-tests/ui-cases.md` bezeichnet alle 25 Fälle als hypothetisch und untersagt Browser-/Projektaktionen. `wordpress-cases.md` verlangt ebenfalls keine Ausführung. Der Bericht `luna6-65-results.md` nennt jeweils 5/5 ausgewählte UI- und WordPress-Fälle. Beide historischen Member-Pläne führen W-002 mit `USER-DEFERRED-TESTS`; WordPress `development/acceptance-astra.md` begrenzt seine Teilabnahme ausdrücklich auf Textproben.

**Folge:** Regelverständnis, Routing und bekannte Antworten sind teilweise dokumentiert. Tatsächliche Fehlererkennung, gute Informationsarchitektur und funktionierende Bedienung sind dadurch nicht nachgewiesen.

**Fix:** Ein kleiner, vorab definierter Vergleich mit echten Oberflächen und versteckten Fehlern. Gleiche Aufgaben, Inhalte, Werkzeuge und Budgets ohne UI-Skill, mit bisherigem Paket und mit Kandidat. Routing-Proben separat erhalten. Alte Testverschiebungen nicht stillschweigend als erledigt behandeln.

### F2 · P1 · Doppelte Pflege hat bereits unterschiedliche Prüfpflichten erzeugt

**Beleg:** Die beiden `references/validation.md` enthalten 122 exakt gleiche Zeilen in zusammenhängenden Blöcken ab drei Zeilen, bei 245 UI- und 148 WordPress-Zeilen. UI `validation.md:41–62` enthält Themes/Kontrastmodi, reduzierte Bewegung und relevante Eingabewechsel. WordPresss Validierung und responsive Matrix haben dafür keine gleichwertige explizite Auswahlregel. Allgemeine Keyboard-, Fokus- und WCAG-Pflichten bestehen dort bereits.

**Folge:** WordPress übernimmt die Abnahme allein, kann aber weniger konkrete Prüfbedingungen auswählen. Eine Verbesserung des allgemeinen Skills erreicht den Spezialisten nicht automatisch.

**Fix:** Qualitäts- und Validierungsgrundlage jeweils einmal pflegen und in beide Pakete bauen. WordPress behält nur zusätzliche Plattformregeln. Gleicher Unterbau bedeutet gleiche Anforderungen und Evidenzgrenzen, nicht identische Komponenten oder Breakpoints.

### F3 · P2 · Informationsaufbau ist zu wenig als gemeinsamer prüfbarer Vertrag formuliert

**Beleg:** UI `ui-quality.md` stellt Hierarchie, Priorität und Workflow wiederholt als Design-Entscheidung voran; WordPress `ui-guidance.md` formuliert dafür eigene direkte Regeln. Wiedererkennen statt Erinnern, sichtbarer Wirkungsbereich einer Aktion und begründete Offenlegung zusätzlicher Informationen sind nicht durchgängig gleich konkret.

**Folge:** Ein Agent kann Regeln zur Implementierung korrekt wiedergeben, ohne zu prüfen, ob Menschen die Information finden und eine Handlung richtig zuordnen können.

**Fix:** Den unten vorgeschlagenen kompakten Unterbau in beiden Varianten anwenden. Die normale UI-Aufgabe umfasst diese Usability-Prüfung. Ein bestehender Produktbeschluss bleibt erhalten; ein belegter Nutzungskonflikt wird konkret zurückgemeldet.

### F4 · P2 · Accessibility braucht gezielte Auslöser statt nur eine globale Normreferenz

**Beleg:** Beide nennen WCAG 2.2 AA. WordPress nennt bereits unbeeinträchtigten Fokus und `24 × 24 CSS px` samt Ausnahmen. Nicht gleich konkret sind Ablaufprüfungen für Dialogrückkehr, Drag-Alternativen, zugängliche Authentifizierung und Eingabewiederholung. UI besitzt bereits einen wertvollen Eingabewechsel-Trigger.

**Fix:** Wenige bedingte Szenarien ergänzen: Dialog öffnen/schließen und Fokus zurückführen; Drag-Funktion auch ohne Ziehen bedienen; verdeckten Fokus prüfen; bei betroffenen Formularen Paste/Autofill und Fehlerkorrektur erhalten. Exakte Pflichten einschließlich Ausnahmen aus WCAG 2.2 ableiten. APG ist Umsetzungshilfe, keine zusätzliche WCAG-Norm [U4, U5]. Keine Vollprüfung aller Kriterien bei einem lokalen Abstandsfix.

### F5 · P2 · Laufzeitqualität und Zustandswechsel sind weniger konkret als Geometrie

**Beleg:** Beide behandeln Loading/Error/Recovery und stabile Orientierung. UI verlangt, vor einer Messung auf Fonts, Inhalt und Übergänge zu warten. Ein expliziter bedingter Check auf Layoutsprünge während des Ladens, stockende Eingaben und veraltete asynchrone Ergebnisse fehlt. Der Endzustand allein kann solche Probleme nicht zeigen.

**Fix:** Bei betroffenen dynamischen Flows auch den Übergang beobachten: Verzögerung/Fehler, Werterhalt, Doppelaktion, veraltetes Ergebnis, Fokus und Layout-Stabilität. Performance nur bei konkretem Risiko messen. Keine allgemeine Lighthouse-Pflicht und kein erzwungenes React-Tuning. Core-Web-Vitals-Feldaussagen brauchen passende Felddaten; ein lokaler Screenshot oder Laborlauf reicht nicht [S9].

### F6 · P2 · Abnahme muss den gemeinsamen Unterbau und seine Paketvarianten erfassen

**Beleg:** Das Manifest kopiert derzeit getrennte Qualitäts-/Validierungsquellen. Die vorhandenen Szenarien prüfen unterschiedliche Ausschnitte; die 11 Member-JSON-Fälle des allgemeinen UI-Skills konzentrieren sich stark auf die Grenze zwischen Produktentscheidung und UI-Implementierung. Während dieses Audits wurden Referenzen durch parallele Suite-Arbeit aktualisiert.

**Fix:** Gemeinsame Fälle mit identischem Bewertungsmaßstab, ergänzt durch WordPress-Adapterfälle. Immer Paketstand, Layout und Profil benennen. Ein alter Modellbericht beweist den veränderten Arbeitsbaum nicht.

## Kompakter Regelentwurf für Informationsaufbau und Nutzerfreundlichkeit

Die Regeln sind eine eigene Synthese aus Nielsen-Heuristiken, W3C COGA, visueller Hierarchie und Plattformmustern [U1–U7]. Sie sind keine universelle Garantie und kein zusätzlicher Geschmacksstil. WCAG-Anforderungen sind getrennt normativ. COGA kennzeichnet seine weitergehenden Empfehlungen ausdrücklich als nicht erforderlich für WCAG-Konformität.

| Regel für den gemeinsamen Unterbau | Konkretes Fehlersignal / Prüfung |
| --- | --- |
| **1. Aufgabe und Ort erkennbar machen.** Titel, aktueller Bereich und relevante nächste Handlung müssen aus der Oberfläche hervorgehen. | Nutzer müssten internen Code, eine vorherige Chat-Erklärung oder den letzten Bildschirm kennen, um den Zweck zu verstehen. |
| **2. Information in Entscheidungsreihenfolge ordnen.** Benötigte Voraussetzungen und Folgen stehen vor der auslösenden Handlung; zusammengehörige Informationen bleiben zusammen. | Kosten oder destruktive Folgen erscheinen erst nach Bestätigung; Vergleichswerte stehen ohne sachlichen Grund auf getrennten Ansichten. |
| **3. Bedeutung sichtbar gruppieren.** Überschriften, Nähe, Abstand und Kontrast zeigen Beziehungen und Rang mit den Mitteln des Frameworks. | Alles ist gleich stark hervorgehoben; eine Karte oder Trennlinie suggeriert eine sachlich falsche Grenze. Keine universelle Pixel-Skala. |
| **4. Aktionen ihrem Wirkungsbereich zuordnen.** Ein primärer nächster Schritt pro Entscheidungsbereich, verständliche Konsequenz und klare Zuordnung zu betroffenen Daten. | Mehrere gleich betonte „Speichern“-Aktionen lassen offen, welche Felder gespeichert werden. Kein pauschales Ein-Button-Limit für die ganze Seite. |
| **5. Nur Sekundäres schrittweise offenlegen.** Seltene Details dürfen hinter verständlichen Bedienelementen liegen; erforderliche Information und kritische Folgen bleiben rechtzeitig auffindbar. | Pflichtfelder oder Fehler verschwinden in geschlossenen Bereichen; Expertinnen müssen bei jeder Wiederholung unnötige Zwischenschritte ausführen. |
| **6. Wiedererkennen erleichtern.** Begriffe, Navigation und gleichartige Aktionen bleiben konsistent; nötiger Kontext und Eingaben bleiben im Ablauf verfügbar. | Nutzer müssen Werte aus einem vorigen Schritt erinnern oder erraten, ob zwei verschiedene Begriffe dieselbe Aktion meinen. |
| **7. Zustand und Ergebnis am Vorgang zeigen.** Start, Fortschritt, Teilergebnis, Erfolg, Fehler und fehlende Berechtigung erhalten unterscheidbare, zugeordnete Rückmeldung. | Stille Wartezeit; leere Daten und gefilterte Nulltreffer wirken gleich; Erfolg erscheint trotz fehlgeschlagenem Speichern. |
| **8. Fehler verhindern und Erholung ermöglichen.** Anforderungen vorher zeigen, Fehler am Feld zuordnen, gültige Eingaben erhalten und reale Korrektur/Abbruch/Undo anbieten. | Generischer Toast ohne betroffenes Feld; verlorene Eingaben; nicht funktionierendes „Rückgängig“. Bestätigung nach Konsequenz, nicht für jeden Klick. |
| **9. Sprache und Hilfe dienen der Aufgabe.** Sichtbare Namen erklären Handlung und Objekt; notwendige Hilfe steht im Kontext. Geschützte Texte und Fakten bleiben erhalten. | Technische Innensicht, Platzhalter als einziger Feldname, widersprüchliche Benennung oder lange Erklärungen als Ersatz für eine verständliche Struktur. |
| **10. Den vollständigen Ablauf zugänglich halten.** Dieselbe Aufgabe bleibt bei relevanter Eingabeart, Textvergrößerung, Breite, Sprache und Einstellung bedienbar. | Optisch sauberes Mobile-Bild, aber verlorener Fokus, verdeckte Aktion, unbedienbarer Drag oder abgeschnittener notwendiger Inhalt. |

**Abnahme:** An einer konkreten Aufgabe zeigen, wo benötigte Informationen stehen, welche Aktion welchen Bereich betrifft und wie der Fehlerweg zurück zur Aufgabe führt. Ein heuristischer Expertencheck wird als solcher bezeichnet. Die Aussage „für die Zielgruppe nachweislich nutzerfreundlich“ benötigt Beobachtungen mit passenden Nutzerinnen und Nutzern, nicht nur ein Agentenurteil [U1, U7].

**Nicht pauschal übernehmen:** „7 ± 2“ als Menülimit, Drei-Klick-Regel, F-/Z-Lesemuster als Seitenvorlage, feste Schrift-/Abstandsrezepte, universelle 44px-AA-Ziele oder eine Frage pro Seite für jedes Dashboard. GOV.UK empfiehlt eine Frage pro Seite für seinen Fragentyp und verlangt dort eine Fehlerzusammenfassung auch bei einem Fehler [U6]. Das ist ein nützlicher Plattformvertrag, kein Grund, WordPresss bedarfsgerechte Fehlerzusammenfassung zu überschreiben. WCAG 2.2 AA nennt beim Mindestziel 24 CSS px einschließlich Ausnahmen [U4].

## Gemeinsame Pflege ohne Laufzeitabhängigkeit

**Empfehlung:** Zwei gemeinsame Quelldateien, keine neue Skill-Schicht und kein Remote-Regeldownload.

| Vorgeschlagener Besitzer | Inhalt | Auslieferung |
| --- | --- | --- |
| `../shared/ui/quality.md` | Aufgabenbezug, Informationsaufbau, Interaktion, Zustände, Accessibility-Grundlage; kurze Quellenzuordnung. | In beide Pakete als `references/ui-quality.md`. Die heutige lokale UI-Datei wird als Autoritätsquelle ersetzt. |
| `../shared/ui/validation.md` | Gemeinsame Auswahl relevanter Bedingungen, Source → Measurement → Sight, Interaktionsnachweise, Coverage und ehrliche Grenzen. | In beide Pakete als `references/validation-common.md`. |
| UI-Member | Framework erkennen, kanonische Komponenten/Tokens und Anpassungspunkte bestimmen; Adapterprüfung. | Bestehende `framework-alignment.md` und eine verkürzte lokale `validation.md`. |
| WordPress-Member | Unterstützte Oberflächen; Classic/Core Components/WPDS/Hybrid; Core-CSS, Versionen, Tokenladen, i18n und WordPress-spezifische Abnahme. | Bestehende spezialisierte Referenzen; generische Doppelregeln daraus entfernen. |

`suite.json` kann bereits `files[].source: shared:ui/quality.md` an beide lokalen Paketziele binden. Der Besitzer `../shared/build/build_suite.py` löst `shared:` auf und paketiert die Datei. `sync_suite_sources.py` übernimmt explizit deklarierte Shared-Dateien auch außerhalb seiner Standardordner; Receipts erfassen deren Hashes. **Quellprüfung spricht deshalb dafür, dass keine neue Buildarchitektur nötig ist.** Der konkrete neue Eintrag und der isolierte Export müssen bei Umsetzung getestet werden.

Installationen erhalten vollständige lokale Dateien. Sie importieren weder den anderen Skill noch `../shared`. Die Suite stellt weiterhin genau einen UI-Abnahmebesitzer je Oberfläche. Gemeinsame Dateien werden bei gleichem Profil/Layout bytegleich geprüft; Entwicklungs-Snapshots und Paketkopien werden nur generiert.

**Klein halten:** Vorhandene Regeln zusammenführen und ersetzen, nicht zehn Regeln zusätzlich vor jedes bisherige Kapitel setzen. Cores enthalten nur Auswahl, Zuständigkeit und kurze Invarianten. Qualitätsregeln nur bei Informations-/Interaktionsarbeit, Validierung nur bei passenden Claims laden; Quellenpflege ist kein Pflichtlesen pro Task. Im Vorher-/Nachher-Vergleich geladene Bytes/Tokens und Toolaufrufe messen. Eine kürzere Datei allein beweist keine höhere Verständlichkeit [S10].

**Aufgabengrenze:** Der gemeinsame Unterbau besitzt die grundlegende Nutzbarkeit und Informationsvermittlung beider UI-Varianten. Ausdrücklich verlangte Art Direction und Formulierungsarbeit behalten ihren eigenen Auftragsumfang. Routinemäßige Struktur- und Bedienbarkeitsprüfung braucht keinen zusätzlichen Auftrag; bestehende freigegebene Entscheidungen und geschützte Texte werden nicht still verändert.

## Vorgeschlagene praktische Vergleichsfälle

1. Einstellungsseite mit unklaren Gruppengrenzen und mehreren nicht zugeordneten Speicheraktionen; korrekte native Unterschiede als Negativkontrolle.
2. Datenansicht mit Filtern, Nulltreffern, Teilergebnis und verzögert eintreffender älterer Antwort; Zustand und nächste Handlung müssen klar bleiben.
3. Formularfehler mit erhaltenen Eingaben; Dialog schließen und zur richtigen Stelle zurückkehren; Keyboard-/Pointer-Wechsel im selben Ablauf.
4. Reflow, vergrößerter Text und verzögert geladene Inhalte; bei relevantem Drag dessen Abbruch/Alternative und Erholung.
5. WordPress Classic 7.0/7.1 und ein Core-Components-/Hybrid-Fall: native Margins, Notice-Verschiebung, Portal, tatsächliche Tokens und Übersetzbarkeit bleiben korrekt. Nur deklarierte Versionen und Sprachen zählen als geprüft.
6. Audit-only und fehlender Renderer: erreichbare Fehler finden, keine Implementierung ändern, unbekannte Zustände benennen und keine pauschale Freigabe.

Vorab festlegen: gefundene Defekte, Fehlalarme, Aufgabenabschluss, Owner-Verstöße, unberechtigte Änderungen, falsche Erfolgsmeldungen und Aufwand. Bewertungsschlüssel bleiben dem ausführenden Modell verborgen. Mindestens der projektseitig vorgesehene Luna-Lauf ist nötig; breitere Modellbehauptungen benötigen entsprechende zusätzliche Läufe. Dieser Audit hat diese Tests nicht gestartet.

## Tatsächlich ausgeführte Prüfungen

- Öffentliche Skill-Quellen am unten verlinkten Commitstand gelesen; offizielle UX-/Accessibility-Quellen und WordPress-Verträge geprüft. Externe Beispiele und Tools wurden nicht installiert oder ausgeführt.
- Vollständiger `--layout suite --profile general`-Build in Task-temp erfolgreich; Receipt-SHA-256 `2f30466ba7463ad0057e9fccb8c02d8a65304fff03ff7419cb4d645de80c0c52`. Ein vorheriger Member-Teilbuild wurde erwartungsgemäß mit „suite packages require the complete member set“ abgewiesen. Keine Veröffentlichung oder lokale Installation.
- Gemeinsamen Source-Resolver und Snapshot-Aufnahme inspiziert; Duplication-Vergleich durchgeführt. Keine allgemeine Test-Suite oder Runtime-Abnahme daraus abgeleitet.
- Lokale Dokumentlinks sowie UTF-8/LF geprüft. Die erste Profilprüfung fand eine parallel entstandene Plan-ID-Kollision; nur der neue eigene Entwurf wurde auf PLAN-0006 umnummeriert. Die anschließende Profilprüfung war mit null Fehlern und Warnungen gültig. Das belegt Struktur, keine UI-Wirksamkeit.

## Quellen

Alle Quellen am 2026-09-24 abgerufen. Commit-Links fixieren Quelltexte; Dokumentationsseiten und Issues sind zeitabhängig. Gelesen wurden die relevanten Volltexte oder ausdrücklich benannten Abschnitte, nicht nur Suchtreffer.

- **S1:** [Anthropic frontend-design](https://github.com/anthropics/skills/blob/34040c9c568585f6929bedeaad110ad08f079624/skills/frontend-design/SKILL.md).
- **S2:** [Vercel Skill](https://github.com/vercel-labs/agent-skills/blob/063bee94c3f4df8453406c830b0a7df0f2860278/skills/web-design-guidelines/SKILL.md), [konkrete Regeln](https://github.com/vercel-labs/web-interface-guidelines/blob/e3d624baaf29dc1fc645aff3e38f03e564d2d6b1/command.md).
- **S3:** [shadcn-Skill: Kontext, Principles, Critical Rules, Dokumentationszugriff](https://github.com/shadcn-ui/ui/blob/98a1fe67b439324ddc857f47fbdce056600a4329/skills/shadcn/SKILL.md).
- **S4:** [Impeccable Core](https://github.com/pbakaus/impeccable/blob/e0881d2de397d5e9761d7b35ff5017d8f5ebf69b/.agents/skills/impeccable/SKILL.md), [Hardening: Eingaben, i18n, Fehler](https://github.com/pbakaus/impeccable/blob/e0881d2de397d5e9761d7b35ff5017d8f5ebf69b/.agents/skills/impeccable/reference/harden.md).
- **S5:** [UI/UX Pro Max: Kategorien und Query Contract](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill/blob/dcc40ff5133ef78276117db0cc34e7b83cc8aeba/.claude/skills/ui-ux-pro-max/SKILL.md).
- **S6:** [Impeccable Issue 805](https://github.com/pbakaus/impeccable/issues/805), geschlossen; Bericht, nicht unabhängige Reproduktion.
- **S7:** [UI/UX Pro Max PR 434](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill/pull/434), gemergt am 2026-07-31; Tests im PR nur berichtet, hier nicht ausgeführt.
- **S8:** [Vercel PR 317](https://github.com/vercel-labs/agent-skills/pull/317), beim Abruf offen.
- **S9:** [Core Web Vitals](https://web.dev/articles/vitals): LCP, INP, CLS; Unterscheidung Labor/Feld und 75. Perzentil.
- **S10:** [Agent Skills Specification: Progressive disclosure](https://agentskills.io/specification).
- **U1:** [Nielsen: 10 Usability Heuristics](https://www.nngroup.com/articles/ten-usability-heuristics/), insbesondere 1–6 und 8–10.
- **U2:** [Nielsen: Progressive Disclosure](https://www.nngroup.com/articles/progressive-disclosure/).
- **U3:** [NN/g: Visual Hierarchy](https://www.nngroup.com/articles/visual-hierarchy-ux-definition/): Kontrast, Maßstab, Nähe und gemeinsame Regionen.
- **U4:** [WCAG 2.2](https://www.w3.org/TR/WCAG22/), insbesondere 2.4.11, 2.5.7, 2.5.8, 3.3.7 und 3.3.8.
- **U5:** [W3C COGA](https://www.w3.org/TR/coga-usable/), insbesondere 4.2.1, 4.2.6, 4.3.3 und 4.6.1; [APG Modal Dialog](https://www.w3.org/WAI/ARIA/apg/patterns/dialog-modal/).
- **U6:** [GOV.UK Question Pages](https://design-system.service.gov.uk/patterns/question-pages/), [Error Summary](https://design-system.service.gov.uk/components/error-summary/).
- **U7:** [USWDS Design Principles](https://designsystem.digital.gov/design-principles/): reale Bedürfnisse, Vertrauen, Accessibility und Kontinuität.
- **W1:** [WordPress 7.1 Theming Dev Note](https://make.wordpress.org/core/2026/07/31/design-system-theming-in-wordpress-7-1/).
- **W2:** [Core 7.1 script-loader.php](https://github.com/WordPress/WordPress/blob/b998fef9238af183f9523b3df71618e6e57498b6/wp-includes/script-loader.php).
- **W3:** [öffentlicher Theme-Export](https://github.com/WordPress/gutenberg/blob/7fe6fa42d4cf9cdd084223e3150f796567914f87/packages/theme/src/index.ts), [Provider-Implementierung](https://github.com/WordPress/gutenberg/blob/7fe6fa42d4cf9cdd084223e3150f796567914f87/packages/theme/src/theme-provider.tsx).
- **W4:** [Core common.css](https://github.com/WordPress/WordPress/blob/b998fef9238af183f9523b3df71618e6e57498b6/wp-admin/css/common.css), [buttons.css](https://github.com/WordPress/WordPress/blob/b998fef9238af183f9523b3df71618e6e57498b6/wp-includes/css/buttons.css), [WordPress Accessibility Standard](https://developer.wordpress.org/coding-standards/wordpress-coding-standards/accessibility/).
- **W5:** [offizieller wpds-Skill](https://github.com/WordPress/agent-skills/blob/9f4a603340bc7a474037967f66459391087e9165/skills/wpds/SKILL.md), [wp-plugin-development](https://github.com/WordPress/agent-skills/blob/9f4a603340bc7a474037967f66459391087e9165/skills/wp-plugin-development/SKILL.md).
