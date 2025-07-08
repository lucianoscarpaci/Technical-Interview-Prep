def can_split_coffee(coffee, n):
    total_volume = sum(coffee)

    if total_volume % n != 0:
        return False

    target = total_volume // n
    return can_divide(coffee, n, target, 0)


def can_divide(coffee, n, target, current_sum):
    if n == 0:
        return True
    if current_sum == target:
        return can_divide(coffee, n - 1, target, 0)
    if not coffee:
        return False

    # Try including the first coffee cup
    included = can_divide(coffee[1:], n, target, current_sum + coffee[0])
    # Try excluding the first coffee cup
    excluded = can_divide(coffee[1:], n, target, current_sum)

    return included or excluded


print(can_split_coffee([4, 4, 8], 2))
print(can_split_coffee([5, 10, 15], 4))
