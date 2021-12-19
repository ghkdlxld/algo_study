import sys
sys.stdin = open('input.txt')

def dfs(i, j):
    stack.append((i, j))
    now_i, now_j = stack.pop()
    word.append(board[now_i][now_j])

    if len(word) == 6:
        ans.append(''.join(word))
        return

    di = [0, 0, 1, -1]
    dj = [1, -1, 0, 0]

    for k in range(4):
        ni = now_i + di[k]
        nj = now_j + dj[k]
        if 0<= ni < 5 and 0<= nj < 5:
            dfs(ni, nj)
            word.pop()


board = [list(input().split()) for _ in range(5)]
stack = []
ans = []
for i in range(5):
    for j in range(5):
        word = []
        dfs(i, j)
print(len(set(ans)))