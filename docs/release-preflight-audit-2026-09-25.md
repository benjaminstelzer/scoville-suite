# Release-Audit: Scoville, Ask und private Skills

Stand: 2026-09-25. Dieses Dokument hält den vom Nutzer vorgemerkten Prüf- und Veröffentlichungsumfang fest. Es ist kein Freigabebeleg und kein Ersatz für die nativen Pläne und Entscheidungen. Außer diesem Audit-Dokument werden durch seine Erstellung keine Quellen, Installationen oder GitHub-Repositories geändert.

## Vor dem Release zu erledigen

1. **Aktuellen Stand erfassen.** Kanonische Quellen unter `<workspace-root>/skills/private/`, lokale Installationen, Suite-Manifeste und GitHub erneut vergleichen. Die GitHub-Beobachtungen unten sind eine Momentaufnahme. Parallele und uncommittete Arbeit erhalten.
2. **Native Pläne prüfen.** Vor Veröffentlichung `PROJECT_INDEX.md`, die betroffenen Pläne, Work Items und Entscheidungen auf Status, Reihenfolge, Abhängigkeiten, Zielnamen, Acceptance und Evidenz prüfen. Plan und tatsächliche Quellen, Builds sowie GitHub-Ziele dürfen nicht auseinanderlaufen. Neue Entscheidungen und laufende Arbeit seit diesem Audit einbeziehen. Insbesondere PLAN-0006, PLAN-0002/W-010 und W-011 sowie die Ask-Punkte W-001/W-002 mit ADR-0013, ADR-0016, ADR-0040, ADR-0042 und ADR-0043 abgleichen. Veröffentlichungsreihenfolge und Ask-Mitgliedschaft auf Basis des dann geltenden Auftrags klären.
3. **Aktivierung, Zuständigkeit und Familie prüfen.** Für jeden aktuellen Scoville-Skill Auslöser, explizite Aktivierung, Ausschlüsse, fachlichen Besitzer, Übergaben und Familienverweise prüfen. Standalone und allgemeine Ausgabe müssen fehlende oder inaktive Geschwister korrekt behandeln. Bei Suite-Paketen entfällt dieser bedingte Geschwisterpfad: vollständige Installation aller Mitglieder des gewählten Profils ist Pflicht. Fachliche Zuständigkeiten und gezieltes Laden bleiben auch dort korrekt.
4. **Build-Prozess prüfen.** Gegen die finalen Skill-Änderungen Manifest, kanonische Fragmente, gemeinsame Helper, Tests, `general`- und `codex`-Profil, Standalone-Pakete, Suite-Exporte und isolierten Wiederaufbau prüfen. Mitgliedschaft, Sichtbarkeit, Dateien, README-Blöcke, Links, Quellenhashes und Buildbelege müssen je Profil zusammenpassen. Nur den vorgesehenen Release-Stagingbaum verwenden und laufende Leser berücksichtigen.
5. **Python-Vertrag prüfen.** Alle Scoville-Skills und ihre gebauten Varianten auf die vereinbarte Trennung prüfen: Codex verwendet Python und vorgesehene Helper verpflichtend, ohne manuelle Python-Ersatzrouten. Die allgemeine Ausgabe enthält nur die vorgesehenen bedingt geladenen Fallbacks. Ein defekter Helper bei vorhandenem Python darf nicht still auf manuelle Ausführung ausweichen. `scoville-ask-for-codex` benötigt zusätzlich seine festgelegten Modell- und Claude-CLI-Wege.
6. **Alle READMEs prüfen.** Mit `benjaminstelzer-imitate-me` auf Benjamins Stimme prüfen. Innerhalb der Gruppen private Skills und Scoville-Skills müssen Ton, Aussagen, Voraussetzungen, Installation und Verweise konsistent sein. Eingefügte Textbausteine in Mitglieds- und Suite-READMEs müssen an ihrem Ort Sinn ergeben. Generierte Fassungen aus kanonischen Fragmenten erzeugen und mit diesen abgleichen; keine generierte Kopie getrennt pflegen.
7. **Neuinstallation und Upgrade getrennt erklären.** Die kurze Neuinstallation steht zuerst. Der Upgrade-Auftrag entfernt die unten aufgeführten exakt benannten Altinstallationen samt Einstellungen sofern vorhanden und installiert anschließend die aktuellen Pakete des gewählten Profils. Fehlende Einträge werden übersprungen; fremde Skills bleiben unangetastet. Es gibt keine Sicherung oder Einstellungsübernahme. Die fünf Ask-Altvarianten gehören in beiden Profil-READMEs zur vollständigen Bereinigung.
8. **Deprecated Skills und Namensschema festlegen.** Anhand finaler Pläne und Manifeste die wirklich abgelösten Skills und GitHub-Repositories bestimmen. Beim beauftragten Release deren Repositories privat setzen. `anti-ai-slop` aus den Namen aktueller Scoville-Skills entfernen und Repository-Namen, Skill-IDs, Paketpfade, Dokumentation, Links, Profil und Installation ohne Drift ausrichten. Die Zusammenführung der bisherigen UI- und WordPress-UI-Pakete zu `scoville-ui` berücksichtigen.
9. **Private `benjaminstelzer-*`-Skills abgleichen und einordnen.** Die kanonischen privaten Skillquellen gehören unter `<workspace-root>/skills/private/benjaminstelzer/<skill-repository>/`, nicht direkt unter `skills/private/`. Die drei derzeit direkt dort liegenden Quellverzeichnisse `benjaminstelzer-github-skill`, `benjaminstelzer-imitate-me-skill` und `benjaminstelzer-skillwriter-skill` beim beauftragten Umbau unter diesen gemeinsamen Elternordner verschieben. Vorher Git-Roots, lokale Änderungen und Verbraucherpfade prüfen; danach Build-, Test-, Dokumentations- und Installationsverweise auf den neuen Ort abgleichen und die Historie erhalten. Kanonische Quellen mit vorhandenen privaten GitHub-Repositories vergleichen, fehlende Skills privat hochladen und abweichende Repository- und Paketnamen vereinheitlichen. Besonders `benjaminstelzer-github-skill` versus Paket `benjaminstelzer-github`, `benjaminstelzer-imitate-me` und das bislang fehlende Repository für `benjaminstelzer-skillwriter` prüfen.
10. **Executables für GitHub-Releases neu erstellen.** Alle vom betroffenen Release benötigten ausführbaren Dateien, Installer und zugehörigen Checksummen aus dem finalen freigegebenen Quellenstand neu bauen. Die vorgesehenen Plattformvarianten und Artefaktprüfungen durchführen; Paket- und Versionszuordnung vor dem Hochladen abgleichen. Insbesondere den bestehenden Plan-Viewer-Asset-Vertrag für Scoville Plan und die Scoville Suite erfüllen. Die neu erstellten Dateien als Assets an die jeweils richtigen GitHub-Releases anhängen und heruntergeladene Remote-Assets samt Checksummen verifizieren.
11. **Finale Release-Prüfung und Veröffentlichung.** Alle betroffenen Pakete auf finalen Bytes gegen Pläne, Akzeptanzkriterien, Verständlichkeits- und Build-Gates prüfen. Erst im beauftragten Veröffentlichungsablauf GitHub-Namen, Sichtbarkeit, Repositories, Releases und Profil ändern. Danach Remote-Dateibäume, Versionen, Tags, Assets, Sichtbarkeit, Installationslinks und die tatsächliche Installation beziehungsweise Skill-Erkennung verifizieren.

## GitHub-Momentaufnahme für die Entfernungsliste

Am 2026-09-25 zeigen die veröffentlichten Paketverzeichnisse von `benjaminstelzer/scoville-suite` diese zehn Skill-IDs:

- `scoville-brainstorm`
- `scoville-code-anti-ai-slop`
- `scoville-design-anti-ai-slop`
- `scoville-handoff`
- `scoville-plan`
- `scoville-research`
- `scoville-scribe-anti-ai-slop`
- `scoville-ui-anti-ai-slop`
- `scoville-wordpress-ui-backend-anti-ai-slop`
- `scoville-workflow-for-codex`

Das veröffentlichte `benjaminstelzer/ask-suite-for-codex` enthält fünf weitere installierbare Skill-IDs. Sie sind Teil der verpflichtenden Bereinigung bei Migration auf den zusammengeführten Codex-Ask-Skill:

- `ask-astra-for-review-for-codex`
- `ask-sol-for-review-for-codex`
- `ask-claude-for-codex`
- `ask-claude-and-astra-for-codex`
- `ask-claude-and-sol-for-codex`

Das private Repository `benjaminstelzer/scoville-workflow-codex` enthält außerdem `scoville-workflow-codex/SKILL.md`. Diesen weiteren Altnamen nur entfernen, falls er tatsächlich installiert ist. `ask-suite-for-codex` ist ein Repository-Name, keine zusätzliche Skill-ID aus dem geprüften Paketverzeichnis.

Die vollständige Entfernungsliste umfasst auch unverändert benannte alte Skills. Beide Profil-READMEs verwenden dieselbe Liste aus den zehn früher veröffentlichten Scoville-Suite-IDs, `scoville-workflow-codex` und den fünf Ask-IDs. Die endgültige Liste unmittelbar vor Veröffentlichung gegen alte Installationsanleitungen prüfen.

## Gegenwärtige Abweichungen und offene Grenzen

- GitHub veröffentlicht noch zehn Scoville-Pakete und fünf einzelne Ask-Pakete. Die lokal eingesehene Scoville-Quelle hatte während laufender Arbeit fünf Manifestmitglieder, darunter bereits `scoville-ui`. Das ist kein fertiger Release-Beleg; eine neue Aufnahme des finalen Quellenstands ist nötig.
- ADR-0042 nennt den neuen Skill **`scoville-ask-for-codex`**. Frühere Gesprächsnotizen mit `scoville-ask` sind überholt. Der Skill gehört zur Codex-Suite und soll zusätzlich aus der allgemeinen Suite-README einzeln installierbar sein, mit dem Hinweis „Codex online“. Er ist kein Laufzeitmitglied der allgemeinen Suite.
- ADR-0043 beauftragt den Ask-Umbau und seine Tests parallel zur UI-Arbeit. Die Planpunkte zur späteren Veröffentlichung müssen vor dem Release gegen diese neue Entscheidung geprüft werden; lokale Ask-Umsetzung allein ist keine Veröffentlichung.
- Die exakte Deprecated-Liste ist noch nicht abschließend bestimmt. Alte UI- und WordPress-UI-Pakete sind durch `scoville-ui` abzulösen; die Behandlung weiterer nicht mehr aktueller Mitglieder folgt den finalen Plan- und Manifestentscheidungen.
- Zwei private `benjaminstelzer-*`-Repositories waren auf GitHub vorhanden. Ihre installierten Skill-Dateien stimmten bei der Stichprobe nicht bytegleich mit GitHub überein. Der vollständige Paketvergleich steht aus. Die drei lokalen Quellverzeichnisse liegen derzeit direkt unter `skills/private/`; der gewünschte gemeinsame Elternordner `skills/private/benjaminstelzer/` existiert noch nicht.

Quellen für diese Momentaufnahme: GitHub-Repositoryliste und Paketbäume von `benjaminstelzer/scoville-suite`, `benjaminstelzer/ask-suite-for-codex` und `benjaminstelzer/scoville-workflow-codex`; lokale `suite.json`, `PROJECT_INDEX.md`, PLAN-0002, PLAN-0006, ADR-0013, ADR-0016, ADR-0040, ADR-0042 und ADR-0043 unter `<workspace-root>/skills/private/scoville-suite/`.
