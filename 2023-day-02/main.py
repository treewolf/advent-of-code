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


def main():
    myinput = read_input("input.txt")

    LIMIT = {"red": 12, "green": 13, "blue": 14}

    total = 0

    for game in myinput:
        g = Game()
        g.parse(game)

        print(f"game id: {g.id}")
        for i in g.pulls:

            for selection in i.attempts:
                for color in selection:
                    if selection[color] > LIMIT[color]:
                        print(f"BAD: hand {selection[color]} > limit {LIMIT[color]}")
                        g.valid = False
        if g.valid:
            total += g.id

    print(f"sum of good game ids: {total}")


if __name__ == "__main__":
    main()
