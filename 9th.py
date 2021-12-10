DATA = [l for l in open('9th.txt', 'r').read().splitlines()]

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


def get_mod():
    l = [l for l in open('9th.txt', 'r').read().splitlines()]
    return ['9'*(len(l)+2)] + ['9'+s+'9' for s in l] + ['9'*(len(l)+2)]


def part1():
    data = get_mod()
    low_points = []
    for i in range(1, len(data)-1):
        for j in range(1, len(data[0])-1):
            n = int(data[i][j])
            if n < int(data[i][j+1]) and n < int(data[i][j-1]) and n < int(data[i+1][j]) and n < int(data[i-1][j]):
                low_points.append(int(data[i][j])+1)
    return sum(low_points)


if __name__ == "__main__":
    print(f'Part 1 : {part1()}')
    print(f'Part 2 : {part2()}')
