import numpy as np


with open("day2/input.txt") as file:
    lines = file.read().splitlines()
    data = [[line.split(" ")[0],int(line.split(" ")[1])] for line in lines]

def part1():
    pos = [0,0]
    for instruction in data:
        if instruction[0]=="forward":
            pos[0] += instruction[1]
        elif instruction[0]=="down":
            pos[1] += instruction[1]
        elif instruction[0]=="up":
            pos[1] -= instruction[1]
    print(f"Horizontal: {pos[0]}, depth: {pos[1]}")
    print(f"Product{pos[0]*pos[1]}")

part1()

def part2():
    pos = [0,0]
    aim = 0
    for instruction in data:
        if instruction[0]=="forward":
            pos[0] += instruction[1]
            pos[1] += aim*instruction[1]
        elif instruction[0]=="down":
            aim += instruction[1]
        elif instruction[0]=="up":
            aim -= instruction[1]
    print(f"Horizontal: {pos[0]}, depth: {pos[1]}")
    print(f"Product{pos[0]*pos[1]}")

part2()