r, c = map(int, input().split())

matrix = []
for _ in range(r):
    matrix.append(list(map(int, input().split())))

top = 0
bottom = r - 1
left = 0
right = c - 1

result = []

while top <= bottom and left <= right:

    # Top row
    for i in range(left, right + 1):
        result.append(matrix[top][i])
    top += 1

    # Right column
    for i in range(top, bottom + 1):
        result.append(matrix[i][right])
    right -= 1

    if top <= bottom:
        # Bottom row
        for i in range(right, left - 1, -1):
            result.append(matrix[bottom][i])
        bottom -= 1

    if left <= right:
        # Left column
        for i in range(bottom, top - 1, -1):
            result.append(matrix[i][left])
        left += 1

print(*result)