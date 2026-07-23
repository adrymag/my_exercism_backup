def distance(strand_a, strand_b):
    # When the sequences being passed are not the same length.
    l = len(strand_a)

    if l != len(strand_b):
        raise ValueError("Strands must be of equal length.")

    dist = 0

    for pos in range(l):
        if strand_a[pos] != strand_b[pos]:
            dist = dist + 1

    return dist