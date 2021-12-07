#!/usr/bin/env python

f = open("input.txt").read().split(',')
crab_pos = list(map(int,[line for line in f]))

def horiz_pos(crabs):
    lowest_fuel = 0
    best_hpos = 0
    for i in range(min(crabs), max(crabs)):
        fueluse = 0
        for crab in crabs:
            fueluse += sum(range(abs(crab - i) + 1))
        if lowest_fuel == 0:
            lowest_fuel = fueluse
            best_hpos = i
        elif fueluse < lowest_fuel:
            lowest_fuel = fueluse
            best_hpos = i
    return(lowest_fuel)
       
if __name__ == "__main__":
    print(horiz_pos(crab_pos))
