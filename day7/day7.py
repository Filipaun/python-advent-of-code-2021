def init(debug=False):
    if debug:
        filename = "day7/test_input.txt"
    else:
        filename = "day7/input.txt"
    with open(filename) as file:
        data = [int(x) for x in file.readline().strip().split(",")]
    
    return data

def fuel_consumption(data,point):
    fuel_used = 0
    for data_point in data:
        fuel_used += abs(data_point-point)
    return fuel_used

def fuel_consumption2(data,point):
    fuel_used = 0
    for data_point in data:
        dist = abs(data_point-point)
        fuel_used += dist*(dist+1)/2
    return fuel_used

def part1(debug = False):
    data = init(debug)
    sorted_data = sorted(data)
    len_data = len(data)

    print(f"{sorted_data[len_data//2]},{fuel_consumption(data,sorted_data[len_data//2])}")



    biggest = sorted_data[-1]
    smallest = sorted_data[0]

    fuel_used = fuel_consumption(data,smallest)
    this_i = smallest
    for i in range(smallest+1,biggest+1):
        new_fuel = fuel_consumption(data,i)
        if new_fuel < fuel_used:
            fuel_used = new_fuel
            this_i = i
    print(this_i,fuel_used)

def part2(debug = False):
    data = init(debug)
    sorted_data = sorted(data)
    len_data = len(data)

    print(f"{sorted_data[len_data//2]},{fuel_consumption2(data,sorted_data[len_data//2])}")



    biggest = sorted_data[-1]
    smallest = sorted_data[0]

    fuel_used = fuel_consumption2(data,smallest)
    this_i = smallest
    for i in range(smallest+1,biggest+1):
        new_fuel = fuel_consumption2(data,i)
        if new_fuel < fuel_used:
            fuel_used = new_fuel
            this_i = i
    print(f"average: {sum(data)/len_data}")
    print(this_i,fuel_used)

part1(False)
print("---------------")
part2(False)