stack = []

answer = 'yes'
for a in input():
    if a in {'(', '{', '['}:
        stack.append(a)
    elif a == ')':
        if len(stack) == 0 or stack.pop() != '(':
            answer = 'no'
            break
    elif a == '}':
        if len(stack) == 0 or stack.pop() != '{':
            answer = 'no'
            break 
    elif a == ']':
        if len(stack) == 0 or stack.pop() != '[':
            answer = 'no'
            break 
if len(stack) != 0:
    answer = 'no'
    
print(answer)
        
