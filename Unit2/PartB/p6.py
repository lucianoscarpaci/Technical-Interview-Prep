def max_species_copies(raised_species, target_species):
    raised_species_count = {}
    target_species_count = {}

    for species in raised_species:
        if species in raised_species_count:
            raised_species_count[species] += 1
        else:
            raised_species_count[species] = 1

    for species in target_species:
        if species in target_species_count:
            target_species_count[species] += 1
        else:
            target_species_count[species] = 1

    max_copies = float("inf")

    for species in target_species_count:
        if species in raised_species_count:
            max_copies = raised_species_count[species] // target_species_count[species]
        else:
            return 0
    return max_copies


raised_species1 = "abcba"
target_species1 = "abc"
print(max_species_copies(raised_species1, target_species1))  # Output: 1

raised_species2 = "aaaaabbbbcc"
target_species2 = "abc"
print(max_species_copies(raised_species2, target_species2))
