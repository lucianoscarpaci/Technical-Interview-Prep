def print_todo_list(task):
    for i in range(len(task)):
        print(f"{i + 1}. {task[i]}")

task = ["Count all the bees in the hive", "Chase all the clouds from the sky", "Think", "Stoutness Exercises"]
print_todo_list(task)

task = []
print_todo_list(task)