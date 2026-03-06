def find_longest_harmonious_travel_sequence(ratings):
    # Initialize a dictionary to store the frequency of each rating
    frequency = {}

    # Count the occurrences of each rating
    for rating in ratings:
        frequency[rating] = frequency.get(rating, 0) + 1

    max_length = 0

    # Find the longest harmonious sequence
    for rating in frequency:
        if rating + 1 in frequency:
            max_length = max(max_length, frequency[rating] + frequency[rating + 1])

    return max_length


ratings1 = [1, 3, 2, 2, 5, 2, 3, 7]
ratings2 = [1, 2, 3, 4]
ratings3 = [1, 1, 1, 1]

print(find_longest_harmonious_travel_sequence(ratings1))  # 5
print(find_longest_harmonious_travel_sequence(ratings2))  # 2
print(find_longest_harmonious_travel_sequence(ratings3))  # 0
