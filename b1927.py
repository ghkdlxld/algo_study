import sys
sys.stdin = open('input.txt')
from collections import deque
input = sys.stdin.readline

N = int(input())
arr = deque()
for _ in range(N):
    x = int(input())

    if x == 0:
        if len(arr) == 0:
            print(0)
        else:
            print(arr[0])
            arr.popleft()


    else:
        arr.append(x)
        if len(arr) == 1:
            continue

        else:
            i = len(arr)-1
            while True:
                if i != 0 and arr[i] < arr[i-1]:
                    arr[i], arr[i - 1] = arr[i-1], arr[i]
                    i -= 1
                else:
                    break
