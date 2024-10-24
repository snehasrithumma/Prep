def find_duplicate(nums):
    tortise = nums[0]
    hare = nums[0]
    while True:
        tortise = nums[tortise]
        hare = nums[nums[hare]]
        if tortise == hare:
            break

    ptr1 = nums[0]
    ptr2 = tortise

    while ptr1 != ptr2:
        ptr1 = nums[ptr1]
        ptr2 = nums[ptr2]

    return ptr2


nums = [1, 3, 4, 2, 2]
print("Duplicate number:", find_duplicate(nums))

# If you want to find a duplicate in an array without modifying the array and using constant extra space, you can use Floyd's Tortoise and Hare (Cycle Detection) algorithm. 
# This algorithm is typically used for finding cycles in linked lists but can be adapted to find duplicates in arrays.

# Floyd's Tortoise and Hare Algorithm
# This algorithm uses two pointers that move at different speeds to detect a cycle. Here's how you can apply it to find a duplicate number in an array:

# Phase 1: Finding the Intersection Point of the Two Runners

# Initialize two pointers, tortoise and hare.
# Move tortoise one step at a time and hare two steps at a time until they meet inside the cycle.
# Phase 2: Finding the Entrance to the Cycle

# Start a new pointer from the beginning of the list and move it one step at a time, while moving the tortoise pointer one step at a time. 
# The point where they meet is the start of the cycle, which is the duplicate number.