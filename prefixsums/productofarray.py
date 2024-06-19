def productExceptSelf(nums):
    n = len(nums)
    if n == 0:
        return []

    # Initialize prefix and suffix arrays
    prefix_products = [1] * n
    suffix_products = [1] * n
    
    # Fill prefix_products
    for i in range(1, n):
        prefix_products[i] = prefix_products[i - 1] * nums[i - 1]

    # Fill suffix_products
    for i in range(n - 2, -1, -1):
        suffix_products[i] = suffix_products[i + 1] * nums[i + 1]

    # Generate result array by multiplying prefix and suffix products
    result = [1] * n
    for i in range(n):
        result[i] = prefix_products[i] * suffix_products[i]
    
    return result

# Example usage
nums = [1, 2, 3, 4]
print(productExceptSelf(nums))  # Output: [24, 12, 8, 6]
