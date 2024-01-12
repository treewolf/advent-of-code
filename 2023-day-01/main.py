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


def extract_digit(entry: str) -> list:
    """Extract all digits and return ordered list"""
    digits = list()
    for i in entry:
        try:
            num = int(i)
            digits.append(num)
        except Exception:
            continue
    return digits


def main():
    total = 0

    myinput = read_input("input.txt")
    for line in myinput:
        print(line)

        digits = extract_digit(line)
        first = digits[0]
        last = digits[-1]

        print(first, last)

        total += first * 10 + last
        print(total)

    print(total)


if __name__ == "__main__":
    main()
