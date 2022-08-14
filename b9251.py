import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

x = [0] + list(input().strip())
y = [0] + list(input().strip())
board = [[0]*(len(x)) for _ in range(len(y))]

for i in range(1, len(y)):
    for j in range(1, len(x)):
        if x[j] == y[i]:
            board[i][j] = max(board[i][j-1], board[i-1][j-1]+1)
        else:
            board[i][j] = max(board[i][j - 1], board[i-1][j])

print(board[-1][-1])