def identify_conflicts(venue1_schedule, venue2_schedule):
    # return a dictionary containing the key-value pairs
    # that are the same in each schedule
    conflicts = {}
    for artist in venue1_schedule:
        if artist in venue2_schedule and venue1_schedule[artist] == venue2_schedule[artist]:
            conflicts[artist] = venue1_schedule[artist]
    return conflicts

venue1_schedule = {
    "Stromae": "9:00 PM",
    "Janelle Monáe": "8:00 PM",
    "HARDY": "7:00 PM",
    "Bruce Springsteen": "6:00 PM"
}

venue2_schedule = {
    "Stromae": "9:00 PM",
    "Janelle Monáe": "10:30 PM",
    "HARDY": "7:00 PM",
    "Wizkid": "6:00 PM"
}

print(identify_conflicts(venue1_schedule, venue2_schedule))
