import sys
sys.stdin = open('input.txt')

N = int(input())
M = int(input())
if M != 0:
    broken = list(map(int, input().split()))
else:
    broken = []
ans = abs(N-100)

cnt = 0

def can_make(x):
    for i in list(str(x)):
        if int(i) in broken:
            return False
    return True


while True:
    if cnt >= ans:
        print(ans)
        break

    elif N-cnt >= 0 and can_make(N-cnt) and cnt + len(str(N-cnt)) < ans:
        print(cnt + len(str(N-cnt)))
        break

    elif can_make(N+cnt) and cnt + len(str(N+cnt)) < ans:
        print(cnt + len(str(N+cnt)))
        break

    cnt += 1


