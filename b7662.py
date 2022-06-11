import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
import heapq

T = int(input())
for tc in range(T):
    max_q = []
    min_q = []
    key = [False]*1000001
    k = int(input())
    for i in range(k):
        method, n = input().split()
        if method == 'I':
            heapq.heappush(min_q, (int(n), i))
            heapq.heappush(max_q, (-int(n), i))
            key[i] = True

        else:
            if int(n) < 0:
                if len(min_q) == 0:
                    continue
                x = heapq.heappop(min_q)
                key[x[1]] = False

            else:
                if len(max_q) == 0:
                    continue
                x = heapq.heappop(max_q)
                key[x[1]] = False

            while max_q and not key[max_q[0][1]]:
                heapq.heappop(max_q)
            while min_q and not key[min_q[0][1]]:
                heapq.heappop(min_q)



    if len(max_q) == 0:
        print('EMPTY')

    else:
        print(-max_q[0][0], min_q[0][0])