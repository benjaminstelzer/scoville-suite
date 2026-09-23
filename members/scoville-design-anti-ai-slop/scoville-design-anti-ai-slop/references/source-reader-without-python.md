# Source coverage without Python

Read the requested source through the host's ordinary file reader in numbered,
bounded ranges. Record the requested total line range and the intact line
numbers actually received. Reread every missing or cut-through interval with
an intact line on each side, then join only intact received lines in source
order. If the reader cannot establish the file's end or recover an interval,
mark dependent coverage unverified; do not treat a final heading or footer as
proof that the middle arrived.
