#!/usr/bin/env python3
from __future__ import annotations

import argparse
from pathlib import Path


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--design-root", type=Path, default=Path(__file__).resolve().parents[2] / "scoville-design-anti-ai-slop")
    parser.add_argument(
        "--ui-root",
        type=Path,
        default=Path(__file__).resolve().parents[3]
        / "scoville-ui-anti-ai-slop"
        / "scoville-ui-anti-ai-slop",
    )
    args = parser.parse_args()
    design = " ".join((args.design_root / "SKILL.md").read_text(encoding="utf-8").split())
    ui = " ".join((args.ui_root / "SKILL.md").read_text(encoding="utf-8").split())

    required_design = {
        "design owns visual definition": "Design defines and judges; that partner implements",
        "Design standalone operation": "without a partner, handle authorised work directly within the same ownership floors",
        "no sibling dependency": "Never require or simulate another Skill",
        "visual identity owner": "corporate-design/visual-identity definition",
        "owner-attributed record": "canonical owner",
    }
    required_ui = {
        "active Design contract": "**DESIGN ACTIVE:**",
        "UI fallback contract": "**GREENFIELD FALLBACK:**",
        "UI standalone fallback": "If Design is absent, inactive, inapplicable, or explicitly excluded and no visual owner exists, retain this Skill's bounded standalone direction",
        "strict implementation": "UI owns framework-valid implementation",
        "no sibling search": "Never search",
        "visual identity input": "corporate-design/visual-identity constraints",
        "owner-attributed record": "`canonical owner`",
        "unresolved is not permission": "An unresolved or invalidated field is not permission",
    }

    errors: list[str] = []
    for label, text in required_design.items():
        if text not in design:
            errors.append(f"Design missing {label}: {text!r}")
    for label, text in required_ui.items():
        if text not in ui:
            errors.append(f"UI missing {label}: {text!r}")

    if errors:
        for error in errors:
            print(f"ERROR {error}")
        print(f"INVALID design_ui_boundary errors={len(errors)}")
        return 1
    print("VALID design_ui_boundary active_design=strict_ui ui_only=greenfield_fallback")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
