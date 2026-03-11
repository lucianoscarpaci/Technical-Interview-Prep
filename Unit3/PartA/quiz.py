def engagement_boost(engagements):
    squared_engagements = []

    for i in range(len(engagements)):
        squared_engagement = engagements[i] * engagements[i]
        squared_engagements.append((squared_engagement, i))

    squared_engagements.sort(reverse=True)
    left, right = 0, len(engagements)
    result = [0] * len(engagements)
    position = len(engagements) - 1
    squared_left = []
    squared_right = []
    while left <= right:
        squared_left[left] = engagements[left] * engagements[left]
        squared_right[right] = engagements[right] * engagements[right]

        if left < right:
            result[position] = squared_engagements[left]
            result[position] = squared_engagements[right]
        else:
            right
    return result


print(engagement_boost([-4, -1, 0, 3, 10]))
print(engagement_boost([-7, -3, 2, 3, 11]))
"""
[0, 1, 9, 16, 100]
[4, 9, 9, 49, 121]
"""
