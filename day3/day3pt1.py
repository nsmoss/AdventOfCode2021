#!/usr/bin/env python

diagnostic_report = open("input.txt").read().splitlines()

def power_consumption(report):
    
    line_length = len(report[0])
    bit_counter_one, bit_counter_zero = ([0 for i in range(line_length)] for i in range(2))

    for line in report:
        for i in range(line_length):
            if line[i] == "1":
                bit_counter_one[i] += 1
            if line[i] == "0":
                bit_counter_zero[i] += 1
    
    g_rate, e_rate = gam_eps_calc(bit_counter_one, bit_counter_zero, line_length)

    return(g_rate * e_rate)

def gam_eps_calc(counter_one, counter_zero, line_length):
    gamma_counter = []
    epsilon_counter = []

    for i in range(line_length):
        if int(counter_one[i]) > int(counter_zero[i]):
            gamma_counter.append("1")
            epsilon_counter.append("0")
        if int(counter_one[i]) < int(counter_zero[i]):
            gamma_counter.append("0")
            epsilon_counter.append("1")
    
    gamma_rate = int("".join(gamma_counter), 2)
    epsilon_rate = int("".join(epsilon_counter), 2)
    
    return (gamma_rate, epsilon_rate)

if __name__ == "__main__":
    print(power_consumption(diagnostic_report))
