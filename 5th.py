import re


def testing():
    lines = [[(0, 9), (5, 9)],
            [(8, 0), (0, 8)],
            [(9, 4), (3, 4)],
            [(2, 2), (2, 1)],
            [(7, 0), (7, 4)],
            [(6, 4), (2, 0)],
            [(0, 9), (2, 9)],
            [(3, 4), (1, 4)],
            [(0, 0), (8, 8)],
            [(5, 5), (8, 2)]]
    new_lines = []
    print(len(lines))
    for line in lines:
        tup1, tup2 = line
        if tup1[0] == tup2[0] or tup1[1] == tup2[1]:
            new_lines.append([tup1, tup2])
    print(*new_lines, sep='\n')
    print('================')



def get_data():
    # with open('5th.txt') as f:
    #     return [list(map(int, re.findall('\d+', l))) for l in f]
    return [[int(l) for l in line.replace(' -> ', ',').split(',')] for line in open('5th.txt')]

def part1(data):

    new_data = []
    for x1, y1, x2, y2 in data:
        if x1 == x2 or y1 == y2:
            new_data.append([x1,y1,x2,y2])

    grid = [[0 for _ in range(1000)] for _ in range(1000)]

    for x1, y1, x2, y2 in new_data:
        if x1 == x2:
            x = x1
            if y1 > y2:
                while y1 >= y2:
                    grid[y1][x] += 1
                    y1 -= 1
            elif y2 > y1:
                while y2 >= y1:
                    grid[y2][x] += 1
                    y2 -= 1
        elif y1 == y2:
            y = y1
            if x1 > x2:
                while x1 >= x2:
                    grid[y][x1] += 1
                    x1 -= 1
            elif x2 > x1:
                while x2 >= x1:
                    grid[y][x2] += 1
                    x2 -= 1
        
    count = 0
    for row in grid:
        for n in row:
            if n > 1:
                count += 1
    print('Part 1 : ', count)



def part2(data):
    grid = [[0 for _ in range(1000)] for _ in range(1000)]
    def sign(n):
        # return (1 if n > 0 else -1) if n else 0
        if not n:
            return 0
        elif n > 0:
            return 1
        else:
            return -1

    for x1, y1, x2, y2 in data:
        dx, dy = sign(x2 - x1), sign(y2 - y1)
        x, y = x1, y1
        while x != x2 or y != y2:
            grid[y][x] += 1
            x += dx
            y += dy
        grid[y2][x2] += 1
    
    count = 0
    for row in grid:
        for n in row:
            if n > 1:
                count += 1

    print('Part 2 : ', count)




if __name__ == "__main__":
    data = get_data()
    part1(data)
    part2(data)

    if -1:
        print('-1 = yes')
    else:
        print('-1 = no')
    if 0:
        print('0 = yes')
    else:
        print('0 = no')
    if 1:
        print('1 = yes')
    else:
        print('1 = no')