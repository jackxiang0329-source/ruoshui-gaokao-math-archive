#!/usr/bin/env bash
# One entrypoint for all pinned Git tree imports; keeps binary blobs intact.
set -euo pipefail
cd "$(dirname "$0")/.."
if [[ "$#" -eq 0 ]]; then
  exec python3 scripts/import_pinned_git_trees.py --push
elif [[ "$#" -eq 2 && "$1" == "--source" ]]; then
  exec python3 scripts/import_pinned_git_trees.py --source "$2" --push
else
  echo "Usage: bash scripts/mirror_all_upstream.sh [--source all|SOURCE_ID]" >&2
  exit 2
fi
