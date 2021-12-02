#!/usr/bin/env python

planned_course = open("input.txt").read().splitlines()

def plot_course(course):
    horizontal_position = 0
    depth = 0

    for shift in course:
        direction = shift.split()[0]
        distance = int(shift.split()[1])

        if direction == 'up':
            depth -= distance
        if direction == 'down':
            depth += distance
        if direction == 'forward':
            horizontal_position += distance

    return(horizontal_position * depth)

        
if __name__ == "__main__":
    print(plot_course(planned_course))
