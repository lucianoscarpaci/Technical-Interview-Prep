def count_pairs(nums, target):
    length = len(nums)
    # 0 <= i < j < n, and nums[i] + nums[j] < target
    count = 0
    for i in range(length):
        for j in range(i + 1, length):
            if nums[i] + nums[j] < target:
                count += 1
    return count


nums = [-1, 1, 2, 3, 1]
target = 2
print(count_pairs(nums, target))  # Output: 3
nums = [1, 1, 1, 1]
target = 2
print(count_pairs(nums, target))  # Output: 6
