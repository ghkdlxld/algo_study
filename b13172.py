import sys
from fractions import Fraction
sys.stdin = open('input.txt')

M = int(input())
dice_exp = 0
for _ in range(M):
    N, S = map(int, input().split())
    dice_exp += Fraction(S, N)

# 분자
a = dice_exp.numerator
# 분모
b = dice_exp.denominator

X = 1000000007
def sol(n):
    if n == 1:
        return b

    elif n % 2 == 0:
        half = sol(n//2)
        return half*half%X

    else:
        return b*sol(n-1)%X

print(a*sol(X-2)%X)