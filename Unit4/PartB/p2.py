# You have a list of work sessions, each with a start time and an end time.
# Write a function to find the smallest gap between any two consecutive work sessions.
# The gap is measured in minutes.
def find_smallest_gap(work_sessions):
    # Sort the work sessions by start time
    work_sessions.sort()
    print(work_sessions)
    # Set the smallest gap to the difference between the first two work sessions
    difference = work_sessions[1][0] - work_sessions[0][1]
    smallest_gap = difference  
    # Loop through the work sessions starting from the second one
    for i in range(1, len(work_sessions)):
        # If the gap is smaller than the smallest gap, update the smallest gap
        if difference < smallest_gap:
            smallest_gap = difference
        # Calculate the difference between the current work session and the next one
        difference = work_sessions[i-1][0] - work_sessions[i][0]
    # Return the smallest gap
    return smallest_gap

work_sessions = [(900, 1100), (1300, 1500), (1600, 1800)]
print(find_smallest_gap(work_sessions)) # [100]

work_sessions_2 = [(1000, 1130), (1200, 1300), (1400, 1500)]
print(find_smallest_gap(work_sessions_2)) # [70]

work_sessions_3 = [(900, 1100), (1115, 1300), (1315, 1500)]
print(find_smallest_gap(work_sessions_3)) # [15]