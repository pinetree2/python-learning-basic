money = [500, 100, 50, 10, 5, 1]
n = 1000
m = int(input())
charge = n - m
count = 0
for coin in money:
  count += charge // coin
  charge %= coin

print(count)
