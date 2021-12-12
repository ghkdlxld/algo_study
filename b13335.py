import sys
from collections import deque
sys.stdin = open('input.txt')


N, W, L = map(int, input().split())
truck = deque(map(int, input().split()))
stack = deque([0]*W)
out = 0
time = 0
stack_sum = 0
while True:
    time += 1
    out_truck = stack.popleft()
    if out_truck != 0:
        out += 1
        if out == N:
            break


    if len(truck) != 0 and sum(stack) + truck[0] <= L:
        stack.append(truck.popleft())
    else:
        stack.append(0)

print(time)