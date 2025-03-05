#Each string represents a string where each character
# corresponds to a performance slot. Merge the schedules
# by adding performances in alternating order, starting with
# schedule1. If one schedule is longer than the other,
# append the additional performances onto the end of the 
# merged schedule. Return the merged schedule.
def merge_schedules(schedule1, schedule2):
    """ 
    merged = ""
    i = 0
    while i < len(schedule1) and i < len(schedule2):
        merged += schedule1[i] + schedule2[i] #[a, p], [b, q], [c, r]
        i += 1 # [1, 2, 3]
    merged += schedule1[i:] + schedule2[i:] # [apbqcr],
    """
    merged = ""
    left = len(schedule1) - len(schedule2)
    right = len(schedule1) + len(schedule2)
    position = right
    while left <= right:
        left_schedule = schedule1[left] + schedule2[left] #ap, #bq #cr
        right_schedule = position

        if left < right:
            merged += left_schedule
            left += 1
        else:
            merged += right_schedule
            right -= 1
        position -= 1

    return merged 

print(merge_schedules("abc", "pqr")) 
print(merge_schedules("ab", "pqrs")) 
print(merge_schedules("abcd", "pq"))