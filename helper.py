#!/usr/bin/env python

from sys import argv
from pathlib import Path

DOT_DIR = Path(__file__).parent
HOME = Path.home()


def get_module_targets(module):
    try:
        targets = __import__(module).TARGETS
    except ModuleNotFoundError:
        print(f"Unable to import module {module}")
        return []
    except AttributeError:
        print(f"Unable to read TARGETS from module {module}")
        return []
    print(f"{module} targets: {targets}")
    return targets


def prompt_override(link):
    override = input(f"File found at {link}, override? [y/N] ")
    if override and override[0].lower() == "y":
        link.unlink()
        return True
    return False


def make_link(link, target):
    link.parent.mkdir(parents=True, exist_ok=True)
    if not link.exists() or prompt_override(link):
        print(f"Linking {link} -> {target}")
        link.symlink_to(target)


def link_modules(modules):
    for module in modules:
        targets = get_module_targets(module)
        for link, target in targets:
            link = HOME / link
            target = DOT_DIR / module / target
            make_link(link, target)


def unlink_modules(modules):
    for module in modules:
        targets = get_module_targets(module)
        for link, _ in targets:
            link = HOME / link
            if not link.exists():
                print(f"{link} does not exist, skipping")
            elif not link.is_symlink():
                print(f"{link} is not a symlink, skipping")
            else:
                print(f"Unlinking {link}")
                link.unlink()


def print_usage():
    print("Usage:")
    print(f"\t{argv[0]} link [modules]")
    print(f"\t{argv[0]} unlink [modules]")


if len(argv) < 2 or (command := argv[1]) not in ["link", "unlink"]:
    print("Unknown command")
    print_usage()
    exit(1)

modules = argv[2:]
if len(modules) == 0:
    print("No modules provided")
    print_usage()
    exit(1)

# Removing ourself from the module list makes ./helper.py link * valid for convenience.
script_name = Path(__file__).name
if script_name in modules:
    modules.remove(script_name)

print("Linking modules: ", modules)

if command == "link":
    link_modules(modules)
elif command == "unlink":
    unlink_modules(modules)
