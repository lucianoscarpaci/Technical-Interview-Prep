def find_cruise_length(cruise_lengths, vacation_length):
    # binary search find the midpoint
    # if midpoint is less than vacation_length, search right
    # if midpoint is more than vacation_length, search left
    # if midpoint is equal to vacation_length, return vacation_length
    left = 0
    right = len(cruise_lengths) - 1
    while left <= right:
        mid = (left + right) // 2
        if cruise_lengths[mid] < vacation_length:
            left = mid + 1
        elif cruise_lengths[mid] > vacation_length:
            right = mid - 1
        else:
            return True
    return False


print(find_cruise_length([9, 10, 11, 12, 13, 14, 15], 13))
print(find_cruise_length([8, 9, 12, 13, 13, 14, 15], 11))
