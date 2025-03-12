def max_tasks_within_time(tasks, time_limit):
    tasks.sort() #[5, 7, 8, 10]
    count = 0 
    for task in tasks: #5, 7, 8, 10
        if time_limit - task >= 0: #20 - 5 = 15, 15 - 7 = 8, 8 - 8 = 0
            time_limit -= task #15, 8, 0
            count += 1 #1, 2, 3
    return count #3

tasks = [5, 10, 7, 8]
time_limit = 20
print(max_tasks_within_time(tasks, time_limit))

tasks_2 = [2, 4, 6, 3, 1]
time_limit = 10
print(max_tasks_within_time(tasks_2, time_limit))

tasks_3 = [8, 5, 3, 2, 7]
time_limit = 15
print(max_tasks_within_time(tasks_3, time_limit))

