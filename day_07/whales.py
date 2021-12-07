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
