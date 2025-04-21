flights = {
    "JFK": ["LAX", "DFW"],
    "LAX": ["JFK"],
    "DFW": ["ATL", "JFK"],
    "ATL": ["DFW"]
}

print(list(flights.keys()))
print(list(flights.values()))
print(flights["JFK"])
'''
['JFK', 'LAX', 'DFW', 'ATL']
[['LAX', 'DFW'], ['JFK'], ['ATL', 'JFK'], ['DFW']]
['LAX', 'DFW']
'''