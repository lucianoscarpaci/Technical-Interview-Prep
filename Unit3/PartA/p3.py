# post title is a string
# requirements use two pointer technique
# two pointer is a type of swapping where we swap the values of two pointers
# let l and r be the two pointers, initially l = 0 and r = len(s) - 1
# l and r get swapped inwards until l >= r or until the condition is met
# The goal is to see if the post titles are symmetrical
# if the post title is symmetrical, return True
def is_symmetrical_title(title):
    l = -1
    r = len(title)

    while l < r:
        l += 1
        r -= 1
        if title[l].lower() != title[r].lower():
            return False
        else:
            return True
            
print(is_symmetrical_title("A Santa at NASA"))
print(is_symmetrical_title("Social Media"))
print(is_symmetrical_title("A Toyota"))
print(is_symmetrical_title("Racecar"))
print(is_symmetrical_title("aibohphobia"))
print(is_symmetrical_title("cryptography"))