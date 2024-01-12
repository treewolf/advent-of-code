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


def extract_digit(entry: str) -> list:
    """Extract all digits and return ordered list"""
    word_num = {
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
        "1": 1,
        "2": 2,
        "3": 3,
        "4": 4,
        "5": 5,
        "6": 6,
        "7": 7,
        "8": 8,
        "9": 9,
    }
    digits = list()

    # use look forward pattern because oneight should equal 18 even if
    # they share the "e"
    pattern = "(?=(" + "|".join(word_num.keys()) + "))"
    print(pattern)

    for m in re.findall(pattern, entry):
        digits.append(word_num[m])
    print(f"done: {digits}")

    return digits


def main():
    total = 0

    myinput = read_input("input.txt")
    for line in myinput:
        print(line)

        digits = extract_digit(line)
        first = digits[0]
        last = digits[-1]

        print(f"real number: {first}{last}")

        total += first * 10 + last
        print(total)

    print(f"final: {total}")


if __name__ == "__main__":
    main()
