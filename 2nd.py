l = [n.split() for n in open('2nd.txt', 'r').read().split('\n')]

# pt 1
hor, dep = 0, 0

for i in range(len(l)):
    d, n = l[i]
    if d == 'forward':
        hor += int(n)
    elif d == 'up':
        dep -= int(n)
    elif d == 'down':
        dep += int(n)

print(hor*dep)  # 1690020 correct



# pt 2
hor, dep, aim = 0, 0, 0

for i in range(len(l)):
    d, n = l[i]
    if d == 'forward':
        hor += int(n)
        dep += aim * int(n)
    elif d == 'up':
        aim -= int(n)
    elif d == 'down':
        aim += int(n)

print(hor*dep)  # 1408487760 correct

