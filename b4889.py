import sys
sys.stdin = open('input.txt')

tc = 1
while True:
    string = list(input())
    if string.count('-') != 0:
        break
    cnt = 0
    stack = []
    for x in string:
        if x == '{':
            stack.append(x)
        else:
            if len(stack) == 0:
                stack.append('{')
                cnt += 1
            else:
                stack.pop()
    if len(stack) != 0:
        cnt += len(stack)//2
    print(f'{tc}. {cnt}')
    tc += 1
