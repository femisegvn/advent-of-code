def part1(input):
    sum = 0
    with open(input) as f:
        id_ranges = f.readlines()[0].split(",")
    for id_range in id_ranges:
        id1, id2 = id_range.split("-")
        for idx in range(int(id1), int(id2)+1):
            id = str(idx)
            id_len = len(id)
            if id_len % 2 == 0:
                midpoint = int(id_len/2)
                parts = id[:midpoint], id[midpoint:]
                if parts[0] == parts[1]:
                    sum+= idx

    return sum

def part2(input):
    """
    Approach: 
    1. Determine the length of ID
    2. Determine all of the factors of `len(id)`
    3. For each factor, `m`, take the first `m` digits of ID
    4. Check if ID is the same as `m` digits repeated `len(id)/m` times
    """

    def factors(length):
        fctrs = []
        for m in range(1, (length//2)+1):
            n, r = divmod(length, m)
            if r == 0:
                fctrs.append((m, n))
        return fctrs

    sum = 0
    with open(input) as f:
        id_ranges = f.readlines()[0].split(",")
    for id_range in id_ranges:
        id1, id2 = id_range.split("-")
        for idx in range(int(id1), int(id2)+1):
            id = str(idx)
            id_len = len(id)
            id_factors = factors(id_len)

            for m, n in id_factors:
                c = id[:m]
                if id == n*c:
                    sum+=idx
                    break
    return sum