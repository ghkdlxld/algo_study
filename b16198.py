import sys
sys.stdin = open('input.txt')

# 오답
# def energy(n):
#     global total
#     if n == 2:
#         return total
#     else:
#         idx, big = 0, 0
#         for i in range(2, n):
#             if W[i - 1] * W[i + 1] > big:
#                 idx, big = i, W[i - 1] * W[i + 1]
#         total += big
#         W.pop(idx)
#         return energy(len(W) - 1)


# N = int(input())
# W = [0] + list(map(int, input().split()))
# total = 0
# energy(N,2)


# 완전탐색으로 변경
import sys
sys.stdin = open('input.txt')

def energy(lst, total):
    global big
    if len(lst) == 2:
        if total > big:
            big = total
            return big
    else:
        for i in range(1, len(lst)-1):
            w = (lst[i - 1] * lst[i + 1])
            pick = [i, lst.pop(i)]
            energy(lst, total+w)
            lst.insert(pick[0], pick[1])


N = int(input())
W = list(map(int, sys.stdin.readline().split()))
big = 0
energy(W, 0)
print(big)