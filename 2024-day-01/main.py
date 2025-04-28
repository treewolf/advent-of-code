#!/usr/bin/env python

left, right = [], []
with open("input.txt", "r") as f:
    lines = f.readlines()
    for i in lines:
        x, y = i.split()
        left.append(int(x))
        right.append(int(y))

left.sort()
right.sort()

total = 0
for x, y in zip(left, right):
    total += abs(x - y)

print(f"total: {total}")
