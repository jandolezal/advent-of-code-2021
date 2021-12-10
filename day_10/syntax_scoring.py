"""
Day 9: Syntax scoring
https://adventofcode.com/2021/day/10
"""


def load_input(filepath):
    with open(filepath) as f:
        return [line.strip() for line in f.readlines()]


def reduce(line):
    chunks = ['()', '[]', '{}', '<>',]

    for chunk in chunks:
        line = line.replace(chunk, '')
    
    if [line.find(chunk) for chunk in chunks] == [-1] * 4:
        return line
    else:
        return reduce(line)


def find_illegal_closing(line):
    map = {
        ')': '(',
        ']': '[',
        '}': '{',
        '>': '<',
    }
    closing_indexes = []

    closing_indexes = [line.find(c) for c in map if line.find(c) != -1 ]

    try:
        first_index = min(closing_indexes)
    except ValueError: # closing_indexes is empty
        return None

    first_char = line[first_index]

    if line[first_index-1] != map[first_char]:
        return line[first_index]


if __name__ == '__main__':
    # 1
    data = load_input('day_10/input.txt')
    chars = []
    for line in data:
        reduced_line = reduce(line)
        char = find_illegal_closing(reduced_line)
        if char:
            chars.append(char)

    points = []
    for char in chars:
        if char == ')':
            points.append(3)
        elif char == ']':
            points.append(57)
        elif char == '}':
            points.append(1197)
        elif char == '>':
            points.append(25137)
    total = sum(points)

    print(total)
