def distance(strand_a, strand_b):
    if len(strand_a) != len(strand_b):
        raise ValueError("Unequal Strings")

    return sum(1 for a, b in zip(strand_a, strand_b) if a != b)

#Time Complexity is O(n) - Linear
