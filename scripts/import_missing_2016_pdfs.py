#!/usr/bin/env python3
"""Import exactly four missing 2016 PDFs from a pinned upstream Git commit.

Requires git, network access to GitHub, and a local checkout of this repository.
The downloaded bytes are checked against expected Git blob IDs before staging.
This program does not make a Git commit or push automatically.
"""
import hashlib
import json
import subprocess
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PIN = "08179f1fc0a3300787155d92800ac82b57ee4118"
SOURCE = "https://github.com/deekur/gaokaomath.git"
FILES = {
    "普通高考/2016/2016天津文.pdf": "de8a81c7e41013835fd732f3b69a9957628b327e",
    "普通高考/2016/2016山东理.pdf": "83d9a18fbca14aa5d1d03f2cbda49dfc881cbabe",
    "普通高考/2016/2016浙江文.pdf": "bff4bc4f22c8531faee72bc007c8f228983cf69f",
    "普通高考/2016/2016浙江理.pdf": "a5d27c9ea092897aa485080613dcd4c34db328ed",
}

def git(*args, cwd=None):
    return subprocess.check_output(["git", *args], cwd=cwd)

def blob_sha(data):
    return hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest()

def main():
    if not (ROOT / ".git").exists():
        raise SystemExit("Run in a real Git checkout, not a ZIP download.")
    with tempfile.TemporaryDirectory() as temp:
        upstream = Path(temp) / "upstream"
        subprocess.run(["git", "init", "-q", str(upstream)], check=True)
        subprocess.run(["git", "-C", str(upstream), "remote", "add", "origin", SOURCE], check=True)
        subprocess.run(["git", "-C", str(upstream), "fetch", "--depth", "1", "origin", PIN], check=True)
        actual_pin = git("-C", str(upstream), "rev-parse", "FETCH_HEAD").decode().strip()
        if actual_pin != PIN:
            raise RuntimeError("Pinned revision mismatch")
        staged = []
        for relative, expected in FILES.items():
            data = git("-C", str(upstream), "show", "FETCH_HEAD:" + relative)
            if not data.startswith(b"%PDF-"):
                raise RuntimeError("Not a PDF: " + relative)
            if blob_sha(data) != expected:
                raise RuntimeError("Git Blob SHA mismatch: " + relative)
            destination = ROOT / "mirror" / "gaokaomath" / relative
            if destination.exists() and blob_sha(destination.read_bytes()) != expected:
                raise RuntimeError("Existing file differs: " + relative)
            destination.parent.mkdir(parents=True, exist_ok=True)
            destination.write_bytes(data)
            staged.append(destination.relative_to(ROOT).as_posix())
            print("VERIFIED:", relative, len(data), expected)
        subprocess.run(["git", "add", "--", *staged], cwd=ROOT, check=True)
        for relative, expected in FILES.items():
            path = "mirror/gaokaomath/" + relative
            staged_sha = git("rev-parse", ":" + path, cwd=ROOT).decode().strip()
            if staged_sha != expected:
                raise RuntimeError("Git index SHA mismatch: " + path)
        print(json.dumps({"verified_and_staged": len(staged), "pinned": PIN}, ensure_ascii=False))
        print("Review the changes, then commit and push manually.")

if __name__ == "__main__":
    main()
