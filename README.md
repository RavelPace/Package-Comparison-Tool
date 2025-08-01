# 📦 Package Comparison Tool

A lightweight command-line utility to compare two `.txt` files containing package names, showing all differences in a clear, numbered format.  
**Useful for comparing packages you may need to uninstall or reinstall.**

---

## 🔍 Features

- Reads package names from two `.txt` files (automatically appends `.txt` if omitted).
- Displays packages **unique to each file**, and the **combined list of all differing names**, all with counts and numbering.
- Interactive input: prompts for filenames at runtime.
- Handles missing files gracefully: displays an error message, waits 5 seconds, then restarts the process.
- Stops at the end with a final prompt so the console doesn’t close immediately.

---

## 🛠️ Requirements

- Python 3.x (no external dependencies)

---

## 🚀 Installation & Setup

1. Save the script below as `compare_packages.py`.
2. Make sure your two package files (e.g. `packages1.txt`, `packages2.txt`) exist in the same directory—or specify full paths.

---

## ▶️ Usage

Run the script:

```bash
python main.py
