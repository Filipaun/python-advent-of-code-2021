def init(debug=False):
    if debug:
        filename = "day6/test_input.txt"
    else:
        filename = "day6/input.txt"
    with open(filename) as file:
        fish_data = [int(x) for x in file.readline().strip().split(",")]
    
    #fish_dict = {0:0,1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0}
    fish_list = [0]*9

    for fish in fish_data:
        fish_list[fish] += 1
    return fish_list

def fishy(days = 18):
    debug = False
    fish_list = init(debug)
    print(f"day 0: {fish_list}")
    for day in range(0,days):
        for i in range(9):
            if i == 0:
                old_0 = fish_list[i]
                fish_list[i] = fish_list[i+1]
                continue
            elif i == 6:
                fish_list[i] = old_0 + fish_list[i+1]
            elif i == 8:
                fish_list[i] = old_0
            else:
                fish_list[i] = fish_list[i+1]
        print(f"day {day+1}: {fish_list}")
    print(f"After {days} days, n_fish: {sum(fish_list)}")

fishy(80)
fishy(256)




