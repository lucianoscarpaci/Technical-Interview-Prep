# Binary search to find subarray sum
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    sum = left + right
    if sum < target:
        return 0
    while left <= right:
        mid = (left + right) // 2  # Corrected to use integer division
        # mid = 1
        if arr[mid] < target:
            return mid + 1
        else:
            return mid - 1


arr = [1, 1, 1]
target = 2
print(binary_search(arr, target))  # Output: 2
arr = [1, 2, 3]
target = 7
print(binary_search(arr, target))  # Output: 0
