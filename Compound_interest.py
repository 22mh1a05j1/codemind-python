p, r, t = map(float, input().split())
amount = p * (1 + r / 100) ** t
k= "{:.2f}".format(amount)
print(k)
