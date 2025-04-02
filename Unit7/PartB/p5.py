def find_shallowest_point(arr):
    def find_min_in_subarray(left, right):
        if left == right:
            return arr[left]  # None

        # Find the midpoint of the current subarray
        mid = (right + left) // 2
        # Recursively find the minimum in the left and right subarrays
        left_min = find_min_in_subarray(left, mid)
        right_min = find_min_in_subarray(mid + 1, right)
        # return the smaller of the two minimums
        return min(left_min, right_min)

    return find_min_in_subarray(0, len(arr) - 1)


print(find_shallowest_point([5, 7, 2, 8, 3]))
print(find_shallowest_point([12, 15, 10, 21]))
