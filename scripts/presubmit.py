#!/usr/bin/env python3
"""Pre-submit gate (stdlib only, Python 3.9+). Read-only.

Usage: python3 .agents/scripts/presubmit.py [workspace_dir]
Exit 0 = all checks passed, 1 = at least one check failed,
2 = nothing was checked (zero checks is never a pass).
"""
import os
import re
import subprocess
import sys

REQUIRED_DOCS = ["TASK.md", "AGREEMENT.md", "DECISIONS.md", "VERIFICATION.md",
                 "WORKLOG.md", "HANDOFF.md", "DESIGN.md"]
PLACEHOLDER = re.compile(r"\{\{[^}\n]*\}\}")
SECRET_PATTERNS = [
    ("aws access key", re.compile(r"AKIA[0-9A-Z]{16}")),
    ("openai-style key", re.compile(r"\bsk-[A-Za-z0-9_-]{20,}")),
    ("github token", re.compile(r"\b(ghp|gho|ghs|ghu)_[A-Za-z0-9]{30,}|github_pat_[A-Za-z0-9_]{30,}")),
    ("slack token", re.compile(r"\bxox[abprs]-[A-Za-z0-9-]{10,}")),
    ("private key", re.compile(r"-----BEGIN [A-Z ]*PRIVATE KEY-----")),
    ("hardcoded secret", re.compile(r"(?i)(api[_-]?key|secret|password|token)\s*[:=]\s*['\"][^'\"\s]{16,}['\"]")),
]
SKIP_DIRS = {".git", "node_modules", ".venv", "venv", "__pycache__", "dist", "build", ".next", "templates"}
TEXT_EXT = {".py", ".js", ".ts", ".tsx", ".jsx", ".json", ".md", ".txt", ".yml", ".yaml",
            ".toml", ".env", ".cfg", ".ini", ".html", ".css", ".sh", ".csv", ".sql"}


class Gate:
    def __init__(self):
        self.ran = 0
        self.failed = 0

    def result(self, name, ok, detail=""):
        self.ran += 1
        if not ok:
            self.failed += 1
        print("[%s] %s%s" % ("PASS" if ok else "FAIL", name, (" - " + detail) if detail else ""))


def git(ws, *args):
    try:
        out = subprocess.run(["git", "-C", ws] + list(args), stdout=subprocess.PIPE,
                             stderr=subprocess.PIPE, universal_newlines=True, timeout=20)
        return out.returncode, out.stdout
    except (OSError, subprocess.TimeoutExpired):
        return 127, ""


def read(path):
    try:
        with open(path, encoding="utf-8", errors="replace") as fh:
            return fh.read()
    except OSError:
        return ""


def iter_text_files(ws):
    for root, dirs, files in os.walk(ws):
        dirs[:] = [d for d in dirs if d not in SKIP_DIRS]
        for f in files:
            p = os.path.join(root, f)
            if os.path.splitext(f)[1].lower() in TEXT_EXT or f.startswith(".env"):
                try:
                    if os.path.getsize(p) <= 1000000:
                        yield p
                except OSError:
                    pass


def main():
    ws = os.path.abspath(sys.argv[1] if len(sys.argv) > 1 else ".")
    g = Gate()
    docs = os.path.join(ws, "docs")

    if os.path.isdir(docs):
        missing = [d for d in REQUIRED_DOCS if not os.path.isfile(os.path.join(docs, d))]
        g.result("required docs in docs/", not missing, "missing: " + ", ".join(missing) if missing else "")

        hits = []
        for d in REQUIRED_DOCS:
            for i, line in enumerate(read(os.path.join(docs, d)).splitlines(), 1):
                if PLACEHOLDER.search(line):
                    hits.append("docs/%s:%d" % (d, i))
        g.result("no template placeholders {{...}} left", not hits,
                 ", ".join(hits[:8]) + (" ..." if len(hits) > 8 else ""))

        dec = read(os.path.join(docs, "DECISIONS.md"))
        n_dec = len([l for l in dec.splitlines() if re.match(r"^###\s+D\d+", l) and not PLACEHOLDER.search(l)])
        g.result("DECISIONS.md has >=1 decision (### D1 ...)", n_dec > 0, "%d found" % n_dec)

        ver = read(os.path.join(docs, "VERIFICATION.md"))
        rows = [l for l in ver.splitlines() if re.match(r"^\|\s*C\d+", l) and not PLACEHOLDER.search(l)]
        judged = [l for l in rows if re.search(r"\b(PASS|FAIL)\b", l)]
        g.result("VERIFICATION.md has >=1 criterion judged PASS/FAIL", len(judged) > 0,
                 "%d judged / %d rows" % (len(judged), len(rows)))

        handoff = read(os.path.join(docs, "HANDOFF.md"))
        g.result("HANDOFF.md has 'Current level:' and '## Review Q&A'",
                 "Current level:" in handoff and "## Review Q&A" in handoff)

    code, _ = git(ws, "rev-parse", "--is-inside-work-tree")
    if code == 0:
        _, status = git(ws, "status", "--porcelain")
        dirty = [l for l in status.splitlines() if l.strip()]
        g.result("no uncommitted changes", not dirty,
                 "%d paths, e.g. %s" % (len(dirty), dirty[0].strip()) if dirty else "")
        _, log = git(ws, "log", "--oneline", "-n", "50")
        n = len([l for l in log.splitlines() if l.strip()])
        g.result("has commits", n > 0, "%d recent commits" % n)

    files = list(iter_text_files(ws))
    if files:
        leaks = []
        for p in files:
            if p.endswith(os.path.join("scripts", "presubmit.py")):
                continue
            for i, line in enumerate(read(p).splitlines(), 1):
                for label, pat in SECRET_PATTERNS:
                    if pat.search(line):
                        leaks.append("%s:%d (%s)" % (os.path.relpath(p, ws), i, label))
        g.result("no secret-like strings in %d text files" % len(files), not leaks,
                 ", ".join(leaks[:5]))

    print("-- %d checks, %d failed" % (g.ran, g.failed))
    if g.ran == 0:
        print("NOTHING CHECKED -> exit 2 (zero checks is not a pass). Run from the workspace root.")
        return 2
    return 1 if g.failed else 0


if __name__ == "__main__":
    sys.exit(main())
