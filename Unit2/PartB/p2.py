# Species in the endangered_species list are considered endangered.
# All observed species in a particular region are represented by observed species.
# The goal is to determine how many instances of the species are also endangered.
# Use the set data type to solve this problem.
# intersection is elements that belong to both sets
# Example: set1 & set2 {'a', 'A'}
# Now to solve it return how many occurances
# of the endangered species are also observed species.
# Example: count_endangered_species("aA", "aAAbbbb") -> 2
# count_endangered_species("z", "ZZ") -> 0
# count_endangered_species("ff", "ffFFFFF") -> 2
def count_endangered_species(endangered_species, observed_species):
    endangered_species = set(endangered_species)
    observed_species = set(observed_species)
    return len(endangered_species & observed_species)
endangered_species1 = "aA"
observed_species1 = "aAAbbbb"

endangered_species2 = "z"
observed_species2 = "ZZ"

print(count_endangered_species(endangered_species1, observed_species1)) 
print(count_endangered_species(endangered_species2, observed_species2)) 