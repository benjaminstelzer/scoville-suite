## Developer links

<details>
<summary>Development and builds</summary>

Both suite editions share one maintained source and Plan. Sources live under
`members/`. Edit README fragments in `development/readme/`,
then run `python development/build_suite.py --write-readmes`. The manifest
`suite.json` owns package membership and README composition.

Shared runtime files use the same manifest file entries as member-owned files
and copy directly from their declared sources. The builder checks the packaged
inventory, source hashes and helper routes.
The shared development snapshot still supports builds from an isolated suite
checkout. The build guide gives the current checks and export commands.

[Development notes]({{ include: suite.repository }}/blob/main/docs/README.md)
explain the problems behind the suite. The
[build guide](development/shared/build/fragments.md) covers package generation,
runtime checks and Skill publication integrity. Installed Skills need only their own packages.

</details>
