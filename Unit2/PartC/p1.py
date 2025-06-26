from collections import Counter
def intersect(nums1, nums2):
    #return the intersection of nums1 and nums2
    # in ascending order
    count_nums1 = Counter(nums1)
    count_nums2 = Counter(nums2)
    intersection = count_nums1 & count_nums2
    result = []
    for num in intersection:
        result.extend([num] * intersection[num])
    return sorted(result)

nums1 = [1,2,2,1]
nums2 = [2,2]
print(intersect(nums1, nums2))  # Output: [2, 2]