from collections import deque


N = int(6)
queue = deque()
for n in range(1, N+1):
    queue.append(n)

for _ in range(N-1):
    queue.popleft()
    left = queue.popleft()
    queue.append(left)

print(*queue)
