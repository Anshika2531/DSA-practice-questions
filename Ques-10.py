n = int(input())
arr = list(map(int, input().split()))

count = {}

for num in arr:
    if num in count:
        count[num] += 1
    else:
        count[num] = 1

for key in sorted(count):
    print(f"{key} occurs {count[key]} times")