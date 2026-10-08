# Native Ask review

Handle: /root/plan0035_public_paths_sol_review

Die folgende vollständige native Abschlussantwort gehört zum unveränderten
Paketstand vor den drei Korrekturen. Angefordert gpt-6.1-sol/high; tatsächliche
Host-Telemetrie vom Reviewer nicht berichtet. Kein Testlauf durch den Reviewer.

**Review-Urteil: changes_requested.** Ich bestätige drei Fehler im installierten Paketstand. Ich habe keine Änderungen, Tests, Delegation oder Veröffentlichung ausgeführt.

`adviser_id: sol`  
`consultation_reference: plan0035-public-skill-paths-sol`  
Scope unverändert: Public installed Skill paths, imports and helper diagnostics from the machine inventory. Angefordert: `gpt-6.1-sol/high`; tatsächliches Modell und Effort sind mangels Host-Telemetrie unbekannt.

1. **[P2] Report-Lesefehler verlieren Eingabe und Korrekturweg.**  
   **GROUP-099, SITE-005688 und SITE-005865**, run_feedback.py:182 (`<workspace>/temp/2026-10-06-plan0036/result-contract-runtime-candidate/packages/codex-suite/scoville-workflow-for-codex/scoville-workflow-for-codex/scripts/run_feedback.py:182`), außerdem die Report-Lesewege in Zeilen 129, 143, 164, 189 und 200; gemeinsame Fehlerausgabe in Zeile 390.  
   **Mechanismus:** `report_path()` prüft Dateiform und Lage. Danach lesen die Consumer direkt mit `read_text(encoding='utf-8')`. Ein `UnicodeDecodeError` erreicht `parser.error(str(error))` unverändert. Die reine Decode-Meldung enthält weder `--report-file` noch den betroffenen Pfad, die erwartete Reportform oder einen Korrekturweg.  
   **Auswirkung:** Ein beschädigter oder anders codierter bestehender Report blockiert insbesondere die verpflichtende abschließende Report-Lektüre mit einer nicht ausreichend zuordenbaren Diagnose. Der Fehlerstatus bleibt erhalten; hier liegt kein fälschlicher Erfolg vor.  
   **Kleinste Korrektur:** Die vorhandenen Report-Lesewege mit einer gemeinsamen kontexttragenden Lesefunktion versehen: Argument und Pfad nennen, einen vollständig lesbaren UTF-8-Report erwarten und zur Wiederherstellung der bekannten Reportbytes beziehungsweise zur Prüfung des tatsächlich von `create` zurückgegebenen Pfades anleiten. Keine Ersatzdatei erzeugen und keine Inhalte erraten. Kanonischer Besitzer: `members/scoville-workflow-for-codex/scoville-workflow-for-codex/scripts/run_feedback.py`.

2. **[P2] Selector-Dateidiagnosen enthalten keinen Korrekturweg.**  
   **GROUP-053, SITE-002315**, select_context.py:270 (`<workspace>/temp/2026-10-06-plan0036/result-contract-runtime-candidate/packages/codex-suite/scoville-plan/scoville-plan/scripts/select_context.py:270`); gleichartige unmittelbar benachbarte Branches **SITE-002311** und **SITE-002322**, Zeilen 266 und 272. Betroffen sind alle vier aufgeführten Paketpositionen, einschließlich der Workflow-Kopie.  
   **Mechanismus:** Ungültiges UTF-8, BOM und inkonsistente Zeilenenden erzeugen `SelectorError` mit Code, Pfad und Feststellung. `diagnostic_payload()` ergänzt keine Handlungsanweisung. Beispielsweise endet `FILE_UTF8_INVALID` mit „canonical file is not valid UTF-8“.  
   **Auswirkung:** Der Aufrufer erhält einen eindeutigen Fehler und keinen partiellen Kontext, aber nicht den für W-017 geforderten Korrekturweg. Die Root-Diagnosen erfüllen diesen Teil bereits; die Dateidiagnosen tun es nicht.  
   **Kleinste Korrektur:** Die bestehenden Meldungen um die jeweilige erwartete Dateiform und konkrete inhaltserhaltende Korrektur ergänzen: bekannte beabsichtigte UTF-8-Bytes wiederherstellen, nur BOM entfernen beziehungsweise Zeilenenden vereinheitlichen, ohne beschädigten Inhalt zu erraten. Codes, Pfad und Exitstatus beibehalten. Kanonischer Besitzer: `members/scoville-plan/scoville-plan/scripts/select_context.py`.

3. **[P2] Validator öffnet einen nicht regulären Indexpfad vor einer Dateitypprüfung.**  
   **GROUP-054, SITE-002955 und SITE-002963**, validate_profile.py:474 (`<workspace>/temp/2026-10-06-plan0036/result-contract-runtime-candidate/packages/codex-suite/scoville-plan/scoville-plan/scripts/validate_profile.py:474`); Consumer `_parse_index()` in Zeile 1420, **SITE-003231**.  
   **Mechanismus:** `_read_file()` liest den `lstat`-Status in `before`, prüft aber vor `os.open(..., O_RDONLY)` nicht `stat.S_ISREG(before.st_mode)`. Für Plan- und Decision-Dateien übernimmt `_scan_markdown()` diese Prüfung; `PROJECT_INDEX.md` wird unmittelbar gelesen.  
   **Abgeleitete Auswirkung:** Ein irrtümlich als `PROJECT_INDEX.md` vorhandener FIFO kann auf Linux/macOS beim Öffnen auf einen Writer warten, statt eine vollständige Dateidiagnose mit Fehlerstatus zurückzugeben. Das ist eine Codefolgerung, keine ausgeführte Reproduktion. Die reguläre Dateiform ist bereits durch die anderen Consumer etabliert.  
   **Kleinste Korrektur:** Den bereits erhobenen Status vor dem Öffnen auf reguläre Datei prüfen und bei abweichender Form eine bestehende strukturierte Diagnose mit Pfad, Erwartung und Wiederherstellungshinweis zurückgeben. Kanonischer Besitzer: `members/scoville-plan/scoville-plan/scripts/validate_profile.py`.

Die tatsächlich geprüfte Abdeckung umfasst **GROUP-001 bis GROUP-105**: vollständige öffentliche Python-Helper, ihre Aufrufer und Consumer sowie die pfadbezogenen Anleitungsabschnitte, Assets, Fallbackregeln und Paketpositionen. Alle **246 installierten Dateien** existieren und stimmen mit ihren Indexhashes überein. Die beiden vorgegebenen Inventarhashes und der zusätzlich gelieferte Auflösungsindexhash stimmen ebenfalls.

Im Auflösungsindex sind **298 echte lokale Markdown-Dateireferenzen und 26 lokale Python-Imports** vorhanden. Die **45 explizit verankerten lokalen Referenzpositionen** haben passende Zielüberschriften. Die zwei „fehlenden“ Referenzen `request` sind lexikalische Fehlklassifikationen von `OPERATIONS[operation](request)`, keine Dateipfade. Ich finde keinen bestätigten fehlenden Paketpfad oder Import aus einem benachbarten installierten Skill. Workflow löst benötigte Suite-Skills ausdrücklich auf; seine Bibliothekskopien liegen lokal. Die General-Fallbacks sind auf fehlendes Python beschränkt, Codex enthält keine entsprechenden manuellen Helper-Fallbackdateien.

Projektpfade, Reportpfade, temporäre Verzeichnisse, `sys.executable`, `CODEX_HOME` und Sessionpfade sind dynamische Eingaben beziehungsweise Hostpfade. `<…>`-Argumente, Beispiel-Projektbäume und WordPress-Pluginpfade sind beabsichtigte Platzhalter oder Consumer-Beispiele, keine fehlenden Skill-Assets.

**Prüflücken:** Keine relevante Inhaltsgruppe blieb unbetrachtet. Die tatsächliche Laufzeitausführung auf den drei Betriebssystemen, Hostzugriff, Dateisystemunterstützung für Hardlinks und externe URLs wurden nicht geprüft. Die berichteten CI-Erfolge ersetzen diese unabhängige Laufzeitprüfung nicht; der reale Linux-Gesamtlauf bleibt nach den gelieferten Angaben ungestartet. Weitere unbestätigte Bedenken führe ich nicht als Befunde an.
