def binary_search(nums, target):
    left, right = 0, len(nums)-1
    while left <= right:
        mid = left + (right-left) //2
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            right = mid-1
        else:
            left = mid + 1
    return -1
print(binary_search([0,1,2,3,4,5,6], 4))

# Binary search performs search on a sorted array with O(logN) time. There are two templates for binary search.

# Template 1, basic binary search, searching closed intervals of [left, right] for cases where we don't need access to mid index's neighbor.