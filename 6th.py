def main():
    print(f'Part 1 : {solve(80)}')
    print(f'Part 2 : {solve(256)}')

    


def solve(n):
    from collections import Counter
    data = get_data()
    fish_dict = Counter(data)

    for _ in range(n):
        # decrease keys by one each iteration
        fish_dict = {k-1: v for k, v in fish_dict.items()}

        # add new fishes at key 8 from fish all that has reached -1
        new_fishes = fish_dict.get(-1, 0)
        fish_dict[8] = new_fishes

        # reset all -1 fish to 6
        reset_fish = fish_dict.pop(-1, 0)
        six_fishes = fish_dict.get(6, 0)
        fish_dict[6] = reset_fish + six_fishes
    
    return sum(fish_dict.values())


def get_data():
    return [int(n) for n in open('6th.txt', 'r').read().split(',')]


if __name__ == "__main__":
    main()

