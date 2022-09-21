#!/usr/bin/python3

"""Print the alphabet in lowercase, not followed by a new line."""
for letter in range(97, 123):
    if chr(letter) != 101 and chr(letter) != 113:
        print("{}".format(chr(letter)), end="")
