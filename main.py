import os
import time

def read_names(path):
    with open(path, 'r', encoding='utf-8') as f:
        return {line.strip() for line in f if line.strip()}

def compare(file_a, file_b):
    a = read_names(file_a)
    b = read_names(file_b)
    return sorted(a - b), sorted(b - a)

def print_numbered(title, items):
    print(f"{title} ({len(items)}):")
    if items:
        for i, name in enumerate(items, 1):
            print(f" {i}. {name}")
    else:
        print(" (none)")

def ask_filename(prompt):
    name = input(prompt).strip()
    # Add .txt automatically if missing
    if not name.lower().endswith('.txt'):
        name += '.txt'
    return name

def main():
    print("📄 Package Comparison Tool (By RavelPace)")
    while True:
        f1 = ask_filename("Enter first filename (with or without .txt): ")
        f2 = ask_filename("Enter second filename (with or without .txt): ")

        missing = [f for f in (f1, f2) if not os.path.isfile(f)]
        if missing:
            print("\n⚠️ File not found:", ", ".join(missing))
            print("Retrying in 5 seconds...\n")
            time.sleep(5)
            continue

        only1, only2 = compare(f1, f2)
        print()
        print_numbered(f"Unique to {f1}", only1)
        print()
        print_numbered(f"Unique to {f2}", only2)
        print()
        diffs = sorted(set(only1 + only2))
        print_numbered("All differing package names", diffs)
        print("\nDone! Press Enter to exit…")
        input()
        break

if __name__ == "__main__":
    main()
    
    
# made with <3 by RavelPace    
