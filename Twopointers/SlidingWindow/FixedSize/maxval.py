
# Example
# Input:

# python
# Copy code
# nums = [1,3,-1,-3,5,3,6,7]
# k = 3
# Output:

# python
# Copy code
# [3, 3, 5, 5, 6, 7]

def FixedSize(nums, k):
    start = 0
    window_sum = sum(nums[0:3])
    max_val = window_sum 
    for i in range(k,len(nums)):
        window_sum = window_sum - nums[start] + nums[i]
        if window_sum > max_val:
            max_val = window_sum 
        start+=1
    return max_val

print(FixedSize( [1,3,-1,-3,5,3,6,7], 3))