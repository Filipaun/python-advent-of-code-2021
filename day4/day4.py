from pprint import pprint
def initialize():
    with open("day4/input.txt") as file:
        number_draw = [int(x) for x in file.readline().split(",")]
        boards_data = file.readlines()
    boards = []
    current_board = []
    for i,line in enumerate(boards_data[1:]):
        if line == "\n":
            boards.append(current_board)
            current_board = []
        else:
            current_board.append([int(x) for x in line.strip().strip("\n").split(" ") if x != ""])
            if i == len(boards_data)-2:
                boards.append(current_board)
    return number_draw,boards

def index_2d(list,value):
    for i,sublist in enumerate(list):
        if value in sublist:
            return(i,sublist.index(value))
    else:
        return None

def board_draw_value(board,bingo_board,value):
    value_index = index_2d(board,value)
    #if board_
    if value_index != None:
        bingo_board[value_index[0]][value_index[1]] = 1
    else:
        pass

def check_bingo(bingo_board):
    board_size = len(bingo_board)
    for i in range(board_size):
        hor = sum(bingo_board[i])
        ver = sum([bingo_board[j][i] for j in range(board_size)])

        if hor == board_size or ver == board_size:
            return True
    return False

def sum_unmarked(board,bingo_board):
    partial_sum = 0
    for i,subblist in enumerate(board):
        for j,val in enumerate(subblist):
            partial_sum += val*(1-bingo_board[i][j])
    return partial_sum

def generate_bingo_boards(n_boards,board_size):
    bingo_boards = [[[0 for x in range(board_size)] for y in range(board_size)] for z in range(n_boards)]
    return bingo_boards

def part1():
    number_draw,boards = initialize()
    
    n_boards = len(boards)
    print(n_boards)
    board_size = len(boards[0])

    bingo_boards = generate_bingo_boards(n_boards,board_size)

    for i,val in enumerate(number_draw):
        for board_number in range(n_boards):
            board_draw_value(boards[board_number],bingo_boards[board_number],val)
            if board_number == 2:
                print(bingo_boards[board_number])
            if check_bingo(bingo_boards[board_number]):
                final_score = sum_unmarked(boards[board_number],bingo_boards[board_number])
                pprint(bingo_boards[board_number])
                print(f"final score: {final_score}, last value ={val}")
                print(final_score*val)
                return
def part2():
    number_draw,boards = initialize()
    
    n_boards = len(boards)
    board_size = len(boards[0])

    bingo_boards = generate_bingo_boards(n_boards,board_size)

    remaining_boards = [i for i in range(n_boards)]

    

    for i,val in enumerate(number_draw):
        winning_boards = []
        print(val,remaining_boards)
        for board_number in remaining_boards:
            board_draw_value(boards[board_number],bingo_boards[board_number],val)

            if check_bingo(bingo_boards[board_number]):
                if len(remaining_boards) > 1:
                    winning_boards.append(board_number)
                else:
                    final_score = sum_unmarked(boards[board_number],bingo_boards[board_number])
                    print(remaining_boards)
                    pprint(bingo_boards[board_number])
                    print(f"final score: {final_score}, last value ={val}")
                    print(final_score*val)
                    return
        for board in winning_boards:
            remaining_boards.remove(board)
    return

part2()
