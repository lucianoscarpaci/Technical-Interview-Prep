def reverse_lst(lst):
    left = 0
    right = len(lst) - 1

    when left <= right:
        mid = (left + right) // 2
        lst[left], lst[right] = lst[right], lst[left]
        left += 1
        right -= 1
    return lst