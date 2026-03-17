import heapq

nums = list(map(int, input().strip("[]").split(",")))
k = int(input())

heap = []

for num in nums:
    heapq.heappush(heap, num)
    if len(heap) > k:
        heapq.heappop(heap)

print(heap[0])