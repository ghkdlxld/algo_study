import sys
sys.stdin = open('input.txt')

def find_chon(a):
    ppl = [a]
    visited = [0]*(n+1)
    visited[a] = 1

    while len(ppl) != 0:
        x = ppl.pop(0)
        for i in link[x]:
            if visited[i] == 0:
                visited[i] = 1
                chon[i] = chon[x] + 1
                ppl.append(i)

n = int(sys.stdin.readline())
a, b = map(int, sys.stdin.readline().split())
m = int(sys.stdin.readline())
link = [[] for _ in range(n + 1)]
chon = [0]*(n+1)

for _ in range(m):
    x, y = map(int, sys.stdin.readline().split())
    link[x].append(y)
    link[y].append(x)

find_chon(a)
if chon[b]:
    print(chon[b])
else:
    print('-1')


