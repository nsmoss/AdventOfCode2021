#!/usr/bin/env python

planned_course = open("input.txt").read().splitlines()

def plot_course(course):
    horizontal_position = 0
    depth = 0
    aim = 0

    for shift in course:
        direction = shift.split()[0]
        adjustment = int(shift.split()[1])

        if direction == 'up':
            aim -= adjustment
        if direction == 'down':
            aim += adjustment
        if direction == 'forward':
            horizontal_position += adjustment
            depth += aim * adjustment

    return(horizontal_position * depth)

        
if __name__ == "__main__":
    print(plot_course(planned_course))
