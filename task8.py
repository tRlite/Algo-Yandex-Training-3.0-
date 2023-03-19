k = int(input())

left = None
right = None 
for i in range(k):
    x, y = map(int, input().split())
    if left is None:
        left = (x, y)
        right = (x, y)
    else: 
        left = (min(left[0], x), min(left[1], y))
        right = (max(right[0], x), max(right[1], y))
        
print(*left, *right)
