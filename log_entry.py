#!/usr/bin/env python3
"""log_entry.py — CLI helper to append entries to log.csv"""
from pathlib import Path

LOG = Path(__file__).with_name("log.csv")
QUIT_WORDS = {"quit", "exit", "q"}


def ask(prompt, default=""):
    val = input(f"  {prompt}" + (f" [{default}]" if default else "") + ": ").strip()
    if val.lower() in QUIT_WORDS:
        raise KeyboardInterrupt
    return val or default


def main():
    print(f"Log entry helper -> {LOG.name}. Type 'quit' to exit.\n")

    with LOG.open("a", encoding="utf-8") as f:
        f.write(";;;;;;;;\n")

    while True:
        try:
            sentence = ask("Sentence (description)")
            role     = ask("Role (a=assertion, c=command, q=query)", "c")
            typ      = ask("Type (stat, activity, loc, mode, rel, dyn)", "stat")
            entity1  = ask("Entity 1")
            entity2  = ask("Entity 2", "")
            relation = ask("Relation / quark", "")
            value1   = ask("Value 1", "50")
            value2   = ask("Value 2", "60")

            row = f"{sentence};{role};{typ};{entity1};{entity2};{relation};{value1};{value2};"
            sep = ask("Add separator line? (y/n)", "y")
            lines = [row] + ([";;;;;;;;"] if sep.lower() == "y" else [])

            print("\n  Preview:")
            for l in lines:
                print(f"    {l}")

            confirm = ask("Append to log.csv? (y/n)", "y")
            if confirm.lower() == "y":
                with LOG.open("a", encoding="utf-8") as f:
                    f.write("\n".join(lines) + "\n")
                print(f"  Saved to {LOG.name}.\n")
            else:
                print("  Skipped.\n")

            again = ask("Add another entry? (y/n)", "y")
            if again.lower() != "y":
                break

        except KeyboardInterrupt:
            print()
            break


if __name__ == "__main__":
    main()
