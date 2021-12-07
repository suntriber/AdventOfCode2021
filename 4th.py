# for n in numbers:
# check if bingo in any board
# if bingo, get sum of all unmarked numbers
# multiply with number that was last drawn

import numpy as np

def get_data():
    data = open('4th.txt', 'r').read().splitlines()
    numbers = list(map(int, data[0].split(',')))
    boards = []

    for i in range(2, len(data), 6):
        boards.append(data[i:i+5])
        boards[-1] = [list(map(int, n.split())) for n in boards[-1]]
    
    return numbers, boards


def is_bingo(nums, row):
    row_length = 0
    for n in row:
        if n in nums:
            row_length += 1
    return row_length == len(row)


def check_bingo(nums, board):

    for row in board:
        if is_bingo(nums, row):
            return True
    for flipped_row in np.array(board).T:
        if is_bingo(nums, flipped_row):
            return True
    return False


def get_unmarked(board, nums):
    unmarked = []
    for row in board:
        for n in row:
            if n not in nums:
                unmarked.append(n)
    return unmarked


def part1():
    numbers, boards = get_data()
    nums_drawn = []
    for n in numbers:
        nums_drawn.append(n)
        for b in boards:
            if check_bingo(nums_drawn, b):
                return b, nums_drawn
                

def part2():
    numbers, boards = get_data()
    nums_drawn, win = [], []
    for n in numbers:
        nums_drawn.append(n)
        for b in boards:
            if check_bingo(nums_drawn, b):
                win.append((b, [j for j in nums_drawn], nums_drawn[-1]))
                boards.remove(b)
                if len(boards) == 0:
                    return win
            

def main():

    winning_board, nums_drawn = part1()
    print(f'Part 1 : {sum(get_unmarked(winning_board, nums_drawn)) * nums_drawn[-1]}')

    win = part2()
    print(f'Part 2 : {sum(get_unmarked(win[-1][0], win[-1][1])) * win[-1][2]}')


if __name__ == "__main__":
    main()
