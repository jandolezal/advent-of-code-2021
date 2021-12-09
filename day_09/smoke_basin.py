"""
Day 9: Smoke Basin
https://adventofcode.com/2021/day/9
"""


def load_input(filepath):
    with open(filepath) as f:
        return [[int(num) for num in line.strip()] for line in f.readlines()]


def check_left(heightmap, row, col):
    left_col = col - 1 # beware -1 index
    if left_col < 0:
        return True
    return heightmap[row][col] < heightmap[row][left_col]


def check_right(heightmap, row, col):
    try:
        return heightmap[row][col] < heightmap[row][col+1]
    except IndexError:
        return True


def check_up(heightmap, row, col):
    upper_row = row - 1 # beware -1 index
    if upper_row < 0:
        return True
    return heightmap[row][col] < heightmap[upper_row][col]


def check_down(heightmap, row, col):
    try:
        return heightmap[row][col] < heightmap[row+1][col]
    except IndexError:
        return True


def check_adjacent(heightmap, row, col):
    is_lowest =  (
        check_left(heightmap, row, col)
        and check_right(heightmap, row, col)
        and check_up(heightmap, row, col)
        and check_down(heightmap, row, col)
    )

    if is_lowest:
        return heightmap[row][col]



if __name__ == '__main__':
    # 1
    data = load_input('day_09/input.txt')

    rows = len(data)
    cols = len(data[0])

    heights = []

    for row in range(rows):
        for col in range(cols):
            height = check_adjacent(data, row, col)
            if height or height == 0:
                heights.append(height)

    risk_level_sum = sum([level + 1 for level in heights])
    print(f'Sum of risk levels: {risk_level_sum}')

