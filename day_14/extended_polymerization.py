"""
Day 14: Extended Polymerization
https://adventofcode.com/2021/day/14
"""

from array import array
import collections
import itertools


def load_input(filepath='day_14/test_input.txt'):
    with open(filepath) as f:
        lines = [line.strip() for line in f.readlines()]
        template = array('b', (ord(char)  for char in lines[0]))
        rules = {(ord(k[0]), ord(k[1])) : ord(v) for k, v in [line.split(' -> ') for line in lines[2:]]}
        return template, rules


def update_template(template, rules):
    # https://stackoverflow.com/questions/5434891/iterate-a-list-as-pair-current-next-in-python
    # https://stackoverflow.com/questions/61126284/zipped-python-generators-with-2nd-one-being-shorter-how-to-retrieve-element-tha
    a, b = itertools.tee(template)
    next(b, None)

    elements = array('b', [])

    for pair in zip(a, b):
        elements.append(rules[pair])
    
    combined = array('b', (item for subtuple in zip(template, elements) for item in subtuple))
    combined.append(template[-1]) # append last original element which is missing

    return combined

def make_steps(template, rules, steps=10, verbose=False):
    for step in range(steps):
        template = update_template(template, rules)
        if verbose:
            print(f'Finished step {step}') # with: {"".join(chr(char) for char in template)}
    return template


if __name__ == '__main__':
    # 1
    template, rules = load_input('day_14/input.txt')

    final_template = make_steps(template, rules, steps=10, verbose=True)

    c = collections.Counter(final_template)
    most_common = c.most_common()
    most = most_common[0][1]
    least = most_common[-1][1]
    
    print(most, least, most - least)
