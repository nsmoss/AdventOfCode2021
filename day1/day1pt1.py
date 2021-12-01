#!/usr/bin/env python3

f = open("input.txt", "r")
depths = [line.rstrip() for line in f]

increased_depth = 0
prev_depth = depths[0]

for depth in depths:
    if int(depth) > int(prev_depth):
        print(depth + " increased from " +  prev_depth)
        increased_depth += 1
    prev_depth = depth

print(increased_depth)

