import sys
sys.stdin = open('input.txt')

def egg_price(X):
    global result, price
    for x in range(X, -1, -1):
        revenue = P[x-1]*x
        if revenue > result:
            result = revenue
            price = P[x-1]

N, M = map(int, input().split())
P = [int(input()) for _ in range(M)]
P = sorted(P, reverse=True)
result = 0
price = 0
if M < N:
    egg_price(M)
else:
    egg_price(N)

print(price, result)
