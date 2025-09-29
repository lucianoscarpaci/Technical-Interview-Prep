"""
Imagine you are working on a wildlife conservation database. Write a function named most_endangered() that returns the species with the highest conservation priority based on its population.

The function should take in a list of dictionaries named species_list as a parameter. Each dictionary represents data associated with a species, including its name, habitat, and wild population. The function should return the name of the species with the lowest population.

If there are multiple species with the lowest population, return the species with the lowest index.
"""

"""
Need to access the name key that has the lowest population key
Find lowest population and access the name Vaquita.
I want to use for loop d[key].get().lowest()
"""

"""
def most_endangered(species_list):
    lowest_val_species = min(species_list, key=lambda x: x["population"])
    return lowest_val_species["name"]


species_list = [
    {"name": "Amur Leopard", "habitat": "Temperate forests", "population": 84},
    {"name": "Javan Rhino", "habitat": "Tropical forests", "population": 72},
    {"name": "Vaquita", "habitat": "Marine", "population": 10},
]

print(most_endangered(species_list))
# Expected output: "Vaquita"
"""
"""
As part of conservation efforts, certain species are considered endangered and are represented by the string endangered_species. Each character in this string denotes a different endangered species. You also have a record of all observed species in a particular region, represented by the string observed_species. Each character in observed_species denotes a species observed in the region.

Your task is to determine how many instances of the observed species are also considered endangered.

Note: Species are case-sensitive, so "a" is considered a different species from "A".

Write a function to count the number of endangered species observed.
"""
"""
Input: endangered_species = "aA", observed_species = "aAAbbbb"
Output: 3
Constraints: 1 <= len(endangered_species), len(observed_species) <= 1000
Explanation: The endangered species are 'a' and 'A'. In the observed_species string, there are 3 instances of these endangered species: one 'a' and two 'A's.
"""
"""
def count_endangered_species(endangered_species, observed_species):
    endangered_set = set(endangered_species)
    count = 0
    for species in observed_species:
        if species in endangered_set:
            count += 1
    return count
"""


def count_endangered_species(endangered_species, observed_species):
    count = 0
    for species in observed_species:
        if species in endangered_species:
            count += 1
    return count


endangered_species1 = "aA"
observed_species1 = "aAAbbbb"

endangered_species2 = "z"
observed_species2 = "ZZ"

print(count_endangered_species(endangered_species1, observed_species1))
print(count_endangered_species(endangered_species2, observed_species2))
