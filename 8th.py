def get_data():
    return [l.split('|') for l in open('8th.txt', 'r').read().splitlines()]


def part1():
    data = get_data()
    data_digits = []
    for n in data:
        for m in n[1].split():
            data_digits.append(m)
    return (sum(len(x) in (2,3,4,7) for x in data_digits))
    

def part2():
    data = get_data()

    # 1 = len(2)
    # 4 = len(4)
    # 7 = len(3)
    # 8 = len(7)

    # if 1 in len(5) --> 3
    # if 4 in len(6) --> 9
    # if len(6) in 8 --> 0
    # if 3/5 len(5) in 4 --> 5
    # if 2/5 len(5) in 4 --> 2 
    # if len(6) in 8 and not in 1 --> 6

    
    tot = []
    for i in range(len(data)):
        sum_ = []
        seq = get_digit(data[i][0].split())    
        for n in data[i][1].split():
            for k, v in seq.items():
                if set(n) == set(v):
                    sum_.append(str(k))
        tot.append(int(''.join(c for c in sum_)))
    return sum(tot)


def get_digit(pattern):
    digits = {i:'' for i in range(10)}

    for s in pattern:
        if len(s) == 2:digits[1] = s
        elif len(s) == 3:digits[7] = s
        elif len(s) == 4:digits[4] = s
        elif len(s) == 7:digits[8] = s
    
    for s in pattern:
        if len(s) == 5:
            if nbr_a_in_b(digits[1], s) == 2:digits[3] = s
            elif nbr_a_in_b(digits[4], s) == 3:digits[5] = s
            elif nbr_a_in_b(digits[4], s) == 2:digits[2] = s
        if len(s) == 6:
            if nbr_a_in_b(digits[4], s)==4:digits[9] = s
            elif nbr_a_in_b(digits[7], s) == 2:digits[6] = s
            else:digits[0] = s       

    return digits


def nbr_a_in_b(a, b):
    return len([n for n in a if n in b])


if __name__ == "__main__":
    print(f'Part 1 : {part1()}')
    print(f'Part 2 : {part2()}')
