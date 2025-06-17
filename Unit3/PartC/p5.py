def min_changes_to_make_balanced(schedule):
    empty_stack = []
    close_needed = 0

    for ch in schedule:
        if ch == "(":
            empty_stack.append(ch)
        elif ch == ")":
            if empty_stack:
                empty_stack.pop()
            else:
                close_needed += 1
    return len(empty_stack) + close_needed


print(min_changes_to_make_balanced("())"))
print(min_changes_to_make_balanced("((("))
