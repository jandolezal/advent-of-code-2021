"""
Day 9: Smoke Basin
https://adventofcode.com/2021/day/9
"""

from collections import defaultdict
import math


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


def gather_lowest_points(heightmap):
    rows = len(heightmap)
    cols = len(heightmap[0])

    lowest = []

    for row in range(rows):
        for col in range(cols):
            if all_neighbours_are_higher(row, col, heightmap):
                lowest.append((row, col))

    return lowest


def list_neighbours_lower_than_nine(row, col, heightmap):        
    rows = len(heightmap)
    cols = len(heightmap[0])

    lower = []

    maybe = [(row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)]
    # Filter out illegal indices   
    allowed_indices = [(row, col) for row, col in maybe if (row >= 0) and (row < rows) and (col >= 0) and (col < cols)]

    for adjacent_row, adjacent_col in allowed_indices:
        if heightmap[adjacent_row][adjacent_col] < 9:
            lower.append((adjacent_row, adjacent_col))

    return lower


def walk(row, col, heightmap, visited_dict, lowest):
    lower_neighbours = list_neighbours_lower_than_nine(row, col, heightmap)
    if not lower_neighbours:
        return
    else:
        for r, c in lower_neighbours:
            if (r, c) not in visited_dict[lowest]:
                visited_dict[lowest].append((r,c))
                walk(r, c, heightmap, visited_dict, lowest)


def walk_all_lowest_points(lowest_points):
    visited_dict = defaultdict(list)
    for row, col in lowest_points:
        walk(row, col, heightmap, visited_dict, lowest=(row,col))
    return visited_dict


if __name__ == '__main__':
    # 1
    heightmap = load_input('day_09/input.txt')
    heights = gather_heights(heightmap)
    risk_level_sum = sum([level + 1 for level in heights])
    print(f'Sum of risk levels: {risk_level_sum}')
    
    # 2
    heightmap = load_input('day_09/input.txt')
    lowest_points = gather_lowest_points(heightmap)
    visited = walk_all_lowest_points(lowest_points)
    top_3 = sorted([len(v) for v in visited.values()])[-3:]
    print(f'Multiplication of top 3 smoke basins is: {math.prod(top_3)}')
