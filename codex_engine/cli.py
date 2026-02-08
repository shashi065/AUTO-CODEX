import sys

from codex_engine.generate import run as generate_run
from codex_engine.init import run as init_run
from codex_engine.improve import run as improve_run


def main():
    print("🔥 CLI MODULE LOADED")
    print("🔥 sys.argv =", sys.argv)

    if len(sys.argv) < 2:
        print("❌ No command provided")
        print("Usage: autocodex [init|generate|improve]")
        sys.exit(1)

    command = sys.argv[1]

    if command == "generate":
        generate_run()

    elif command == "init":
        init_run()

    elif command == "improve":
        improve_run()

    else:
        print(f"❌ Unknown command: {command}")
        print("Available commands: init, generate, improve")
        sys.exit(1)
