def majorityElement(nums):
    count = 0
    candidate = None

    for num in nums:
        if count == 0:
            candidate = num
        
        if num == candidate:
            count += 1
        else:
            count -= 1

    return candidate


# Examples
print(majorityElement([3,2,3]))
print(majorityElement([2,2,1,1,1,2,2]))