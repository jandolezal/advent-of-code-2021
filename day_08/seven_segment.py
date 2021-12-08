"""
Day 8: Seven Segment Search
https://adventofcode.com/2021/day/8
"""

from typing import List


def load_input(filepath) -> List[List[str]]:
    with open(filepath) as f:
        lines =  [line.split('|') for line in f.readlines()]
        data = []
        for line in lines:
            data.append([part.strip().split(' ') for part in line ])
        return data


def count_easy_digits(data):
    count = 0
    for _, output in data:
        for letters in output:
            if len(letters) in [2, 3, 4, 7]:
                count += 1
    return count


def identify_digits(line):
    input = line[0]
    digits = {}

    # easy digits
    digits[1] = [letters for letters in input if len(letters) == 2][0]
    digits[4] = [letters for letters in input if len(letters) == 4][0]
    digits[7] = [letters for letters in input if len(letters) == 3][0]
    digits[8] = [letters for letters in input if len(letters) == 7][0]
    
    # complicated digits
    digits[3] = [letters for letters in input if ((len(letters) == 5) and set(digits[1]) <= set(letters))][0]
    digits[6] = [letters for letters in input if ((len(letters) == 6) and not set(digits[1]) <= set(letters))][0]
    digits[9] = [letters for letters in input if ((len(letters) == 6) and set(digits[4]) <= set(letters))][0]
    digits[0] = [letters for letters in input if ((len(letters) == 6) and set(letters) != set(digits[6]) and set(letters) != set(digits[9]))][0]
    digits[5] = [letters for letters in input if ((len(letters) == 5) and set(letters) <= set(digits[6]))][0]
    digits[2] = [letters for letters in input if ((len(letters) == 5) and set(letters) != set(digits[3]) and set(letters) != set(digits[5]))][0]

    return digits


def reverse_mapping(mapping):
    return {''.join(sorted(v)): k for k, v in mapping.items()}


def apply_mapping(line, mapping):
    output = line[1]
    digits = ''
    for letters in output:
        sorted_letters = ''.join(sorted(letters))
        digits += str(mapping[sorted_letters])
    return int(digits)


if __name__ == '__main__':
    # 1
    data = load_input('day_08/input.txt')
    easy_count = count_easy_digits(data)
    print(easy_count)

    # 2
    data = load_input('day_08/input.txt')
    num_sum = 0
    for line in data:
        digits = identify_digits(line)
        mapping = reverse_mapping(digits)
        number = apply_mapping(line, mapping)
        num_sum += number
    print(num_sum)
