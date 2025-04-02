def count_checked_in_passengers(rooms):
    n = len(rooms)
    left, right = 0, n - 1
    first_one_index = n

    while left <= right:
        mid = left + (right - left) // 2
        # print(mid) 3
        if rooms[mid] == 1:
            first_one_index = mid
            right = mid - 1
        else:
            left = mid + 1
    return n - first_one_index


rooms1 = [0, 0, 0, 1, 1, 1, 1]
rooms2 = [0, 0, 0, 0, 0, 1]
rooms3 = [0, 0, 0, 0, 0, 0]

print(count_checked_in_passengers(rooms1))
print(count_checked_in_passengers(rooms2))
print(count_checked_in_passengers(rooms3))
