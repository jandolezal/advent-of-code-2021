"""
Day 7: The Treachery of Whales
https://adventofcode.com/2021/day/7
"""

import statistics


def load_input(filepath):
    with open(filepath) as f:
        return [int(num) for num in f.read().split(',')]


if __name__ == '__main__':
    # 1
    data = load_input('day_07/input.txt')
    median = statistics.median(data)
    fuel_spent = int(sum([abs(num - median) for num in data]))
    print(fuel_spent)

    # 2
    # Faster version after learning about partial sums @junior.guru
    data = load_input('day_07/input.txt')
    low, high = min(data), max(data)
    fuel_sums = []
    for position in range(low, high):
        basic_diffs = [abs(num - position) for num in data]
        fuel_sums.append(sum([n*(n+1)/2 for n in basic_diffs]))
    print(int(min(fuel_sums)))
