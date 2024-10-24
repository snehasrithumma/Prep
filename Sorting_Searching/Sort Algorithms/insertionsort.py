def insertion(nums):
    for i in range(1, len(nums)):
        val = nums[i]
        j = i-1
        while j>=0 and nums[j] > val:
            nums[j+1] = nums[j]
            j-=1
        nums[j+1] = val
    return nums


print(insertion([7,3,5,9,5,4]))