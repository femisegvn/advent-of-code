
def part1(input):
    with open(input) as f:
        lines = [line.strip("\n") for line in f.readlines()]

    for i, s in enumerate(lines[0]):
        if s == "S":
            beam = {i}
            break
    
    counter = 0
    
    for i, line in enumerate(lines):
        line = list(line)
        
        for b in sorted(beam):
            if b >= len(line) or b < 0:
                continue

            if line[b] == '.':
                line[b] = '|'
            elif line[b] == '^':
                line[b+1] = '|'
                line[b-1] = '|'

                counter+=1

                beam.remove(b)
                beam.add(b-1)
                beam.add(b+1)

        line = ''.join(line)
        lines[i] = line
        print(line)

    return counter

def part2(input):
    ...