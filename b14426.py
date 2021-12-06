import sys
sys.stdin = open('input.txt')

N, M = map(int, input().split())
ans = 0
strings = [input() for _ in range(N)]
words = [input() for _ in range(M)]
for word in words:
    for string in strings:
        if word == string[:len(word)]:
            ans += 1
            break
print(ans)