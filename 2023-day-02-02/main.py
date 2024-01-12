#!/usr/bin/env python3


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


class Pick:
    def __init__(self):
        self.attempts = list()

    def parse(self, entry: str):
        tries = entry.split(";")
        for i in tries:
            i = i.strip()
            mapping = dict()
            for c in i.split(","):
                c = c.strip()
                colorsep = c.split()
                mapping[colorsep[1]] = int(colorsep[0])
            self.attempts.append(mapping)


class Game:
    def __init__(self):
        self.id = 0
        self.pulls = list()
        self.valid = True

    def parse(self, entry: str):
        gametag, gameresult = entry.split(":")
        self.id = int(gametag.split()[1])
        print(f"id str is {self.id}")

        p = Pick()
        p.parse(gameresult)
        self.pulls.append(p)


def multiply(nums: list) -> int:
    """Return product from list of integers"""
    total = 1
    for i in nums:
        total *= i
    return total


def main():
    myinput = read_input("input.txt")

    total = 0
    for game in myinput:
        g = Game()
        g.parse(game)

        print(f"game id: {g.id}")
        pull_count = dict()
        for i in g.pulls:
            attempt_count = dict()
            for selection in i.attempts:
                for color in selection:
                    if color not in attempt_count:
                        attempt_count[color] = selection[color]
                    else:
                        attempt_count[color] = max(
                            attempt_count[color], selection[color]
                        )
            for color in attempt_count:
                if color not in pull_count:
                    pull_count[color] = attempt_count[color]
                else:
                    pull_count[color] = max(attempt_count[color], pull_count[color])

        total += multiply(pull_count.values())

    print(f"sum of good game ids: {total}")


if __name__ == "__main__":
    main()
