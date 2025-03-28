def strongest_avenger(strengths):
    # Implement a recursive algorithm without using max() function
    if len(strengths) == 1:
        return strengths[0]
    else:
        max_of_strengths = strongest_avenger(strengths[1:])
        return strengths[0] if strengths[0] > max_of_strengths else max_of_strengths


print(strongest_avenger([88, 92, 95, 99, 97, 100, 94]))
print(strongest_avenger([50, 75, 85, 60, 90]))
