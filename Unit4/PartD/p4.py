def process_numbers(nums, threshold):
    stack = []
    for num in nums:
        if num < threshold:
            stack.append(num)
        elif num <= 10 and stack:
            stack.pop()
    return stack


print(process_numbers([1, 2, 3, 11, 4, 5, 6], 8))  # Output: [1, 2]
