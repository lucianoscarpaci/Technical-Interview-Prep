# Use a stack to simulate the process of collecting points
# and return the total points collected at each festival.
def collect_festival_points(points):
    stack = []
    for point in points:
        
        if stack:
            last_point = stack[-1]
            next_point = last_point + point
            stack.pop()
            stack.append(next_point)
        
        else:
            stack.append(point)
    return stack[0]

print(collect_festival_points([5, 8, 3, 10])) 
print(collect_festival_points([2, 7, 4, 6])) 
print(collect_festival_points([1, 5, 9, 2, 8])) 