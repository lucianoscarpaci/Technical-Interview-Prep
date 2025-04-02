def is_profitable(excusion_counts):
    n = len(excusion_counts)
    # Binary search to find the special x
    left, right = 0, n - 1
    while left <= right:
        mid = left + (right + left) // 2
        # print(mid) # 0
        x = n - mid
        # print(x) # 2
        if excusion_counts[mid] >= x:
            if mid == 0 or excusion_counts[mid - 1] < x:
                return x  # 2
            right = mid - 1
        else:
            left = mid + 1
    return -1


print(is_profitable([3, 5]))
