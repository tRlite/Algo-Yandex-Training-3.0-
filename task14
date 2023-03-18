stack = []
input()

curr_val = 1

for a in map(int, input().split()):
    if a == curr_val:
        curr_val += 1
        while len(stack) and stack[-1] == curr_val:
            stack.pop()
            curr_val += 1
    else:
        stack.append(a)
if len(stack):
    print('NO')
else:
    print('YES')
