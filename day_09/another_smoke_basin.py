"""
Day 9: Smoke Basin
https://adventofcode.com/2021/day/9
"""


def load_input(filepath):
    with open(filepath) as f:
        return [[int(num) for num in line.strip()] for line in f.readlines()]


def check_neighbours(row, col, heightmap):
    neighbours = []

    this_height = heightmap[row][col]
    
    rows = len(heightmap)
    cols = len(heightmap[0])

    ok = [
        (row - 1, col),
        (row + 1, col),
        (row, col - 1),
        (row, col + 1),
        ]
    # Filter out illegal indices     
    ok = [(row, col) for row, col in ok if (row >= 0) and (row < rows) and (col >= 0) and (col < cols)]
    for row in range(rows):
        for col in range(cols):
            if (row, col) in ok:
                neighbours.append(heightmap[row][col])

    return all(True if this_height < height else False for height in neighbours)

def check_all_points(heightmap):
    rows = len(heightmap)
    cols = len(heightmap[0])

    heights = []

    for row in range(rows):
        for col in range(cols):
            if check_neighbours(row, col, heightmap):
                heights.append(heightmap[row][col])

    return heights


if __name__ == '__main__':
    # 1
    heightmap = load_input('day_09/input.txt')
    low_points = check_all_points(heightmap)
    print(sum(point + 1 for point in low_points))
