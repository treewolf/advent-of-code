#!/usr/bin/env python3

with open("input.txt", "r") as f:
    lines = f.readlines()

# number of safe reports
total = 0

myiter = iter(lines)
for report in myiter:
    is_increase = False
    is_decrease = False
    in_range = False

    levels = report.split()
    for i in range(len(levels[:-1])):
        diff = int(levels[i]) - int(levels[i + 1])

        # unsafe
        if diff == 0:
            in_range = False
            break

        if diff > 0:
            is_decrease = True
        else:
            is_increase = True

        if abs(diff) >= 1 and abs(diff) <= 3:
            in_range = True
        else:
            in_range = False
            break

    if (is_increase ^ is_decrease) and in_range:
        total += 1

print(f"total: {total}")
