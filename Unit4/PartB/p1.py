# Find a pair of tasks that fit exactly into a specific time slot
# Write the find_task_pair() function that takes a list of task times and an available time slot
# and returns the pair of tasks that fit exactly into the available time slot.
# Given a list of integers representing the time required for each task an an integer representing
# the available time slot, write a function that returns True if there exists a pair of task
# that exactly matches the available time slot and False otherwise.
def find_task_pair(task_times, available_time):
  counter = len(task_times)
  # The counter has to exactly match the length of the task_times list to return False
  # Loop through the task_times list
  for i in range(counter):
    for j in range(i+1, counter):
      # Return true if there exists a pair of tasks that exactly matches the available time slot  
      if task_times[i] + task_times[j] == available_time:
        return True

  return False



task_times = [30, 45, 60, 90, 120]
available_time = 105
print(find_task_pair(task_times, available_time))

task_times_2 = [15, 25, 35, 45, 55]
available_time = 100
print(find_task_pair(task_times_2, available_time))

task_times_3 = [20, 30, 50, 70]
available_time = 60
print(find_task_pair(task_times_3, available_time))