#Each string represents a string where each character
# corresponds to a performance slot. Merge the schedules
# by adding performances in alternating order, starting with
# schedule1. If one schedule is longer than the other,
# append the additional performances onto the end of the 
# merged schedule. Return the merged schedule.
def merge_schedules(schedule1, schedule2):
    merged = ""
    i = 0
    j = 0

    while i < len(schedule1) and j < len(schedule2):
        merged += schedule1[i] + schedule2[j]
        i += 1
        j += 1
    
    while i < len(schedule1):
        merged += schedule1[i]
        i += 1
    
    while j < len(schedule2):
        merged += schedule2[j]
        j += 1
    return merged 

print(merge_schedules("abc", "pqr")) 
print(merge_schedules("ab", "pqrs")) 
print(merge_schedules("abcd", "pq"))