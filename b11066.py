import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

T = int(input())
for tc in range(1, T+1):
    K = int(input())
    paper = list(map(int, input().split()))
    d = []

    def dp(l, r):
        tmp = [0, 1e9]
        for i in range(r):
            if sum(paper[l:i]) + sum(paper[i:r]) < tmp[1]:
                tmp = [i, sum(paper[l:i]) + sum(paper[i:r])]
        d.append(tmp[1])
        dp(0, tmp[0])
        dp(tmp[0], r)


    dp(0, K)

