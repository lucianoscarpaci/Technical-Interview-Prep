# Find the peak element.
# Given a 0-indexed integer array nums, find a peak element, and return its index.
# Imagine nums[-1] = nums[n] = -∞.
# The element is always considered to be strictly greater than its neighbors.
def find_peak_element(nums):
    left, right = 0, len(nums) - 1

    while left < right:
        mid = (left + right) // 2

        if nums[mid] > nums[mid + 1]:
            right = mid
        else:
            left = mid + 1

    return left


nums = [1, 2, 3, 1]
print(find_peak_element(nums))  # Output: 2
nums = [1, 2, 1, 3, 5, 6, 4]
print(find_peak_element(nums))  # Output: 5
