import sys
sys.stdin = open('input.txt')

woods = list(input())
stacks = []
ans = 0
for i in range(len(woods)):
    if woods[i] == '(':
        stacks.append(woods[i])
    elif woods[i] == ')':
        if woods[i-1] == '(':
            stacks.pop()
            ans += len(stacks)
        else:
            stacks.pop()
            ans += 1
print(ans)