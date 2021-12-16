"""
Day 9: Smoke Basin
https://adventofcode.com/2021/day/9
"""


def load_input(filepath):
    with open(filepath) as f:
        return [[int(num) for num in line.strip()] for line in f.readlines()]


def all_neighbours_are_higher(row, col, heightmap):        
    rows = len(heightmap)
    cols = len(heightmap[0])

    maybe = [(row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)]
    # Filter out illegal indices   
    allowed_indices = [(row, col) for row, col in maybe if (row >= 0) and (row < rows) and (col >= 0) and (col < cols)]

    for adjacent_row, adjacent_col in allowed_indices:
        if heightmap[row][col] >= heightmap[adjacent_row][adjacent_col]:
            return False
    return True


def gather_heights(heightmap):
    rows = len(heightmap)
    cols = len(heightmap[0])

    heights = []

    for row in range(rows):
        for col in range(cols):
            if all_neighbours_are_higher(row, col, heightmap):
                heights.append(heightmap[row][col])

    return heights


if __name__ == '__main__':
    # 1
    heightmap = load_input('day_09/input.txt')
    heights = gather_heights(heightmap)
    risk_level_sum = sum([level + 1 for level in heights])
    print(f'Sum of risk levels: {risk_level_sum}')
