"""Verify the committed release bytes using only the Python standard library."""
import hashlib
import json
from pathlib import Path

root = Path(__file__).resolve().parent
manifest = json.loads((root / 'MANIFEST.json').read_bytes())
for row in manifest['files']:
    path = (root / row['path']).resolve()
    if not path.is_relative_to(root):
        raise ValueError('Invalid manifest path')
    data = path.read_bytes()
    if len(data) != row['size_bytes'] or hashlib.sha256(data).hexdigest() != row['sha256']:
        raise ValueError('Identity mismatch: ' + row['path'])
print(f"Verified {len(manifest['files'])} files")
