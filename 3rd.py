# Part 1
l = [n for n in open('3rd.txt', 'r').read().split('\n')]
bits = []

for i in range(12):
    one = 0
    zero = 0
    for rows in l:
        if rows[i] == '1':
            one += 1
        elif rows[i] == '0':
            zero += 1
    
    if one > zero:
        bits.append('1')
    else:
        bits.append('0')

gamma = int(''.join(b for b in bits), 2)
epsilon = int(''.join('0' if int(b) else '1' for b in bits), 2)

print('Part 1 : ', gamma*epsilon)


# Part 2
d1 = [n for n in open('3rd.txt', 'r').read().split('\n')]
d2 = [n for n in open('3rd.txt', 'r').read().split('\n')]

for i in range(12):

    if len(d1)>1:
        z, o = 0, 0
        for l in d1:
            if l[i] == '1':
                o += 1
            else:
                z += 1
        r = '1' if o >= z else '0'
        d1 = [n for n in d1 if n[i] == r]
    
    if len(d2)>1:
        z, o = 0, 0
        for l in d2:
            if l[i] == '1':
                o += 1
            else:
                z += 1
        r = '0' if z <= o else '1'
        d2 = [n for n in d2 if n[i] == r]

oxy, c02 = int(d1[0], 2), int(d2[0], 2)

print('Part 2 : ', oxy*c02)





