# Native Decision batches

For an explicitly authorized accept-or-reject batch, read each affected
Decision and prepare its new status and acceptance date together.

Give the batch one unused ID `batch-YYYYMMDD-N`, where N is a positive integer.
List the complete ordered member IDs in `transition_batch_members` on every
member and use the same `transition_batch` value. Check existing batch IDs
before choosing N. No digest or receipt is needed.

Check that each member lists itself and that all members carry the same ID and
member order. Preserve this metadata in later lifecycle transitions. Apply the
prepared changes and validate their references and statuses together. Report a
partial write instead of treating it as a complete transition.

New readers also accept historical 64-hex batch IDs without recomputing them.
Older readers that require that shape reject the new readable IDs. Update the
validator and selector before writing new batch IDs; existing
records need no migration. This is read compatibility with old records, not a
promise that older readers accept new syntax.

The Viewer does not read Decision-batch metadata.
