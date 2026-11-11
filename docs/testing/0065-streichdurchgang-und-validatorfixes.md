# PLAN-0065: Streichdurchgang und Validatorfixes

## Quellen und Stand

Suite-Baseline 3a6fb5d, Shared-Baseline f7e16ae. Beide entsprechen den ausgelieferten Paketen scoville-suite 4e2a7a5 und scoville-suite-for-codex-mainloop 8ded51a. Geändert wurden nur kanonische Quellen in `members/`, `development/readme/` und `../shared/`; README-Vorschauen und der Shared-Snapshot sind daraus erzeugt.

Dieser Bericht belegt Quellenänderungen, mechanische Prüfungen und einen Textvergleich. Die Wirkungsmessung (Variante A) steht im letzten Abschnitt; sie belegt keinen Vorteil beim Aufgabenerfolg.

Leitlinien waren Anthropics „Prompting Claude Fable 5.2" und „Skill authoring best practices" (beide am 2026-11-10 gelesen). Maßgeblich daraus: Verbote, Stopp- und Freigaberegeln werden wörtlich angewendet; eine Ausnahme wirkt nur in derselben Regel; Vorsichtsnotizen ohne noch gültigen Grund sind zu löschen; Referenzen liegen eine Ebene unter SKILL.md; Referenzen über 100 Zeilen bekommen ein Inhaltsverzeichnis.

## Teil 1: Plan-Validator

| Fehler | Korrektur | Regressionstest |
| --- | --- | --- |
| `WORK_DEPENDENCY_CANCELLED` traf auch abhängige Items, die selbst `done` oder `cancelled` sind. Ein Plan mit zwei abgebrochenen, voneinander abhängigen Items war nie gültig abschließbar. | `validate_profile.py` meldet den Fehler nur noch für `todo`, `in_progress` und `paused`. | `test_cancelled_dependent_of_cancelled_work_closes_validly`: beide Items abgebrochen ergibt ein gültiges Profil; dasselbe Profil mit einem offenen abhängigen Item meldet den Fehler weiter. |
| Ein Profil ohne Decisions war nach einem frischen Clone ungültig, weil Git das leere `docs/decisions` nicht speichert (`PROFILE_PATH_MISSING`; `--proposals` endete mit `PATH_MISSING`). | Bei gültigem Index gilt ein fehlendes `docs/decisions` als leere Menge. `select_context.py` behandelt `--proposals` und `--next-id decision` genauso. `docs/plans` bleibt Pflicht. | `test_missing_decisions_directory_is_an_empty_record_set`, `test_missing_decisions_directory_keeps_link_and_index_errors`, `test_missing_plans_directory_remains_invalid`, `test_missing_decisions_directory_is_an_empty_inventory`. |

Ein Verweis auf eine nicht vorhandene Decision bleibt `WORK_DECISION_MISSING`, und ein fehlender Index meldet weiterhin auch das fehlende Verzeichnis. Die manuellen Routen ohne Python (`validate_profile-fallback.md`, `select_context-fallback.md`) und `progress.md` beschreiben dasselbe Verhalten.

## Teil 2: Was sich an den Texten geändert hat

### Ladetiefe

Tiefe 1 bedeutet: direkt aus SKILL.md verlinkt. Gemessen an den gebauten Paketen.

| Skill | Tiefe vorher | Tiefe nachher | Verbleibend tiefer als 1 |
| --- | --- | --- | --- |
| Code | 3 | 1 (General 2) | General: `fallbacks/check_text_size-fallback.md` |
| Handoff | 3 | 1 (General 2) | wie Code |
| Plan | 2 | 1 (General 2) | wie Code |
| UI | 3, davon 23 Dateien tiefer als 1 | 1 (General 2) | wie Code |
| Project Context Cleanup | 3 | 1 (General 2) | wie Code |
| Workflow | 3 | 1 | keine |
| Ask | 3 | 1 | keine; `adviser.md` und `code-quality.md` sind wie zuvor unverlinkt, weil die Helper sie in den Auftrag einbetten |
| Setup | 2 | 1 | keine |
| Skillwriter | 1 | 1 | keine |

Die Kette `SKILL.md → writing.md → shell-commands.md → python-discovery.md` ist aufgelöst. Jede SKILL.md enthält stattdessen die gemeinsame Liste „Shared references" (`../shared/runtime/shared_references.md`, Include `rules.references`) mit einer sachlichen Lesebedingung je Datei. `writing.md` und `shell-commands.md` verweisen auf keine weitere Pflichtlektüre mehr; ein Test in `../shared/tests/test_shared_rules.py` hält das fest.

Die No-Python-Route bleibt in General auf Tiefe 2. Der Builder erzwingt genau eine erzeugte Route vom Helper-Vertrag in `output-delivery.md` dorthin; das zu ändern wäre eine Änderung des Helper-Routings.

### Größe

Bytes der Instruktionstexte (alle `.md` im Skillverzeichnis), General-Profil, Standalone-Layout:

| Skill | SKILL.md vorher | nachher | Referenzen vorher | nachher | Gesamt |
| --- | ---: | ---: | ---: | ---: | ---: |
| Code | 10393 | 11525 | 50463 | 48049 | −2 % |
| Handoff | 8193 | 9111 | 27331 | 24184 | −6 % |
| Plan | 10340 | 11077 | 101771 | 100657 | ±0 % |
| UI | 8688 | 10221 | 137974 | 136740 | ±0 % |
| Project Context Cleanup | 6428 | 7466 | 26107 | 22960 | −6 % |
| Skillwriter | 4859 | 5009 | 11366 | 13117 | +12 % |
| Summe | | | | | 403913 → 400116 (−0,9 %) |

Codex-Profil, Suite-Layout:

| Skill | SKILL.md vorher | nachher | Referenzen vorher | nachher | Gesamt |
| --- | ---: | ---: | ---: | ---: | ---: |
| Code | 9245 | 10144 | 47430 | 45901 | −1 % |
| Handoff | 7560 | 8512 | 24285 | 21984 | −4 % |
| Plan | 10031 | 10758 | 83056 | 82200 | ±0 % |
| UI | 8482 | 10049 | 134928 | 134540 | +1 % |
| Workflow | 5368 | 6688 | 46194 | 45730 | +2 % |
| Ask | 6376 | 7529 | 46785 | 46116 | +1 % |
| Setup | 6929 | 7970 | 23061 | 20760 | −4 % |
| Project Context Cleanup | 6024 | 7053 | 23061 | 20760 | −4 % |
| Skillwriter | 4859 | 5009 | 11366 | 13117 | +12 % |
| Summe | | | | | 505040 → 504820 (±0 %) |

Gemeinsame Referenzen, die in fast jedem Skill liegen:

| Datei | vorher | nachher |
| --- | ---: | ---: |
| writing.md | 4723 | 3474 |
| machine-data.md | 3770 | 3292 |
| shell-commands.md | 2071 | 1837 |
| output-delivery.md (General) | 7810 | 7249 |
| check_text_size-fallback.md | 3972 | 3407 |
| code-quality.md | 4224 | 5073 |

Einordnung:

- Die Texte sind umgebaut, aber nicht kürzer geworden. Der Gesamtumfang ist praktisch unverändert, und die SKILL.md-Einstiege sind um 3 bis 25 % gewachsen.
- Gründe für das Wachstum der Einstiege: Die Liste der gemeinsamen Referenzen (rund 1.000 Bytes) ersetzt den früheren Vorab-Leseabsatz (rund 330 Bytes). Dazu kommen Begründungen, in Code und UI die direkten Verweise und Beispiele, und die nach dem Bedeutungsvergleich wieder eingesetzten Regeln.
- `output-delivery.md` ist nur von 7,8 auf 7,2 KB gesunken. Eine erste Fassung lag bei 5,6 KB. Der Bedeutungsvergleich zeigte, dass ihr Vertragsangaben des Helpers fehlten: die Pflicht zu `--publish-full` bei nicht wiederholbaren Befehlen, das Ausgabelayout, die Felder der Fehlermetadaten und die Fehlerzeile ohne gespeicherte Kopie. Diese stehen wieder drin. Die Fehlersemantik selbst steht jetzt in den `instruction`-Feldern.
- Die Lektüre der Transportregeln hängt jetzt an Bedingungen. Nach altem Text waren für eine Code-Umsetzung mit Shellbefehlen SKILL.md, writing, shell-commands, python-discovery, change, validation und code-quality zu lesen, zusammen rund 35 KB. Nach neuem Text sind es SKILL.md, change, validation, code-quality und für den Abschlussbericht writing, zusammen rund 33 KB; shell-commands, python-discovery, machine-data und output-delivery sind nur bei zutreffender Bedingung fällig. Das ist eine Rechnung aus dem Regeltext, keine Beobachtung. PLAN-0064 hat für eine Codeempfehlung mit dem alten Stand 6 gelesene Skilldateien und rund 32 KB gemessen; ein Vergleichswert für den neuen Stand fehlt.
- Der Hebel zum Kürzen liegt bei den Regeln mit unklarer Herkunft, die nach Vorgabe nicht gestrichen wurden (siehe „Nicht gestrichen"), und bei der Frage, ob Verbote zu Begründungssätzen verkürzt werden dürfen (siehe „Bedeutungsvergleich").

### Gestrichene Regeln

Grundlage ist eine Herkunftsrecherche über rund 1.130 Verbots-, Gegen- und Stoppregeln (Commit, CHANGELOG, Plan-, Decision- und Testrecords). Klassen: beobachtet (ein Record nennt den Vorfall), Review (Befund einer Quellenprüfung ohne Vorfall), präventiv (mit dem Feature eingeführt), unklar. Die Recherche hat etwa 16 Regelcluster einzeln gegen Records geprüft und sonst die Klasse des einführenden Commits übernommen; „präventiv" heißt dort „kein Vorfall gefunden". Ersatzlos gestrichen wurde nur Präventives und Review-Herkunft, dazu die von dir ausdrücklich genannten Stellen.

| Skill | Gestrichen | Grund |
| --- | --- | --- |
| Gemeinsame Regeln | „These rules grant no command, write or other permission …" in writing, machine-data und shell-commands | Präventiv. Gegenregel ohne Anlass. |
| Gemeinsame Regeln | „Before requesting or reading machine reports …, read machine-data.md", „Before shell commands, read …", „Before Python commands … read python-discovery.md", „Before potentially large output … read output-delivery.md" | Pauschale Vorab-Lesepflichten; ersetzt durch die bedingte Liste in SKILL.md. |
| machine-data | Stiller Selbstcheck vor der Ausgabe („Before executing display code, check its output expressions … without printing this self-check") | Von dir benannt; Herkunft unklar. Die Ausgaberegeln selbst bleiben. |
| output-delivery | Beschreibung der Checker-Interna: Signalbehandlung, Timeout- und Cleanup-Zustände, „a tool yield is no deadline" | In die `instruction`-Felder der Helper-Ausgabe verlagert; Review-Herkunft. Die Ergebnisfelder selbst bleiben beschrieben. |
| output-delivery | „Use another agent's artifact as evidence only when explicitly supplied" | Präventiv. |
| shell-commands | „File reading does not require Python" | Review; kein Vorfall zu diesem Satz. |
| Code | Vorrangreihenfolge (ein Satz bleibt), „mode labels grant no permissions", „A future task or a risk label adds no reading requirement", „Reading both does not authorize editing both", „Recording future work does not authorize its implementation …", „If a needed reference is unavailable, obtain its text …", „Ordinary code edits do not request cleanup" | Von dir benannt oder Review/präventiv ohne Vorfall. |
| Code-Referenzen | „this reference adds no review phase", „This reference does not activate Handoff", „This requires neither another Skill nor a new record system", „this fallback creates no planning system" | Präventiv. |
| Handoff | „Handoff grants no additional task authority", „They grant no additional task reads or actions", Vorab-Leseabsatz | Präventiv und Review. Die Grenze „die Übergabe bewegt die Aufgabe nicht" bleibt, jetzt mit Grund. |
| Plan | Drei Vorab-Lesepflichten, „Ordinary Plan progress does not load Cleanup", ausführliche Vorrangreihenfolge | Präventiv; Routing steht in der Liste. |
| Project Context Cleanup | Vorab-Leseabsatz, „ordinary Plan progress needs no cleanup call" | Präventiv. |
| Setup | Zwei Vorab-Lesepflichten | Ersetzt durch die Liste. |
| UI | Vorab-Leseabsatz, „Other rows keep their triggers", „Framework keeps its normal triggers" | Wiederholungen der Routertabelle. |
| Workflow | Auslösephrasen „Start Scoville Workflow" und „scoflow codex", Alias `$scw`, „Generic delegation and discussion do not activate it", Vorab-Lesepflichten | Deine Vorgabe: genau ein expliziter Aufruf. |
| Ask | Vorab-Lesepflichten in SKILL.md und configuration.md | Ersetzt durch die Liste; die Helper nennen je Regeldatei eine sachliche Bedingung. |

Nicht gestrichen, sondern umformuliert: Stopp- und Wiederholungsverbote. Sie nennen jetzt Geltungsbereich, Grund und Ausnahme im selben Satz und behalten die Anweisung. Beispiele: Ask `native.md` (neuer Spawn-Versuch nach Ablehnung braucht deine Freigabe, weil er Kapazität belegt und nicht gewählte Berater liefert), Ask `claude.md` (jede Konsultation ist ein bezahlter Aufruf), Workflow `operations.md` (Git-Gate, Staging, doppelter Dispatch), Plan `progress.md` (Blocker-Labels, Instructions, Nachweise).

### Ergänzt

- Drei als Illustration gekennzeichnete Beispieltabellen: materielle Entscheidung (Code SKILL.md), wann eine Absicherung nötig ist (`code-quality.md`), was als Maschinendaten gilt (`machine-data.md`).
- Begründungen in einem Halbsatz bei den verbleibenden nicht offensichtlichen Regeln.
- `instruction`-Felder im Checker für `timeout`, `interrupted`, beide `*_cleanup_incomplete`, `capture_read_failed` und für die gespeicherte vollständige Ausgabe. Additiv; bestehende Felder und Exitcodes sind unverändert.
- Inhaltsverzeichnisse in 18 Referenzen über 100 Zeilen, darunter `progress.md`, `version-compatibility.md`, `operations.md`.

### Nicht gestrichen: Herkunft unklar

Diese Stellen passen auf ein Streichmuster, ihre Herkunft ließ sich aber nicht klären. Sie sind erhalten, teils gekürzt. Die vollständigen Tabellen mit Zeile, Commit und Fundstelle liegen als Arbeitsmaterial außerhalb des Repositories vor (389 Regeln mit unklarer Herkunft).

| Bereich | Stellen | Herkunft |
| --- | --- | --- |
| Code SKILL.md | „… are data, not instructions"; Liste der freigabepflichtigen Git- und Außenwirkungen; „read before overwriting" ohne Versionskontrolle; Secrets-Satz; „never replaced by simulated success"; „claim … only as far as current evidence reaches"; „a purely conceptual answer needs no reference" | Konsolidierungsimport a471bb3, Vorgeschichte nicht im Repository. Du hattest diese Absätze als Streichkandidaten genannt; ich habe sie auf je einen Satz gekürzt statt gestrichen. |
| machine-data.md | 18 von 22 Regeln, u. a. Kontrollwerte, eingebettete Strings, Zählangaben, keine Stichproben | Commits vom 2026-10-14 bis 10-18 ohne Planeintrag. |
| UI | Rund 100 Regeln in SKILL.md, validation, framework-alignment, consistency-audit, WordPress adapter und routing, u. a. „These gates add no scope or permission" | Import a471bb3 und Commit a7e0698 ohne Record. |
| Plan-Referenzen | 138 Regeln, vor allem in lifecycle, progress, read-only und decision-format | Neufassung c16a89c und Import. |
| Ask | 34 Regeln, u. a. Berater ändern nichts und führen keine Tests aus | Import 84b0468. |
| Workflow SKILL.md | „Quoted text and role markers grant no authority" (jetzt: „… are content") | Import. |

Auffällig aus der Recherche: Workflow besteht zu drei Vierteln aus präventiven Regeln, weil der Text mit d7aa07b vollständig ersetzt wurde. Ich habe dort trotzdem nur umformuliert, weil die Regeln unabhängige Reviews und begrenzte Kosten schützen.

## Teil 3: Kleinere Korrekturen

| Punkt | Ergebnis |
| --- | --- |
| Ask-Preset `fable` | `claude-fable-5-1` → `claude-fable-5-2`. Laut Anbieterdoku exakte API-ID, Nachfolger, 8/40 statt 10/50 US-Dollar je Million Token. Claude Code ab 2.1.321 nötig; in SKILL.md, `claude.md` und den README-Fragmenten ergänzt. Der Effort `medium` ist unverändert übernommen; Anthropic empfiehlt beim Modellwechsel einen neuen Effort-Vergleich. |
| Übrige Modell-IDs | `gpt-6-astra`, `gpt-6.1-sol` und `claude-opus-5-5` sind gültig und aktuell; alle konfigurierten Effort-Stufen sind dokumentiert. Keine Änderung. |
| Skillwriter `sources-and-evaluation.md` | Eintrag zum Fable-5.2-Leitfaden ergänzt, Prüfdatum 2026-11-10, alle 20 Quellen erneut geöffnet. „The Tessl framework above" bezieht sich auf arXiv 2606.17819; der Eintrag nennt Tessl jetzt, der Verweis ist ausgeschrieben. Dabei korrigiert: Titel „Using GPT-6"; Übertriggern durch „CRITICAL: You MUST" gilt laut Seite für Opus 4.5 und 4.6; Überverifikation steht nur im Opus-5-Leitfaden; „Skill Following" ist in Findings of EMNLP 2026 angenommen; „Skill-Use" belegt unabhängiges Scheitern nur für Aktivierung und Prozedurtreue. |
| Workflow-Aufruf | Einziger expliziter Aufruf ist `$scoville-workflow-for-codex`. Beschreibung, Abschnitt „Activation" und README-Fragment sind angeglichen. |
| Inhaltsverzeichnisse | Siehe „Ergänzt". SKILL.md-Dateien bekommen keines, weil sie immer vollständig geladen werden. |

## Bedeutungsvergleich gegen die Baseline

Drei unabhängige Gegenleser haben alten und neuen Stand Satz für Satz verglichen: gemeinsame Regeln und Code; Plan, Handoff, Cleanup und Skillwriter; UI, Ask, Workflow und Setup samt den Prompttexten der Helper. Sie kannten nur die beabsichtigten Änderungen, nicht meine Begründungen.

Ergebnis des ersten Vergleichs: 104 Befunde, davon 1 hoch, 15 mittel, 88 niedrig. Die Vorlagen für Plan, Work Item, Decision, Index und Handoff-Prompt, alle Befehle und alle Mermaid-Diagramme waren byte-identisch; alle Linkanker lösten auf.

| Muster | Beispiele | Behandlung |
| --- | --- | --- |
| Verbot zu Begründungssatz abgeschwächt, die Anweisung fehlte | „never repeat an accepted effect", „Never stage foreign or unreviewed work", „do not select or paraphrase binding sections" | Anweisung wieder eingesetzt, Grund im selben Satz behalten. |
| Schutzregel enger oder weiter als zuvor | Die Test-Integritätsregel in Code galt für jeden Test statt für geforderte Garantien. Setup erlaubte einen automatischen zweiten Speicherversuch. Workflow-Dispatch forderte nach einer Kapazitätsablehnung zum erneuten Lauf auf. | Auf den alten Umfang zurückgeführt. |
| Vertragsangabe des Helpers fehlte | `--publish-full` vor dem ersten Lauf, Ausgabelayout, Fehlerfelder, „mindestens eine der beiden Optionen" | Wieder in `output-delivery.md`. |
| Lesebedingung zu eng | In der Liste der gemeinsamen Referenzen griff Output Delivery erst nach dem Befehl; die Shell-Regeln nannten zusammengesetzten Text nicht. | Bedingungen erweitert. |
| Widerspruch zwischen Dateien | Workflow: Fortsetzen nur per Aufruf oder „authorized". Plan: `progress.md` gegen `repair.md` beim Wiederöffnen und bei gleichzeitigen Änderungen. | Vereinheitlicht. In Workflow ist die Aktivierung der Aufruf, auch für das Fortsetzen nach einem Stopp. |
| Prompttext der Helper sagte dem Empfänger etwas Unzutreffendes | Der Reviewer erhielt für Instruction Design die Bedingung „when authoring"; der Ask-Berater bekam Code quality ohne Leseauftrag. | Formulierungen korrigiert. |

81 Korrekturen sind eingearbeitet. Bewusst nicht übernommen wurden diese Befunde, weil sie beabsichtigte Streichungen betreffen:

| Befund | Grund |
| --- | --- |
| Die ausführliche Vorrangreihenfolge in Code und Plan fehlt | Von dir als selbstverständlich benannt; je ein Satz bleibt. |
| „Use another agent's artifact as evidence only when explicitly supplied" | Präventiv, kein Vorfall. |
| „If a needed reference is unavailable, obtain its text …" | Review-Herkunft, kein Vorfall. |
| „Ordinary Plan progress does not load Cleanup" und das Gegenstück in Cleanup | Präventiv; die Cleanup-Beschreibung schließt Routine-Updates weiter aus. |
| „Generic delegation and discussion do not activate it" in der Workflow-Beschreibung | Die implizite Aktivierung ist abgeschaltet. |

Grenze dieses Vergleichs: Er ist eine Quellenprüfung durch Modelle. Nach den Korrekturen hat kein zweiter vollständiger Vergleich stattgefunden. Geprüft ist, dass jede Korrektur an der benannten Stelle angewendet wurde und dass Build und Tests weiter bestehen. Der Vergleich zeigt nicht, wie Modelle mit dem neuen Text arbeiten.

## Prüfungen

- `python development/check_all.py` nach allen Korrekturen: 12 bestanden, 0 fehlgeschlagen, 2 Testpfade ohne Python-Tests (Code und Handoff haben nur Modellfälle). Enthalten sind Shared-Tests (101), Suite-Tests (73), Plan (147), Workflow (87), Ask (63), Setup (31), README-Vorschauen beider Profile und die Laufzeittests aller Profilpakete (33).
- Die vier neuen Regressionstests zu den Validatorfehlern schlagen mit dem alten Validator fehl und bestehen mit dem neuen.
- Geändertes paketiertes Python: `validate_profile.py`, `select_context.py`, `check_text_size.py`, `build_dispatch_prompt.py`, `ask.py`, `build_adviser_prompt.py`. Vor einer Veröffentlichung ist deshalb eine neue private Laufzeitmatrix nötig. Sie wurde nicht gestartet, weil sie einen Push in das private CI-Repository erfordert.
- Nicht ausgeführt: Exporte, Pushs, Tags, lokale Installation. Modelltests siehe „Messung Variante A".

## Messvorschlag

Ziel: prüfen, ob der neue Stand gegenüber dem alten und gegenüber „ohne Skill" weniger Abbrüche und unnötige Rückfragen bei gleichem Aufgabenerfolg erzeugt, und was das an Token kostet.

Aufgaben, jeweils in einer Wegwerfkopie mit festem Ausgangscommit:

1. **Fehlerkorrektur mit Regressionstest.** Der Fehler `WORK_DEPENDENCY_CANCELLED` im Validator auf dem Baseline-Stand. Erfolg: ein zurückgehaltener Test besteht, die übrigen Tests bleiben grün, kein Test wurde abgeschwächt.
2. **Diagnose mit Maschinendaten und gewöhnlichem Hindernis.** „Warum schlägt die Suite fehl?" mit einem mehrere tausend Zeilen langen Testreport; der erste Testaufruf scheitert einmal an einer gesperrten Datei. Erfolg: richtige Ursache benannt, kein Rohdump des Reports, der Aufruf wurde wiederholt statt abgebrochen.
3. **Planpflege mit einer materiellen und zwei unwesentlichen offenen Stellen.** Ein Work Item ergänzen, starten und abschließen. Erfolg: gültiges Profil, genau eine Rückfrage zur materiellen Stelle, keine zu den unwesentlichen.

Bedingungen je Aufgabe: ohne Skill, alter Stand (ausgelieferte Pakete), neuer Stand (Build aus dieser Quelle in ein temporäres Verzeichnis, keine Installation in deine Umgebung). Drei Wiederholungen je Zelle, also 27 Läufe je Modell.

Gezählt wird aus den Sitzungsaufzeichnungen: Abbruch (Turn endet mit offener, ohne Nutzer lösbarer Arbeit), unnötige Rückfrage (Frage zu einer nicht materiellen Stelle oder zu bereits Erlaubtem), Aufgabenerfolg nach den Kriterien oben, Eingabe- und Ausgabetoken, gelesene Skilldateien. Erfolg und Token werden per Skript ermittelt, Abbrüche und Rückfragen von Hand aus den Abschlussnachrichten.

| Variante | Modell | Läufe | Erwartete Kosten |
| --- | --- | ---: | --- |
| A | `gpt-6.1-sol`, Effort `low`, in Codex | 27 | etwa 11 US-Dollar, Spanne 6 bis 20 |
| B | zusätzlich `claude-fable-5-2`, Effort `medium`, über Claude Code | 27 | etwa 45 US-Dollar, Spanne 25 bis 80 |

Die Schätzung nimmt je Lauf rund 150.000 abrechnungswirksame Eingabetoken und 12.000 Ausgabetoken an, bei 2/10 US-Dollar (Sol 6.1) und 8/40 US-Dollar (Fable 5.2) je Million Token. Die tatsächlichen Werte hängen vom Caching und von der Lauflänge ab.

Variante A entspricht der Arbeitsbereichsregel, nach der Modelltests mit `gpt-6.1-sol` und Effort `low` laufen. Variante B weicht davon ab und braucht deshalb deine ausdrückliche Ausnahme. Sie ist die aussagekräftigere, weil der Streichdurchgang mit Befunden zu Fable 5.2 begründet ist. Neun Läufe je Bedingung zeigen grobe Unterschiede, keine kleinen; das Ergebnis wird als Stichprobe berichtet, nicht als Statistik.

## Messung Variante A (2026-11-11)

Freigegeben und ausgeführt: 27 Läufe mit `gpt-6.1-sol`, Effort `low`, über den Codex-CLI 0.167.0-alpha.3.2 der installierten Codex-App (`codex exec`). Modell und Effort sind für jeden Lauf aus der Sitzungsaufzeichnung gelesen, nicht aus Selbstauskünften. Dazu kamen vier Probeläufe zur Einrichtung; sie zählen nicht zum Ergebnis.

Aufbau:

- Getrenntes Codex-Home mit eigener Anmeldung. Die installierten Skills des Nutzers wurden je Lauf per Konfiguration abgeschaltet, Plugins ebenfalls. Bedingung „ohne" hat keine Scoville-Skills, „alt" die ausgelieferten Pakete (8ded51a), „neu" einen Build aus b395d1a.
- Je Lauf eine frische Arbeitskopie des Fixtures als Git-Repository, Sandbox `workspace-write`, ein einzelner Auftrag ohne Rückkanal. Eine Rückfrage beendet deshalb den Lauf.
- Auswertung per Skript aus Ereignisprotokoll, Arbeitskopie und Abschlussnachricht; bei Aufgabe 3 zusätzlich von Hand.

### Ergebnis

| Aufgabe | Bedingung | Erfolg | Abbrüche | Unnötige Rückfragen | Eingabetoken (Mittel) | davon nicht gecacht | Ausgabetoken (Mittel) | Gelesene Skilldateien (Mittel) |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 1 Fehlerkorrektur | ohne | 3/3 | 0 | 0 | 351.299 | 31.427 | 1.361 | 0 |
| 1 Fehlerkorrektur | alt | 3/3 | 0 | 0 | 396.807 | 40.114 | 1.947 | 9,3 |
| 1 Fehlerkorrektur | neu | 3/3 | 0 | 0 | 315.913 | 39.945 | 1.579 | 5,3 |
| 2 Diagnose | ohne | 3/3 | 0 | 0 | 94.931 | 21.203 | 581 | 0 |
| 2 Diagnose | alt | 3/3 | 0 | 0 | 147.262 | 18.537 | 1.068 | 7,3 |
| 2 Diagnose | neu | 3/3 | 0 | 0 | 104.524 | 22.860 | 935 | 5,0 |
| 3 Planpflege | ohne | 3/3 Profil gültig, Item angelegt | 0 | 0 | 92.236 | 13.388 | 826 | 0 |
| 3 Planpflege | alt | 2/3 Item angelegt | 1 | 0 | 154.782 | 22.473 | 1.626 | 7,7 |
| 3 Planpflege | neu | 3/3 Profil gültig, Item angelegt | 0 | 0 | 163.616 | 28.150 | 1.592 | 8,3 |

Beobachtungen je Aufgabe:

- **Aufgabe 1.** Alle neun Läufe beheben den Fehler, bestehen den zurückgehaltenen Test, ergänzen einen Regressionstest und schwächen keinen Test ab. Die Bedingungen unterscheiden sich im Erfolg nicht.
- **Aufgabe 2.** Alle neun Läufe wiederholen den Testaufruf nach der gesperrten Datei und nennen die richtige Ursache, ohne Code zu ändern. Ohne Skill wird der 182 KB große Testreport in allen drei Läufen roh ausgegeben; mit altem wie mit neuem Stand in keinem Lauf (größte Befehlsausgabe rund 20 KB, das sind die gelesenen Skilldateien).
- **Aufgabe 3.** Der Konflikt mit der akzeptierten Entscheidung zum JSON-Export wird mit altem und neuem Stand in allen sechs Läufen als offene Klärung benannt. Ohne Skill geschieht das in einem Lauf klar, in einem nur als Hinweis, und ein Lauf setzt stillschweigend die Ablösung der Entscheidung voraus. Ein Lauf mit altem Stand stellt die nötige Frage, legt das Work Item aber nicht an und beruft sich dabei auf „New work must fit Goal and Non-goals; ask only about unresolved scope"; er ist als Abbruch gezählt. Eine Proposal-Decision legen je ein Lauf mit altem und mit neuem Stand an.
- **Gelesene Skilldateien.** Bei den beiden Code-Aufgaben liest der neue Stand im Mittel 5 statt 7 bis 9 Dateien: `shell-commands.md` und `output-delivery.md` werden nicht mehr gelesen, `machine-data.md` und `writing.md` nur noch in jedem zweiten Lauf. Bei der Planpflege ist die Zahl gleich.

### Was das zeigt und was nicht

- Der neue Stand ist in dieser Stichprobe nicht schlechter als der alte: gleicher Erfolg, keine unnötige Rückfrage, kein Abbruch.
- Ein Vorteil beim Aufgabenerfolg ist nicht belegt. Die Aufgaben 1 und 2 löst das Modell auch ohne Skill; die Aufgaben waren dafür zu leicht.
- Die Skills haben in dieser Stichprobe zwei messbare Wirkungen gegenüber „ohne": kein Rohdump des Reports, und der Entscheidungskonflikt wird benannt. Beide zeigen alter und neuer Stand gleich.
- Der neue Stand liest in den Code-Aufgaben weniger Skilldateien. Bei Aufgabe 2 liegt die Eingabetokenzahl damit bei 105.000 statt 147.000; bei Aufgabe 1 streuen die Läufe stärker als die Bedingungen (197.000 bis 623.000). Bei Aufgabe 3 gibt es keinen Unterschied.
- Mit Skill kostet jeder Lauf mehr Token als ohne.
- Grenzen: drei Wiederholungen je Zelle, ein Modell, eine Effort-Stufe, kurze Aufgaben von ein bis zwei Minuten. Früh endende Läufe, um die es im Fable-5.2-Leitfaden geht, treten in so kurzen Aufgaben kaum auf. Für Fable 5.2 und Opus 5.5 liegt keine Messung vor.

### Abweichungen vom Vorschlag

- Das Fixture von Aufgabe 1 enthielt zwei unabhängig von der Aufgabe fehlschlagende Tests (`test_routing_contract`), weil die Skilltexte, auf die sie zugreifen, nicht mitkopiert waren. Das galt für alle Bedingungen gleich. Als Erfolg zählt, dass nach der Änderung genau diese beiden und keine weiteren Originaltests fehlschlagen. Vier der neun Läufe erwähnen die beiden Fehler im Abschlussbericht.
- „Unnötige Rückfrage" ließ sich nur an der Abschlussnachricht messen, weil der Lauf keinen Rückkanal hat.
- Tatsächlicher Verbrauch aller 31 Läufe: 6,05 Millionen Eingabetoken, davon 5,27 Millionen aus dem Cache, und 38.000 Ausgabetoken. Nach Listenpreis sind das je nach Cache-Tarif etwa 2 bis 3 US-Dollar, ohne Cache-Rabatt höchstens 12,50. Die Läufe liefen über die ChatGPT-Anmeldung; eine Abrechnung habe ich nicht eingesehen.

## Verhaltenskorrekturen und zweite Messreihe (2026-11-11)

Nach Variante A hat der Nutzer dieselben drei Aufgaben mit Opus 5.5 (medium) angeordnet, dazu Aufgaben für den UI-Skill mit Schwerpunkt auf Abständen, Größen und Ausrichtung, und die Korrektur aller dabei gefundenen Fehlverhalten in beiden Modellen. Codex-Läufe: gpt-6.1-sol/low wie in Variante A. Claude-Läufe: `claude -p --model claude-opus-5-5 --effort medium`, Skills im Arbeitsverzeichnis unter `.claude/skills`.

### Befunde und Korrekturen

| Befund | Beleg vor der Korrektur | Korrektur | Beleg danach |
| --- | --- | --- | --- |
| Plan: Opus fragt, statt das gewünschte Work Item anzulegen, wenn es mit einer akzeptierten Decision kollidiert | 6 von 6 Läufen mit altem und neuem Stand ohne Item | `authoring.md` und Punkt 3 der SKILL.md: gewünschte Arbeit trotz Konflikt als `todo` festhalten, Konflikt und offene Wahl im Item und im Bericht nennen; vorab fragen nur, wenn unklar ist, was festzuhalten ist | Opus 3 von 3, Sol 3 von 3: Item angelegt, Profil gültig, Konflikt benannt, Frage im Bericht |
| Code: Opus aktiviert den Skill bei einer Diagnoseaufgabe nicht | 0 von 6 Läufen | Beschreibung nennt Diagnose und „find out why a test, build or command fails" | 3 von 3 Läufen aktiviert |
| UI: Abstands- und Größenfehler bleiben mit und ohne Skill | Plan Viewer, je 3 Läufe: Sol ohne 2, alt 2, neu 1 fehlerfrei; Opus ohne, alt und neu je 2 | immer geladener Abschnitt „Spacing, size and alignment" in der SKILL.md | siehe nächste Tabelle |
| UI: Sol lädt mit dem neuen Einstieg keine UI-Referenzen | Formularprüfung: alt 3 von 3 Läufen mit Themenreferenzen, neu 0 von 3 | Auslöser nach Art der Aufgabe, ausdrückliche „Read … before"-Formulierungen und ein erster Arbeitsschritt „Start … by reading the references" | nur teilweise behoben, siehe unten |

### Plan Viewer: Suche und Decision-Badges ergänzen

Reales Svelte-Projekt in einer temporären Kopie. Gewertet werden 36 im gerenderten Ergebnis gemessene Punkte (Höhen, Schriftgrößen, Radien, Mittellinien, Innenabstände, Abstände zwischen Elementen, Überlauf bei drei Breiten, Stabilität der Nachbarn, Filterfunktion). Die Referenzlösung erreicht 36 von 36. „Fehlerfrei" heißt 36 von 36.

| Modell | ohne Skill | Abschnitt, erste Fassung | Abschnitt mit Wirt-Regel | dazu erster Leseschritt |
| --- | --- | --- | --- | --- |
| gpt-6.1-sol/low | 7 von 8 | 2 von 8 | 7 von 8 | 7 von 8 |
| Opus 5.5 medium | 5 von 8 | 8 von 8 | 8 von 8 | nicht gemessen |

- **Opus.** Ohne Skill bleiben in 3 von 8 Läufen Fehler (Feldhöhe 34 statt 36, Schriftgröße 13 px außerhalb der Skala, ungleicher Zeilenabstand). Mit dem Abschnitt sind es 0 von 16. Opus rendert und misst mit Skill in 15 von 16 Läufen selbst nach, ohne Skill in 1 von 8; die Läufe dauern im Mittel etwa doppelt so lang. Das Prüfskript zählt drei dieser 16 Läufe als 35 von 36, weil es den Abstand des Badges zu einem unsichtbaren Screenreader-Text misst; sichtbar ist das Layout korrekt, die Läufe sind hier als fehlerfrei gezählt.
- **Sol, erste Fassung.** Der Skill verschlechterte das Ergebnis. Sol folgte der Regel, vorhandene Komponenten wiederzuverwenden, setzte die 32 oder 36 Pixel hohe Button-Komponente ins Suchfeld und vergrößerte dafür das Feld auf 40 Pixel (dreimal) oder ließ den Button ohne Innenabstand am Feldrand (dreimal). Ohne Skill baut Sol einen schlichten 28-Pixel-Button mit 4 Pixel Abstand.
- **Sol, mit Wirt-Regel.** Der Zusatz „Reusing a component never resizes its host" behebt die Verschlechterung. Sol ist damit gleichauf mit „ohne Skill"; ein Vorteil ist für Sol auf dieser Aufgabe nicht belegt.

### Weitere UI-Aufgaben

- **Prüfung einer wp-admin-Seite und eines Formulars (nur lesen).** Alle Bedingungen und beide Modelle nennen die eingebauten Fehler etwa gleich häufig. Sol nennt beim Formular mit dem letzten Stand in 3 von 3 Läufen alle 7 Fehler.
- **Abstände gegen eine Maßtabelle korrigieren (28 Messpunkte).** Alle Bedingungen 28 von 28; die Aufgabe trennt nicht.
- **Dashboard erweitern (33 Messpunkte).** Opus in allen Bedingungen 33 von 33. Sol: ohne Skill 33, alter Stand dreimal 32, Stand mit Wirt-Regel 33, 32, 32. Die beiden 32er-Läufe mit Wirt-Regel setzen ein sichtbares Label vor das Suchfeld; das Prüfskript misst die linke Kante des Eingabefelds statt der Einheit aus Label und Feld. Das ist kein Abstandsfehler.

### Offen: Sol lädt UI-Referenzen nicht verlässlich

| Aufgabe | alter Stand | Auslöser nach Aufgabenart | dazu „Read … before" | dazu erster Leseschritt |
| --- | --- | --- | --- | --- |
| Formularprüfung | 3 von 3 | nicht gemessen | 0 von 3 | 1 von 3 (nur Framework) |
| Plan Viewer | 2 von 3 | 3 von 8 | 0 von 8 | 3 von 8 |
| Dashboard | nicht ausgewertet | nicht gemessen | 3 von 3 | nicht gemessen |

Sol/low liest die Themenreferenzen des UI-Skills mit keinem der drei Wortlaute verlässlich. In den Messungen hängt das Ergebnis nicht am Nachladen: Läufe mit und ohne geladene Referenzen unterscheiden sich weder bei den gefundenen Fehlern noch bei den Messpunkten. Deshalb stehen die Regeln für Abstände, Größen und Ausrichtung jetzt in der immer geladenen SKILL.md. Opus lädt mit dem Stand mit Wirt-Regel `validation.md` in 4 von 8 Läufen und sonst nur die SKILL.md.

### Was das zeigt und was nicht

- Belegt: Der Plan- und der Code-Befund sind in beiden Modellen behoben. Der UI-Abschnitt senkt bei Opus 5.5 medium auf der Plan-Viewer-Aufgabe die Läufe mit Abstands- oder Größenfehlern von 3 von 8 auf 0 von 16.
- Nicht belegt: ein Vorteil des UI-Skills für Sol. Auf der einzigen Aufgabe, die trennt, ist Sol mit Skill gleichauf mit „ohne Skill".
- Die Wirt-Regel entstand aus den Fehlern dieser einen Aufgabe. Sie ist allgemein formuliert, aber nur dort geprüft.
- Die vom Nutzer berichteten starken Abstandsprobleme von Sol traten in dieser Aufgabe ohne Skill nur in 1 von 8 Läufen auf. Reale Fehlfälle des Nutzers lagen nicht vor; die Messung bildet sie möglicherweise nicht ab. Sol lief mit Effort low.
- Der committete Stand enthält zusätzlich den ersten Leseschritt; mit ihm ist nur Sol gemessen, Opus nicht.
- Acht Läufe je Zelle zeigen nur deutliche Unterschiede. Fable 5.2 ist weiter ungemessen.
- Kosten: Opus-Läufe der ersten drei Aufgaben 7,57 US-Dollar, Plan-Viewer-Läufe mit Opus rund 20 US-Dollar laut CLI-Angabe. Die Sol-Läufe liefen über die ChatGPT-Anmeldung.

## Dritte Messreihe: Wiederverwendung, Größen von außen nach innen, Review (2026-11-11)

Der Nutzer hat nach der zweiten Messreihe drei Vorgaben ergänzt. Erstens: Regeln sind keine absoluten Gebote, sondern gelten, wenn ihre Voraussetzung gegeben ist; gibt es eine Framework-Komponente oder eine vorhandene Klasse, soll kein eigener Button geschrieben werden. Zweitens: Beim Umsetzen wird nicht gerendert und gemessen; die Regeln gelten beim Schreiben des Codes. Drittens: Im Review wird gemessen. Dieser Abschnitt ersetzt die Fassung des UI-Einstiegs aus der zweiten Messreihe; deren Zahlen bleiben als Verlauf stehen.

### Was sich am UI-Einstieg geändert hat

- Wiederverwendung mit Voraussetzung: Wo Framework, Design-System oder Projekt eine Komponente, Klasse, Variante oder ein Token für die Art von Element bereitstellen, wird sie verwendet; eine handgeschriebene Kopie ist ein Fehler. Sie wird über Größenvariante oder lokale Größe eingepasst.
- „Spacing, size and alignment" als Reihenfolge von außen nach innen: erst die Außengröße vom nächsten vorhandenen Gegenstück (dieselbe Zeile, dann Nachbarbereiche derselben Ebene, dann der Rest der Seite), dann einpassen, was hineinkommt; der Behälter behält seine Höhe. Eine Zeile je neuem Control nennt Vorbild und Größe. Eine nicht gesetzte Komponentengröße ist die Standardgröße und nur richtig, wo die Nachbarn sie verwenden.
- Kein Rendern beim Umsetzen: Die Beziehungen werden beim Schreiben aus der Quelle hergeleitet. Validation wird für Review, Audit, ausdrücklich verlangte Prüfung und nicht aus der Quelle erklärbare visuelle Fehler gelesen.
- Werteprüfung beim Abschluss und in jedem Review: jeden neu eingeführten Wert und jede Größenvariante für Höhe, Schriftgröße, Radius, Innenabstand und Lücke in Tokens und vorhandenen Regeln des Projekts suchen; ein sonst nirgends vorkommender Wert ist ein Fehler.

### Wertung

Zusätzlich zu den gerenderten Messpunkten wird gezählt, ob neue Elemente die vorhandenen Projektkomponenten verwenden (aus dem Diff). Drei Prüfpunkte der Plan-Viewer-Aufgaben wurden korrigiert und alle Läufe neu gewertet: Text und Abstand unsichtbarer Screenreader-Elemente zählten fälschlich mit, und eine späte Schriftumschaltung unter Last verschob die ganze Seite zwischen erster und späterer Messung um 2 Pixel. Opus-Läufe, die nur an Screenreader-Elementen scheitern, sind unten als fehlerfrei gezählt.

### Umsetzen: Suche und Decision-Badges (36 Messpunkte)

„Erfüllt" heißt: vorhandene Button-Komponente verwendet und kein Messpunkt verfehlt.

| Modell | ohne Skill | ausgelieferter Stand | endgültige Fassung |
| --- | --- | --- | --- |
| gpt-6.1-sol/low | 0 von 8 (kein Lauf mit Komponente; 8 von 8 ohne Messfehler) | 2 von 3 | 13 von 16 |
| Opus 5.5 medium | 1 von 8 (5 von 8 ohne Messfehler) | 2 von 3 | 4 von 4 |

Restfehler mit der endgültigen Fassung: Sol einmal Feldhöhe 40 statt 36, zweimal ungleicher Abstand über und unter der Suchzeile, davon einmal mit handgeschriebenem Button. Mit den beiden Vorfassungen ohne Rendern erreichte Opus 7 von 8 (ein Lauf ohne Skill-Aktivierung) und 4 von 4.

### Umsetzen: Überschriftzeile mit Zähler-Badge, Sortierauswahl und Icon-Button (33 Messpunkte)

Zweite Aufgabe im selben Projekt, an der keine Regel entstanden ist; die Referenzlösung erreicht 33 von 33.

| Modell | ohne Skill | endgültige Fassung |
| --- | --- | --- |
| gpt-6.1-sol/low | 0 von 6 | 11 von 16 |
| Opus 5.5 medium | 3 von 3 | 3 von 3 |

Sol verwendet in allen Läufen die vorhandenen Komponenten. Der Fehler ist in allen Fehlläufen derselbe: Standardgröße 36 statt der kleinen Controls (32) der Nachbarzeilen, wodurch die Überschriftzeile höher wird als die des Nachbarbereichs. Verlauf mit Skill: 3 von 6, 5 von 8, 11 von 16.

### Review einer fertigen Änderung mit vier eingebauten Fehlern

Feld 40 statt 36 hoch, Icon 3 Pixel über der Feldmitte, Zähler in 13 px, doppelter Badge-Abstand.

| Modell | ohne Skill | Fassung vor der Werteprüfung | mit Werteprüfung |
| --- | --- | --- | --- |
| gpt-6.1-sol/low: alle vier gefunden | 2 von 3 | 0 von 3 | 5 von 6 |
| gpt-6.1-sol/low: 13 px gefunden | 2 von 3 | 0 von 3 | 5 von 6 |
| Opus 5.5 medium: alle vier gefunden | 3 von 3 | 3 von 3 | 5 von 5 |

Alle Läufe beider Modelle rendern und messen im Browser und ändern keinen Code; das gilt auch ohne Skill. Die Sol-Läufe mit Werteprüfung liefen mit der Fassung unmittelbar vor der endgültigen.

### Rendern beim Umsetzen (Opus)

| Fassung | Läufe mit Headless-Browser | Dauer im Mittel | Kosten im Mittel |
| --- | --- | --- | --- |
| ohne Skill | 0 von 8 | 65 s | 0,45 USD |
| ausgelieferter Stand | 3 von 3 | 79 s | 0,57 USD |
| zweite Messreihe (Render-Schritt im Einstieg) | 22 von 23 | 146 bis 171 s | 0,90 bis 1,12 USD |
| endgültige Fassung und ihre beiden Vorfassungen | 0 von 16 | rund 95 s | rund 0,75 USD |

Sol rendert beim Umsetzen in keiner Fassung.

### Kontrollen mit der endgültigen Fassung (Sol)

- Dashboard: vorhandene Klassen in 4 von 4 Läufen wiederverwendet (ohne Skill ebenfalls 4 von 4). Drei Läufe setzen ein sichtbares Label vor das Suchfeld, das der Prüfpunkt zur linken Kante als Abweichung zählt; ein Lauf hat ungleich hohe Chips und einen abweichenden Abstand zur Kopfzeile.
- Formularprüfung: 6, 7 und 7 der 7 eingebauten Fehler genannt, kein Code geändert.
- UI-Themenreferenzen geladen: Formularprüfung 3 von 3, Dashboard 4 von 4, Überschriftzeile 14 von 16, Suche 10 von 16. In der zweiten Messreihe waren es 0 von 3, 3 von 3, nicht gemessen und 3 von 8.

### Was das zeigt und was nicht

- Belegt für Sol: Mit Skill verwendet Sol die vorhandenen Komponenten (31 von 32 Läufen gegenüber 0 von 8 bei der Suche) und macht bei der zweiten Aufgabe deutlich seltener Größenfehler (11 von 16 fehlerfrei gegenüber 0 von 6).
- Nicht erreicht: durchgehend fehlerfreie Sol-Läufe. Auf niedriger Effort-Stufe überspringt Sol in etwa jedem vierten Lauf das Nachschlagen der Nachbargröße. Die vom Nutzer gewünschten 6 von 6 sind nicht belegt.
- Belegt für Opus: kein Rendern beim Umsetzen, Messen im Review, Komponenten in 15 von 16 Läufen der drei renderfreien Fassungen wiederverwendet. Bei der zweiten Aufgabe und beim Review ist Opus auch ohne Skill fehlerfrei; dort zeigt der Skill keinen Vorteil.
- Die Regeln zu Feld und Button sowie zur Überschriftzeile enthalten Beispiele, die den Messaufgaben ähneln. Die zweite Aufgabe wurde gebaut, bevor ihre Regel entstand; eine dritte, unabhängige Umsetzungsaufgabe gibt es nicht.
- Während der Messung aktualisierte sich die Codex-App; die letzten 15 Sol-Läufe (acht der Suche, Dashboard, Formularprüfung) liefen mit codex-cli 0.167.0-alpha.4.1 statt alpha.3.2.
- Reale Fehlfälle des Nutzers lagen weiterhin nicht vor. Sol lief mit Effort low, Fable 5.2 ist ungemessen.
- Kosten: alle Opus-Läufe der zweiten und dritten Messreihe zusammen rund 83 US-Dollar laut CLI-Angabe. Die Sol-Läufe liefen über die ChatGPT-Anmeldung.

### Quellenreview vor der Veröffentlichung und Kontrollmessung

Ein unabhängiger Durchgang hat die Instruktionsänderungen unter `members/` zwischen b395d1a und 0305b89 gegen die übrigen Dateien derselben Skills und die Übergaben zu den Nachbarskills geprüft (Autorisierung, Aktivierung, widersprüchliche und doppelte Regeln, Verweise). Befunde und Korrekturen:

- UI: Layout verwies beim Umsetzen weiter auf Validation; das gilt jetzt für Review, Audit und verlangte Prüfung. „Kein Rendern beim Umsetzen" ist auf das Nachmessen von Abständen, Größen und Ausrichtung begrenzt; das Durchspielen geänderter Interaktionen folgt unverändert der Interactions-Referenz.
- UI: Die Review-Zeile überschnitt sich mit dem Quelltext-Audit und mit der eigenen Durchsicht des fertigen Diffs. Sie gilt jetzt für ein verlangtes Review oder Audit von Aussehen und Verhalten; die eigene Diff-Durchsicht zählt zum Umsetzen.
- UI: Die Regel zu Stil-Ausnahmen stand nur in Validation und wurde beim Umsetzen nicht mehr gelesen. Eine lokale Größe ist jetzt im Einstieg als Stil-Ausnahme benannt und von der Werteprüfung ausgenommen.
- UI: Doppelte Lese- und Renderregeln zusammengeführt, Auslöser in Quality an den Einstieg angeglichen, Reihenfolge Projekt, Design-System, Framework.
- Plan: Die Kurzregel im Einstieg betrifft nur noch das Anlegen neuer Arbeit als `todo`. Kollidiert die Arbeit mit einer akzeptierten Decision, wird die offene Wahl zusätzlich als vorgeschlagene Decision verknüpft, weil die Startprüfung Vorschläge und Blocker liest, nicht den Instructions-Text. Ein Bewertungsfall wurde angepasst.
- Keine Befunde zu erweiterter Autorisierung, zur Überschneidung der Code-Beschreibung mit anderen Beschreibungen, zu Plan-Status und Blockern oder zu toten Verweisen.

Nicht geändert und dem Nutzer vorgelegt: Die WordPress-Referenzen verlangen an mehreren Stellen gerenderte Belege schon beim Umsetzen; ihre Herkunft ist unklar, der Einstieg lässt eine Plattform-Referenz mit ausdrücklich genannter Prüfung gelten. Die Code-Beschreibung „find out why a ... command fails" kann den Skill auch bei Fehlern außerhalb von Code aktivieren; belegt ist das nicht. Offen ist auch, welche Regel bei einem UI-Fehler gilt, den Code reproduzieren und nach der Korrektur erneut prüfen will.

Kontrollmessung des korrigierten Stands:

| Aufgabe | gpt-6.1-sol/low | Opus 5.5 medium |
| --- | --- | --- |
| Suche und Badges, erfüllt | 3 von 8, nach Wiederherstellung eines Halbsatzes 5 von 8 | 4 von 4, kein Rendern |
| Überschriftzeile, fehlerfrei | 7 von 8, danach 3 von 4 | nicht gemessen |
| Review, alle vier Fehler | 3 von 3, im Browser gemessen | 2 von 2, im Browser gemessen |
| Planpflege: Item angelegt, Profil gültig, Wahl als Vorschlag | 3 von 3 | 3 von 3 |

Bei der Suche fehlte im ersten Kontrolldurchgang der Halbsatz „oben und unten gleich" für neue Zeilen; der ungleiche Zeilenabstand trat zweimal auf. Er steht wieder im Text, mit der Ausnahme für ungleichmäßige Nachbarzeilen. Über die drei letzten Fassungen mit demselben Regelkern zusammen erfüllt Sol die Suche in 21 von 32 Läufen (Komponente verwendet in 30 von 32) und die Überschriftzeile in 21 von 28. Die Zahlen der einzelnen Durchgänge streuen zwischen 3 von 8 und 13 von 16; acht Läufe trennen diese Fassungen nicht.

## Auslieferung (2026-11-11)

Der Nutzer hat am 2026-11-11 den lokalen Commit und den Push nach GitHub freigegeben. Lokale Installation, Tags und Releases waren nicht freigegeben und sind nicht erfolgt.

- Quellenstand: Suite 142a6b5, Shared 0ffa1ee. Die neue private [Runtime-Matrix](https://github.com/benjaminstelzer/scoville-runtime-ci/actions/runs/43049849347) besteht mit sechs Jobs auf Windows, Ubuntu und macOS (Python 3.11 und aktuell). Sie lief gegen den Stand 0305b89; die späteren Commits ändern nur Instruktionen, Changelogs und einen Bewertungsfall, der Builder hat den Nachweis für sie wiederverwendet.
- Vier Paketansichten gebaut, ihre Veröffentlichungsbelege geprüft. Beide Quellenexporte bestehen den Planvalidator und enthalten keinen privaten Projektnamen. Die neuen öffentlichen Aufzeichnungen (dieser Bericht und Plan 0065) wurden auf Zugangsdaten und persönliche Pfade durchgesehen; gefunden wurde nichts.
- Veröffentlicht und auf GitHub gegen den lokalen Commit geprüft: General 8e25415, Mainloop e0e2d8e, Code 01f1694, Handoff 398054c, Plan 7002423, Skillwriter 78489fa, UI ac66797, Ask 69992c2. Die Portabilitätsprüfungen beider Suite-Repositories sind auf GitHub erfolgreich.
- Die abschließenden Planrecords folgen als reine Metadatenaktualisierung der beiden Suite-Repositories.
- Nicht geschehen: lokale Installation oder Aktualisierung installierter Skills, Tags, Releases. Die Auslieferung bleibt im Plan offen, bis über die lokale Installation entschieden ist.

## Vierte Messreihe: Größenprüfung, Sol medium, Handoff und Skillwriter (2026-11-11)

Nach der Auslieferung beauftragt: die Regeln stimmig machen, Sol zusätzlich mit Effort medium messen, Handoff und Skillwriter testen und die getesteten Modelle in die READMEs schreiben. Der Nutzer hat den Push dieses Stands am 2026-11-11 freigegeben; die Veröffentlichung steht am Ende dieses Abschnitts.

### Was sich geändert hat

- UI-Einstieg, Schritt 1: Der Nachbar wird gelesen, wie er geschrieben ist (Komponente, Größenvariante, Klassen), und das neue Element genauso geschrieben.
- UI-Einstieg, Schritt 7: Die Werteprüfung listet jede eingesetzte Komponente mit ihrer Größenvariante, auch `default`. Eine Größe, die von den passenden Nachbarn abweicht, ist ein Fehler. Vorher erfasste die Prüfung nur neu geschriebene Werte; eine weggelassene Größenangabe fiel durch.
- UI-Einstieg, Schritt 8: Der Bericht nennt je neuem Bedienelement das Vorbild und die Größe.
- UI-Einstieg, Referenztabelle: kein Nachmessen des Layouts beim Umsetzen, auf jeder Plattform. Ein gemeldeter Layoutfehler, den der Quelltext erklärt, wird dort verfolgt und behoben. Die Ausnahme für Plattform-Referenzen entfällt.
- WordPress `classic-patterns.md` und `routing.md`: Beim Umsetzen gelten die dokumentierten Core-Deklarationen als Quellenbeleg, der Abstand wird als ungeprüft berichtet; Review, Audit und verlangte Prüfung messen. `version-compatibility.md` blieb unverändert: Seine Token-Prüfung steht schon unter „In a rendered check".
- Nicht geändert: die Code-Beschreibung („find out why a ... command fails"). Ein Fehlauslösen ist nicht belegt, und eine engere Fassung hätte die gemessene Aktivierung bei Diagnosen wieder riskiert.

### Ergebnis

Sol ist `gpt-6.1-sol` über `codex exec`; die Stufe ist je Lauf aus der Sitzungsaufzeichnung gelesen. Opus ist `claude-opus-5-5` mit `--effort medium`.

| Aufgabe | Sol low mit Skill | Sol medium mit Skill | Sol medium ohne Skill | Opus 5.5 medium mit Skill |
| --- | --- | --- | --- | --- |
| Überschriftzeile, fehlerfrei | 13 von 16 | 8 von 8 | 0 von 4 | nicht neu gemessen |
| Suche und Badges, erfüllt | 11 von 16 | 8 von 8 | 0 von 4 | 4 von 4 |
| Review, alle vier Fehler | 2 von 3 | 3 von 3 | nicht gemessen | 2 von 2 |
| Handoff erstellen (16 Prüfpunkte) | nicht gemessen | 4 von 4 | 0 von 3 | 3 von 3 (ohne Skill 0 von 2) |
| Zusammenfassung, Handoff darf nicht auslösen | nicht gemessen | 2 von 2 | nicht gemessen | 1 von 1 |
| Skillwriter: Skill vereinfachen (19 Prüfpunkte) | nicht gemessen | 4 von 4 | 3 von 3 | 3 von 3 (ohne Skill 2 von 2) |
| Skillwriter: Review ohne Änderung | nicht gemessen | 3 von 3 | 2 von 2 | 2 von 2 |

- **Sol medium.** Mit Skill sind alle 16 Umsetzungsläufe fehlerfrei und verwenden die vorhandenen Komponenten. Ohne Skill macht Sol medium in allen vier Läufen der Überschriftzeile die bekannten Größenfehler (36 statt 32 px) und schreibt bei der Suche in allen vier Läufen den Button selbst. Die Läufe dauern mit Skill im Mittel rund 150 statt 95 Sekunden auf low.
- **Sol low.** 13 von 16 und 11 von 16 liegen im Bereich der dritten Messreihe (21 von 28 und 21 von 32). Die Fehlläufe zeigen dieselben Fehler: Standardgröße in der Überschrift, Feld 40 statt 36 px. Ein Effekt der neuen Größenprüfung auf low ist nicht belegt. Die Berichtszeile aus Schritt 8 schreibt Sol selten (10 von 48 Berichten nennen Größen), Opus durchgehend.
- **Opus.** Umsetzen ohne Browserstart, rund 98 Sekunden und 0,78 US-Dollar je Lauf, wie vor der Änderung. Review misst im Browser und ändert keinen Code.
- **Handoff.** Die Aufgabe übergibt eine angefangene Korrektur mit Nutzeränderung, verworfenem Ansatz, Freigabevorbehalten und einem Zugangsschlüssel. Mit Skill liefern beide Modelle genau das eingezäunte Artefakt mit vier Abschnitten und drei Schritten, nennen alle geprüften Fakten, schreiben `BILLING_API_TOKEN=[redacted]`, führen keine Tests aus und ändern nichts. Ohne Skill fehlt der Aufbau; der Schlüsselwert erscheint auch dort in keinem Lauf, der Variablenname mit Schwärzung aber auch nicht. Bei der bloßen Zusammenfassung wird Handoff nicht gelesen.
- **Skillwriter.** Die Aufgabe ist ein überladener Skill mit Großbuchstaben-Geboten, Wiederholungen und einem Widerspruch zwischen SKILL.md und Stilreferenz. Mit Skill bleiben in allen Läufen alle geprüften Regeln, Name und Beschreibung erhalten; der Text schrumpft von 2612 auf rund 1570 Zeichen; der Widerspruch wird gemeldet und nicht eigenmächtig entschieden. Ohne Skill gelingt das beiden Modellen ebenso. Ein Vorteil von Skillwriter ist an dieser Aufgabe also nicht belegt, ein Schaden auch nicht.

### Wertung von Hand

- Suche, fünf Läufe: Ein sichtbares Label über dem Feld zählt das Prüfskript als ungleichen Zeilenabstand, obwohl der Zeilenabstand gleich ist (zwei Läufe medium, einer low, dort mit selbst geschriebenem Button und deshalb nicht erfüllt). Ein Feld, das seinen Namen über ein umschließendes `label` bekommt, erkennt das Skript nicht (ein Lauf low). Ein unsichtbarer Screenreader-Text vor dem Badge zählt als Vorgänger (ein Lauf Opus). Diese Läufe sind nach Durchsicht des Diffs gewertet.
- Skillwriter, drei Läufe: Zeilenumbrüche in „Omit empty groups" und „GitHub Release" und Code-Auszeichnung um die Gruppennamen trafen das Prüfmuster nicht; die Muster sind korrigiert und alle Läufe neu gewertet.

### Was das zeigt und was nicht

- Mit Sol medium und Opus 5.5 medium erfüllen UI, Handoff und Skillwriter ihre Aufgaben in dieser Stichprobe ohne Fehllauf. Für UI ist der Vorteil gegenüber „ohne Skill" auf medium belegt (16 von 16 gegen 0 von 8).
- Sol low bleibt bei etwa drei Vierteln. Die READMEs nennen deshalb medium als Mindeststufe.
- Plan und Code sind mit Sol nur auf low gemessen (dort fehlerfrei) und mit Opus auf medium. Auf Sol medium wurden sie auf Wunsch des Nutzers nicht wiederholt.
- Grenzen: zwei UI-Aufgaben in einem Projekt, je acht Läufe auf medium; je eine Aufgabe für Handoff und für die Skillwriter-Überarbeitung; keine WordPress-Aufgabe, die geänderten WordPress-Stellen sind ungemessen; Fable 5.2 ungemessen. Project Context Cleanup, Ask, Workflow und Setup sind in dieser Reihe nicht mit Modellen gemessen.
- Verbrauch: 83 Sol-Läufe über die ChatGPT-Anmeldung, 19 Opus-Läufe für zusammen 7,35 US-Dollar nach CLI-Angabe.

### Veröffentlichung des Stands

- Quellenstand: Suite 70e91a1, Shared 3475631. Paketiertes Python ist unverändert; die vier Paketansichten verwenden den bestandenen Runtime-Lauf 43049849347 weiter, ihre Veröffentlichungsbelege sind gültig.
- Beide Quellenexporte bestehen den Planvalidator, enthalten keinen privaten Projektnamen und wurden auf persönliche Pfade und Zugangsdaten durchsucht; gefunden wurde nichts.
- Veröffentlicht und auf GitHub gegen den lokalen Commit geprüft: General 8866244, Mainloop 5fa7077, Code ffcbdec, Handoff 8cffb95, Plan d9d7a13, Skillwriter d493c79, UI d5ffc8d, Ask 35a8f24.
- Dieser Nachtrag folgt als reine Aktualisierung von Plan und Bericht in den beiden Suite-Repositories.
- Nicht geschehen: lokale Installation, Tags, Releases.
