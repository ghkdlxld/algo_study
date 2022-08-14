import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input().strip())
ans = 0
q = [0]*N

def check(x, y):
    for k in range(x):
        if q[k] == y or x-k == abs(q[k]-y):
            return False
    return True


def n_queens(i):
    global ans
    if i == N:
        ans += 1
        return
    else:
        for j in range(N):
            q[i] = j
            if check(i, j):
                n_queens(i+1)

n_queens(0)
print(ans)