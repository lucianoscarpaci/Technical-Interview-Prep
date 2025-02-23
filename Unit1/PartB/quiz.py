def sort_by_parity(nums):
    evens = []
    odds = []
    for num in nums:
        if num % 2 == 0:
            evens.append(num)
        if num % 2 == 1: 
            odds.append(num)
    return evens + odds

nums = [3, 1, 2, 4]
print(sort_by_parity(nums))