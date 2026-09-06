# AutoCAM Data

Public derived voxel geometry and action masks for the AutoCAM Shadow Gym.
The UI lives in `mingwucn/AutoCAM_UI`. This release includes block, overhang,
cylinder, 3-29-00350 and 3-29-00289. The two industrial cases support both
milling and turning; the simple cylinder supports turning.

`releases/v1/catalog.json` indexes one JSON dataset per case and one fallback
PNG per case. Dataset JSON contains the 3D grid geometry and packed masks;
the browser creates the displayed surfaces from these masks. Original CAD,
internal source files, and the report/tutorial are not distributed here.

Consumers should reference an exact Git commit in their raw.githubusercontent.com
URL. The catalog records SHA-256 and byte length for each asset. `MANIFEST.json`
identifies all release files and the verified parent export from which they
were split. Per-case scenes, actions, dimensions, units and reachable masks
are retained without numerical changes. `verification/parity.json` contains
916 saved reference fixtures used by the UI tests; it is not loaded by the gym.

Run `python verify.py` to check every release file against the manifest.
The UI additionally validates supported schemas, geometry dimensions, action
references and downloaded bytes before constructing a session.

The catalog schema is `shadow-gym-catalog-1`; each case retains the existing
`shadow-gym-visual-data-1` format with exactly one scene. Asset URLs are
relative to the catalog. Masks use `packed-lsb-rle1`; lengths and coordinates
use millimetres, volumes cubic millimetres. Turning uses each scene's declared
spindle axis and holding end. These experimental geometric examples confer
no manufacturing qualification.
