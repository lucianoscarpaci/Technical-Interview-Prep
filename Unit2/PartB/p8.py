def num_equiv_species_pairs(species_pairs):
    count = {}
    for pair in species_pairs:
        normalized_pair = tuple(sorted(pair))
        if normalized_pair in count:
            count[normalized_pair] += 1
        else:
            count[normalized_pair] = 1

    pairs = 0
    for c in count.values():
        pairs += c * (c - 1) // 2
    return pairs


species_pairs1 = [[1, 2], [2, 1], [3, 4], [5, 6]]
species_pairs2 = [[1, 2], [1, 2], [1, 1], [1, 2], [2, 2]]

print(num_equiv_species_pairs(species_pairs1))
print(num_equiv_species_pairs(species_pairs2))
