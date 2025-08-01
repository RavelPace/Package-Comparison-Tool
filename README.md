# 📦 Package Comparison Tool

A lightweight interactive CLI utility to compare two `.txt` files containing package names, and output clear, numbered differences.  
**Perfect for identifying apps you may want to uninstall or reinstall between Android device states.**

---

## 🔍 Features

- 📝 Accepts two filenames interactively (with or without `.txt` extension).
- 📋 Displays:
  - Packages **unique** to the first file
  - Packages **unique** to the second file
  - All **differing** package names combined (numbered).
- 🚫 Detects and warns if a file is missing.
- ⏱️ Waits 5 seconds before retrying after any error.
- ✅ Exits only after user presses **Enter**—no auto-closing.

---

## 🧰 Requirements

- Python 3.x  
(No external libraries required — pure Python.)

---

## ⚙️ Installation & Setup

1. Clone or save the script.
2. Create two package list files (`.txt`) with package names — one per line.

Example:

```text
# packages_A.txt
com.android.chrome
com.example.app1
````

```text
# packages_B.txt
com.example.app1
com.example.app2
```

---

## ▶️ Usage

Run the script:

```bash
python main.py
```

Then follow these steps:

1. Input the **first filename** (e.g. `packages_A` or `packages_A.txt`)

2. Input the **second filename**

3. The tool compares and displays:

   * Packages only in file A
   * Packages only in file B
   * All differing packages

4. Press **Enter** to exit once done.

---

## 🧪 Output Example

```
📄 Package Comparison Tool

Enter first filename (with or without .txt): packages_A
Enter second filename (with or without .txt): packages_B

Unique to packages_A.txt (1):
 1. com.android.chrome

Unique to packages_B.txt (1):
 1. com.example.app2

All differing package names (2):
 1. com.android.chrome
 2. com.example.app2

Done! Press Enter to exit…
```

---

## 🛟 Safety & Use Cases

* ✅ Helpful when diffing packages before **uninstalling system apps**.
* 📊 Good for comparing system state after Android updates or reset.
* 🧼 Use with uninstall scripts to confirm changes safely.

---

## 🧾 Summary

This tool simplifies the comparison of Android package lists and is ideal for:

* Verifying system app removals
* Preparing clean uninstall/reinstall batches
* Spotting differences between backups or ROMs

---

**Made with ❤️ by RavelPace**
