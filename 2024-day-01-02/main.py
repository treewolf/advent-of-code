#!/usr/bin/env python3

left, right = [], {}
with open("input.txt", "r") as f:
    lines = f.readlines()
    for i in lines:
        x, y = i.split()
        left.append(int(x))
        y = int(y)
        right.setdefault(y, 0)
        right[y] += 1

total = 0
myiter = iter(left)
for i in myiter:
    if i in right:
        total += i * right[i]

print(f"total: {total}")
