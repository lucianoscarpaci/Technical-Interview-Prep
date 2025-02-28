# Two list observed_species and priority_species are given.
# The elements of priority_species are distinct and all elements in
# priority species are also in observed_species.
# Write a function prioritize_observations() that sorts the elements
# of observed_species such that the relative order of the items in
# observed_species matches the order of the items in priority_species.
# Species that do not appear in the priority_species should be placed
# at the end of the observed species in ascending order. 
def prioritize_observations(observed_species, priority_species):
    # Create a dictionary to store the priority of each species
    priority_dict = {species: i for i, species in enumerate(priority_species)}
    
    # Sort the observed_species based on the priority, and then by natural order for non-priority species
    observed_species.sort(key=lambda species: (priority_dict.get(species, float('inf')), species))
    
    return observed_species

observed_species1 = ["🐯", "🦁", "🦌", "🦁", "🐯", "🐘", "🐍", "🦑", "🐻", "🐯", "🐼"]
priority_species1 = ["🐯", "🦌", "🐘", "🦁"]

observed_species2 = ["bluejay", "sparrow", "cardinal", "robin", "crow"]
priority_species2 = ["cardinal", "sparrow", "bluejay"]
print(prioritize_observations(observed_species1, priority_species1))
print(prioritize_observations(observed_species2, priority_species2))