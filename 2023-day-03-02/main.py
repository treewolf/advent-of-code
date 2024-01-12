#!/usr/bin/env python3

import math
import re


def read_input(filepath: str) -> list:
    """Read a file for input and return list.
    1 entry per line
    """
    myinput = list()
    with open(filepath, "r") as f:
        lines = f.readlines()
    for i in lines:
        myinput.append(i.strip())
    return myinput


class Star:
    """Hold data for stars that have neighbor Part
    A star is the symbol `*`.
    """

    def __init__(self, position: tuple):
        # position is tuple(linenum, index) with index from input
        self.position = position

    def __repr__(self):
        return f"pos:{self.position}"


class SObj:
    """Hold data for what may or may not be
    a schema part"""

    def __init__(self, numbers: int, line: int, position: tuple):
        self.value = numbers
        self.line = line
        # position is tuple(start, end) index from input
        self.position = position
        self.is_valid_schema = False
        # hold a list of Star objects
        self.stars = list()

    def __repr__(self):
        return f"{self.value} line:{self.line} pos:{self.position}"


def check_adjacent(myobj: SObj, graph: list):
    """Check if object is next to a symbol"""

    # this handles diagonals.
    leftbound = max(0, myobj.position[0] - 1)
    # for adjacent, reduce length by 1
    rightbound = min(myobj.position[1] + 1, len(graph[myobj.line]))

    # obj's line is not first
    if myobj.line > 0:
        i = leftbound
        while i < rightbound:
            # print(f"{myobj} - {rightbound} - {i}")
            if graph[myobj.line - 1][i] == "*":
                myobj.stars.append(Star((myobj.line - 1, i)))
            i += 1

    # check that object is not on leftbound
    if leftbound < myobj.position[0]:
        print(f"leftside {myobj} - {rightbound}")
        if graph[myobj.line][leftbound] == "*":
            myobj.stars.append(Star((myobj.line, leftbound)))

    # check that object rightside is not on rightbound
    print(f"rightbound before: {rightbound}")
    if rightbound - 1 <= myobj.position[1]:
        print(f"rightside {myobj} - {rightbound}")
        if graph[myobj.line][rightbound - 1] == "*":
            print("continue")
            myobj.stars.append(Star((myobj.line, rightbound - 1)))

    # obj's line is not last
    if myobj.line < len(graph) - 1:
        i = leftbound
        while i < rightbound:
            # print(f"{myobj} - {rightbound} - {i}")
            if graph[myobj.line + 1][i] == "*":
                myobj.stars.append(Star((myobj.line + 1, i)))
            i += 1


def main():
    myinput = read_input("input.txt")

    possible_matches = list()

    for linenum in range(len(myinput)):
        # print(f"on line: {linenum}")
        for m in re.finditer(r"[0-9]+", myinput[linenum]):
            # print(f"{m.group(0)} on {m.span()}")
            possible_matches.append(SObj(int(m.group(0)), linenum, m.span(0)))

    print(possible_matches)

    star_pos = dict()

    for i in possible_matches:
        check_adjacent(i, myinput)
        for star in i.stars:
            star_pos.setdefault(star.position, list())
            star_pos[star.position].append(i)

    total = 0
    for i in star_pos:
        print(f"star pos {i}:{star_pos[i]} len:{len(star_pos[i])}")
        if len(star_pos[i]) > 1:
            print("^ greater than 1")
            total += math.prod([oid.value for oid in star_pos[i]])

    print(f"final: {total}")


if __name__ == "__main__":
    main()
