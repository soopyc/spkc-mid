import sys

import colorama

colorama.init(autoreset=True)


def ask(q) -> str:
    return input(f'?{q}\n> {colorama.Fore.GREEN}')


def main() -> int:
    name: str = ask("Your character name...")

    print(f"hello, {name}")
    if not ask("Are you ready to start your adventure? [y/n]").lower().startswith("y"):
        print("come back later, we will be waiting.")
        return 0
    print("Good. Let's see what the magic ball's got for you.")
    print("Story\n===============================================")

    return 0


if __name__ == "__main__":
    sys.exit(main())
