def bidirectional_flights(flights):
    n = len(flights)

    for i in range(n):
        for j in flights[i]:
            if i not in flights[j]:
                return False
    return True

flights1 = [[1, 2], [0], [0, 3], [2]]
flights2 = [[1, 2], [], [0], [2]]

print(bidirectional_flights(flights1))
print(bidirectional_flights(flights2))
# Expected output:
# True
# False