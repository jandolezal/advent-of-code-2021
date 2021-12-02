"""
Day 1: Sonar Sweep
https://adventofcode.com/2021/day/1
"""


def get_increase_count(data):
    count = 0
    for i in range(len(data) - 1):
        if data[i+1] > data[i]:
            count += 1
    return count


# def get_decrease_count(data):
#     return sum(True if data[i+1] > data[i] else False for i in range(len(data) - 1))


def get_window_increase_count(data, window_size=3):
    count = 0
    for i in range(len(data) - window_size):
        first_sum = sum(data[i:i+window_size])
        second_sum = sum(data[i+1:i+1+window_size])
        # print(first_sum, second_sum)
        if first_sum < second_sum:
            count += 1
    return count


if __name__ == '__main__':
    with open('day_01/input.txt') as f:
        data = [int(word.strip()) for word in f.readlines()]

    #1
    print(get_increase_count(data))

    #2
    print(get_window_increase_count(data))

    assert get_window_increase_count(data, 1) == get_increase_count(data)
