"""
Author: Nanxer
Date: 2025-03-14 20:52:15
Description: This script generates a new task directory with the given name.
"""
import os
import generate_random_flag as grf


def generate_new_task(task_name):
    # generate a new directory with the given name
    os.mkdir(task_name)
    print(f"New task directory {task_name} created.")

    # create a README.md file in the new directory to describe and analyze the task
    with open(os.path.join(task_name, "README.md"), "w") as f:
        f.write(f'## {task_name}\n\n### description:\n\n### analysis:\n\n### exp:\n\n### attach:\n\n')
        f.close()
    print(f"README.md file created in {task_name}.")

    # create a secret.py file in the new directory to store the flag
    with open(os.path.join(task_name, "secret.py"), "w") as f:
        f.write(f'flag = "{grf.generate_random_flag(30)}"')
        f.close()
    print(f'secret.py file created in {task_name}.')

    # create a task.py file in the new directory to write the code
    with open(os.path.join(task_name, "task.py"), "w") as f:
        f.write('''#!/usr/bin/env python3\n# -*- coding: utf-8 -*-\n''')
        f.close()
    print(f"task.py file created in {task_name}.")


def main():
    task_name = input("Enter the name of the task: ")
    generate_new_task(task_name)
    print(f"New task {task_name} created.")


if __name__ == "__main__":
    main()