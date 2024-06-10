def majority_element(nums):
    # Phase 1: Find a candidate for the majority element
    candidate = None
    count = 0
    
    for num in nums:
        if count == 0:
            candidate = num
            count = 1
        elif num == candidate:
            count += 1
        else:
            count -= 1
    print('majority', candidate)
    # Phase 2: Verify if the candidate is indeed the majority element
    count = 0
    for num in nums:
        if num == candidate:
            count += 1
    
    if count > len(nums) // 2:
        return candidate
    else:
        return None

# Example usage
nums = [2, 2, 1, 1, 1, 2, 2]
print(majority_element(nums))  # Output: 2

nums = [3, 3, 4, 2, 4, 4, 2, 4, 4]
print(majority_element(nums))  # Output: 4

nums = [1, 2, 3, 4]
print(majority_element(nums))  # Output: None
