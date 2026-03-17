nums = list(map(int, input().strip("[]").split(",")))

n = len(nums)
expected_sum = n * (n + 1) // 2
actual_sum = sum(nums)

print(expected_sum - actual_sum)