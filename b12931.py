import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


def inholsu(lst):
    for i in range(len(lst)):
        if lst[i]%2 != 0:
            return 1
    return 0

def makeeven(lst):
    global cnt
    for i in range(len(lst)):
        if lst[i]%2 != 0:
            lst[i] -= 1
            cnt += 1
    return lst

N = int(input())
A = [0]*N
B = list(map(int, input().split()))

cnt = 0
for i in range(N):
    if B[i]%2 != 0:
        B[i] -= 1
        cnt += 1

while True:
    if A == B:
        break
    B = list(map(lambda x: x // 2, B))
    cnt += 1
    if inholsu(B):
        B = makeeven(B)

print(cnt)


