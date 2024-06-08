# For an unsorted array, the two-pointer approach can still be used, but it typically involves sorting the array first, which would take O(n log n) time. Here's an example:

# Example Problem
# Given an unsorted array of integers and a target sum, find two numbers in the array that add up to the target sum.

# Solution
# Sort the array.
# Use two pointers, one at the beginning and one at the end.
# Adjust pointers based on the current sum.
def twoSumUnsorted(arr, target):
    arr.sort()
    left = 0
    right = len(arr) - 1
    while left < right:
        current_sum = arr[left] + arr[right]
        
        if current_sum == target:
            return [left, right]  # Return the indices in the sorted array
        elif current_sum < target:
            left += 1
        else:
            right -= 1
    
    return []  # If no solution is found

# Example Usage:
print(twoSumUnsorted([3, 2, 4, 6, 1], 10))  
# Output might be [1, 4] after sorting
