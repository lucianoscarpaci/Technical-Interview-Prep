def count_suits_iterative(suits):
    unique_suits = set(suits)
    return len(unique_suits)


def count_suits_recursive(suits):
    if not suits:
        return 0
    start_indx = suits[0]
    unique_suits = count_suits_recursive(suits[1:])
    if start_indx in suits[1:]:
        return unique_suits
    else:
        return 1 + unique_suits


print(count_suits_iterative(["Mark I", "Mark I", "Mark III"]))
print(count_suits_recursive(["Mark I", "Mark I", "Mark III"]))
