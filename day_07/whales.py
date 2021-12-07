"""
Day 7: The Treachery of Whales
https://adventofcode.com/2021/day/7
"""

import statistics
import math
from collections import Counter

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
    data = load_input('day_07/input.txt')
    low, high = min(data), max(data)
    fuel_sums = {}
    for position in range(low, high):
        basic_diffs = [abs(num - position) for num in data]
        new_diffs = []
        for diff in basic_diffs:
            new_diffs.append(sum([x + 1 for x in range(diff)]))
        fuel_sums[position] = sum(new_diffs)
    print(Counter(fuel_sums).most_common()[-1][1])


    # This is a wrong model. Mean minimises sum of squared errors.
    # mean = int(round((statistics.mean(data))))
    # basic_differences = [abs(num - mean) for num in data]
    # new_differences = []
    # for diff in basic_differences:
    #     new_differences.append(sum([x + 1 for x in range(diff) ]))
    # fuel_spent = sum(new_differences)
    # print(fuel_spent)

    # It is not 98925156