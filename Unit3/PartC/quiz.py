

def two_sum(numbers, target):
    mapping = {}
    left, right = 0, len(numbers) - 1
    while left < right:
        current_sum = numbers[left] + numbers[right]
        if current_sum == target:
            return [left, right]
        elif current_sum < target:
            left += 1
        else:
            right -= 1
    return current_sum

numbers = [2, 7, 11, 15]
target = 9
print(two_sum(numbers, target))  # Expected output: [0, 1]