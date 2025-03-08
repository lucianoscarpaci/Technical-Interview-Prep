# Given two integer arrays nums1, and nums2,
# return an array of their intersection.
# The intersection of two arrays is the set of
# elements that are present in both arrays.
# Each element in the result must be unique.
# The result can be in any order.
def intersection(nums1, nums2):
    left = 0
    right = 0
    result = []
    nums1.sort()
    nums2.sort()
    while left < len(nums1) and right < len(nums2): #1, 
        if nums1[left] == nums2[right]: #False, [-1, 0, 1, 2]
                                                #[0, 2, 3]   > at 0 index
            if nums1[left] not in result: #True
                result.append(nums1[left]) #0, #2
            left += 1 #2, #3, #4
            right += 1 #1, #2
        elif nums1[left] < nums2[right]: #True
            left += 1 #1
        else:
            right += 1
    while left < len(nums1):
        if nums1[left] == nums2[right]:
            if nums1[left] not in result:
                result.append(nums1[left])
            left += 1
        elif nums1[left] < nums2[right]:
            left += 1
        else:
            right += 1    
    return result # [0, 2]


nums1 = [-1, 0, 1, 2]
nums2 = [0, 2, 3]
print(intersection(nums1, nums2))  # [0, 2]