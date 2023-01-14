import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input())
sea = [list(map(int, input().split())) for _ in range(N)]
baby = [0, 0]


print(sea)

# 초기
for x in range(N):
    for y in range(N):
        if sea[x][y] == 9:
            baby = [x, y]

print(baby)

# 먹을 수 있는 물고기 찾기
def can_eat():
    pass