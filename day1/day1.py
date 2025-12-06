import re
from operator import sub, add

def part1(input):
    pos = 50
    pattern = re.compile(r"([LR])(\d+)")
    operator = {"L": sub, "R": add}
    positions = []

    with open(input, 'r') as f:
        for line in f:
            match = pattern.match(line)
            direction, clicks= match.groups()
            op = operator[direction]
            pos = op(pos, int(clicks)) % 100
            positions.append(pos)

    return positions.count(0)

def part2(input):
    pos = 50
    pattern = re.compile(r"([LR])(\d+)")
    operator = {"L": sub, "R": add}
    counter = 0

    with open(input, 'r') as f:
        for line in f:
            match = pattern.match(line)
            direction, clicks = match.groups()
            op = operator[direction]
            rotations, clicks = divmod(int(clicks), 100)
            counter += rotations
            new_pos = op(pos, int(clicks))
            if pos != 0 and not (0 < new_pos < 100):
                counter += 1
            pos = new_pos % 100
    
    return counter