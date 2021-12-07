#!/usr/bin/env python

f = open("input.txt").read().split(',')
fish_list = list(map(int,[line for line in f]))

def day_calc(fishes):
    for num in range(len(fishes)):
        if fishes[num] == 0:
            fishes[num] = 6
            fishes.append(8)
        else:
            fishes[num] -= 1

def lantern_count(fish_list, days):
    fishes = fish_list
    for day in range(days):
        day_calc(fishes)
        print(str(day) + ": " + str(len(fishes)))
    return(len(fishes))
        
if __name__ == "__main__":
    print(lantern_count(fish_list, 256))
