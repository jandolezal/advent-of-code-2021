"""
Day 5: Hydrothermal Venture
https://adventofcode.com/2021/day/5
"""

from collections import defaultdict


def load_input(filepath):
    with open(filepath) as f:
        lines = [line.strip().split(' -> ') for line in f.readlines()]
        raw_lines = []
        for start, end in lines:
            start = tuple([int(num) for num in start.split(',')])
            end = tuple([int(num) for num in end.split(',')])
            raw_lines.append([start, end])
        return raw_lines


def line_from_both_ends(ends):
    sorted_ends = sorted(ends)
    xs = [i for i in range(sorted_ends[0][0], sorted_ends[1][0] + 1)] # +1 to build from start including end
    ys = [i for i in range(sorted_ends[0][1], sorted_ends[1][1] + 1)]
    line = []
    for x in xs:
        for y in ys:
            line.append((x, y))
    return line
            

def make_lines(raw_lines, skip_diagonal=True):
    lines = []
    for raw_line in raw_lines:
        if skip_diagonal:
            if (raw_line[0][0] == raw_line[1][0]) or ( raw_line[0][1] == raw_line[1][1]): #do not include diagonal
                lines.extend(line_from_both_ends(raw_line))
    return lines


def build_diagram(lines):
    d = defaultdict(int)
    for line in lines:
        d[line] += 1
    return d


def calculate_points(diagram):
    return sum(True for v in diagram.values() if v >= 2)


if __name__ == '__main__':
    # 1
    data = load_input('day_05/input.txt')
    lines = make_lines(data)
    diagram = build_diagram(lines)
    points = calculate_points(diagram)
    print(f'Points with at least two overlaps: {points}')
