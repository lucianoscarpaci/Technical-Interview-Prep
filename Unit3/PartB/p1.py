# You are given a list changes of strings where each string represents a change action.
# The actions can be: "Schedule X", "Cancel", "Reschedule"
# Return a list of performance ID that remain scheduled on the stage after all changes
# have been made.
def manage_stage_changes(changes):
    stack = []
    for change in changes: # 'Schedule A'
        if change.startswith("Schedule"):
            stack.append(change[-1])
        if change == "Cancel":
            if stack:
                stack.pop()
        elif change == "Reschedule":
            if stack:
                last_scheduled = stack.pop()
                stack.append(last_scheduled)
    return stack

print(manage_stage_changes(["Schedule A", "Schedule B", "Cancel", "Schedule C", "Reschedule", "Schedule D"]))
print(manage_stage_changes(["Schedule A", "Cancel", "Schedule B", "Cancel", "Reschedule", "Cancel"])) #[]
print(manage_stage_changes(["Schedule X", "Schedule Y", "Cancel", "Cancel", "Schedule Z"])) #['Z']