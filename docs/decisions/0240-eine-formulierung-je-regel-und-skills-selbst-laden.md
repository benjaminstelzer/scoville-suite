---
format_version: 1
id: ADR-0240
status: accepted
created: 2026-11-20
accepted: 2026-11-20
scope: suite/quality
---

# Eine Formulierung je Regel; Prüfer laden die Skills selbst

## Decision

Binding sections: complete

Jede Regel eines Skills steht einmal, an der Stelle, die auf jedem Weg geladen ist, auf dem die Regel gilt. Sie gilt für Schreiben, Review und Audit gleich. Abschnitte für Review, Audit oder Schlusskontrolle sagen, dass gegen den Skill geprüft wird und wie berichtet wird; sie formulieren keine eigenen Regeln und zählen die Regeln nicht in anderen Worten auf. Andere Stellen verweisen auf den Eigentümer. Eine engere Regel, die etwas ergänzt, bleibt zulässig.

Ein Prüfer prüft gegen den ganzen Skill, mit dem der Schreibende gearbeitet hat. Agenten laden die Skills, die sie brauchen, selbst; das ist Voraussetzung der Skills. Kein Skill gibt einem Prüfer Regeln als eingebetteten Text mit, und kein Skill enthält einen Ersatzweg für einen Agenten, der keine Skills laden kann.

- Code: Der getrennte Prüfer prüft mit dem Skill; der Ersatz „Regeltext mitgeben" entfällt.
- Workflow: Der Auftrag an einen neuen Reviewer nennt Scoville Code und für Oberflächen Scoville UI. Das Hilfsskript bettet keine Code-Regeln ein und enthält keine eigenen Reviewregeln. Workflow führt keine Kopie der Code-Regeln.
- Ask: Für ein Code-Review nennt der Auftrag Scoville Code und Scoville UI, wenn sie neben Ask installiert sind. Sind sie es nicht, prüft der Berater ohne Skill. Ask schickt keine Code-Regeln mit und führt keine Kopie.

Schreib- und Shell-Regeln bleiben in den Aufträgen von Workflow und Ask eingebettet: Sie regeln, wie der Agent berichtet, und ein Explorer oder Berater lädt unter Umständen keinen Skill.

Diese Entscheidung ersetzt in ADR-0229 den Satz, dass Workflow und Ask den Bestand der Code-Regeln über eigene Ladewege nutzen. Der Grundsatz aus ADR-0229, dass Autoren und Reviewer dieselben Kriterien verwenden, bleibt.

## Problem

Regeln standen mehrfach: für Schreibende und in anderen Worten für Prüfer, in SKILL.md und in Referenzen, in Hilfsskripten. Die Fassungen wichen voneinander ab. Die Fragen am Ende der Code-Regeln deckten weniger ab als die Regeln, und die Review-Anleitung machte sie zur Prüfliste. Ein Review prüfte dadurch Teile der Regeln nicht und an anderer Stelle Dinge, die der Schreibende nicht kannte.

## Drivers

- Nutzerentscheidungen vom 2026-11-19 und 2026-11-20: keine doppelt formulierten Regeln; Prüfer laden die Skills selbst; keine Ausnahme für Agenten ohne Skill-Zugriff; Ask nutzt Scoville Code, wenn installiert, sonst keinen Skill.
- Derselbe Grundsatz, den Regel 4 der Code-Regeln für Code festlegt: eine Quelle je Tatsache.

## Considered alternatives

- Code-Regeln als erzeugte Kopie einbetten: Die Kopie weicht nicht von Hand ab, enthält aber nur einen Teil des Skills; Testregeln und UI fehlen dem Prüfer.
- Je nach Installation einbetten oder laden: zwei Wege für dieselbe Aufgabe.

## Consequences

Eine einzeln installierte Fassung von Ask prüft Code ohne Regeln. Der Berater liest die Skill-Ordner außerhalb des Arbeitsordners; mit den Einstellungen von Ask ist dieser Lesezugriff für die Claude-CLI an einem echten Aufruf bestätigt. Referenzen werden nur bei Anlass geladen: Der Eigentümer einer Regel wird nach dem Ladeweg gewählt, nicht nur nach dem Thema.

## Confirmation

Die Gesamtprüfung der Suite besteht auf Suite `7950535` und Shared `a3c8cab`. Zwei unabhängige Prüfungen mit Claude Opus 5.5 (xhigh) je Änderungsschritt; ihre Befunde sind eingearbeitet. Modelltests des Standes mit gpt-6.2-sol und Claude Opus 5.5 auf medium stehen im Testbericht zu PLAN-0067. Unter Codex sind die Aufträge von Workflow und Ask an echte Agenten nicht erprobt.

## Revisit when

Ein Modelltest zeigt, dass Prüfer die genannten Skills nicht laden, oder der Nutzer ändert die Voraussetzung, dass Agenten Skills selbst laden.
