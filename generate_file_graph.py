"""
Author: Nanxer
Date: 2025-03-14 20:35:15
Description: This script is used to generate a directory tree structure.
"""

import os
import textwrap


def list_files(directory, ignore=None, prefix="", output_file=None):
    if ignore is None:
        ignore = set()
    try:
        entries = os.listdir(directory)
    except PermissionError:
        if output_file:
            output_file.write(prefix + " [权限拒绝]\n")
        else:
            print(prefix + " [权限拒绝]")
        return
    except FileNotFoundError:
        if output_file:
            output_file.write(prefix + " [目录未找到]\n")
        else:
            print(prefix + " [目录未找到]")
        return

    entries = [entry for entry in entries if entry not in ignore]

    for i, entry in enumerate(entries):
        path = os.path.join(directory, entry)
        if i == len(entries) - 1:
            line = prefix + "└── " + entry
        else:
            line = prefix + "├── " + entry

        if output_file:
            output_file.write(line + "\n")
            print(line)
        else:
            print(line)

        new_prefix = prefix + "│   " if i != len(entries) - 1 else prefix + "    "
        if os.path.isdir(path):
            list_files(path, ignore, new_prefix, output_file)


def main():
    target_directory = "."
    output_filename = "README.txt"

    content="""CTFtasks
This repository mainly stores some personal CTF tasks that I have done or are being researched.

--------------------------------------------------
--------------------------------------------------

Directory tree structure:
"""

    # ignore files or directories
    ignore_files = {'__pycache__','.git'}

    print("Generating directory tree structure...\n\n")
    with open(output_filename, 'w', encoding='utf-8') as output_file:
        output_file.write(content)
        list_files(target_directory, ignore_files, output_file=output_file)
        output_file.close()

    print("\n\nDirectory tree structure generated successfully:", output_filename)


if __name__ == "__main__":
    main()