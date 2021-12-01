#!/usr/bin/env python3

f = open("input.txt", "r")
depths = list(map(int,[line.rstrip() for line in f]))

i = 0
windows = []

while(len(depths[i:i+3]) == 3):
    window = sum(depths[i:i+3])
    windows.append(window)
    i += 1

increased_depth = 0
prev_depth = windows[0]

for depth in windows:
    if depth > prev_depth:
        increased_depth += 1
    prev_depth = depth

print(increased_depth)

