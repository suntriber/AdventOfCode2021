def main():
    print(f'Part 1 : {solve1()}')
    print(f'Part 2 : {solve2()}')


def solve1():
    # going from median position
    import statistics
    data = get_data()
    med = statistics.median(data)
    total_med = 0

    for i in range(len(data)):
        num_med = data[i] - med
        total_med += abs(num_med)
    
    return int(total_med)
    

def solve2():
    # going from average
    data = get_data()
    total_avg = 0
    avg = sum(data) // len(data)

    for i in range(len(data)):
        num_avg = data[i] - avg
        total_avg = total_avg + abs(num_avg) +sum([n for n in range(abs(num_avg))])
    
    return total_avg


def get_data():
    return [int(n) for n in open('7th.txt', 'r').read().split(',')]


if __name__ == "__main__":
    main()
