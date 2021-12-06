"""
Day 6: Lanternfish
https://adventofcode.com/2021/day/6
"""
from collections import Counter


def load_input(filepath):
    with open(filepath) as f:
        return [int(num) for num in f.read().split(',')]


def load_input_as_counter(filepath):
    with open(filepath) as f:
        numbers = [int(num) for num in f.read().split(',')]
        c = Counter(numbers)
        for i in range(9):
            if i not in c:
                c[i] = 0
        return c


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
    return len(fishes), fishes


def another_simulate(fishes, days):
    for day in range(days):
        for i in range(0,8):
            if i == 0:
                new_sixes = fishes[i]
                fishes[i] = fishes[i+1]
            else:
                fishes[i] = fishes[i+1]
        fishes[6] += new_sixes # update count of six
        fishes[8] = new_sixes # add new fishes
    return fishes.total()


if __name__ == '__main__':
    # 1
    fishes = load_input('day_06/input.txt')
    count, new_fishes = simulate(fishes, 80)
    print(count)

    # 2
    fishes = load_input_as_counter('day_06/input.txt')
    total = another_simulate(fishes, 256)
    print(total)
