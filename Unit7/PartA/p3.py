def count_suits_iterative(suits):
    unique_suits = set()
    for suit in suits:
        unique_suits.add(suit)
    return len(unique_suits)


def count_suits_recursive(suits):
    if not suits:
        return 0
    first = suits[0]
    rest_unique_count = count_suits_recursive(suits[1:])
    if first in suits[1:]:
        return rest_unique_count
    else:
        return 1 + rest_unique_count


print(count_suits_iterative(["Mark I", "Mark II", "Mark III"]))
print(count_suits_recursive(["Mark I", "Mark I", "Mark III"]))
