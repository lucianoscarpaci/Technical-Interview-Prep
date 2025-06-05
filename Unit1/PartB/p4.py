def sum_of_digits(num):
    total_sum = 0
    while num > 0:
        total_sum += num % 10
        num //= 10
    return total_sum


num = 423
print(sum_of_digits(num))

num = 4
print(sum_of_digits(num))
