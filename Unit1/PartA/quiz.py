def reverse_lst(lst):
    left = 0 # index 0
    right = len(lst) - 1 #index 4
    
    while left < right:
        lst[left], lst[right] = lst[right], lst[left]
        left += 1
        right -= 1 
    
    return lst

print(reverse_lst([1, 2, 3, 4, 5]))
