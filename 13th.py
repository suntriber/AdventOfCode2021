def get_data(): return [l for l in open('13th.txt').read().splitlines()]


def solve():
    data = get_data()
    dots = [list(map(int, l.split(','))) for l in data if l and not l.startswith('fold')]
    folds = [l[11:].split('=') for l in data if l.startswith('fold')]
    
    
    grid = [[' ' for i in range(1311)] for j in range(895)]
    for x, y in dots: grid[y][x] = '#'

    for index, (a, f) in enumerate(folds):

        grid = fold(grid, a, int(f))
        if index==0:
            cnt = 0
            for r in grid:
                cnt += len([c for c in r if c=='#'])
            print(f'Part 1 : {cnt}\nPart 2 :')

    
    for r in grid: print(' '.join(r[::]))


def fold(grid, axis, fold):

    if axis == 'x':
        dfh = [l[:fold] for l in grid]
        dsh = [l[fold+1:] for l in grid]

        for i in range(len(dsh)):
            for j in range(len(dsh[i])):
                if dfh[i][-(j+1)] != '#':
                    dfh[i][-(j+1)] = dsh[i][j]

    elif axis == 'y':
        dfh = grid[:int(fold)]
        dsh = grid[int(fold)+1::]

        for i in range(len(dsh)):
            for j in range(len(dsh[i])):
                if dfh[-(i+1)][j] != '#':
                    dfh[-(i+1)][j] = dsh[i][j]

    return dfh
    

if __name__ == "__main__":
    solve()
