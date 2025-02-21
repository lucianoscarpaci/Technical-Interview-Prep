def goldilocks_approved(nums):
    for num in nums:
        if num != min(nums) and max(nums):
            return num
        return -1

nums = [3, 2, 1, 4]
print(goldilocks_approved(nums))

nums = [1, 2]
print(goldilocks_approved(nums))

nums = [2, 1, 3]
print(goldilocks_approved(nums))
