# Two list observed_species and priority_species are given.
# The elements of priority_species are distinct and all elements in
# priority species are also in observed_species.
# Write a function prioritize_observations() that sorts the elements
# of observed_species such that the relative order of the items in
# observed_species matches the order of the items in priority_species.
# Species that do not appear in the priority_species should be placed
# at the end of the observed species in ascending order. 
def prioritize_observations(observed_species, priority_species):
    list1 = observed_species
    list2 = priority_species
    # if there are elements that are the same in both lists
    # remove them from list1
    for i in list2:
        if i in list1:
            list1.remove(i)
    # sort the remaining elements in list1
    list1.sort()
    # extend the sorted list1 with list2
    list1.extend(list2)
    # now group the same elements together in list1
    # and return the result
    list1 = [i for i in list1 if i in priority_species]
    list1.extend([i for i in list1 if i not in priority_species])

    return list1

observed_species1 = ["🐯", "🦁", "🦌", "🦁", "🐯", "🐘", "🐍", "🦑", "🐻", "🐯", "🐼"]
priority_species1 = ["🐯", "🦌", "🐘", "🦁"]  

print(prioritize_observations(observed_species1, priority_species1))