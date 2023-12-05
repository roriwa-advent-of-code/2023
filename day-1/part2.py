# -*- coding=utf-8 -*-
r"""

"""
import io
import re

example = io.StringIO(r"""two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen""")

NUMMAP = dict(
    one="1",
    two="2",
    three="3",
    four="4",
    five="5",
    six="6",
    seven="7",
    eight="8",
    nine="9",
)

pattern = re.compile(fr'(?=({"|".join(NUMMAP)}|[0-9]))')

numbers = []

# for line in example:
for line in open("./input.txt"):
    matches = pattern.findall(line)
    print([line, matches])
    first = matches[0]
    second = matches[-1]
    number = NUMMAP.get(first, first) + NUMMAP.get(second, second)
    numbers.append(number)
    print(f"{line[:-1]:<20} | {number}")

print(f"Sum: {sum(map(int, numbers))}")
