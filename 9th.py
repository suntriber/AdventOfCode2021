DATA = [l for l in open('9th.txt', 'r').read().splitlines()]


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
    new = []
    for line in DATA:
        line = line.replace('9', ' ').replace('0', '1').replace('2', '1').replace('3', '1').\
                    replace('4', '1').replace('5', '1').replace('6', '1').replace('7', '1').replace('8', '1')
        line = line.replace(' ', '0')
        new.append([int(n) for n in line])

    basins = sorted([len(n) for n in find_clusters(new)])
    return basins[-1] * basins[-2] * basins[-3]
    

def find_clusters(matrix):
    clusters = []
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 1:
                clusters.append(find_cluster(matrix, i, j))
    return clusters


def find_cluster(matrix, i, j):
    if i < 0 or j < 0 or i >= len(matrix) or j >= len(matrix[0]) or matrix[i][j] == 0:
        return []
    matrix[i][j] = 0
    return [matrix[i][j]] + find_cluster(matrix, i-1, j) + find_cluster(matrix, i+1, j) + find_cluster(matrix, i, j-1) + find_cluster(matrix, i, j+1)


if __name__ == "__main__":
    print(f'Part 1 : {part1()}')
    print(f'Part 2 : {part2()}')
