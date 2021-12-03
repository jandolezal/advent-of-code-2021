"""
Day 3: Binary Diagnostic
https://adventofcode.com/2021/day/3
"""

from collections import defaultdict
from collections import Counter


def load_input(filepath):
    with open(filepath) as f:
        return [line.strip() for line in f.readlines()]


def compute_rate(data, rate):
    binary_length = len(data[0])

    rate_string = ''

    d = defaultdict(list)

    for value in data:
        for i in range(binary_length):
            d[i].append(value[i])
    
    for k, v in d.items():
        c = Counter(v)
        if rate == 'gamma':
            rate_string += str(c.most_common()[0][0])
        elif rate == 'epsilon':
            rate_string += str(c.most_common()[-1][0])
    return int(rate_string, 2)


if __name__ == '__main__':
    data = load_input('day_03/input.txt')
    
    gamma_rate = compute_rate(data, 'gamma')
    epsilon_rate = compute_rate(data, 'epsilon')

    power_consumption = gamma_rate * epsilon_rate
    print(f'The power consumption is: {power_consumption}')
