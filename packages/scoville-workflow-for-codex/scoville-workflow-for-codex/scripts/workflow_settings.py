"""Workflow defaults and project overrides for Workflow and suite Setup."""
import sys
if sys.version_info < (3, 11):
    raise SystemExit("Python 3.11 or newer is required for Workflow helpers")
from pathlib import Path
import tomllib
from scoville_config import merge, section as config_section


ROUTES = ("ultra_low", "low", "medium", "high", "ultra_high")
EFFORTS = {"none", "minimal", "low", "medium", "high", "xhigh", "max", "ultra"}


def load_config(path: Path, project_root: Path | str | None = None) -> dict:
    with path.open("rb") as stream:
        config = merge(tomllib.load(stream), config_section('workflow', project_root))
    if type(config.get("schema_version")) is not int or config["schema_version"] != 1:
        raise ValueError("unsupported workflow schema_version")
    if set(config) - {"schema_version", "context", "execute", "review"}:
        raise ValueError("unknown workflow configuration keys")
    for section in ("execute", "review"):
        table = config.get(section)
        if not isinstance(table, dict) or set(table) != set(ROUTES):
            raise ValueError(f"{section} must contain exactly the five routes")
        for route, pair in table.items():
            if not isinstance(pair, dict) or set(pair) != {"model", "reasoning"}:
                raise ValueError(f"invalid {section}.{route} pair")
            if (not isinstance(pair["model"], str) or not pair["model"]
                    or not isinstance(pair["reasoning"], str) or pair["reasoning"] not in EFFORTS):
                raise ValueError(f"invalid {section}.{route} values")
    return config



def read_thresholds(path: Path, project_root: Path | str | None = None) -> dict:
    with path.open("rb") as stream:
        config = merge(tomllib.load(stream), config_section('workflow', project_root))
    if type(config.get("schema_version")) is not int or config["schema_version"] != 1:
        raise ValueError("unsupported workflow schema_version")
    thresholds = config.get("context")
    if not isinstance(thresholds, dict) or set(thresholds) != {"coordinator_percent", "worker_percent"}:
        raise ValueError("context requires exactly coordinator_percent and worker_percent")
    if any(type(value) is not int or not 1 <= value <= 99 for value in thresholds.values()):
        raise ValueError("context percentages must be integers from 1 through 99")
    return thresholds

