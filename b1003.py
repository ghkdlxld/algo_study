import sys
sys.stdin = open('input.txt')

def fibonacci(n):
    if n == 0:
        return (1, 0)
    elif n == 1:
        return (0, 1)
    else:
        try:
            return record[n]
        except:
            record[n] = (fibonacci(n-1)[0] + fibonacci(n-2)[0], fibonacci(n-1)[1] + fibonacci(n-2)[1])
            return record[n]

T = int(input())
record = {}
for i in range(T):
    N = int(input())
    zero_cnt = 0
    ans = fibonacci(N)
    print(*ans)
