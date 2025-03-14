import os
import textwrap


def list_files(directory, ignore=None, prefix=""):
    if ignore is None:
        ignore = set()
    try:
        entries = os.listdir(directory)
    except PermissionError:
        print(prefix + " [权限拒绝]")
        return
    except FileNotFoundError:
        print(prefix + " [目录未找到]")
        return

    entries = [entry for entry in entries if entry not in ignore]

    for i, entry in enumerate(entries):
        path = os.path.join(directory, entry)
        if i == len(entries) - 1:
            print(prefix + "└──", entry)
            new_prefix = prefix + "    "
        else:
            print(prefix + "├──", entry)
            new_prefix = prefix + "│   "

        if os.path.isdir(path):
            list_files(path, ignore, new_prefix)


if __name__ == "__main__":
    target_directory = "."
    ignore_files = {'.git', 'README.md', 'make_file_graph.py'}
    print("目录树结构:")
    list_files(target_directory, ignore_files)
