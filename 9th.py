DATA = [l for l in open('9th.txt', 'r').read().splitlines()]
# DATA = [[2199943210],
#         [3987894921],
#         [9856789892],
#         [8767896789],
#         [9899965678]]


def get_data():
    return [l for l in open('9th.txt', 'r').read().splitlines()]


def part1():
    data = get_data()
    low_points = []

    # check horizontal
    # - if j != 0 check left ([i][j-1])
    # - if j != len(data)-1 check right ([i][j+1])

    # check vertical
    # - if i != 0 check above ([i-1][j])
    # - if i != len(data)-1 check below ([i+1][j])

    if int(data[0][0]) < int(data[0][1]) and int(data[0][0]) < int(data[1][0]): # top left
        low_points.append(int(int(data[0][0]))+1)
    if int(data[0][99]) < int(data[0][98]) and int(data[0][99]) < int(data[1][99]): # top right
        low_points.append(int(int(data[0][99]))+1)
    if int(data[99][0]) < int(data[99][1]) and int(data[99][0]) < int(data[98][0]): # bottom left
        low_points.append(int(int(data[0][0]))+1)
    if int(data[99][99]) < int(data[99][98]) and int(data[99][99]) < int(data[98][99]): # bottom right
        low_points.append(int(int(data[0][0]))+1)
    
    for i in range(1, 99): 
        if int(data[i][0]) < int(data[i][1]) and int(data[i][0]) < int(data[i+1][0]) and int(data[i][0]) < int(data[i-1][0]): 
            low_points.append(int(data[i][0])+1) # check leftmost column
        
        if int(data[i][99]) < int(data[i][98]) and int(data[i][99]) < int(data[i+1][99]) and int(data[i][99]) < int(data[i-1][99]):
            low_points.append(int(data[i][99])+1) # check rightmost column
        
        if int(data[0][i]) < int(data[1][i]) and int(data[0][i]) < int(data[0][i+1]) and int(data[0][i]) < int(data[0][i-1]):
            low_points.append(int(data[0][i])+1) # check top row
        
        if int(data[99][i]) < int(data[98][i]) and int(data[99][i]) < int(data[99][i+1]) and int(data[99][i]) < int(data[99][i-1]):
            low_points.append(int(data[99][i])+1) # check bottom row

    for i in range(1, 99):
        for j in range(1, 99):
            if int(data[i][j]) < int(data[i][j+1]) and int(data[i][j]) < int(data[i][j-1]) and int(data[i][j]) < int(data[i+1][j]) and int(data[i][j]) < int(data[i-1][j]):
                low_points.append(int(data[i][j])+1)
    
    return(sum(low_points))


def part2():
    data = get_data()
    basin = 0
    basins = []
    b = {}

    for i in range(len(DATA)):
        for j in range(len(DATA[0])):
            # print(f'i:{i}\tj:{j}')
            # basin = check_horizontal(j, i) 
            # basin += check_vertical(j, i) 
            basin += check_diagonal(j, i)
            basins.append(basin)
            b[(j, i)] = basin

    basins = sorted(basins)

    return basins[-1] * basins[-2] * basins[-3]
    

def check_vertical(x1, y1):
    x, y = x1, y1
    val = DATA[y][x]

    basins = 1

    while y-1 >= 0:
        y -= 1
        if int(DATA[y][x]) == 9:
            break
        elif int(val) - int(DATA[y][x]) <= 0:
            basins += 1
            val = DATA[y][x]
        else:
            break

    x, y = x1, y1
    val = DATA[y][x]
    while y+1 < len(DATA):
        y += 1
        if int(DATA[y][x]) == 9:
            break
        elif int(val) - int(DATA[y][x]) <= 0:
            basins += 1
            val = DATA[y][x]
        else:
            break
        
    return basins


def check_horizontal(x1, y1):
    x, y = x1, y1
    val = DATA[y][x]
    basin = 1
    while x > 0:
        x -= 1
        if int(DATA[y][x]) == 9:
            break
        elif int(val) - int(DATA[y][x]) <= 0:
            basin += 1
            val = DATA[y][x]
        else:
            break
    
    x, y = x1, y1
    val = DATA[y][x]
    while x+1 < len(DATA[0]):
        x += 1
        if int(DATA[y][x]) == 9:
            break
        elif int(val) - int(DATA[y][x]) <= 0:
            basin += 1
            val = DATA[y][x]
        else:
            break
        
    return basin
            

def check_diagonal(x1, y1):
    basin = 1
    x, y = x1, y1
    val = DATA[y][x]
    while x > 0 and y > 0: # x>y> x- y-
        x -= 1
        y -= 1
        if int(DATA[y][x]) == 9:
            break
        elif int(val) - int(DATA[y][x]) <= 0:
            basin += 1
            val = DATA[y][x]
        else:
            break

    x, y = x1, y1   
    val = DATA[y][x]
    while x+1 < len(DATA[0]) and y+1 < len(DATA): # x<y< x+ y+
        x += 1
        y += 1
        if int(DATA[y][x]) == 9:
            break
        elif int(val) - int(DATA[y][x]) <= 0:
            basin += 1
            val = DATA[y][x]
        else:
            break

    x, y = x1, y1   
    val = DATA[y][x]
    while x > 0 and y+1 < len(DATA): # x>y< x- y+ 
        x -= 1
        y += 1
        if int(DATA[y][x]) == 9:
            break
        elif int(val) - int(DATA[y][x]) <= 0:
            basin += 1
            val = DATA[y][x]
        else:
            break

    x, y = x1, y1   
    val = DATA[y][x]
    while x+1 < len(DATA) and y > 0: # x<y>  x+ y-
        x += 1
        y -= 1
        if int(DATA[y][x]) == 9:
            break
        elif int(val) - int(DATA[y][x]) <= 0:
            basin += 1
            val = DATA[y][x]
        else:
            break
    
    return basin


def p2():
    b = []
    for i in range(len(DATA)):
        for j in range(len(DATA[0])):
            b.append(all_directions(i, j, 1))
    b = sorted(b)
    print(b[-10:])
    return b[-1] * b[-2] * b[-3]
    

def east(x, y, val):
    tmp = DATA[y][x]
    if x == len(DATA[0])-1:
        return val
    elif int(DATA[y][x+1]) == 9:
        return val
    elif int(DATA[y][x]) - int(DATA[y][x+1]) > 0:
        return val
    else:
        val += 1
        x += 1
        # return east(x, y, val)
        return east(x, y, val)

def west(x, y, val):
    tmp = DATA[y][x]
    if x == 0:
        return val
    elif int(DATA[y][x-1]) == 9:
        return val
    elif int(DATA[y][x]) - int(DATA[y][x-1]) > 0:
        return val
    else:
        val += 1
        x -= 1
        # return west(x, y, val)
        return west(x, y, val)

def south(x, y, val):
    tmp = DATA[y][x]
    if y == len(DATA)-1:
        return val
    elif int(DATA[y+1][x]) == 9:
        return val
    elif int(DATA[y][x]) - int(DATA[y+1][x]) > 0:
        return val
    else:
        val += 1
        y += 1
        # return south(x, y, val)
        return south(x, y, val)

def north(x, y, val):
    tmp = DATA[y][x]
    if y == 0:
        return val
    elif int(DATA[y-1][x]) == 9:
        return val
    elif int(DATA[y][x]) - int(DATA[y-1][x]) > 0:
        return val
    else:
        val += 1
        y -= 1
        # return north(x, y, val)
        return north(x, y, val)
        

def southeast(x, y, val): # xy++
    tmp = DATA[y][x]
    if y == len(DATA)-1 or x == len(DATA[0])-1:
        return val
    elif int(DATA[y+1][x+1]) == 9:
        return val
    elif int(DATA[y][x]) - int(DATA[y+1][x+1]) > 0:
        return val
    else:
        val += 1
        y += 1
        x += 1
        return southeast(x, y, val) 
        
def southwest(x, y, val): # xy -+
    tmp = DATA[y][x]
    if y == len(DATA)-1 or x == 0:
        return val
    elif int(DATA[y+1][x-1]) == 9:
        return val
    elif int(DATA[y][x]) - int(DATA[y+1][x-1]) > 0:
        return val
    else:
        val += 1
        y += 1
        x -= 1
        return southwest(x, y, val) 

def northeast(x, y, val): # xy +-
    tmp = DATA[y][x]
    if y == 0 or x == len(DATA)-1:
        return val
    elif int(DATA[y-1][x+1]) == 9:
        return val
    elif int(DATA[y][x]) - int(DATA[y-1][x+1]) > 0:
        return val
    else:
        val += 1
        y -= 1
        x += 1
        return northeast(x, y, val) 

def northwest(x, y, val): # xy --
    tmp = DATA[y][x]
    if y == 0 or x == 0:
        return val
    elif int(DATA[y-1][x-1]) == 9:
        return val
    elif int(DATA[y][x]) - int(DATA[y-1][x-1]) > 0:
        return val
    else:
        val += 1
        y -= 1
        x -= 1
        return northwest(x, y, val) 

def all_directions(x, y, val):
    val += south(x, y, val)
    val += north(x, y, val)
    val += east(x, y, val)
    val += west(x, y, val)
    # val += southeast(x, y, val)
    # val += southwest(x, y, val)
    # val += northeast(x, y, val)
    # val += northwest(x, y, val)

    return val

def find_minima(matrix):
    """
    Finds the three biggest local minima in a matrix.
    """
    minima = []
    for i in range(1, 99):
        for j in range(1, 99):
            if matrix[i][j] < matrix[i-1][j] and matrix[i][j] < matrix[i+1][j] and matrix[i][j] < matrix[i][j-1] and matrix[i][j] < matrix[i][j+1]:
                minima.append((i, j))
    minima = sorted(minima, key=lambda x: matrix[x[0]][x[1]])
    return minima[:3]


if __name__ == "__main__":
    # print(f'Part 1 : {part1()}')
    # print(f'Part 2 : {part2()}')
    # print(f'Part 2 : {p2()}')
    # print(*DATA, sep='\n')
    # print(east(9,0,1))
    # print(west(9,0,1))
    # print(south(0, 2, 1))
    # print(north(0, 2, 1))
    import numpy as np
    d = np.array(get_data())
    print(find_minima(d))

    print(all_directions(1, 76, 1) * all_directions(2, 24, 1) * all_directions(3, 16, 1))






