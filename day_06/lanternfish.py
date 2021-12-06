"""
Day 6: Lanternfish
https://adventofcode.com/2021/day/6
"""


def load_input(filepath):
    with open(filepath) as f:
        return [int(num) for num in f.read().split(',')]


def simulate(fishes, days):
    for day in range(days):
        new = []
        for i, fish in enumerate(fishes):
            if fish == 0:
                fishes[i] = 6
                new.append(8)
            else:
                fishes[i] = fishes[i] - 1
        fishes.extend(new)
        # print(f'{day}: {fishes}')
    return len(fishes), fishes


if __name__ == '__main__':
    # 1
    fishes = load_input('day_06/test_input.txt')
    count, new_fishes = simulate(fishes, 18)
    print(count)
