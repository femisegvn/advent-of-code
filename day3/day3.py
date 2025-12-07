
def part1(input):
    with open(input) as f:
        banks = [line.strip('\n') for line in f.readlines()]
    
    def get_joltage(bank):
        jr1 = (0,'0')
        jr2 = '0'
        for i, cell in enumerate(bank[:-1]):
            jr = int(cell)
            if jr > int(jr1[1]):
                jr1 = (i, cell)
        for cell in bank[jr1[0]+1:]:
            jr = int(cell)
            if jr > int(jr2):
                jr2 = cell
        joltage = jr1[1] + jr2
        return int(joltage)
    
    sum = 0

    for bank in banks:
        joltage = get_joltage(bank)
        sum += joltage
    
    return sum

def part2(input):
    """
    Approach:
    1. Enumerate through each bank, up to the 11th last digit.
    2. Find the first instance of largest number in this sub array
    3. Store its index, `i`,  and its joltage rating, `jr`.
    4. Adjust the search space to enumerate from `i` to 10th digit
    5. Repeat steps 2 - 4 until all 12 digits obtained
    6. Repeat for each bank and find the sum of all banks
    """

    with open(input) as f:
        banks = [line.strip('\n') for line in f.readlines()]
    
    def get_joltage(bank):
        cells = []
        
        def get_cells():
            best = (0,'0')
            start = cells[-1][0] + 1 if len(cells) != 0 else 0
            end = len(bank) - (12 - len(cells))
            for i, cell in enumerate(bank):
                if not start <= i <= end:
                    continue
                jr = int(cell)
                if jr > int(best[1]):
                    best = (i, cell)
            cells.append(best)
            if len(cells) != 12:
                get_cells()
        
        get_cells()
        
        joltage = ''

        for cell in cells:
            joltage += cell[1]

        return int(joltage)
    
    sum = 0
    
    for bank in banks:
        joltage = get_joltage(bank)
        sum += joltage

    return sum
