import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N, M = map(int, input().split())
known = list(map(int, input().split()))[1:]
party = [list(map(int, input().split()))[1:] for _ in range(M)]
p = list(range(N+1))

def find_p(x):
    if x != p[x]:
        p[x] = find_p(p[x])
    return p[x]

def update_p(arr, new_p):
    # 뒤늦게 연결되었을 때 그와 연결된 모든 부모 변경해줘야함
    for i in range(1, N+1):
        if p[i] in arr:
            p[i] = new_p
        p[i] = find_p(p[i])


for participants in party:
    parents = list(map(lambda x: p[x], participants))
    new_p = min(parents)
    not_new = []
    for participant in participants:
        if p[participant] != new_p:
            not_new.append(p[participant])
        p[participant] = new_p
    update_p(not_new, new_p)

total = [False]*(N+1)
for i in range(1, N+1):
    for x in known:
        if p[i] == p[x]:
            total[i] = True

ans = 0
for x in party:
    flag = True
    for y in x:
        if total[y]:
            flag = False
            break
    if flag:
        ans += 1

print(ans)