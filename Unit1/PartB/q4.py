def count_digits(n):
    count = 0
    while n > 0:
        count += 1
        n = n // 10
        if n == 0:
            count = 1
    print(count)
    return count

n = 964
count_digits(n)
n = 0
count_digits(n)