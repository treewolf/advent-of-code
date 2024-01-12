#!/usr/bin/env python3
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


class SObj:
    """Hold data for what may or may not be
    a schema part"""

    def __init__(self, numbers: int, line: int, position: tuple):
        self.value = numbers
        self.line = line
        # position is tuple(start, end) index from input
        self.position = position
        self.is_valid_schema = False

    def __repr__(self):
        return f"{self.value} line:{self.line} pos:{self.position}"


def check_adjacent(myobj: SObj, graph: list):
    """Check if object is next to a symbol"""

    # this handles diagonals.
    # for adjacent, reduce length by 1
    leftbound = max(0, myobj.position[0] - 1)
    rightbound = myobj.position[1] + 1

    neighbors = set()
    symbols = set("# % & * + - / = @ $".split())

    # obj's line is not first
    if myobj.line > 0:
        pie = graph[myobj.line - 1][leftbound:rightbound]
        neighbors = neighbors.union(set(list(pie)))

    # check right and left of object. -1 right and +1 left bounds for adjacent
    leftsym = list(graph[myobj.line][leftbound : leftbound + 1])
    neighbors = neighbors.union(set(leftsym))
    rightsym = list(graph[myobj.line][rightbound - 1 : rightbound])
    neighbors = neighbors.union(set(rightsym))

    # obj's line is not last
    if myobj.line < len(graph) - 1:
        pie = graph[myobj.line + 1][leftbound:rightbound]
        neighbors = neighbors.union(set(list(pie)))

    if neighbors.intersection(symbols):
        print(f"{myobj} has good neighbors {neighbors.intersection(symbols)}")
        myobj.is_valid_schema = True
    else:
        print(f"{myobj} has no neighbors {neighbors}")


def main():
    myinput = read_input("input.txt")

    possible_matches = list()

    for linenum in range(len(myinput)):
        # print(f"on line: {linenum}")
        for m in re.finditer(r"[0-9]+", myinput[linenum]):
            # print(f"{m.group(0)} on {m.span()}")
            possible_matches.append(SObj(int(m.group(0)), linenum, m.span(0)))

    print(possible_matches)

    for i in possible_matches:
        check_adjacent(i, myinput)

    total = 0
    for i in possible_matches:
        if i.is_valid_schema:
            total += i.value

    print(f"final: {total}")


if __name__ == "__main__":
    main()
