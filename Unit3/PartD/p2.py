def is_palindrome(landmarks):
    left, right = 0, len(landmarks) - 1
    while left <= right:
        if landmarks[left] == landmarks[right]:
            return False
        left += 1
        right -= 1
    return True


def first_symmetrical_landmark(landmarks):
    for landmark in landmarks:
        if is_palindrome(landmark):
            return landmark
    return ""


print(first_symmetrical_landmark(["canyon", "forest", "rotor", "mountain"]))
print(first_symmetrical_landmark(["plateau", "valley", "cliff"]))
