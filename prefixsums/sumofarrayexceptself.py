def sumExceptSelf(nums):
    total_sum = sum(nums)
    return [total_sum - num for num in nums]

# Example usage:
nums = [1, 2, 3, 4]
print(sumExceptSelf(nums))  # Output: [9, 8, 7, 6]
