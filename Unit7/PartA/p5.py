def power_of_four(n):
    # This function calculates 4 raised to the power of n using recursion.
    if n == 0:
        return 1
    elif n > 0:
        return 4 * power_of_four(n - 1)
    else:
        return (1 / 4) * power_of_four(n + 1)


print(power_of_four(2))
print(power_of_four(-2))
