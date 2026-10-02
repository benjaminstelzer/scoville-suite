<details>
<summary>Development and builds</summary>

Sources live under `members/`. Edit README fragments in `development/readme/`,
then run `python development/build_suite.py --write-readmes`. The manifest
`suite.json` owns package membership and README composition.

[Development notes]({{ include: suite.repository }}/blob/main/docs/README.md)
explain the problems behind the suite. The
[build guide](development/shared/build/fragments.md) covers package generation,
runtime checks and Viewer assets. Installed Skills need only their own packages.

</details>
