from collections import deque

def first_uniq_char(s):
    char_count = {}
    char_index = {}
    for i, char in enumerate(s):
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
            char_index[char] = i

    first_unique_index = float('inf')
    for char, count in char_count.items():
        if count == 1:
            first_unique_index = min(first_unique_index, char_index[char])

    return first_unique_index if first_unique_index != float('inf') else -1