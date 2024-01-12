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


class Card:
    def __init__(self, value: str):
        self.id = None
        self.win = None
        self.hand = None
        self.parse(value)

    def parse(self, value: str):
        pattern = r"Card\s+(\d+): ([\d ]+) \| ([\d ]+)$"
        m = re.match(pattern, value)
        if not m:
            print(f"bad regex, empty: {value}")
            exit(1)

        self.id = m.group(1)
        self.win = m.group(2).strip().split()
        self.hand = m.group(3).strip().split()

    def __repr__(self):
        return f"Card {self.id} win:{self.win} hand:{self.hand}"


def main():
    myinput = read_input("input.txt")

    total = 0

    for i in myinput:
        c = Card(i)
        matches = set(c.win).intersection(set(c.hand))
        print(matches)
        if matches:
            total += pow(2, len(matches) - 1)

    print(f"total: {total}")


if __name__ == "__main__":
    main()
