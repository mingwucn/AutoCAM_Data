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

## CAD inspection and original face records (2026-09-20)

`releases/adaptive-cad-inspection-20260920/cad/release.json` updates the
browser CAD worker and shared Python preparation archive. Original face records
are available after STEP import and during the uploaded machining session.
Rational nominal faces support read-only cell queries and display highlights.
The twelve-case catalogue, its runtime, models and raw STEP files are unchanged.
No geometry healing, tolerance increase or industrial qualification is implied.
Earlier immutable releases remain available.

## Completion cache validation (2026-09-20)

`releases/adaptive-completion-cache-20260920/` updates the catalogue and CAD
preparation Python archives. The completion assessors now validate immutable
snapshot and obligation inputs before reusing cached relations. This prevents
invalid mutable snapshots from producing false zero-residual completion reports.
Only three Python modules change in each archive. The twelve ordered examples,
task inputs, model weights, CAD importers and WASM kernels retain their bytes.
Earlier immutable releases remain available for rollback.

## Direct-session transition records (2026-09-20)

`releases/adaptive-browser-transitions-20260920/runtime/` adds accepted-transition
recording for direct task4/task5/task6 browser sessions. Five Python archive
members change; the existing twelve-case catalogue, weights, Pyodide and WASM
assets keep their bytes. CAD preparation keeps its previous release. Records
are separate from ordinary decisions and do not imply manufacturing qualification.
Other session families still use their existing exports.

## Journal transition records (2026-09-20)

`releases/adaptive-journal-transitions-20260920/runtime/` adds selected material
transition recording to combined, regional, objective and indexed browser sessions.
Seven Python archive members change; the twelve existing catalogue cases, weights,
Pyodide and WASM assets retain their bytes. CAD preparation keeps its prior release.
The recording is separate from ordinary decisions; it does not imply model or
manufacturing qualification. Prepared and cylindrical capture remain separate work.

## Prepared tool transition records (2026-09-20)

`releases/adaptive-prepared-transitions-20260920/runtime/` adds material-transition
records for prepared drilling and face milling, including inherited stock history.
Exactly two Python archive members change; the twelve catalogue examples, models,
Pyodide, WASM and separate CAD release retain their existing bytes. Records
supplement ordinary decisions. Full/mixed/cylindrical capture remains separate
work; these records do not confer model or manufacturing qualification.

## Mill-turn transition records (2026-09-21)

`releases/adaptive-mill-turn-transitions-20260921/runtime/` adds material
records for compound, full initial-stock and mixed-learning sessions. Accepted
turning history continues through transfer, indexing, tool exchange, face milling
and drilling. Records supplement ordinary decisions and preserve rejected actions
without publishing material. Exactly seven Python archive members change; the
twelve catalogue examples, inputs, models, Pyodide, WASM and separate CAD release
retain their bytes. These recording changes do not qualify a model or a
manufacturing process.

## Cylindrical material records (2026-09-21)

`releases/adaptive-cylindrical-transitions-20260921/runtime/` adds material records for supported cylindrical
choice sessions and policy wrappers. Records retain inherited turning, tool
exchange and indexed milling history, with accepted material separate from
ordinary rejected decisions. Eight Python archive members change; the twelve
catalogue cases and existing geometry, models, Pyodide, WASM and CAD assets
retain their bytes. Full-size correctness was checked separately; operations
on that case take minutes and are not interactive. This release grants no
model admission, industrial support or manufacturing qualification.
