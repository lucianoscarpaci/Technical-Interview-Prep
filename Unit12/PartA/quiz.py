def pow(x, n):
    if n == 0:
        return 1
    elif n < 0:
        x = 1 / x
        n = -n
    result = 1
    while n > 0:
        if n % 2 == 1:
            result *= x
        x *= x
        n //= 2
    return result

print(f"{pow(2, 10):.2f}") # Output: 1024.00
print(f"{pow(2.1, 3):.2f}") # Output: 9.26
print(f"{pow(2, -2):.2f}") # Output: 0.25
