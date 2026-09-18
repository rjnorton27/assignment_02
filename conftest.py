"""Make the project package importable without shadowing stdlib modules."""

import os
import sys

root = os.path.abspath(os.path.dirname(__file__))
project_code_dir = os.path.join(root, "code")

for path in list(sys.path):
    if path in ("", ".") or os.path.abspath(path) == root:
        sys.path.remove(path)

if os.path.isdir(project_code_dir) and project_code_dir not in sys.path:
    sys.path.insert(0, project_code_dir)
