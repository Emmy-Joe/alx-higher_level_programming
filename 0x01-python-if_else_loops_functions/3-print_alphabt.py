#!/usr/bin/python3

"""Print the alphabet in lowercase, not followed by a new line."""
for letter in range(97, 123):
    if chr(letter) not 101 and chr(letter) not 113:
        print("{}".format(chr(letter)), end="")
