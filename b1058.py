import sys
sys.stdin = open('input.txt')

N = int(input())
arr = []
for _ in range(N):
    arr.append(list(input()))
relation = [[] for _ in range(N)]
result = [[] for _ in range(N)]
for i in range(N):
    for j in range(N):
        if arr[i][j] == 'Y':
            relation[i].append(j)
            result[i].append(j)

for i in range(N):
    for j in range(len(relation[i])):
        for a in relation[relation[i][j]]:
            if a not in result[i]:
                result[i].append(a)

for i in range(N):
    if i in result[i]:
        result[i] = len(result[i])-1
    else:
        result[i] = len(result[i])
print(max(result))

