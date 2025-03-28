def count_deposits(resources):
    if not resources:
        return 0
    elif resources[0] == "V":
        return 1 + count_deposits(resources[1:])
    else:
        return count_deposits(resources[1:])


print(count_deposits("VVVVV"))
print(count_deposits("VXVYGA"))
