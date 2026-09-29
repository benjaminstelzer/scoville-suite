# Astra-Review zu PLAN-0020

Angefordert: GPT-6 Astra, Effort medium. Konsolidierter Review vom 29.09.2026,
Referenz `plan0020-review-20260929-r2`, Berater-Chat
`01a0ebc4-c4e0-7b53-82d2-5ba52800853f`.
Tatsächliches Modell/Effort wurde im Review nicht durch Telemetrie bestätigt.

Ergebnis: changes_requested mit zwei P2-Befunden. W-007 und ADR-0115 wurden
für ihren Planungsumfang ohne zusätzlichen Befund bewertet.

| Befund | Korrektur am Entwurf |
| --- | --- |
| W-005 vermischt Entscheidungsvorlage und Umsetzung als Abschluss | Outcome/Acceptance verlangen umgesetzten, geprüften Vertrag oder belegten unveränderten Vertrag; eine offene materielle Entscheidung blockiert abhängige Umsetzung. |
| Shared-Helper pauschal dem falschen Owner zugeordnet | Selector und Validator ausdrücklich beim Plan-Mitglied belassen; Shared-Aussage eingegrenzt. |

Zusätzlich aufgenommen: gewöhnlichen blockierten Nachfolger vom blockierten
Rückkehrpunkt unterscheiden; bei Warten und Modellübernahme vor neuen Regeln
die konkrete Lücke gegenüber den bestehenden Regeln bestimmen.

Der Reviewer bestätigte die bestehende Kopplung von Abnahme und Nachfolgerwahl
in Plan-Instruktionen und Validator. Der Selector wählt keinen Nachfolger und
erteilt keine Startfreigabe. Eine Entkopplung erfordert eine entschiedene
Zustandsdarstellung, keine bloße Workflow-Umformulierung.

Erhalten bleiben explizite Aktivierung, materielle Stopps, ein Produktschreiber,
Deltareviews, Kontextschwellen und Workflow-Ausstieg. W-004 endet zulässig mit
einer Entscheidungsvorlage. Ask erhält keine Polling-Schleife oder automatische
Archivierung.

Grenzen: Review war lesend, ohne Live-Host-Verhaltensfälle oder schreibende Tests.
Trace-Zählungen und Manager-Telemetrie wurden nicht vollständig unabhängig
verifiziert. Die anschließenden Plantextkorrekturen wurden vom aufrufenden
Agenten gegen die Befunde geprüft, nicht erneut unabhängig begutachtet.
