# In a wildlife research stationm each letter of the alphabet represents
# a different observation point laid out in a single row. Given a string
# station_layout of length 26 indicating the layout of these observation
# points 0 to 25 from left to right and a string observations of length n
# The time taken to navigate from one observation point to another is
# is the absolute difference between their indices. |i - j| where i and j
# are the indices of the observation points. Return the total time taken
# to navigate all the observation points in the order given by observations.
# Example: station_layout = "pqrstuvwxyzabcdefghijklmno"
# observations = "wildlife"
# navigate_research_station(station_layout, observations) -> 45


def navigate_research_station(station_layout, observations):
    total_time = 0
    current_position = 0
    # use the enumerate function to get the index and value
    for index, observation in enumerate(observations): # wildlife
        # get the index of the observation
        next_position = station_layout.index(observation) #7
        # get the absolute difference between the current position and the next position
        total_time += abs(next_position - current_position) #7
        # update the current position to the next position
        current_position = next_position
        
    return total_time

station_layout1 = "pqrstuvwxyzabcdefghijklmno"
observations1 = "wildlife"

station_layout2 = "abcdefghijklmnopqrstuvwxyz"
observations2 = "cba"

print(navigate_research_station(station_layout1, observations1))
print(navigate_research_station(station_layout2, observations2))