"""
Author: Nanxer
Date: 2025-03-14 20:35:15
Description: This script generates a random flag of given length.
"""

import random
import string


def generate_random_flag(length):
    letters = string.ascii_letters + string.digits
    return ''.join(random.choice(letters) for i in range(length))


def mian():
    key = int(input("Enter the length of the flag: "))
    random_flag = 'flag{'+ generate_random_flag(key) + '}'
    print(f"Random flag: {random_flag}")


if __name__ == '__main__':
    mian()