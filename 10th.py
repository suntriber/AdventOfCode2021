LEFT = ['{', '[', '(', '<']
RIGHT = ['}', ']', ')', '>']
D = {'}': '{', ']': '[', ')': '(', '>': '<'}
N1 = {'}': 1197, ']': 57, ')': 3, '>': 25137}
N2 = {'{': 3, '[': 2, '(': 1, '<': 4}

def get_data():
    return open('10th.txt', 'r').read().splitlines()


def part1():
    invalid = [get_chunk(l) for l in get_data() if get_chunk(l) in RIGHT]
    return sum([N1[c] for c in invalid])


def get_chunk(line):
    stack = []
    for c in line:
        if c in '{[(<':
            stack.append(c)
        elif c in '}])>':
            if D[c] == stack[-1]:
                stack.pop()
            else:
                return c


def get_left(line):
    stack = []
    for c in line:
        if c in LEFT:
            stack.append(c)
        elif c in RIGHT:
            if D[c] == stack[-1]:
                stack.pop()
            else:
                return
    return stack


def part2():
    inc = [get_left(l) for l in get_data() if get_left(l)]    
    tot_score = [get_score(l[::-1]) for l in inc]
    
    return sorted(tot_score)[len(tot_score)//2]


def get_score(line):
    score = 0
    for c in line:
        score *= 5
        score += N2[c]
    return score


if __name__ == "__main__":
    print(f'Part 1 : {part1()}')
    print(f'Part 2 : {part2()}')
