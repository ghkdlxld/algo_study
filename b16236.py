import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input())
sea = [list(map(int, input().split())) for _ in range(N)]
baby = [0, 0, 2]


print(sea)

# 초기
for x in range(N):
    for y in range(N):
        if sea[x][y] == 9:
            baby = [x, y]

print(baby)

# 먹을 수 있는 물고기 찾기
can_eat = []
def eat():
    for i in range(N):
        for j in range(N):
            if sea[i][j] < baby[2]:
                can_eat.append([i, j, abs(i-baby[0])+abs(j-baby[1])]) # i,j, 거리


# 먹으러 갈 수 있는지
def can_go(r, c):
    # r,c 에서 시작해서 baby[0], baby[1]까지 이동 가능여부
    # 이동 가능 -> 이동, can_eat 다시 점검?
    # 이동 불가능
    pass




while True:
    eat()
    if len(can_eat) == 0:
        break

    # 먹을 수 있는 물고기 중 거리가 가까운 순으로 정렬
    can_eat = sorted(can_eat, key=lambda x : [x[2], x[0], x[1]])

    for a, b, c in can_eat:
        can_go(a, b)


    can_eat = []


# 아니면 아예 가까운곳, i,j 작은순 부터 순회 -> 갈 수 있으면 이동 방법 2
# 전체 점검은 너무 오래걸릴듯