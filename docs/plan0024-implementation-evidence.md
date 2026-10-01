# Nachweise für PLAN-0024

## W-001: Skillverhalten

Skill Creator validiert den neuen Skill. Die gemeinsame Schreibreferenz wird
aus `../shared/prompting/common.md` übernommen, nicht unabhängig gepflegt.

Codex CLI 0.159.0 mit angefordertem `gpt-6-luna`/`high` bearbeitete acht
isolierte Dateifälle. Die gespeicherten Ergebnisse wurden gegen die Aufträge
und die erforderlichen Bedeutungsbestandteile geprüft:

- Ergänzung erhält vorhandenen Testbefehl und neue Voraussetzung.
- Dublette und bereits geeignete Regel bleiben bytegleich.
- Kürzung erhält Quellenpfad, Begründung und manuell gepflegte Ausnahme.
- Ergänzte Regenerationsregel erhält die vorhandene Ausnahme.
- Ungeklärte Deployment-Berechtigung bleibt unverändert und wird konkret gefragt.
- Fremder Index erhält Metadaten, vorhandenen Link und neuen Navigationseintrag.
- Nativer Index verliert nur wiederholten Navigationstext und bleibt idle.

Alle neun strukturellen Sanity-Checks bestanden. Die Texte wurden zusätzlich
inhaltlich gelesen. Drei wiederholte Ergänzungsaufträge wurden in einem neuen
Lauf geprüft und ließen alle drei Dateien bytegleich.

Der erste Lauf konnte durch die CLI-Policy nicht lesen oder schreiben und ist
kein Pass. Nach Anpassung der Wegwerf-Testumgebung an den tatsächlich verfügbaren
Dateizugriff wurde der erfolgreiche Lauf ausgeführt. Keine Fixture-Befehle
wurden als Arbeitsauftrag ausgeführt, kein Plan initialisiert, keine
Modell-/Workfloweinstellung im Projekt geändert.

Rohdaten, ursprüngliche Texte, Ergebnisse und CLI-Traces liegen unter
`<workspace-root>/temp/2026-09-30-project-context-cleanup-review/behavior-core/`.
Der erste Fehlversuch ist dort unter `attempt-1/` erhalten. Die Läufe verwenden
explizite Skillauswahl und gerenderte Anweisungen des kanonischen Builders.
Die implizite Auswahl am vollständig gebauten Suite-Paket gehört zu W-002.
Die gezielten Luna-Fälle sind keine allgemeine Leistungs- oder Kostenmessung.

## W-002: Suite und Auswahl

`suite.json` registriert das neue Mitglied für General und Codex, ohne ein
eigenständiges Repository. Die zuvor vorhandenen Mitgliedsobjekte sind gegenüber
dem zu Beginn gesicherten Arbeitsstand unverändert. Code und Plan erhalten je
einen bedingten Suite-Verweis. Plan behält Felder und Lebenszyklus, Cleanup gibt
Formulierungs- und Platzierungshinweise innerhalb derselben Schreibinstanz.

README-Fragmente besitzen die Beschreibung und Nutzungshinweise. Vorschauen und
Paketdateien stammen vom kanonischen Builder. Die gemeinsame Schreibreferenz
wird in jedes Paket kopiert. Die Mindestmodellvoraussetzung gemäß ADR-0035 bleibt
von den tatsächlich beobachteten Luna-Prüfungen getrennt.

Technische Prüfungen bestanden:

- 13 Suite-Buildtests, darunter genaue Mitgliedschaft, enthaltene Schreibreferenz
  in allen drei Layouts und Abbruch bei fehlender Referenz.
- Vier kanonische Profil-/Exporttests: beide General-Layouts, Codex-Suite,
  reproduzierbare Pakete, Refresh-Schutz, Profilgrenzen und isolierte Exporte.
- Beide Exporte wurden aus einem separaten Testrepository erzeugt und ohne
  privaten Shared-Checkout bytegleich neu gebaut. Das Quellrepository wurde
  weder committed noch exportiert; seine bestehenden Freigabegates bleiben aktiv.
- Skill Creator für Quelle und gebautes Codex-Paket, README-Abgleich,
  Shared-Snapshot-Abgleich und Runtime-Helper-Prüfung.
- Drei aktuelle Builds unter `skills/temp/release/`: `general`, `codex` und
  `standalone-general`. Der Paketabgleich meldete für jeden Build keine Fehler.
  Frühere Bäume wurden vor dem Austausch anhand ihres Inventars geprüft und
  unter `state/2026-09-30-project-context-cleanup-staging/` erhalten.

Die kanonischen Shared-Profiltests erhalten die neue Mitgliedszahl und die
tatsächliche Anzahl der Cleanup-Nutzungsbeispiele. Ihre Suite-Kopie wurde
generiert. Shared-Runtime und Buildlogik wurden für diesen Plan nicht geändert.

Sieben getrennte Codex-CLI-Läufe mit angefordertem `gpt-6-luna`/`high` verwendeten
das vollständig gebaute Codex-Paket in Wegwerfprojekten:

| Auftrag | Beobachtetes Ergebnis |
| --- | --- |
| Füge das den Projektregeln hinzu | Cleanup gelesen, AGENTS.md ergänzt, bestehender Testbefehl erhalten |
| Ergänze AGENTS.md | Cleanup gelesen, manuelle Ausnahme neben bestehender Regenerationsregel ergänzt |
| Aktualisiere PROJECT_INDEX.md | Cleanup gelesen, Link ergänzt, fremde Metadaten und vorhandener Link erhalten |
| README-Tippfehler | Nur Tippfehler geändert, Cleanup nicht gelesen |
| Parseränderung | Leere Eingabe geprüft, bestehendes Split-Verhalten erhalten, Cleanup nicht gelesen |
| Überschrift aus AGENTS.md lesen | Antwort aus Datei, keine Änderung, Cleanup nicht gelesen |
| Next action eines aktiven Plans ändern | Nur benanntes Feld geändert, Index und Status bytegleich erhalten, Plan-Validator erfolgreich, Cleanup nicht gelesen |

Alle 21 Exit-, Auswahl- und Ergebniskontrollen bestanden. Die gespeicherten
Texte wurden zusätzlich inhaltlich gelesen. Der Dateiaudit bestätigt alle
installierten Skillkopien unverändert und keine unerwarteten Projektdateien.
Die Auswahl wurde durch tatsächliche Leseaufrufe im CLI-Trace festgestellt,
nicht allein durch die Abschlussantwort. Keine zweite Schreibinstanz oder
zusätzliche Freigaberunde war in diesen Fällen erforderlich.

Rohdaten liegen unter
`<workspace-root>/temp/2026-09-30-project-context-cleanup-review/behavior-routing/`.
Der geprüfte Codex-Build bleibt dort unter `built-suite-before-integration/`
erhalten. Die Hostumgebung enthielt weitere Skill-Metadaten; nur die Dateien der
Testprojekte waren isoliert. Die Fälle belegen diese Auswahl auf diesem Host,
keine universelle Aktivierungsgarantie oder Tokenersparnis.

Nach Abschluss aller Paketleser wurden Manifest, Shared-Snapshot, generierte
READMEs und Release-Staging für die parallel angekündigte Ask-/Workflow-
Integration freigegeben. Diese Nachweise beziehen sich auf den vorher gesicherten
Cleanup-Build. Öffentliche Ziele und installierte Skills wurden durch diesen
Plan nicht synchronisiert. Veröffentlichung und Installation bleiben außerhalb
seines Umfangs.
