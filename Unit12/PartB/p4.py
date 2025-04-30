def can_attend_meetings(intervals):
    intervals.sort(key=lambda x: x[0])

    for i in range(1, len(intervals)):
        if intervals[i][0] < intervals[i - 1][1]:
            return False
    return True


intervals_1 = [[0, 30], [5, 10], [15, 20]]
intervals_2 = [[7, 10], [2, 4]]
intervals_3 = [[4, 5], [2, 3], [1, 2]]
intervals_4 = [[0, 400], [400, 800], [1555, 1200], [1200, 1600], [1600, 2000]]

print(can_attend_meetings(intervals_1))
print(can_attend_meetings(intervals_2))
print(can_attend_meetings(intervals_3))
print(can_attend_meetings(intervals_4))
