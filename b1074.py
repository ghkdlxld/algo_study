import sys
sys.stdin = open('input.txt')

N, r, c = map(int, input().split())
ans = 0
def solution(x, y, l):
    global ans
    for i in range(x, x+l):
        for j in range(y, y+l):
            if i == r and j == c:
                print(ans)
                return

            elif l//2 != 1:
                if x <= r < x+l//2 and y <= c < y+l//2:
                    solution(x, y, l//2)
                elif x <= r < x+l//2 and y + l//2 <= c < y+l:
                    ans += l**2//4
                    solution(x, y+l//2, l//2)
                elif x + l // 2 <= r < x + l and y <= c < y + l // 2:
                    ans += l ** 2 // 2
                    solution(x+l//2, y, l//2)
                elif x+l//2 <= r < x + l and y+l//2 <= c < y + l:
                    ans += (3 * (l**2)) // 4
                    solution(x+l//2, y+l//2, l//2)
                return
            ans += 1


solution(0, 0, 2**N)