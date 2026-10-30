#!/usr/bin/env python3
"""Read-only environment recon for a sandboxed workspace (stdlib only, Python 3.9+).

Usage: python3 scripts/recon.py [workspace_dir]
Prints tool versions, write permission, disk, timezone pitfalls, port binding.
Never installs anything, never writes outside a temp file it deletes.
"""
import datetime
import os
import platform
import shutil
import socket
import subprocess
import sys
import tempfile


def run(cmd):
    """Return first line of `cmd --version`-style output, or a reason it failed."""
    exe = shutil.which(cmd[0])
    if not exe:
        return "NOT FOUND"
    try:
        out = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                             timeout=10, universal_newlines=True)
        line = (out.stdout or "").strip().splitlines()
        return line[0] if line else "(no output, exit %d)" % out.returncode
    except Exception as exc:  # timeout, permission, etc.
        return "ERROR: %s" % exc


def check_write(path):
    try:
        fd, name = tempfile.mkstemp(dir=path, prefix=".recon_")
        os.close(fd)
        os.remove(name)
        return "OK"
    except Exception as exc:
        return "NO (%s)" % exc


def check_port(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind(("0.0.0.0", port))
        return "free"
    except OSError as exc:
        return "busy (%s)" % exc.strerror
    finally:
        s.close()


def tz_pitfalls():
    """Show how this Python parses common timestamp shapes (3.9 fromisoformat rejects 'Z')."""
    samples = ["2024-01-15T09:30:00Z", "2024-01-15T09:30:00+09:00",
               "2024-01-15T09:30:00+0900", "2024-01-15 09:30:00"]
    rows = []
    for s in samples:
        try:
            d = datetime.datetime.fromisoformat(s)
            rows.append("  fromisoformat(%r) -> %s (tz=%s)" % (s, d.isoformat(), d.tzinfo))
        except ValueError:
            rows.append("  fromisoformat(%r) -> ValueError  (use s.replace('Z', '+00:00') or strptime %%z)" % s)
    return rows


def main():
    ws = os.path.abspath(sys.argv[1] if len(sys.argv) > 1 else ".")
    print("== recon (read-only) ==")
    print("workspace     :", ws)
    print("os            :", platform.platform())
    print("python        :", sys.version.split()[0], "(" + sys.executable + ")")
    for name, cmd in [("node", ["node", "--version"]), ("npm", ["npm", "--version"]),
                      ("pip", [sys.executable, "-m", "pip", "--version"]),
                      ("git", ["git", "--version"]), ("codex", ["codex", "--version"]),
                      ("curl", ["curl", "--version"])]:
        print("%-14s:" % name, run(cmd))
    print("write access  :", check_write(ws) if os.path.isdir(ws) else "dir missing")
    try:
        du = shutil.disk_usage(ws if os.path.isdir(ws) else ".")
        print("disk free     : %.1f GB / %.1f GB" % (du.free / 1e9, du.total / 1e9))
    except OSError as exc:
        print("disk free     : ERROR", exc)
    now = datetime.datetime.now().astimezone()
    print("local time    :", now.isoformat(), "| TZ env =", os.environ.get("TZ", "(unset)"))
    print("timestamp parsing on this python:")
    for row in tz_pitfalls():
        print(row)
    print("ports on 0.0.0.0:", ", ".join("%d %s" % (p, check_port(p)) for p in (3000, 5000, 8000, 8080)))
    print("workspace top-level:")
    if os.path.isdir(ws):
        names = sorted(os.listdir(ws))
        for n in names[:40]:
            print("  " + n + ("/" if os.path.isdir(os.path.join(ws, n)) else ""))
        if len(names) > 40:
            print("  ... (%d more)" % (len(names) - 40))
        if not names:
            print("  (empty)")
    print("note: bind servers to 0.0.0.0 for the built-in Browser preview.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
