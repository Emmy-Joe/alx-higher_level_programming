#!/usr/bin/python3

"""print the alphabet letters in lower case, and not followed by a new line"""

for alphabet in range(97, 123):
    print("{}".format(chr(alphabet), end=""))
