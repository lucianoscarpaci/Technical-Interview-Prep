def fibonacci_growth(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_growth(n - 1) + fibonacci_growth(n - 2)


print(fibonacci_growth(5))
print(fibonacci_growth(8))
