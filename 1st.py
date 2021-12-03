l = [int(n) for n in open('1st.txt', 'r').read().split('\n')]

sum2 = l[0]
inc = 0

for i in range(len(l)):
    if l[i] > sum2:
        inc += 1
    sum2 = l[i]


print(inc)


sum3 = 0
for b in [B > A for A, B in zip(l,l[3:])]:
    if b:
        sum3 += 1

print(sum3)
   



bl = [int(a)<int(b) for a,b in zip(l,l[3:])]

bll22 = [True, True, False, False, True]

print(sum(bll22))

