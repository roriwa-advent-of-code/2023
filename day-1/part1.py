# -*- coding=utf-8 -*-
r"""

"""
import io

example = io.StringIO("""1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet""")

numbers = []

for line in open("input.txt"):
    first: str | None = None
    second: str | None = None
    for i in range(0, len(line), 1):
        char = line[i]
        if char.isdigit():
            first = char
            break
    for i in range(len(line)-1, 0-1, -1):
        char = line[i]
        if char.isdigit():
            second = char
            break
    if first is None or second is None:
        raise LookupError("didn't find any digit")
    number = first + second
    numbers.append(number)
    print(f"{line[:-1]:<20} | {number}")


print(f"Sum: {sum(map(int, numbers))}")
