"""Read one project's Scoville overrides without creating files."""
from __future__ import annotations

import copy
import json
from pathlib import Path


def merge(base: dict, overlay: dict) -> dict:
    if not isinstance(base, dict):
        raise ValueError("base must be an object; pass the default configuration as a JSON object")
    return _merge(base, overlay, "overlay")


def _merge(base: dict, overlay: dict, path: str) -> dict:
    if not isinstance(overlay, dict):
        raise ValueError(f"{path} must be an object; provide a JSON object such as {{}}")
    result = copy.deepcopy(base)
    for key, value in overlay.items():
        child = f"{path}.{key}"
        result[key] = (_merge(result[key], value, child)
                       if isinstance(value, dict) and isinstance(result.get(key), dict)
                       else copy.deepcopy(value))
    return result


def read_config(project_root: Path | str | None = None) -> dict:
    try:
        root = Path(project_root) if project_root is not None else Path.cwd()
    except TypeError as error:
        raise ValueError("project_root must be a filesystem path string or Path; provide an existing project directory") from error
    if not root.is_dir():
        raise ValueError(f"project_root={str(root)!r} is not an existing directory; pass the project's directory path")
    path = root / ".scoville" / "config.json"
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        return {}
    except UnicodeError as error:
        raise ValueError(f"{path} must be UTF-8 JSON; save the file as UTF-8: {error}") from error
    except json.JSONDecodeError as error:
        raise ValueError(
            f"{path} is invalid JSON at line {error.lineno}, column {error.colno}; "
            f"correct the syntax near {error.msg}"
        ) from error
    if not isinstance(value, dict):
        raise ValueError(f"{path} must contain a JSON object at the root; wrap settings in {{}}")
    for section in ("ask", "workflow"):
        if section in value and not isinstance(value[section], dict):
            raise ValueError(f"{path}: $.{section} must be an object; wrap its settings in {{}}")
    return value


def section(name: str, project_root: Path | str | None = None) -> dict:
    if name not in {"ask", "workflow"}:
        raise ValueError(f"name={name!r} is not a Scoville configuration section; choose 'ask' or 'workflow'")
    return read_config(project_root).get(name, {})
