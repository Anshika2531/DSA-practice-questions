def rotate(nums, k):
    n = len(nums)
    k = k % n
    nums[:] = nums[-k:] + nums[:-k]
    return nums


# Examples
print(rotate([1,2,3,4,5,6,7], 3))
print(rotate([-1,-100,3,99], 2))