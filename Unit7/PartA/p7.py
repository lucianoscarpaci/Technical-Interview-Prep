def count_deposits(resources):
    if not resources:
        return 0

    count = 0
    for char in resources:
        if char == "V":
            count += 1
    return count


print(count_deposits("VVVVV"))
print(count_deposits("VXVYGA"))
