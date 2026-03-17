def countPairs(arr, target):
    freq = {}
    count = 0

    for num in arr:
        complement = target - num

        if complement in freq:
            count += freq[complement]

        freq[num] = freq.get(num, 0) + 1

    return count


# Examples
print(countPairs([1,5,7,-1,5], 6))   # Output: 3
print(countPairs([1,1,1,1], 2))      # Output: 6
print(countPairs([10,12,10,15,-1], 125))  # Output: 0