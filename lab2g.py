#!/usr/bin/env python3

# Author: sk-c13
# Author ID: sk-c13
# Date Created: 2024/05/23

import sys


timer = 3


if len(sys.argv) > 1:
    try:
        timer = int(sys.argv[1])
    except ValueError:
        print("Invalid input. Please enter an integer value.")
        sys.exit(1)


while timer > 0:
    print(timer)
    timer -= 1

print("blast off!")
