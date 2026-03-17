n = int(input())

items = []
discounts = []

for i in range(n):
    name, price, discount = input().split(',')
    price = int(price)
    discount = int(discount)
    
    discount_amount = price * discount // 100
    items.append(name)
    discounts.append(discount_amount)

min_discount = min(discounts)

for i in range(n):
    if discounts[i] == min_discount:
        print(items[i])