from collections import defaultdict


def grouped_anagrams(strs):
    anagrams = defaultdict(list)

    for s in strs:
        # Sort the string to create a key
        key = "".join(sorted(s))
        anagrams[key].append(s)

    # Return the grouped anagrams as a list of lists
    return list(anagrams.values())


strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(
    grouped_anagrams(strs)
)  # Output: [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]
strs = [""]
print(grouped_anagrams(strs))  # Output: [[""]]
strs = ["a"]
print(grouped_anagrams(strs))  # Output: [["a"]]
