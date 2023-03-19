stack = []

for a in input().strip().split():
    if a == '*':
        stack.append(stack.pop() * stack.pop())
    elif a == '+':
        stack.append(stack.pop() + stack.pop())
    elif a == '-':
        x1, x2 = stack.pop(), stack.pop()
        stack.append(x2 - x1)
    else:
        stack.append(int(a))
    
print(stack[-1])
