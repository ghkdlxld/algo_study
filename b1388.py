N, M = map(int, input().split())
wood = []
for _ in range(N):
    wood.append(list(input()))

cnt = 0
stack = []
for i in range(N):
    for j in range(M):
        if wood[i][j] == '-':
            stack.append([1])
        if stack and wood[i][j] == '|':
            stack = []
            cnt += 1
    if stack:
        stack =[]
        cnt += 1

for j in range(M):
    for i in range(N):
        if wood[i][j] == '|':
            stack.append([2])
        if stack and wood[i][j] == '-':
            stack = []
            cnt += 1
    if stack:
        stack =[]
        cnt += 1

print(cnt)