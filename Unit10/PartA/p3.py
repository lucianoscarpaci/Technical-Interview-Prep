def get_direct_flights(flights, source):
    direct_flights = []
    n = len(flights)

    for destination in range(n):
        if flights[source][destination] == 1:
            direct_flights.append(destination)
    return direct_flights

flights = [
            [0, 1, 1, 0],
            [1, 0, 0, 0],
            [1, 1, 0, 1],
            [0, 0, 0, 0]]

print(get_direct_flights(flights, 2))
print(get_direct_flights(flights, 3))
print(get_direct_flights(flights, 1))
