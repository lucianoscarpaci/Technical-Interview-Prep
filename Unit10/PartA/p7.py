from collections import deque

def get_all_destinations(flights, start):
    visited = set()
    result = []

    def dfs(airport):
        visited.add(airport)
        result.append(airport)

        for neighbor in flights.get(airport, []):
            if neighbor not in visited:
                dfs(neighbor)
    dfs(start)
    return result

flights = {
    "Tokyo": ["Sydney"],
    "Sydney": ["Tokyo", "Beijing"],
    "Beijing": ["Mexico City", "Helsinki"],
    "Helsinki": ["Cairo", "New York"],
    "Cairo": ["Helsinki", "Reykjavik"],
    "Reykjavik": ["Cairo", "New York"],
    "Mexico City": ["Sydney"]   
}

print(get_all_destinations(flights, "Helsinki"))
