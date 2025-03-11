# You have a list of work sessions, each with a start time and an end time.
# Write a function to find the smallest gap between any two consecutive work sessions.
# The gap is measured in minutes.
def find_smallest_gap(work_sessions):
    work_sessions.sort()
    # Sort the work sessions by start time
    n = len(work_sessions)
    if n < 2:
        return 0
    
    smallest_gap = float("inf")

    for i in range(1, n):
        current_gap = work_sessions[i][0] - work_sessions[i - 1][1]
        if current_gap < smallest_gap:
            smallest_gap = current_gap
    return smallest_gap

work_sessions = [(900, 1100), (1300, 1500), (1600, 1800)]
print(find_smallest_gap(work_sessions)) # [100]

work_sessions_2 = [(1000, 1130), (1200, 1300), (1400, 1500)]
print(find_smallest_gap(work_sessions_2)) # [70]

work_sessions_3 = [(900, 1100), (1115, 1300), (1315, 1500)]
print(find_smallest_gap(work_sessions_3)) # [15]