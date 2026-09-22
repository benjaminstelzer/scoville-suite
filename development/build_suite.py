#!/usr/bin/env python3
"""Suite-local entrypoint for the canonical sibling shared build tool."""
import importlib.util
from pathlib import Path

_ROOT = Path(__file__).resolve().parents[1]
_SHARED = _ROOT.parent / "shared" / "build" / "build_suite.py"
if not _SHARED.is_file():
    _SHARED = _ROOT / "development/shared/build/build_suite.py"
_spec = importlib.util.spec_from_file_location("shared_suite_builder", _SHARED)
_module = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_module)

# Expose the same callable contract to suite tests.
within = _module.within
load = _module.load
readme = _module.readme
payload = _module.payload
build = _module.build
render_readmes = _module.render_readmes

if __name__ == "__main__":
    raise SystemExit(_module.main(default_root=_ROOT))
