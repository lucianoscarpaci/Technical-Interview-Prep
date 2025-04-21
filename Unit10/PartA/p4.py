def get_adj_dict(flights):
    adj_dict = {}
    for a, b in flights:
        if a not in adj_dict:
            adj_dict[a] = []
        adj_dict[a].append(b)

        if b not in adj_dict:
            adj_dict[b] = []
        adj_dict[b].append(a)
    return adj_dict

flights = [['Cape Town', 'Addis Ababa'], ['Cairo', 'Lagos'], ['Lagos', 'Addis Ababa'], 
            ['Nairobi', 'Cairo'], ['Cairo', 'Cape Town']]
print(get_adj_dict(flights))
# Expected output:
'''
{
    'Cape Town': ['Addis Ababa', 'Cairo'],
    'Addis Ababa': ['Cape Town', 'Lagos'],
    'Lagos': ['Cairo', 'Addis Ababa'],
    'Cairo': ['Cape Town', 'Nairobi'],
    'Nairobi': ['Cairo']
}
'''