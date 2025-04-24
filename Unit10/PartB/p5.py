def calculate_cost(flights, start, dest):
    visited = set()

    def dfs(current, total_cost):
        if current == dest:
            return total_cost
        
        # Mark the current airport as visited
        visited.add(current)

        for neighbor, cost in flights.get(current, []):
            if neighbor not in visited:
                result = dfs(neighbor, total_cost + cost)
                if result != -1:
                    return result
        # Unmark the current airport before backtracking
        visited.remove(current)
        # If no valid path is found, return -1
        return -1
    # Start DFS from the start airport
    return dfs(start, 0)

flights = {
    'LAX': [('SFO', 50)],
    'SFO': [('LAX', 50), ('ORD', 100), ('ERW', 210)],
    'ERW': [('SFO', 210), ('ORD', 100)],
    'ORD': [('ERW', 300), ('SFO', 100), ('MIA', 400)],
    'MIA': [('ORD', 400)]
}

print(calculate_cost(flights, 'LAX', 'MIA'))
# Explain Lax -> SFO = 50 -> SFO -> ORD = 100 -> ORD -> MIA = 400
# Total cost = 50 + 100 + 400 = 550
