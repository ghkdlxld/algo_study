import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input())
num = list(map(int, input().split()))
cal = list(map(int, input().split())) # +,-,*,//
visited = [0]*4
ans_max = -int(1e9)
ans_min = int(1e9)

def sol(x, tmp):
    global ans_max, ans_min

    if x == N:
        ans_max = max(ans_max, tmp)
        ans_min = min(ans_min, tmp)
        return

    for k in range(4):
        if cal[k] > visited[k]:
            visited[k] += 1
            if k == 0:
                sol(x + 1, tmp+num[x])
            elif k == 1:
                sol(x+1, tmp-num[x])
            elif k == 2:
                sol(x+1, tmp*num[x])
            else:
                sol(x+1, int(tmp/num[x]))

            visited[k] -= 1

sol(1, num[0])
print(ans_max)
print(ans_min)