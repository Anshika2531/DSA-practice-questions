limit = 20

for a in range(1, limit):
    for b in range(a, limit):
        for c in range(b, limit):
            if a*a + b*b == c*c:
                print(a, b, c)