
import collections


def initialize(debug=False):
    if debug is True:
        filename = "day5/test_input.txt"
    else:
        filename = "day5/input.txt"

    horizontal = {}
    vertical = {}
    diagonal_neg = {}
    diagonal_pos = {}

    with open(filename) as file:
        line = file.readline()
        while line:
            line_data = [[int(x) for x in point.split(",")] for point in line.strip().split(" -> ")]
            valid, direction,slope = check_direction(line_data)
            if valid and direction == "h":
                if line_data[0][1] in horizontal:
                    horizontal[line_data[0][1]].append(sorted([line_data[0][0],line_data[1][0]]))
                else:
                    horizontal[line_data[0][1]] = [sorted([line_data[0][0],line_data[1][0]])]
            elif valid and direction == "v":
                if line_data[0][0] in vertical:
                    vertical[line_data[0][0]].append(sorted([line_data[0][1],line_data[1][1]]))
                else:
                    vertical[line_data[0][0]] = [sorted([line_data[0][1],line_data[1][1]])]
            elif valid and direction == "x":
                if slope == 1:
                    norm = offset_manhattan(line_data[0])
                    if norm in diagonal_pos:
                        diagonal_pos[norm].append(sorted([line_data[0][0],line_data[1][0]]))
                    else:
                        diagonal_pos[norm] = [sorted([line_data[0][0],line_data[1][0]])]
                if slope == -1:
                    norm = manhattan(line_data[0])
                    if norm in diagonal_neg:
                        diagonal_neg[norm].append(sorted([line_data[0][0],line_data[1][0]]))
                    else:
                        diagonal_neg[norm] = [sorted([line_data[0][0],line_data[1][0]])]
            line = file.readline()
    return horizontal, vertical,diagonal_pos,diagonal_neg

def manhattan(vector):
    # negative slope: line is up to the right
    return vector[0] + vector[1]


def offset_manhattan(vector):
    # positve slope: line is down to the right
    return vector[0]-vector[1]
    
def check_direction(points):
    if points[0][0] == points[1][0]:
        return True,"v",0
    elif points[0][1] == points[1][1]:
        return True,"h",0
    elif abs(points[0][0]-points[1][0]) == abs(points[0][1]-points[1][1]):
        return True,'x',((points[0][0]-points[1][0])/(points[0][1]-points[1][1]))
    else:
        return False,"0",0

def straight_colinear_collisions(directional_lines,type = 0):
    collisions = []
    # vertical directional_lines
    for i,(key,sublist) in enumerate(directional_lines.items()):
        for i in range(len(sublist)):
            for j in range(i+1,len(sublist)):
                for val in range(max(sublist[i][0], sublist[j][0]), min(sublist[i][1], sublist[j][1])+1):
                    if type == 0:
                        collisions.append([key,val])
                    elif type == 1:
                        collisions.append([val,key])
    return collisions

def straight_non_colinear_collisions(vertical_lines,horizontal_lines):
    collisions = []
    for i,(key_v,sublist_v) in enumerate(vertical_lines.items()):
        for j,(key_h,sublist_h) in enumerate(horizontal_lines.items()):
            for i_sub_h in range(len(sublist_h)):
                if (sublist_h[i_sub_h][0] <= key_v and sublist_h[i_sub_h][1] >= key_v):
                    for i_sub_v in range(len(sublist_v)):
                        if(sublist_v[i_sub_v][0] <= key_h and sublist_v[i_sub_v][1] >= key_h):
                            collisions.append([key_v,key_h])
    return collisions

def diagonal_colinear_collisions(directional_lines,type):
    collisions = []
    # vertical directional_lines
    for i,(key,sublist) in enumerate(directional_lines.items()):
        for i in range(len(sublist)):
            for j in range(i+1,len(sublist)):
                for val in range(max(sublist[i][0], sublist[j][0]), min(sublist[i][1], sublist[j][1])+1):
                    if type == 0:
                        collisions.append([val,key-val])
                    elif type == 1:
                        collisions.append([key+val,-key+val])
    return collisions

def diagonal_non_colinear_collisions(diagonal_pos,diagonal_neg):
    collisions = []
    for i,(key_pos,sublist_pos) in enumerate(diagonal_pos.items()):
        for j,(key_neg,sublist_neg) in enumerate(diagonal_neg.items()):
            for i_sub_neg in range(len(sublist_neg)):
                    for i_sub_pos in range(len(sublist_pos)):
                        cross_x = (key_pos + key_neg)/2
                        if((sublist_pos[i_sub_pos][0] <= cross_x and sublist_pos[i_sub_pos][1] >= cross_x) 
                            and (sublist_neg[i_sub_neg][0] <= cross_x and sublist_neg[i_sub_neg][1] >= cross_x)):
                            collisions.append([cross_x,key_neg-cross_x])
    return collisions

def diag_straight_collisions(diagonal_pos,diagonal_neg,vertical,horizontal):
    collsions = []

    for i,(key_pos,sublist_pos) in enumerate(diagonal_pos.items()):
        for j,(key_v,sublist_v) in enumerate(vertical.items()):
            for i_sub_pos in range(len(sublist_pos)):
                if sublist_pos[i_sub_pos][0] <= key_v and sublist_pos[i_sub_pos][1] >= key_v:
                    y_diag_pos = key_pos+key_v
                    for j_v in range(len(sublist_v)):
                        if sublist_v[j_v][0] <= y_diag_pos <= sublist_v[j_v][1]:
                            collsions.append([key_v,y_diag_pos])
        for j,(key_h,sublist_h) in enumerate(horizontal.items()):
            for j_h in range(len(sublist_h)):
                if offset_manhattan([sublist_h[j_h][0],key_h]) <= key_pos and  key_pos <= offset_manhattan([sublist_h[j_h][1],key_h]):
                    for i_sub_pos in range(len(sublist_pos)):
                        if -key_pos+sublist_pos[i_sub_pos][0] <= key_h and key_h <= -key_pos+sublist_pos[i_sub_pos][1]:
                            collsions.append([key_pos+key_h,key_h])

    for i,(key_neg,sublist_neg) in enumerate(diagonal_neg.items()):
        for j,(key_v,sublist_v) in enumerate(vertical.items()):
            for i_sub_neg in range(len(sublist_neg)):
                if sublist_neg[i_sub_neg][0] <= key_v and sublist_neg[i_sub_neg][1] >= key_v:
                    y_diag_neg = key_neg-key_v
                    for j_v in range(len(sublist_v)):
                        if sublist_v[j_v][0] <= y_diag_neg <= sublist_v[j_v][1]:
                            collsions.append([key_v,y_diag_neg])
        for j,(key_h,sublist_h) in enumerate(horizontal.items()):
            for j_h in range(len(sublist_h)):
                if manhattan([key_h,sublist_h[j_h][0]]) <= key_neg and  key_neg <= manhattan([key_h,sublist_h[j_h][1]]):
                    for i_sub_neg in range(len(sublist_neg)):
                        if key_neg-sublist_neg[i_sub_neg][0] >= key_h and key_h >= key_neg-sublist_neg[i_sub_neg][0]:
                            collsions.append([key_neg-key_h,key_h])
    return collsions

                



def part1():
    debug = False
    horizontal, vertical,_,_ = initialize(debug)

    #print(f"x : {vertical}")
    #print(f"y : {horizontal}")

    collisions_x = straight_colinear_collisions(vertical,0)
    collisions_y = straight_colinear_collisions(horizontal,1)
    collisions_xy = straight_non_colinear_collisions(vertical,horizontal)

    if debug is True:
        print(collisions_x)
        print(collisions_y)
        print(collisions_xy)
    
    else:
        print(len(collisions_x))
        print(len(collisions_y))
        print(len(collisions_xy))


    unique_collisions = collisions_x
    for col in collisions_y:
        if col not in unique_collisions:
            unique_collisions.append(col)
    for col in collisions_xy:
        if col not in unique_collisions:
            unique_collisions.append(col)
    print(len(unique_collisions))

def part2():
    debug = False
    horizontal, vertical,diagonal_pos,diagonal_neg = initialize(debug)

    


    collisions_x = straight_colinear_collisions(vertical,0)
    collisions_y = straight_colinear_collisions(horizontal,1)
    collisions_xy = straight_non_colinear_collisions(vertical,horizontal)

    collisions_diag_pos = diagonal_colinear_collisions(diagonal_pos,1)
    collisions_diag_neg = diagonal_colinear_collisions(diagonal_neg,0)
    collisions_diag = diagonal_non_colinear_collisions(diagonal_pos,diagonal_neg)
    collisions_dunk = diag_straight_collisions(diagonal_pos,diagonal_neg,vertical,horizontal)

    if debug is True:
        print(f"x : {vertical}")
        print(f"y : {horizontal}")

        print(f"slope down:{diagonal_pos}")
        print(f"slope up:{diagonal_neg}")

        print(collisions_x)
        print(collisions_y)
        print(collisions_xy)
        print(collisions_diag_pos)
        print(collisions_diag_neg)
        print(collisions_diag)
        print("dunk", collisions_dunk)
    
    else:
        print(f"colinear_x : {len(collisions_x)}")
        print(f"colinear_y : {len(collisions_y)}")
        print(f"non colinear straight: {len(collisions_xy)}")
        print(f"isonorm  positive slope: {len(collisions_diag_pos)}")
        print(f"isonorm  negative slope: {len(collisions_diag_neg)}")
        print(f"ortho diagonals : {len(collisions_diag)}")
        print(f"straight/diag intersection : {len(collisions_dunk)}")


    unique_collisions = collisions_x
    for col in collisions_y:
        if col not in unique_collisions:
            unique_collisions.append(col)
    for col in collisions_xy:
        if col not in unique_collisions:
            unique_collisions.append(col)
    for col in collisions_diag_pos:
        if col not in unique_collisions:
            unique_collisions.append(col)
    for col in collisions_diag_neg:
        if col not in unique_collisions:
            unique_collisions.append(col)
    for col in collisions_diag:
        if col not in unique_collisions:
            unique_collisions.append(col)
    for col in collisions_dunk:
        if col not in unique_collisions:
            unique_collisions.append(col)
    print(len(unique_collisions))
    return

#part1()
part2()
