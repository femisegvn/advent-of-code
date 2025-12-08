
def part1(input):
    with open(input) as f:
        rows = [row.rstrip("\n") for row in f.readlines()]
    counter = 0

    for i, row in enumerate(rows):
        upper_row = None if i == 0 else rows[i - 1]
        lower_row = None if i == len(rows) - 1 else rows[i+1]
        
        for j, roll in enumerate(row):
            if not roll == '@':
                continue

            left = j - 1 if j != 0 else None
            right = j + 1 if j != len(row) - 1 else None

            left_roll = row[left] if left is not None else ''
            right_roll = row[right] if right is not None else ''
            
            adjacent = left_roll + right_roll

            if left is None:
                left = j
            if right is None:
                right = j

            if upper_row != None:
                adjacent += upper_row[left:right+1]
            if lower_row != None:
                adjacent += lower_row[left:right+1]
            
            if adjacent.count('@') < 4:
                counter += 1
    
    return counter

def part2(input):
    '''
    Approach:
    1. iterate through each element in the grid, checking if it is a roll or not
    2. if it is a roll, if < 4 rolls are adjacent, remove.
    3. Produce a new grid containing xs where rolls have been removed
    4. Repeat steps 1 - 3 on the new grid.
    5. When counter is no longer increasing, stop.
    '''

    global counter

    counter = 0
    with open(input) as f:
        rows = [row.rstrip("\n") for row in f.readlines()]

    def remove_rolls(rows):
        global counter
        counter_checkpoint = counter
        new_grid = []
        for i, row in enumerate(rows):
            new_row = ''

            upper_row = None if i == 0 else rows[i - 1]
            lower_row = None if i == len(rows) - 1 else rows[i+1]
            
            for j, roll in enumerate(row):
                if not roll == '@':
                    new_row+= '.'
                    continue

                left = j - 1 if j != 0 else None
                right = j + 1 if j != len(row) - 1 else None

                left_roll = row[left] if left is not None else ''
                right_roll = row[right] if right is not None else ''
                
                adjacent = left_roll + right_roll

                if left is None:
                    left = j
                if right is None:
                    right = j

                if upper_row != None:
                    adjacent += upper_row[left:right+1]
                if lower_row != None:
                    adjacent += lower_row[left:right+1]
                
                if adjacent.count('@') < 4:
                    counter += 1
                    new_row+= 'x'
                else:
                    new_row+= '@'

            new_grid.append(new_row)
        if counter != counter_checkpoint:
            remove_rolls(new_grid)
    
    remove_rolls(rows)
    
    return counter