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

def part1(data):
    counter = [0]*5
    for instruction in data:
        for value in instruction[1]:
            counter[evaluate_input(value)] += 1
    print(sum(counter[:-1]))

def part2(data):
    output_sum = 0
    for instructions in data:
        instructions[0] = [sorted([ord(char)-96 for char in signal]) for signal in instructions[0]]
        instructions[1] = [sorted([ord(char)-96 for char in signal]) for signal in instructions[1]]
        #print(instructions)
        evaluate_instruction(instructions)
    
    

data = init(False)

part1(data)
part2(data)