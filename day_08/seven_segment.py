"""
Day 8: Seven Segment Search
https://adventofcode.com/2021/day/8
"""

from typing import List


def load_input(filepath) -> List[List[str]]:
    with open(filepath) as f:
        lines =  [line.split('|') for line in f.readlines()]
        data = []
        for line in lines:
            data.append([part.strip().split(' ') for part in line ])
        return data


def count_easy_digits(data):
    count = 0
    for _, output in data:
        for letters in output:
            if len(letters) in [2, 3, 4, 7]:
                count += 1
    return count


if __name__ == '__main__':
    # 1
    data = load_input('day_08/input.txt')
    easy_count = count_easy_digits(data)
    print(easy_count)

