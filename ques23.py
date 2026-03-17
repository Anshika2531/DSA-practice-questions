def moveZeroes(nums):
    j = 0  # position for next non-zero element
    
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[j], nums[i] = nums[i], nums[j]
            j += 1
            
    return nums


# Examples
print(moveZeroes([0,1,0,3,12]))
print(moveZeroes([0]))