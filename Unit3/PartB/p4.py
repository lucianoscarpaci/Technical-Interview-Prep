# You are given a list of clues, where each clue is either
# a booth number (integer) to visit or the word "back" 
# indicating that the participant should return to the
# previous booth.
from collections import deque
def booth_navigation(clues):
    nums = deque()
    back = deque()
    for clue in clues:
        if clue == "back":
            if not nums:
                continue
            nums.pop()
            back.append(clue)
        else:
            nums.append(clue)
    return list(nums)

clues = [1, 2, "back", 3, 4]
print(booth_navigation(clues)) 

clues = [5, 3, 2, "back", "back", 7]
print(booth_navigation(clues)) 

clues = [1, "back", 2, "back", "back", 3]
print(booth_navigation(clues))