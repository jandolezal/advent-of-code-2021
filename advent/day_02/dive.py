"""
Day 2: Dive!
https://adventofcode.com/2021/day/2
"""

from dataclasses import dataclass

@dataclass
class Submarine:

    horizontal: int = 0
    depth: int = 0
    aim: int = 0

    def dive(self, instructions):
        for direction, value in instructions:
            if direction == 'forward':
                self.horizontal += value
                self.depth += (self.aim * value)
            elif direction == 'down':
                self.aim += value
            elif direction == 'up':
                self.aim -= value
            else:
                print('Wrong line of instructions.')
    
    def multiply(self):
        return self.horizontal * self.depth


def load_input(filepath):
    with open(filepath) as f:
        input = [line.strip().split(' ') for line in f.readlines()]
        input = [(direction, int(value)) for (direction, value) in input]
        return input


def dive(instructions):
    pass


if __name__ == '__main__':
    data = load_input('advent/day_02/input.txt')

    #2
    sub = Submarine()
    sub.dive(data)
    print(sub)
    print(sub.multiply())
 