arr = list(map(int, input().strip("[]").split(",")))

# Remove duplicates and sort
unique = sorted(set(arr))

if len(unique) < 2:
    print("Second Smallest :", -1)
    print("Second Largest :", -1)
else:
    print("Second Smallest :", unique[1])
    print("Second Largest :", unique[-2])