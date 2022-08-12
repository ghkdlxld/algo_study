import sys
sys.stdin = open('input.txt')
input=sys.stdin.readline

N, K = map(int, input().split())
# y 축
item = [[0,0]]
bag = [[0]*(K+1) for _ in range(N+1)]

for i in range(N):
    item.append(list(map(int, input().split())))

for i in range(1, N+1):
    for j in range(1, K+1):
        w, v = item[i]
        if w > j:
            bag[i][j] = bag[i-1][j]
        else:
            # 넣을 수 있다면 가방에 넣는다(가능한 가방 용량 j - w, 넣었으니 + v)
            bag[i][j] = max(bag[i-1][j], bag[i-1][j-w]+v)

print(bag[N][K])
