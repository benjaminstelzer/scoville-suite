Every byte outside what the complete result needs stays as it was, line
endings and encoding included, in every file. A script that rewrites a file
and a Git command that rewrites the working tree can change them, and
`git diff` hides line endings that Git normalizes. Write a file back with the
line endings and encoding it had. To see or test the state before your
change, use a copy, such as the project copied with your change reversed or
the output of `git show <commit>:<path>` saved in a temporary folder; do not
stash, reset, check out or restore files in the working tree for that. A
project check or test that passes before your change still passes after it.
Change or remove one only where the request changes or removes the guarantee
it tests, or to keep testing that guarantee another way, and name the edit
and its reason in the report.
