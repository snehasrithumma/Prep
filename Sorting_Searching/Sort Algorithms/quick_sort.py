def quick(nums):
    if len(nums) == 0: return []
    pivot = nums[-1]
    left, right = [], []
    for x in nums[0:-1]:
        if x<=pivot:
           left.append(x)
        else:
            right.append(x)
    return quick(left) + [pivot] + quick(right)

print(quick([7,3,5,9,4,5]))