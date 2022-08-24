import sys
question = list(input())
ans = ''
cal = {'+': 1, '-': 1, '*':2, '/':2, '(': 3, ')': 3}
q = []
stack = []

for x in question:
    if x not in cal:
        q.append(x)
    elif x != ')' and (len(stack) == 0 or x == '(' or stack[-1] == '('):
        stack.append(x)
    elif x == ')':
        while True:
            if len(stack) > 0 and stack[-1] == '(':
                stack.pop(-1)
                break
            elif len(stack) > 0:
                t = stack.pop(-1)
                q.append(t)
    else:
        while True:
            if len(stack) > 0 and cal[stack[-1]] >= cal[x]:
                t = stack[-1]
                if t == '(':
                    break
                stack.pop(-1)
                q.append(t)
            else:
                break
        stack.append(x)


while stack:
    t = stack.pop(-1)
    q.append(t)

print(''.join(q))