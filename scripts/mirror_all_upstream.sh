#!/usr/bin/env bash
# Import complete pinned source trees as real, non-submodule Git files.
set -euo pipefail
cd "$(dirname "$0")/.."
selection="all"
if [[ "$#" -eq 2 && "$1" == "--source" ]]; then
  selection="$2"
elif [[ "$#" -ne 0 ]]; then
  echo "Usage: bash scripts/mirror_all_upstream.sh [--source all|SOURCE_ID]" >&2
  exit 2
fi
command -v python3 >/dev/null
command -v rsync >/dev/null
command -v git >/dev/null
git rev-parse --is-inside-work-tree >/dev/null
git config user.name 'github-actions[bot]'
git config user.email '41898282+github-actions[bot]@users.noreply.github.com'
export GIT_TERMINAL_PROMPT=0

manifest="$(mktemp)"
trap 'rm -f "$manifest"' EXIT
python3 - "$selection" > "$manifest" <<'PY'
import json, sys
from pathlib import Path
sources = json.loads(Path("sources.json").read_text(encoding="utf-8"))["repositories"]
selection = sys.argv[1]
allowed = {x["id"] for x in sources}
if selection != "all" and selection not in allowed:
    sys.exit("Unknown source: " + selection)
for x in sources:
    if selection != "all" and selection != x["id"]:
        continue
    for key in ("id", "repo", "branch", "initial_commit"):
        assert "\t" not in x[key] and "\n" not in x[key]
    assert len(x["initial_commit"]) == 40
    print("\t".join(x[key] for key in ("id", "repo", "branch", "initial_commit")))
PY
if [[ ! -s "$manifest" ]]; then
  echo "Empty mirror manifest" >&2
  exit 2
fi
while IFS=$'\t' read -r id repo branch pin; do
  printf '\n== Mirroring %s at %s ==\n' "$repo" "$pin"
  tmp="$(mktemp -d)"
  trap 'rm -rf "$tmp"; rm -f "$manifest"' EXIT
  git -c protocol.version=2 clone --filter=blob:none --no-checkout \
    --single-branch --branch "$branch" --depth 1 \
    "https://github.com/$repo.git" "$tmp/project"
  git -C "$tmp/project" fetch --no-tags --depth 1 origin "$pin"
  git -C "$tmp/project" checkout --force --detach "$pin"
  git -C "$tmp/project" submodule update --init --recursive --depth 1
  actual="$(git -C "$tmp/project" rev-parse HEAD)"
  test "$actual" = "$pin" || { echo "Pinned revision mismatch: $id" >&2; exit 1; }
  dest="mirror/$id"
  mkdir -p "$dest"
  rsync -a --delete --exclude='.git' "$tmp/project/" "$dest/"
  git add -f -A -- "$dest"
  python3 scripts/verify_pinned_mirror.py --source-id "$id" --upstream-dir "$tmp/project"
  if ! git diff --cached --quiet; then
    git commit -m "mirror: import $id at $pin [skip ci]"
    git push origin HEAD:main
  else
    echo "No changes for $id"
  fi
  echo "Done: $id, real Git files saved at $dest"
  rm -rf "$tmp"
  trap 'rm -f "$manifest"' EXIT
done < "$manifest"
echo "Selected sources mirrored."
