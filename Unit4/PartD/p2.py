def is_sorted_rotated(nums):
    length = len(nums)
    count = 0
    # if nums[i] == nums[(i+1) % length], we do not count it
    for i in range(length):
        if nums[i] == nums[(i + 1) % length]:
            return True
        if nums[i] > nums[(i + 1) % length]:
            count += 1
            if count > 1:
                return False
    return True


nums = [3, 4, 5, 1, 2]
print(is_sorted_rotated(nums))
# Output: True
nums = [2, 1, 3, 4]
print(is_sorted_rotated(nums))
# Output: False
nums = [1, 2, 3]
print(is_sorted_rotated(nums))
# Output: True
nums = [4, 2, 3]
print(is_sorted_rotated(nums))
# Output: True
