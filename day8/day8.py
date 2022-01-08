import numpy as np
from numpy.core.fromnumeric import std

def init(debug=False):
    if debug:
        filename = "day8/test_input.txt"
    else:
        filename = "day8/input.txt"
    with open(filename) as file:
        lines = file.readlines()
        data = [[x.split(" ") for x in line.strip().split(" | ")] for line in lines]
    
    return data

def evaluate_input(value):
    if len(value) == 2:
        return 0
    elif len(value) == 4:
        return 1
    elif len(value) == 3:
        return 2
    elif len(value) == 7:
        return 3
    else:
        return 4

def evaluate_instruction(instruction):
    numbers_dict = {}
    for i,val in enumerate(instruction):
        if len(val) == 2:
            numbers_dict[1] = val
        elif len(val) == 4:
            numbers_dict[4] = val
        elif len(val) == 3:
            numbers_dict[7] = val
        elif len(val) == 7:
            numbers_dict[8] = val
    pass

def create_segment_matrix(signal_arr):
    signal_matrix = np.zeros((10,10),dtype=int)
    
    for i,pattern in enumerate(signal_arr[0]):
        for char in pattern:
            num_val = ord(char)-97
            signal_matrix[num_val,i] = 1
    for i in range(10):
        if sum(signal_matrix[:,i]) == 2:
            signal_matrix[7,i] = 1
        elif sum(signal_matrix[:,i]) == 4:
            signal_matrix[8,i] = 1
        elif sum(signal_matrix[:,i]) == 7:
            signal_matrix[9,i] = 1
    #print(signal_matrix)
    #print(np.linalg.matrix_rank(signal_matrix))
    return signal_matrix.T
    
def part1(data):
    counter = [0]*5
    for instruction in data:
        for value in instruction[1]:
            counter[evaluate_input(value)] += 1
    print(sum(counter[:-1]))

def part2(data):
    output_sum = 0
    std_arr = np.array([[1, 0, 1, 1, 0, 1, 1, 1, 1, 1], 
                        [1, 0, 0, 0, 1, 1, 1, 0, 1, 1], 
                        [1, 1, 1, 1, 1, 0, 0, 1, 1, 1], 
                        [0, 0, 1, 1, 1, 1, 1, 0, 1, 1], 
                        [1, 0, 1, 0, 0, 0, 1, 0, 1, 0], 
                        [1, 1, 0, 1, 1, 1, 1, 1, 1, 1], 
                        [1, 0, 1, 1, 0, 1, 1, 0, 1, 1],
                        [0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 1, 0]])
    std_arr = std_arr.T
    std_inv = np.linalg.inv(std_arr)

    print(f"Standard matrix: \n {std_arr}")

    signal_matrix = create_segment_matrix(data[0])
    print(signal_matrix)

    b = np.arange(1,11).reshape(-1,1)
    print(signal_matrix@std_inv@b)

data = init(True)

#part1(data)
part2(data)