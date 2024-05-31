def subarraySum(nums, target):
    left = 0
    current_sum = 0
    
    for right in range(len(nums)):
        current_sum += nums[right]
        
        while current_sum > target and left <= right:
            current_sum -= nums[left]
            left += 1
        
        if current_sum == target:
            return True  # Found a subarray with the target sum
    
    return False  # No subarray found

# Example Usage:
print(subarraySum([1, 2, 3, 7, 5], 12))  # Output: True (3, 7, 2)
