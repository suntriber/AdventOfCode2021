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


def who_won(numbers, boards):
    nums_drawn = []
    for n in numbers:
        nums_drawn.append(n)
        for b in boards:
            if check_bingo(nums_drawn, b):
                return b, nums_drawn
                

def who_won2(numbers, boards):
    nums_drawn = []
    win = []
    nums_winning = []
    for n in numbers:
        nums_drawn.append(n)
        for b in boards:
            if check_bingo(nums_drawn, b):

                win.append(b)
                nums_winning.append(nums_drawn)
                if len(win) == 100:
                    return win, nums_winning


def main():

    numbers, boards = get_data()
        
    winning_board, nums_drawn = who_won(numbers, boards)
    num_not_in_b = get_unmarked(winning_board, nums_drawn)

    print(sum(num_not_in_b) * nums_drawn[-1])

    win2, nums2 = who_won2(numbers, boards)
    num_not_in_b2 = get_unmarked(win2[-1], nums2[-1])

    

    
    print(sum(num_not_in_b2) * nums2[-1][-1])

 




    
    




if __name__ == "__main__":
    main()