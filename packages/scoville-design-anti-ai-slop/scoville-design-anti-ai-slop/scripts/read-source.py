#!/usr/bin/env python3
"""Emit numbered UTF-8 source lines; never certify tool delivery or comprehension.

Usage: python scripts/read-source.py PATH [--start N --end N]
Without an interval, emit the whole source. Choose smaller intervals only for an
actual transport need; there is no file-size, module-count or token policy here.
The byte hash identifies the source, not the output later received by an agent.
Recovery: compare returned numbered intervals with requested intervals per file.
Reread gaps and cut-through lines with intact neighbours in smaller responses;
join only received intact lines in source order. Preserve conflicting returns.
An EMITTED footer or final paragraph cannot close missing middle lines. If
coverage cannot be recovered, keep dependent rules/acceptance unverified.
"""

import argparse
import hashlib
from pathlib import Path
import sys


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('path', type=Path)
    parser.add_argument('--start', type=int)
    parser.add_argument('--end', type=int)
    args = parser.parse_args()
    try:
        path = args.path.resolve(strict=True)
        source = path.read_bytes()
        # Match Python's source-line semantics, including blank lines and CRLF.
        # An initial UTF-8 BOM is preserved in line 1; it creates no extra line.
        lines = source.decode('utf-8').splitlines()
    except (OSError, UnicodeError) as error:
        parser.exit(2, f'Cannot read UTF-8 source: {error}\n')
    total = len(lines)
    first = args.start if args.start is not None else (1 if total else 0)
    last = args.end if args.end is not None else total
    if not ((total == 0 and first == last == 0) or 1 <= first <= last <= total):
        parser.error(f'Interval {first}-{last} is outside source lines 1-{total}.')
    if hasattr(sys.stdout, 'reconfigure'):
        sys.stdout.reconfigure(encoding='utf-8', newline='\n')
    output = [f'SOURCE={path.as_uri()} TOTAL={total} RANGE={first}-{last}',
              f'BYTES={len(source)} SHA256={hashlib.sha256(source).hexdigest()}']
    if total:
        output.extend(f'{number}: {lines[number - 1]}'
                      for number in range(first, last + 1))
    output.append(f'EMITTED={first}-{last}; not proof of received coverage')
    sys.stdout.write('\n'.join(output) + '\n')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
