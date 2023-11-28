#!/usr/bin/python3
import random
number = random.randint(-10, 10)
if number > 0:
    print(f"is positive {number:d}")
elif number < 0:
    print(f"is negative {number:d}")
else:
    print(f"is zero {number:d}")
