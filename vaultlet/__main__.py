import sys
from .core import (
    run_with_secrets,
    set_secret,
    list_secrets,
    unset_secret,
    VAULTLET_VERSION
)

def print_usage():
    print(f"Vaultlet v{VAULTLET_VERSION}")
    print("\nUsage:")
    print("  vaultlet <app> <command> [args...]       Run a command with injected secrets")
    print('  vaultlet --set <app> "<key>" "<value>"   Set a secret')
    print("  vaultlet --list <app>                    List stored keys for an app")
    print('  vaultlet --unset <app> "<key>"           Remove a stored key')
    print("  vaultlet --version                       Show Vaultlet version")
    print("  vaultlet --help                          Show this help message")

def main():
    args = sys.argv[1:]

    if not args or args[0] == "--help":
        print_usage()
        sys.exit(0)

    if args[0] == "--version":
        print(f"Vaultlet version {VAULTLET_VERSION}")
        sys.exit(0)

    if args[0] == "--set":
        if len(args) != 4:
            print("Usage: vaultlet --set <app> \"<key>\" \"<value>\"")
            sys.exit(1)
        set_secret(args[1], args[2], args[3])

    elif args[0] == "--list":
        if len(args) != 2:
            print("Usage: vaultlet --list <app>")
            sys.exit(1)
        list_secrets(args[1])

    elif args[0] == "--unset":
        if len(args) != 3:
            print("Usage: vaultlet --unset <app> \"<key>\"")
            sys.exit(1)
        unset_secret(args[1], args[2])

    else:
        if len(args) < 2:
            print_usage()
            sys.exit(1)
        app_name = args[0]
        command = args[1:]
        run_with_secrets(app_name, command)

if __name__ == "__main__":
    main()
