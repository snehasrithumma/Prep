# Given an array of positive integers nums and a positive integer target, return the minimal length of a 
# subarray
#  whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.

 

# Example 1:

# Input: target = 7, nums = [2,3,1,2,4,3]
# Output: 2
# Explanation: The subarray [4,3] has the minimal length under the problem constraint.


def minimal(nums, target):
    start = 0
    minimal_length = len(nums) + 1
    current_sum = 0
    for right in range(len(nums)):
        current_sum+= nums[right]

        while current_sum >= target:
            minimal_length = min(right-start+1, minimal_length)
            current_sum -= nums[start]
            start+=1
    return minimal_length if minimal_length != len(nums) + 1 else 0

print(minimal([2,3,1,2,4,3], 7))

