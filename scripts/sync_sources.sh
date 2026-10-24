#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")/.."
export GIT_TERMINAL_PROMPT=0
git rev-parse --is-inside-work-tree >/dev/null
mkdir -p upstream index
manifest_file="$(mktemp)"
trap 'rm -f "$manifest_file"' EXIT
python3 - <<'PY' > "$manifest_file"
import json
with open("sources.json", encoding="utf-8") as handle:
    sources = json.load(handle)["repositories"]
for src in sources:
    assert all("\t" not in src[k] and "\n" not in src[k] for k in ("id","repo","branch"))
    print(src["id"] + "\t" + src["repo"] + "\t" + src["branch"])
PY
while IFS=$'\t' read -r slug source_repo branch; do
    path="upstream/$slug"
    url="https://github.com/$source_repo.git"
    echo "[upstream] $source_repo -> $path"
    if ! git config -f .gitmodules --get "submodule.$path.url" >/dev/null 2>&1; then
        if [[ -e "$path" ]]; then
            echo "ERROR: unregistered path already exists: $path" >&2
            exit 2
        fi
        git -c protocol.version=2 submodule add --depth 1 -b "$branch" "$url" "$path"
    fi
done < "$manifest_file"
git submodule sync --recursive
git -c protocol.version=2 submodule update --init --remote --depth 1 --jobs 3
python3 scripts/build_index.py
python3 scripts/validate.py
git add .gitmodules upstream index
if ! git diff --cached --quiet; then
    git commit -m "chore: synchronize upstream references and refresh indexes [skip ci]"
else
    echo "No upstream changes."
fi
