def goldilocks_approved(nums):
    """
    Write a function goldilocks_approved() that takes in the
    list of
    distinct positive integers nums and returns
    any number from the list that is neither
    the minimum nor the maximum value in the array, or -1
    """
    for idx in nums:
        if idx != min(nums) and max(nums):
            return idx
        else:
            return -1


nums = [3, 2, 1, 4]
print(goldilocks_approved(nums))

nums = [1, 2]
print(goldilocks_approved(nums))

nums = [2, 1, 3]
print(goldilocks_approved(nums))
