# AutoCAM Data

Public derived geometry/action data and versioned experimental browser runtimes
for the AutoCAM Shadow Gym.
The UI lives in `mingwucn/AutoCAM_UI`. This release includes block, overhang,
cylinder, 3-29-00350 and 3-29-00289. The two industrial cases support both
milling and turning; the simple cylinder supports turning.

`releases/v1/catalog.json` indexes one JSON dataset per case and one fallback
PNG per case. Dataset JSON contains the 3D grid geometry and packed masks;
the browser creates the displayed surfaces from these masks. Original CAD
files and the report/tutorial are not part of that legacy release.

Consumers should reference an exact Git commit in their raw.githubusercontent.com
URL. The catalog records SHA-256 and byte length for each asset. `MANIFEST.json`
identifies all release files and the verified parent export from which they
were split. Per-case scenes, actions, dimensions, units and reachable masks
are retained without numerical changes. `verification/parity.json` contains
916 saved reference fixtures used by the UI tests; it is not loaded by the gym.

Each process mode includes an `example` action array and `example_meta`. Simple
shapes use report-authored teaching sequences. Each industrial scene also has a
`workflow`: one shared stock, a Turning-first default, and a mixed-process
example whose Milling actions consume the material left by Turning. Users may
switch processes without resetting the shared state. These examples are
explanatory geometric replays, not optimal or manufacturing-recommended routes.

Run `python verify.py` to check every release file against the manifest.
The UI additionally validates supported schemas, geometry dimensions, action
references and downloaded bytes before constructing a session.

The catalog schema is `shadow-gym-catalog-1`; each case retains the existing
`shadow-gym-visual-data-1` format with exactly one scene. Asset URLs are
relative to the catalog. Masks use `packed-lsb-rle1`; lengths and coordinates
use millimetres, volumes cubic millimetres. Turning uses each scene's declared
spindle axis and holding end. These experimental geometric examples confer
no manufacturing qualification.

## Adaptive browser runtime release

`RUNTIME_RELEASES.json` pins the runtime release indices. The
`releases/adaptive-20260912/` directory contains an ordered synthetic mill-turn
catalogue and the companion browser STEP preparation runtime. Each `release.json`
uses `autocam-ui-assets-1` and lists exact file sizes and SHA-256 hashes. Keep the
entire directory structure intact and use a Git commit URL to fetch it.

These packages include shared Python runtime source, Pyodide dependencies,
WebAssembly geometry code and prepared adaptive material states. The UI verifies
them during its build, then serves them as static assets. People can select
their own STEP files locally in the browser; those files are not uploaded here.
The selected geometry profiles are experimental and do not support all CAD.
This release preserves the tested historical runtime and does not imply
compatibility with newer task5 model checkpoints or trained-policy qualification.

`python verify.py` checks the legacy data and both runtime releases. The UI's
local preflight covers the six-action turning/transfer/four-face example, three
ball/flank groove routes, and the supported STEP fixture with exact decision
downloads and restores. This is geometric verification, not an optimal workplan
or manufacturing certification. Large replays remain slow.
