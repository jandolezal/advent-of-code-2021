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
        dist, current_vertex  = pq.get()
        visited.add(current_vertex)

        for nrow, ncol in get_neighbours(current_vertex[0], current_vertex[1], rows, cols):
            if (nrow, ncol) not in visited:
                cost = dist + data[nrow][ncol]
                if cost < costs[nrow][ncol]:
                    costs[nrow][ncol] = cost
                    pq.put((cost, (nrow, ncol)))
    return costs


if __name__ == '__main__':
    # 1
    data = load_input('day_15/input.txt')
    costs = dijkstra(data)
    print(costs[-1][-1])
