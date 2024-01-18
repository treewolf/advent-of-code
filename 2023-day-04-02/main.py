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
        # ensure card is handled at least once
        self.repeat = 1
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

    # make the card first
    cards = list()
    for i in range(len(myinput)):
        cards.append(Card(myinput[i]))

    total = 0

    # perform comparison logic on card hands
    for i in range(len(cards)):
        matches = set(cards[i].win).intersection(set(cards[i].hand))
        print(f"matches for card {i}: {matches}")

        while cards[i].repeat > 0:

            # iterate from current card to increase repeat of subsequent cards
            for j in range(len(matches)):
                cards[i + j + 1].repeat += 1

            cards[i].repeat -= 1
            total += 1

    print(f"total: {total}")


if __name__ == "__main__":
    main()
