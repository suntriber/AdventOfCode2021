def solve(n):
    data = [[int(n) for n in l] for l in open('11th.txt', 'r').read().splitlines()]
    flash = 0

    for k in range(n):
        for i in range(len(data)):
            for j in range(len(data[0])):
                data[i][j] += 1

        boom = True
        while boom:
            boom = False
            for i in range(len(data)):
                for j in range(len(data[0])):
                    if data[i][j] > 9:
                        boom, flash, data[i][j] = True, flash+1, 0
                        for y, x in [(0, 1),(0, -1),(1, 0),(-1, 0),(1, 1),(-1, -1),(-1, 1),(1, -1)]:
                            if y+i < 0 or y+i >= len(data) or x+j < 0 or x+j >= len(data[0]):
                                continue
                            if data[y+i][x+j] == 0:
                                continue
                            data[y+i][x+j] += 1

        if all_zero(data):
            return k+1
    return flash


def all_zero(data):
    for n in data:
        if sum(n) > 0:
            return False
    return True


if __name__ == "__main__":
    print(f'Part 1 : {solve(100)}')
    print(f'Part 2 : {solve(1000)}')

# Part 1
# print((u:=lambda i,c,e:1 if(i in e or c[i]<10)else(e.add(i)or[c.__setitem__(i+d,c[i+d]+1)or u(i+d,c,e)for d in(-11,-10,-9,-1,1,9,10,11)if 0<=i+d<100 and-2<i%10-(i+d)%10<2]))and(g:=lambda c:(e:=set())or[u(i,c,e)for i in range(100)]and[c.__setitem__(i,1+(i not in e and c[i]))for i in range(100)]and len(e))and(c:=[int(i)+1 for l in open("11th.txt").read().splitlines()for i in l])and sum(g(c)for _ in range(100)))

# Part 2
# print((u:=lambda i,c,e:1 if(i in e or c[i]<10)else(e.add(i)or[c.__setitem__(i+d,c[i+d]+1)or u(i+d,c,e)for d in(-11,-10,-9,-1,1,9,10,11)if 0<=i+d<100 and-2<i%10-(i+d)%10<2]))and(g:=lambda c:(e:=set())or[u(i,c,e)for i in range(100)]and[c.__setitem__(i,1+(i not in e and c[i]))for i in range(100)]and len(e))and(s:=lambda c,n:n if g(c)==100 else s(c,n+1))and(c:=[int(i)+1 for l in open("11th.txt").read().splitlines()for i in l])and s(c,1))
