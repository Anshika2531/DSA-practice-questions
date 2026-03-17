n = int(input())

for i in range(n):
    cars, bikes = map(int, input().split())
    tyres = cars * 4 + bikes * 2
    print(tyres)