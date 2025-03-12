def max_tasks_within_time(tasks, time_limit):
    tasks.sort()
    count = 0
    for task in tasks:
        if time_limit - task >= 0:
            time_limit -= task
            count += 1
    return count

tasks = [5, 10, 7, 8]
time_limit = 20
print(max_tasks_within_time(tasks, time_limit))

tasks_2 = [2, 4, 6, 3, 1]
time_limit = 10
print(max_tasks_within_time(tasks_2, time_limit))

tasks_3 = [8, 5, 3, 2, 7]
time_limit = 15
print(max_tasks_within_time(tasks_3, time_limit))

