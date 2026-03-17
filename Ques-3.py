sem = int(input())

for i in range(sem):
    n = int(input())
    marks = list(map(int, input().split()))

    if any(m < 0 or m > 100 for m in marks):
        print("You have entered invalid mark")
    else:
        print("Maximum mark:", max(marks))