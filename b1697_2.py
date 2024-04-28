import sys
from collections import deque
sys.stdin = open('input.txt')

N, K = map(int, input().split())
arr = [-1]*100001
arr[N] = 0
arr[K] = K-N

def find(a, b):
    q = deque()
    q.append(a)

    while q:
        now = q.popleft()
        if arr[b] == -1 or arr[now] < arr[b]:
            for d in [1, -1]:
                ni = now+d
                if 0 <= ni <= 100000 and (arr[ni] == -1 or arr[ni] > arr[now]+1):
                    arr[ni] = arr[now]+1
                    q.append(ni)
            ni = 2*now
            if 0 <= ni <= 100000 and (arr[ni] == -1 or arr[ni] > arr[now] + 1):
                arr[ni] = arr[now]+1
                q.append(ni)

find(N, K)
print(arr[K])
