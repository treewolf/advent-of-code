#!/usr/bin/env python3

from enum import Enum


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


class HandType(Enum):
    HIGH_CARD = 1
    ONE_PAIR = 2
    TWO_PAIR = 3
    THREE_KIND = 4
    FULL_HOUSE = 5
    FOUR_KIND = 6
    FIVE_KIND = 7


class Hand:
    def __init__(self, entry: str):
        self.hand: list
        self.bid: int
        self.hand_type = HandType.HIGH_CARD
        self.parse(entry)
        self.convert()
        self.determineHandType()

    def parse(self, entry: str):
        cards, bid = entry.strip().split(" ")
        self.bid = int(bid)
        self.hand = list(cards)

    def convert(self):
        for i in range(len(self.hand)):
            value = self.hand[i]
            match value:
                case "T":
                    value = "10"
                case "J":
                    value = "11"
                case "Q":
                    value = "12"
                case "K":
                    value = "13"
                case "A":
                    value = "14"
            value = int(value)
            self.hand[i] = value

    def determineHandType(self):
        m = {}
        for i in self.hand:
            m.setdefault(i, 0)
            m[i] += 1

        values = list(m.values())
        values.sort(reverse=True)

        if values[0] == 5:
            self.hand_type = HandType.FIVE_KIND
        elif values[0] == 4:
            self.hand_type = HandType.FOUR_KIND
        elif values[0] == 3 and values[1] == 2:
            self.hand_type = HandType.FULL_HOUSE
        elif values[0] == 3:
            self.hand_type = HandType.THREE_KIND
        elif values[0] == values[1] == 2:
            self.hand_type = HandType.TWO_PAIR
        elif values[0] == 2:
            self.hand_type = HandType.ONE_PAIR
        else:
            self.hand_type = HandType.HIGH_CARD

    def __gt__(self, other) -> bool:
        """Compare hand strength by hand type and cards
        Assume no hand is equal
        """
        if not isinstance(other, Hand):
            raise NotImplementedError

        if self.hand_type.value > other.hand_type.value:
            return True
        elif self.hand_type.value < other.hand_type.value:
            return False

        for i in range(len(self.hand)):
            if self.hand[i] > other.hand[i]:
                return True
            elif self.hand[i] < other.hand[i]:
                return False

        # at this point, hands are equal, unhandled in problem statement
        raise NotImplementedError

    def __repr__(self):
        return f"{self.hand} ${self.bid} {self.hand_type}"


def main():
    myinput = read_input("input.txt")

    hands = []
    for i in myinput:
        h = Hand(i)
        hands.append(h)

    hands = sorted(hands)

    # for i in hands:
    #    print(f"DEBUG {i}")

    total_winnings = 0
    for i in range(len(hands)):
        total_winnings += (i + 1) * hands[i].bid

    print(total_winnings)


if __name__ == "__main__":
    main()
