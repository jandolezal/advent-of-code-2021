"""
Day 14: Extended Polymerization
https://adventofcode.com/2021/day/14
"""

import collections
import itertools


def load_input(filepath='day_14/test_input.txt'):
    with open(filepath) as f:
        lines = [line.strip() for line in f.readlines()]
        template = lines[0]
        rules = {tuple(k): v for k, v in [line.split(' -> ') for line in lines[2:]]}
        return template, rules


def update_template(template, rules):
    # https://stackoverflow.com/questions/5434891/iterate-a-list-as-pair-current-next-in-python
    updated_template = []
    a, b = itertools.tee(template)
    next(b, None)

    for pair in zip(a, b):
        element = rules[pair]
        new_elements = list(pair)
        new_elements.insert(1, element)
        updated_template.append(new_elements)

    # keep first group as is, all other groups strip of first element
    updated_template = [updated_template[0]] + [elements[1:] for elements in updated_template[1:]]

    # flatten and covert to string
    return ''.join(list(itertools.chain(*updated_template)))


def make_steps(template, rules, steps=10):
    for step in range(steps):
        template = update_template(template, rules)
    return template


if __name__ == '__main__':
    # 1
    template, rules = load_input('day_14/input.txt')
    final_template = make_steps(template, rules, steps=10)

    c = collections.Counter(final_template)
    most_common = c.most_common()
    most = most_common[0][1]
    least = most_common[-1][1]
    
    print(most, least, most - least)