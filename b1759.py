import sys
sys.stdin = open('input.txt')

def johab(n, lst):
    result = []
    for i in range(1<<n):
        case = []
        for j in range(n):
            if i & (1 << j):
                case.append(lst[j])
        result.append(case)
    return result

L, C = map(int, input().split())
a = list(input().split())
b = []
i = 0
while i < len(a):
    if a[i] in 'aeiou':
        x = a.pop(i)
        b.append(x)
    else:
        i += 1

ans = []
for mo in range(1, L-1):
    if len(b) < mo:
        break
    else:
        mo_lst = johab(len(b), b)
        ja_lst = johab(len(a), a)
        for m in mo_lst:
            if len(m) == mo:
                for j in ja_lst:
                    if len(j) == L - mo:
                        ans.append(m + j)

for a in range(len(ans)):
    for i in range(L):
        ans[a][i] = ord(ans[a][i])
    ans[a] = sorted(ans[a])
    for j in range(L):
        ans[a][j] = chr(ans[a][j])
ans = sorted(ans)
for a in ans:
    print(''.join(a))
