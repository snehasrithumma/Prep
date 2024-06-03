def sort(nums):   
    def partition(left, right):
        pivot  = nums[right]
        wp  = left
        for i in range(left, right):
            if nums[i] <= pivot :
                nums[wp], nums[i] = nums[i], nums[wp]
                wp+=1
        nums[wp], nums[right] = nums[right], nums[wp]
        return wp 

    def quick_sort(left, right):
        if left < right: 
            pivot  = partition(left, right)
            if pivot  > left:
                quick_sort(left, pivot -1)
            else:
                quick_sort(pivot +1, right)
    quick_sort(0, len(nums)-1)
    return nums

print(sort( [9,3,5,1,8,2,0]))