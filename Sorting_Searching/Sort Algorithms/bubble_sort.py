def bubble(nums):
    n = len(nums)
    for i in range(n):
        swap = False
        for j in range(0, n-i-1):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
                swap = True
        if not swap:
            break
        print(nums)
    return nums



print(bubble([7,3,5,9,5,4]))