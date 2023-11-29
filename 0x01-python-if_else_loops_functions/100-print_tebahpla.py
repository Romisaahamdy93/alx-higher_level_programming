#!/usr/bin/python3
for i in range(25, -1, -1):
    c = i + ord('A')
    if i % 2 == 0:
        print("{:c}".format(c), end="")
    else:
        print("{:c}".format(c - 32), end="")
