stack = []
n = int(input())

a = list(map(int, input().split()))

answer = [-1 for i in range(n)]
for i in range(n):
    while len(stack) > 0 and a[i] < stack[-1][1]:
        answer[stack.pop()[0]] = i
    stack.append((i, a[i]))
    
print(*answer)
