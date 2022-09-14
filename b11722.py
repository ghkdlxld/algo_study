import sys
sys.stdin = open('input.txt')

n = int(input())
A = list(map(int, input().split()))
ans = []
print(A)
for i in range(n):
    t = A[i]
    for j in range(i, n):
        if A[j] > t:
            t = A[j]
    ans.append(t)

print(ans)
print(len(set(ans)))