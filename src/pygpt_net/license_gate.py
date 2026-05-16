from __future__ import annotations

import json
import os
import sys
from datetime import datetime, timezone
from hashlib import sha256
from pathlib import Path


APP_NAME = "PyHuey"
GATE_VERSION = 1


def _project_root() -> Path:
    return Path(__file__).resolve().parents[2]


def _config_dir() -> Path:
    base = os.environ.get("XDG_CONFIG_HOME")
    if base:
        return Path(base) / "pyhuey"
    return Path.home() / ".config" / "pyhuey"


def _acceptance_path() -> Path:
    return _config_dir() / "license_acceptance.json"


def _read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace")


def _sha256_text(text: str) -> str:
    return sha256(text.encode("utf-8")).hexdigest()


def _license_files() -> dict[str, Path]:
    root = _project_root()
    return {
        "upstream_mit": root / "licenses" / "LICENSE.UPSTREAM-PYGPT-MIT.txt",
        "pyhuey_gpl_3_0": root / "licenses" / "LICENSE.PYHUEY-GPL-3.0.txt",
    }


def _load_license_payloads() -> dict[str, dict[str, str]]:
    files = _license_files()
    payloads: dict[str, dict[str, str]] = {}

    for key, path in files.items():
        if not path.exists():
            raise FileNotFoundError(f"Required license file not found: {path}")

        text = _read_text(path)
        payloads[key] = {
            "path": str(path),
            "text": text,
            "sha256": _sha256_text(text),
        }

    return payloads


def _already_accepted(payloads: dict[str, dict[str, str]]) -> bool:
    path = _acceptance_path()
    if not path.exists():
        return False

    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except Exception:
        return False

    if data.get("gate_version") != GATE_VERSION:
        return False

    for key, payload in payloads.items():
        item = data.get(key, {})
        if not item.get("accepted"):
            return False
        if item.get("sha256") != payload["sha256"]:
            return False

    return True


def _write_acceptance(payloads: dict[str, dict[str, str]]) -> None:
    path = _acceptance_path()
    path.parent.mkdir(parents=True, exist_ok=True)

    data = {
        "app": APP_NAME,
        "gate_version": GATE_VERSION,
        "accepted_at_utc": datetime.now(timezone.utc).isoformat(timespec="seconds"),
    }

    for key, payload in payloads.items():
        data[key] = {
            "accepted": True,
            "sha256": payload["sha256"],
            "path": payload["path"],
        }

    path.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def _prompt_cli(title: str, text: str) -> bool:
    print("")
    print("=" * 72)
    print(title)
    print("=" * 72)
    print(text)
    print("=" * 72)
    answer = input(f"Do you accept {title}? [y/N] ").strip().lower()
    return answer in {"y", "yes"}


def _prompt_tk(title: str, text: str) -> bool:
    try:
        import tkinter as tk
        from tkinter import messagebox, scrolledtext
    except Exception:
        return _prompt_cli(title, text)

    accepted = {"value": False}

    root = tk.Tk()
    root.title(title)
    root.minsize(900, 650)

    bg = "#000000"
    fg = "#00ff00"
    accent = "#2d2b57"

    root.configure(bg=bg)

    header = tk.Label(
        root,
        text=title,
        bg=bg,
        fg=fg,
        font=("TkDefaultFont", 14, "bold"),
    )
    header.pack(anchor="w", padx=12, pady=(12, 6))

    body = scrolledtext.ScrolledText(
        root,
        wrap=tk.WORD,
        bg=bg,
        fg=fg,
        insertbackground=fg,
        highlightbackground=accent,
        highlightcolor=accent,
        highlightthickness=1,
    )
    body.insert("1.0", text)
    body.configure(state=tk.DISABLED)
    body.pack(fill=tk.BOTH, expand=True, padx=12, pady=8)

    agree_var = tk.BooleanVar(value=False)
    agree = tk.Checkbutton(
        root,
        text=f"I have read and agree to {title}.",
        variable=agree_var,
        bg=bg,
        fg=fg,
        selectcolor=accent,
        activebackground=bg,
        activeforeground=fg,
    )
    agree.pack(anchor="w", padx=12, pady=(4, 8))

    button_frame = tk.Frame(root, bg=bg)
    button_frame.pack(fill="x", padx=12, pady=(0, 12))

    def on_accept() -> None:
        if not agree_var.get():
            messagebox.showwarning("License required", "You must check the agreement box to continue.")
            return
        accepted["value"] = True
        root.destroy()

    def on_decline() -> None:
        accepted["value"] = False
        root.destroy()

    tk.Button(
        button_frame,
        text="Accept",
        command=on_accept,
        bg=accent,
        fg=fg,
        activebackground=accent,
        activeforeground=fg,
    ).pack(side=tk.LEFT, padx=(0, 8))

    tk.Button(
        button_frame,
        text="Decline",
        command=on_decline,
        bg=accent,
        fg=fg,
        activebackground=accent,
        activeforeground=fg,
    ).pack(side=tk.LEFT)

    root.mainloop()
    return bool(accepted["value"])


def ensure_license_acceptance() -> None:
    payloads = _load_license_payloads()

    if _already_accepted(payloads):
        return

    if os.environ.get("PYHUEY_ACCEPT_LICENSES") == "1":
        _write_acceptance(payloads)
        return

    steps = [
        (
            "Original upstream PyGPT MIT license",
            payloads["upstream_mit"]["text"],
        ),
        (
            "PyHuey GPL-3.0 license",
            payloads["pyhuey_gpl_3_0"]["text"],
        ),
    ]

    for title, text in steps:
        if not _prompt_tk(title, text):
            print(f"{APP_NAME}: license not accepted. Exiting.")
            sys.exit(1)

    _write_acceptance(payloads)
