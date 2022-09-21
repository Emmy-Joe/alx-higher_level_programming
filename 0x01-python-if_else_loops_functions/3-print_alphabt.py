#!/usr/bin/python3

"""Print the alphabet in lowercase, not followed by a new line."""
for l in range(97, 123):
    if l != 101 and l != 113:
        print("{}".format(chr(l)), end="")
