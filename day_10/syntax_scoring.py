"""
Day 10: Syntax scoring
https://adventofcode.com/2021/day/10
"""

import statistics

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
    # Check if character preceding first closing character is a match
    if line[first_index-1] != map[first_char]:
        return first_char


def mirror_opening(line):
    map = {
        '(': ')',
        '[': ']',
        '{': '}',
        '<': '>',
    }
    try:
        return ''.join([map[char] for char in line][::-1]) # reverse it
    except KeyError: # this line is corrupted not incomplete, it has closing characters
        return None


if __name__ == '__main__':
    # 1
    data = load_input('day_10/input.txt')
    chars = []
    for line in data:
        reduced_line = reduce(line)
        char = find_illegal_closing(reduced_line)
        if char:
            chars.append(char)

    score_map = {')': 3, ']': 57, '}': 1197, '>': 25137}
    points = [score_map[char] for  char in chars]
    total = sum(points)

    print(total)

    # 2
    data = load_input('day_10/input.txt')

    completions = []
    for line in data:
        opening_chars = reduce(line)
        closing_chars = mirror_opening(opening_chars)
        if closing_chars:
            completions.append(closing_chars)

    score_map = {')': 1, ']': 2, '}': 3, '>': 4}
    scores = []

    for chars in completions:
        total = 0
        for char in chars:
            total = total * 5 + score_map[char]
        scores.append(total)
    
    middle_score = statistics.median(scores)

    print(middle_score)
