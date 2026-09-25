"""Read one project's Scoville overrides without creating files."""
from __future__ import annotations

import copy
import json
from pathlib import Path


def merge(base: dict, overlay: dict) -> dict:
    if not isinstance(overlay, dict):
        raise ValueError("configuration overrides must be an object")
    result = copy.deepcopy(base)
    for key, value in overlay.items():
        result[key] = (merge(result[key], value)
                       if isinstance(value, dict) and isinstance(result.get(key), dict)
                       else copy.deepcopy(value))
    return result


def read_config(project_root: Path | str | None = None) -> dict:
    root = Path(project_root) if project_root is not None else Path.cwd()
    if not root.is_dir():
        raise ValueError(f"project root is not a directory: {root}")
    path = root / ".scoville" / "config.json"
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        return {}
    except (UnicodeError, json.JSONDecodeError) as error:
        raise ValueError(f"invalid Scoville configuration at {path}: {error}") from error
    if not isinstance(value, dict):
        raise ValueError(f"Scoville configuration must be an object: {path}")
    for section in ("ask", "workflow"):
        if section in value and not isinstance(value[section], dict):
            raise ValueError(f"{section} configuration must be an object")
    return value


def section(name: str, project_root: Path | str | None = None) -> dict:
    return read_config(project_root).get(name, {})
