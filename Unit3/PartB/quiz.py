def build_skyscrapers(floors):
    skyscrapers = 0
    stack = []

    for floor in floors:
        if not stack:
            stack.append(floor)
            skyscrapers += 1
        elif stack[-1] >= floor:
            stack.append(floor)
            skyscrapers += 1

print(build_skyscrapers([10, 5, 8, 3, 7, 2, 9])) 
print(build_skyscrapers([7, 3, 7, 3, 5, 1, 6]))  
print(build_skyscrapers([8, 6, 4, 7, 5, 3, 2]))