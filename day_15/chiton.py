"""
Day 15: Chiton
https://adventofcode.com/2021/day/15
"""

from queue import PriorityQueue


def load_input(filepath='day_15/test_input.txt'):
    with open(filepath) as f:
        return [[int(num) for num in line.strip()] for line in f.readlines()]


# Inspiration: https://github.com/messa/aoc/blob/main/2021/15.py
def get_neighbours(row, col, rows, cols):
    if row > 0:
        yield (row - 1, col)
    if row < rows - 1:
        yield (row + 1, col)
    if col > 0:
        yield (row, col - 1)
    if col < cols - 1:
        yield (row, col + 1)


# Explanation which worked for me: https://stackabuse.com/dijkstras-algorithm-in-python/
def dijkstra(data):
    rows = len(data)
    cols = len(data[0])

    costs = [[float('inf') for col in range(cols)] for row in range(rows)]
    costs[0][0] = 0

    visited = set()

    pq = PriorityQueue()
    pq.put((0, (0, 0)))

    while not pq.empty():
        current_cost, (current_row, current_col)  = pq.get()
        visited.add((current_row, current_col))

        for neighbour_row, neighbour_col in get_neighbours(current_row, current_col, rows, cols):
            if (neighbour_row, neighbour_col) not in visited:
                cost = current_cost + data[neighbour_row][neighbour_col]
                if cost < costs[neighbour_row][neighbour_col]:
                    costs[neighbour_row][neighbour_col] = cost
                    pq.put((cost, (neighbour_row, neighbour_col)))
    return costs


if __name__ == '__main__':
    # 1
    data = load_input('day_15/input.txt')
    costs = dijkstra(data)
    print(costs[-1][-1])
