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

## STEP finishing allowance runtime

`releases/adaptive-allowance-20260913/cad/` adds an exact numeric finishing
allowance for supported planar solids and solid coaxial cylindrical parts.
It preserves the reserve through stock preparation, indexed workpiece poses
and source-derived turning/milling actions. Positive allowance for bores and
general CAD is not supported. Zero allowance retains the existing preparation.

The UI supplies the requested amount locally; files stay in the browser.
Machining standoffs must exceed the allowance and completion limits must
accommodate it. Setup values are checked, not adjusted automatically.
The existing ordered catalogue and all previous runtime releases remain
available. This package is experimental, not manufacturing qualification.

## Finite-tool examples (2026-09-15)

`releases/adaptive-tools-20260915/runtime/release.json` describes the browser
Python runtime, six synthetic drilling/face-milling/mill-turn examples and
the compatible experimental learning checkpoint. The two earlier adaptive
examples retain their exact task, stock and comparison bytes under `retained/`.
The separate `cad/release.json` describes the matching shared Python archive
and WebAssembly modules for supported local STEP preparation, including the
restricted rational-prism profile.

The browser checks asset hashes. These examples are development fixtures;
they do not admit the industrial CAD parts or certify manufacturing safety.
Tool inspection preserves accepted stock and saved actions. Training runs
locally; the browser supports compatible model inference and recording.

## Directional-shadow examples (2026-09-19)

`releases/adaptive-shadow-20260919/runtime/release.json` preserves the previous
eight adaptive examples and adds an upstream-fixture shadow demonstration.
Its shared Python runtime supplies candidate-bound point-shadow inspection
for box/union blockers and principal indexed orientations. The matching
`cad/release.json` carries the same Python archive for local STEP preparation.

Shadow inspection preserves accepted stock and decision recordings. Curved or
compound blockers outside this profile remain explicitly unsupported. The
display does not establish finite-tool clearance. Existing example inputs,
model weights and historical release assets are preserved.

## Analytic curved-shadow examples (2026-09-19)

`releases/adaptive-curved-shadow-20260919/runtime/release.json` preserves all
nine previous adaptive examples and appends a round-fixture shadow example.
The matching `cad/release.json` carries the identical shared Python archive.
Analytic point shadows support boxes, spheres, principal cylinders and their
unions along six signed principal engagement directions with checked frame
transforms. The original case inputs and learning checkpoint remain exact.

Shadow controls preserve accepted stock and recorded actions. A blocked
candidate remains rejected. Display meshes do not establish finite-tool
clearance; annular, oblique and general CAD shadows remain unsupported.
Existing historical releases remain available. These are development examples,
not industrial machining qualification.

## Annular shadow examples (2026-09-19)

`releases/adaptive-annular-shadow-20260919/runtime/release.json` preserves all
ten previous adaptive examples and appends axial and transverse through-bore
fixture demonstrations. The matching CAD release uses the same verified Python
archive. Existing case inputs, raw STEP assets and learning weights are unchanged.

One exact coaxial through bore is supported in a principal-axis cylinder.
Its centre is clear axially and blocked by its upstream wall transversely.
Shadow controls preserve accepted stock and action downloads. These diagnostic
examples remain rejected for machining; finite-tool/holder clearance is separate.
Blind/eccentric holes, oblique axes and general CAD shadows remain outside this
profile. Earlier immutable releases remain available.

## Turning shadow runtime (2026-09-19)

`releases/adaptive-turning-shadow-20260919/runtime/release.json` preserves all
twelve adaptive examples and adds candidate-bound turning shadow inspection to
the full mill-turn case. The CAD release shares the same verified Python archive.
Case inputs, raw STEP assets and learning weights are unchanged. Inspection uses
the accepted stock and does not alter action recordings. This bounded point-shadow
profile does not certify finite-tool access, stationary clearance, general CAD
or full machine kinematics. Earlier immutable releases remain available.

## Stationary turning shadow runtime (2026-09-19)

`releases/adaptive-stationary-turning-shadow-20260919/runtime/release.json` preserves all
twelve adaptive examples and adds candidate-bound stationary turning shadow inspection to
the full mill-turn case. The CAD release shares the same verified Python archive.
Case inputs, raw STEP assets and learning weights are unchanged. Inspection uses
the accepted stock and does not alter action recordings. This bounded point-shadow
profile does not certify finite-tool access, whole-machine clearance, general CAD
or full machine kinematics. Earlier immutable releases remain available.
