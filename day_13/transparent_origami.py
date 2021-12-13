"""
Day 13: Transparent Origami
https://adventofcode.com/2021/day/13
"""


def load_input(filepath):
    with open(filepath) as f:
        lines = [line.strip() for line in f.readlines()]

        empty_line_index = lines.index('')

        dots = [(int(x), int(y)) for x,y in [line.split(',') for line in lines[:empty_line_index]]]
        instructions_raw = [tuple(inst) for inst in [[part.strip('fold along ') for part in line.split('=')] for line in lines[empty_line_index+1:]]]
        instructions = []
        for axis, value in instructions_raw:
            instructions.append((axis, int(value)))

        return sorted(dots, key=lambda x: (x[1], x[0])), instructions


def split(dots, axis, fold_index):

    if axis == 'y':
        first = [dot for dot in dots if dot[1] < fold_index]
        second = [dot for dot in dots if dot[1] > fold_index]

        new_second = []
        for x, y in second:
            new_y = y - ((y - fold_index) * 2) # new y index from the fold index
            new_second.append((x, new_y))

    elif axis == 'x':
        first = [dot for dot in dots if dot[0] < fold_index]
        second = [dot for dot in dots if dot[0] > fold_index]

        new_second = []
        for x, y in second:
            new_x = x - ((x - fold_index) * 2) # same logic as for y axis
            new_second.append((new_x, y))  

    return list(set(first + new_second))


def part1(filename='day_13/input.txt'):
    dots, instructions = load_input(filename)
    axis, fold_index = instructions[0] # only first line of instructions
    new_dots = split(dots, axis, fold_index)
    return new_dots


def visualize_dots(dots):
    xs = [x for x, _ in dots]
    ys = [y for _, y in dots]

    lines = ''

    for x in range(max(xs) + 1):
        row = []
        for y in range(max(ys) + 1):
            if (x, y) in dots:
                symbol = '#'
            else:
                symbol = ' '
            lines = lines + symbol
        lines = lines + '\n'
    return lines


def part2(filename='day_13/input.txt'):
    dots, instructions = load_input(filename)
    for axis, fold_index in instructions:
        dots = split(dots, axis, fold_index)
    return dots


if __name__ == '__main__':
    # 1
    new_dots = part1()
    print(len(new_dots))

    # 2
    new_dots = part2('day_13/input.txt')
    print(visualize_dots(new_dots))
 