import sys
import os

# Allow running from /experiments while importing recurrentmodel.py from project root
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from recurrentmodel import boot_v5, iris_tick


def quick_sanity():
    print("=== experiments: quick sanity ===")
    v = boot_v5()

    for _ in range(10):
        v, sym = iris_tick(v, None)
        print(sym or "·")

    v, sym = iris_tick(v, "URGENT HELP NOW!!!")
    print(sym or "·")


def main():
    name = sys.argv[1] if len(sys.argv) > 1 else "quick"

    if name == "quick":
        quick_sanity()
        return

    raise SystemExit(f"unknown experiment: {name}")


if __name__ == "__main__":
    main()
