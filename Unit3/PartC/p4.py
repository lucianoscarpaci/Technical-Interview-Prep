def rearrange_guests(guests):
  attendees = [guest for guest in guests if guest > 0]
  absences = [guest for guest in guests if guest < 0]
  # Initialize attendee_index and absence_index
  attendee_index = 0
  absence_index = 0
  result = []
  while attendee_index < len(attendees) and absence_index < len(absences):
    # Append the next attendee and absence
    result.append(attendees[attendee_index])
    result.append(absences[absence_index])
    attendee_index += 1
    absence_index += 1
  return result


print(rearrange_guests([3,1,-2,-5,2,-4]))  
print(rearrange_guests([-1,1])) 