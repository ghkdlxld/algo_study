import sys
input = sys.stdin.readline
import heapq

T = int(input())
q = []

for tc in range(T):
    k = int(input())
    for _ in range(k):
        method, n = input().split()
        if method == 'I':
            heapq.heappush(q, int(n))

        else:
            if len(q) == 0:
                continue

            elif int(n) < 0:
                heapq.heappop(q)

            else:
                q.sort()
                q.pop(-1)




    if len(q) == 0:
        print('EMPTY')

    else:
        print(q[-1], q[0])