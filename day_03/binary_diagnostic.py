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


def reduce_data(data, rate):
    length = len(data[0])

    for i in range(length):
        bits = []
        for value in data:
            bits.append(value[i])
        c = Counter(bits)
        # Bit criteria
        if rate == 'o':
            most_common = c.most_common()
            if most_common[0][1] == most_common[1][1]: # equal counts
                num = '1'
            else:
                num = most_common[0][0] # higher count wins
        elif rate == 'co2':
            most_common = c.most_common()
            if most_common[-1][1] == most_common[-2][1]: # equal counts
                num = '0'
            else:
                num = most_common[-1][0] # lower count wins
        # Prepare new data which meet the criteria
        data = [binary for binary in data if binary[i] == num]

        if len(data) == 1:
            return int(data[0], 2)


if __name__ == '__main__':
    # 1
    data = load_input('day_03/input.txt')
    
    gamma_rate = compute_rate(data, 'gamma')
    epsilon_rate = compute_rate(data, 'epsilon')

    power_consumption = gamma_rate * epsilon_rate
    print(f'The power consumption is: {power_consumption}')

    # 2
    data = load_input('day_03/input.txt')

    o_rate = reduce_data(data, 'o')
    co2_rate = reduce_data(data, 'co2')
    
    life_support = o_rate * co2_rate
    print(f'Life support rating is: {life_support}')
