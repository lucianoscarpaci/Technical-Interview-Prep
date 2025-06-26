def merge_sorted_lists(lst1, lst2):

    merged_list = []
    i, j = 0, 0

    while i < len(lst1) and j < len(lst2):
        if lst1[i] < lst2[j]:
            merged_list.append(lst1[i])
            i += 1
        else:
            merged_list.append(lst2[j])
            j += 1

    # Append remaining elements from lst1 or lst2
    merged_list.extend(lst1[i:])
    merged_list.extend(lst2[j:])

    return merged_list


lst1 = [1, 3, 5]
lst2 = [2, 4, 6]
print(merge_sorted_lists(lst1, lst2))  # Output should be [1, 2, 3, 4, 5, 6]
