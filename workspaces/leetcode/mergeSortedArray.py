def merge(nums1, m, nums2, n):
    for i in range(n):
        nums1[i+m] = nums2[i]
    nums1.sort()
    print(nums1)
merge([1,2,3,0,0,0], 3, [2,5,6], 3)

def mergeThreePointers(nums1, m, nums2, n):
    # Merge nums2 into nums1
    # Start from the end of nums1 and nums2
    # Compare the last elements of nums1 and nums2
    # Place the larger element at the end of nums1
    # Move the pointer of the larger element
    # Repeat until all elements of nums2 are merged into nums1
    # Time complexity: O(m+n)
    # Space complexity: O(1)
    i = m - 1
    j = n - 1
    k = m + n - 1
    while i >= 0 and j >= 0:
        if nums1[i] > nums2[j]:
            nums1[k] = nums1[i]
            i -= 1
        else:
            nums1[k] = nums2[j]
            j -= 1
        k -= 1
    # If there are remaining elements in nums2, copy them to nums1
    while j >= 0:
        nums1[k] = nums2[j]
        j -= 1
        k -= 1
    return nums1
print(mergeThreePointers([1,2,3,0,0,0], 3, [2,5,6], 3))