def get_all_destinations(flights, start):
    visited = set()
    result = []

    def dfs(destination):
        # Mark the current destination as visited
        visited.add(destination)
        result.append(destination)
        # Explore all reachable destinations that haven't been visited yet
        for location in flights.get(destination, []):  # Use get to handle missing keys
            if location not in visited:
                dfs(location)

    dfs(start)
    return visited


flights = {
    "Tokyo": ["Sydney"],
    "Sydney": ["Tokyo", "Beijing"],
    "Beijing": ["Mexico City", "Helsinki"],
    "Helsinki": ["Cairo", "New York"],
    "Cairo": ["Helsinki", "Reykjavik"],
    "Reykjavik": ["Cairo", "New York"],
    "Mexico City": ["Sydney"],
}

print(get_all_destinations(flights, "Beijing"))
print(get_all_destinations(flights, "Helsinki"))
