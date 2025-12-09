
def part1(input):
    with open(input) as f:
        lines = [line.strip('\n') for line in f.readlines()]

    for i, line in enumerate(lines):
        if line == '':
            split_index = i
        
    id_ranges, check_ids = lines[:split_index], lines[split_index+1:]

    check_ranges = []
    for rnge in id_ranges:
        start_id, end_id = [int(id) for id in rnge.split('-')]
        check_ranges.append((start_id, end_id))

    fresh_ids = []
    for id in check_ids:
        for check in check_ranges:
            if int(id) in range(check[0], check[1]+1):
                fresh_ids.append(id)
                break
    return len(fresh_ids)

def part2(input):
    """
    Approach
    1. Iterate through the sorted ranges
    2. For each range, determine the number of fresh IDs, `start_id - end_id + 1`
    3. Add the range to a `searched` bank.

    2 Cases:
    - `start_id` falls within an existing range
        solution: raise `start_id` to start above the existing range
    - `start_id` and `end_id` fall within an existing range
        solution: ignore -- it adds no more information
    """
    with open(input) as f:
        lines = [line.strip('\n') for line in f.readlines()]
    
    for i, line in enumerate(lines):
        if line == '':
            split_index = i

    id_ranges = []
    for id_range in lines[:split_index]:
        start_id, end_id = [int(id) for id in id_range.split('-')]
        id_ranges.append((start_id, end_id))

    searched_ranges = []

    n = 0

    for id_range in sorted(id_ranges):
        start_id, end_id = id_range

        for searched in searched_ranges:
            if start_id <= searched[1]:
                start_id = searched[1] + 1

            if start_id >= searched[0] and end_id <= searched[1]:
                start_id, end_id = 0, 0

        if start_id != 0 and end_id != 0:
            n += end_id - start_id + 1
            searched_ranges.append((start_id, end_id))
    
    return n