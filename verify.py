"""Verify committed legacy data and runtime releases with Python's standard library."""
import hashlib
import json
from pathlib import Path

root = Path(__file__).resolve().parent

def checked(base, row):
    path = (base / row['path']).resolve()
    if not path.is_relative_to(base) or path == base:
        raise ValueError('Invalid manifest path')
    raw = path.read_bytes()
    if len(raw) != row['size_bytes'] or hashlib.sha256(raw).hexdigest() != row['sha256']:
        raise ValueError('Identity mismatch: ' + row['path'])
    return path, raw


manifest = json.loads((root / 'MANIFEST.json').read_bytes())
for row in manifest['files']:
    checked(root, row)
registry = json.loads((root / 'RUNTIME_RELEASES.json').read_bytes())
if set(registry) != {'schema', 'releases'} or registry['schema'] != 'autocam-runtime-releases-1':
    raise ValueError('Invalid runtime registry')
seen_indices = set()
members = 0
for ref in registry['releases']:
    index, raw = checked(root, ref)
    if index in seen_indices:
        raise ValueError('Repeated runtime index')
    seen_indices.add(index)
    release = json.loads(raw)
    if set(release) != {'schema', 'files'} or release['schema'] != 'autocam-ui-assets-1':
        raise ValueError('Invalid runtime release')
    seen = set()
    for row in release['files']:
        path, _ = checked(index.parent, row)
        if path in seen:
            raise ValueError('Repeated runtime member')
        seen.add(path)
    actual = {p.resolve() for p in index.parent.rglob('*') if p.is_file() and p != index}
    if seen != actual:
        raise ValueError('Unindexed or absent runtime asset')
    members += len(seen)
print(f"Verified {len(manifest['files'])} legacy files, {len(seen_indices)} runtime indices and {members} runtime files")
