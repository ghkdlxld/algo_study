import sys
sys.stdin = open('input.txt')

n = int(input())
A = list(map(int, input().split()))
dp = [1]*n
for i in range(n):
    for j in range(i):
        if A[i] < A[j]:
            # 마지막에 현재원소(A[j])를 붙이는게 더 크냐 안붙이는게 더 크냐 비교
            dp[i] = max(dp[i], dp[j]+1)

print(max(dp))
