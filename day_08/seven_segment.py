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


def identify_easy_digits(line):
    digits = {}
    for letters in line[0]:
        length = len(letters)
        letters = set(letters)
        if length == 2:
            digits[1] = letters
        if length == 3:
            digits[7] = letters            
        if length == 4:
            digits[4] = letters
        if length == 7:
            digits[8] = letters
    return digits


def build_mapping(line):
    digits = identify_easy_digits(line)
    fives = [set(letters) for letters in line[0] if len(letters) == 5]
    sixes = [set(letters) for letters in line[0] if len(letters) == 6]
    
    segments = {}

    segments['a'] = list(digits[7] - digits[1])[0]

    digits[3] = list([letters for letters in fives if digits[1] <= letters])[0]
    digits[6] = list([letters for letters in sixes if not digits[1] <= letters])[0]
    digits[9] = list([letters for letters in sixes if digits[4] <= letters])[0]
    digits[0] = list([letters for letters in sixes if (letters != digits[6] and letters != digits[9] ) ] )[0]
    digits[5] = list([letters for letters in fives if letters <= digits[6]])[0]
    digits[2] = list([letters for letters in fives if (letters != digits[3] and letters != digits[5] ) ] )[0]

    segments['d'] = list(digits[8] - digits[0])[0]    
    segments['e'] = list(digits[6] - digits[5])[0]
    segments['c'] = list(digits[8] - digits[6])[0]
    segments['f'] = list(digits[1] - set(segments['c']))[0]
    segments['b'] = list(digits[4] - set([segments['c'], segments['d'], segments['f']]))[0]
    segments['g'] = list(set('abcdefg') - set(segments.values()))[0]

    return segments


def translate(line, mapping):
    reverse_mapping = {v: k for k, v in mapping.items()}
    digits = []
    for letters in line[1]:
        segments = []
        for letter in letters:
            segments.append(reverse_mapping[letter])
        segments = ''.join(sorted(segments))
        if segments == 'abcefg':
            digits.append(0)
        elif segments == 'cf':
            digits.append(1)
        elif segments == 'acdeg':
            digits.append(2)
        elif segments == 'acdfg':
            digits.append(3)
        elif segments == 'bcdf':
            digits.append(4)
        elif segments == 'abdfg':
            digits.append(5)
        elif segments == 'abdefg':
            digits.append(6)
        elif segments == 'acf':
            digits.append(7)
        elif segments == 'abcdefg':
            digits.append(8)
        elif segments == 'abcdfg':
            digits.append(9)
    return int(''.join([str(num) for num in digits]))


if __name__ == '__main__':
    # 1
    data = load_input('day_08/input.txt')
    easy_count = count_easy_digits(data)
    print(easy_count)

    # 2
    data = load_input('day_08/input.txt')
    num_sum = 0
    for line in data:
        mapping = build_mapping(line)
        number = translate(line, mapping)
        num_sum += number
    print(num_sum)
