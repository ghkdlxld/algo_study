import sys
sys.stdin = open('input.txt')

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
a = sorted(A, reverse=True)
b = sorted(B)
ans = 0
for i in range(N):
    ans += a[i]*b[i]
print(ans)