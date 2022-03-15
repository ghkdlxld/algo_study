import sys
sys.stdin = open('input.txt')

N = int(input())
cnt = 1
t = [1]*(N // 2 + 1)
b = [1]*(N // 2 + 1)
ans = [1]*(N // 2 + 1)
for i in range(1, N // 2+1):
    for j in range(N-i,N-2*i,-1):
        t[i] *= j
    b[i] = b[i-1]*i
    cnt += t[i]//b[i]
print()
print(cnt%10007)