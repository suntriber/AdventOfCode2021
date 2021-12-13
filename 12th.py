def get_data(): return [l.split('-') for l in open('12th.txt').read().splitlines()]
def get_test(): return [l.split('-') for l in open('test.txt').read().splitlines()]

def part1():
    data = get_data()
    # print(*data, sep='\n')
    paths = []
    other = []

    for l in data:
        if 'start' in l:paths.append(l)
        else: other.append(l)

d = {}

def test():
    
    for line in open('12th.txt').read().splitlines():
        s, e = line.split('-')
        if s != 'end' and e != 'start': d.setdefault(s, set()).add(e)
        if e != 'end' and s != 'start': d.setdefault(s, set()).add(s)
    



if __name__ == "__main__":
    test()