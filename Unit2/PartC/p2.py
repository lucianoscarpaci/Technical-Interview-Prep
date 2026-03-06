# Understand: Find unique occourences of souvenirs in a list
# and count them. For example, hat, hat, keychain, keychain, keychain, postcard would return 2 for hat, 3 for keychain and 1 for postcard.
# Match: Hashmap or dictionary to store the souvenir as key and count as value.
# Plan: Count all the souviners in a dictionary, iterate through souveirs, count them, and store them in a dictionary. Put them in a set and compare them in a length of set.
# Implement: Use dictionary to count the souveirs, then use set to find unique count of the souviners.
# Review: Inputs array of souv
# Evaluate:


def unique_souvenir_counts(souvenirs):
    count_souviners = {}
    for souvenir in souvenirs:
        if souvenir in count_souviners:
            count_souviners[souvenir] += 1
        else:
            count_souviners[souvenir] = 1

    visited_souviners = set(count_souviners.values())
    return len(visited_souviners) == len(count_souviners)


souvenirs1 = ["keychain", "hat", "hat", "keychain", "keychain", "postcard"]
souvenirs2 = ["postcard", "postcard", "postcard", "postcard"]
souvenirs3 = ["keychain", "magnet", "hat", "candy", "postcard", "stuffed bear"]

print(unique_souvenir_counts(souvenirs1))
print(unique_souvenir_counts(souvenirs2))
print(unique_souvenir_counts(souvenirs3))
