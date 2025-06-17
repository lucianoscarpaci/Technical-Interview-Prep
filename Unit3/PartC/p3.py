def arrange_attendees_by_priority(attendees, priority):
  n = len(attendees) - 1
  left = 0
  right = n
  i = 0

  while i <= right:
    if attendees[i] < priority:
        attendees[left], attendees[i] = attendees[i], attendees[left]
        left += 1
        i += 1
    elif attendees[i] > priority:
        attendees[right], attendees[i] = attendees[i], attendees[right]
        right -= 1
    else:
        i += 1

    j = n
    right += 1

    while right < n:
        attendees[j], attendees[right] = attendees[right], attendees[j]
        right += 1


    return attendees

print(arrange_attendees_by_priority([9,12,5,10,14,3,10], 10)) 
print(arrange_attendees_by_priority([-3,4,3,2], 2))