def get_adj_dict(flights):
    dict = {}
    for flight in flights:
        if flight[0] not in dict:
            dict[flight[0]] = [flight[1]]
        else:
            dict[flight[0]].append(flight[1])
        if flight[1] not in dict:
            dict[flight[1]] = [flight[0]]
        else:
            dict[flight[1]].append(flight[0])
    return dict

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