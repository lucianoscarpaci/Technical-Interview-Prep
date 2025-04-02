def find_cabin_index(cabins, preferred_deck):
    # write a recursive function find_cabin_index() that returns the index
    # of preferred_deck. If a cabin with the preferred_deck does not exist in cabins
    # return the index where it would be if it were added to the list to maintain
    # the sorted order.
    return search_cabin(cabins, preferred_deck, 0, len(cabins) - 1)


def search_cabin(cabins, preferred_deck, left, right):
    if left > right:
        return left
    mid = (left + right) // 2
    if cabins[mid] == preferred_deck:
        return mid
    elif preferred_deck < cabins[mid]:
        return search_cabin(cabins, preferred_deck, left, mid - 1)
    else:
        return search_cabin(cabins, preferred_deck, mid + 1, right)


print(find_cabin_index([1, 3, 5, 6], 5))
print(find_cabin_index([1, 3, 5, 6], 2))
print(find_cabin_index([1, 3, 5, 6], 7))
