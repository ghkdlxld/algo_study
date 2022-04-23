import sys
import heapq
sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input())
heap = []
for _ in range(N):
    x = int(input())
    if x == 0:
        if len(heap) == 0:
            print(0)
        else:
            # 가장 큰 값 출력, pop
            print(-heap[0])
            heapq.heappop(heap)

    else:
        heapq.heappush(heap, -x)


