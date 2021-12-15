"""
Day 14: Extended Polymerization
https://adventofcode.com/2021/day/14
"""

import collections
import itertools


def make_counter(template):
    # https://stackoverflow.com/questions/5434891/iterate-a-list-as-pair-current-next-in-python
    # https://stackoverflow.com/questions/61126284/zipped-python-generators-with-2nd-one-being-shorter-how-to-retrieve-element-tha
    a, b = itertools.tee(template)
    next(b, None)
    return collections.Counter(list(zip(a, b)))


def load_input(filepath='day_14/test_input.txt'):
    with open(filepath) as f:
        lines = [line.strip() for line in f.readlines()]
        template = make_counter(lines[0])
        rules = {(k[0], k[1]) : v for k, v in [line.split(' -> ') for line in lines[2:]]}
        return template, rules


def update_counter(template, rules):
    for k, v in collections.Counter(template).items():
        first, second = k
        new_element = rules[k]
        # Add count of new pairs
        template[(first, new_element)] += v
        template[(new_element, second)] += v
        # Former pairs are no more
        template[k] -= v


def make_steps(template, rules, steps=10):
    for step in range(steps):
        update_counter(template, rules)


def from_pairs_to_individual_letters(template):
    first = collections.defaultdict(int)
    second = collections.defaultdict(int)
    middle = collections.defaultdict(int)
    individual = collections.defaultdict(int)

    # Make two dictionaries to count separately first and second letters
    # from pairs count
    for k, v in template.items():
        first[k[0]] += v
        second[k[1]] += v

    # Identify count of letters which overlap: letter is first and second in pair
    for item in {**first, **second}:
        middle[item] = min(first[item], second[item])
    
    # Make new dictionary finally with counts for individual letters
    for k, v in template.items():
        individual[k[0]] += v
        individual[k[1]] += v

    # Adjust letter count to reflect situation that letters were duplicated in former pair key
    for k in individual:
        individual[k] -= middle[k]

    return individual


if __name__ == '__main__':

    # 1 & 2
    template, rules = load_input('day_14/input.txt')
    
    make_steps(template, rules, steps=40)
    
    # Convert pairs counts to individual letters counts
    individual = from_pairs_to_individual_letters(template)

    # Final calculation
    c = collections.Counter(individual)
    most_common = c.most_common()
    most = most_common[0][1]
    least = most_common[-1][1]
    
    print(most, least, most - least)
