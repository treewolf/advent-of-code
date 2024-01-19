#!/usr/bin/env python3
import concurrent.futures
import re
import sys


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


class Gmap:
    """
    where in map with { a b c }
    a = dest
    b = source
    c = length of the range

    so if map is seed-to-soil, then seed is the b and soil is the a
    this is opposite logic of how the map is named
    """

    def __init__(self, data: tuple):
        self.sourcename = ""
        self.destname = ""
        self.source_bound = list()
        self.dest_start = list()
        self.parse(data)

    def parse(self, data: tuple):
        """
        data is given as tuple from re package
        structured as (dest, src, numbers).

        numbers are an adjoined list of integers by newline
        """
        self.sourcename = data[0]
        self.destname = data[1]

        ranges = data[2].strip().split("\n")
        for i in ranges:
            dest, src, length = i.split()
            src = int(src)
            length = int(length)
            # minus 1 because inclusive start
            self.source_bound.append((src, src + length - 1))
            self.dest_start.append(int(dest))

    def destination(self, source: int) -> int:
        """Return the destination integer from source"""
        transformed_dest = source

        for i, bound in enumerate(self.source_bound):
            if bound[0] <= transformed_dest <= bound[1]:
                pos = transformed_dest - bound[0]
                transformed_dest = self.dest_start[i] + pos
                break
        return transformed_dest

    def __repr__(self):
        return (
            f"Map from {self.sourcename} to {self.destname}. start src"
            f" {self.source_bound[0]}:[{len(self.source_bound)}] dst"
            f" {self.dest_start[0]}:[{len(self.dest_start)}]"
        )


def location_set(rstart: int, rend: int, sequence: list) -> int:
    """
    Return smallest location from a single seed range
    """
    location = sys.maxsize  # hacky
    while rstart <= rend:
        floc = rstart
        for seq in sequence:
            floc = seq.destination(floc)
        location = min(floc, location)
        rstart += 1
    return location


def main():
    myinput = read_input("input.txt")

    # seeds is first declared
    m = re.match(r"^seeds: (.+)$", myinput[0])
    seed_input = m.group(1).strip().split()

    # parse input
    map_pattern = r"^([a-z]+)\-to\-([a-z]+) map:\n([\n[0-9 ]+)$"
    input_str = "\n".join(myinput).strip()
    m = re.findall(map_pattern, input_str, re.MULTILINE)

    sequence = list()
    for i in m:
        gmap = Gmap(i)
        print(gmap)
        sequence.append(gmap)

    # go through transform chain
    location = sys.maxsize  # hacky
    with concurrent.futures.ProcessPoolExecutor() as executor:
        for i in range(int(len(seed_input) / 2)):
            start = i * 2
            end = i * 2 + 1
            rstart = int(seed_input[start])
            rend = int(seed_input[end]) + rstart - 1

            print(f"seed range: {rstart} to +{rend}")
            future = executor.submit(location_set, rstart, rend, sequence)

            location = min(location, future.result())

    print(location)


if __name__ == "__main__":
    main()
