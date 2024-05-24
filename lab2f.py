#!/usr/bin/env python3

# Author: sagar K C
# Author ID: 143807220
# Date Created: 2024/05/23

import sys


if len(sys.argv) != 2:
    print(f"Usage: {sys.argv[0]} <number>")
    sys.exit(1)

timer = int(sys.argv[1])


while timer > 0:
    print(timer)
    timer -= 1


print("blast off!")
