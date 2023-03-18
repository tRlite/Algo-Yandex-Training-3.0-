input()

n = int(input())
if n == 0:
    lst = []
else:
    x1, x2 = map(int, input().split())
    lst = [[x1, x2]]

for i in range(1, n):
    x1, x2 = map(int, input().split())
    
    left = 0
    right = len(lst) - 1
    while left <= right:
        mid = (left + right) // 2
        
        if (lst[mid][1] >= x1):
            right = mid - 1
        else:
            left = mid + 1
    start_del = left
    
    left = 0
    right = len(lst) - 1
    while left <= right:
        mid = (left + right) // 2
        
        if (lst[mid][0] > x2):
            right = mid - 1
        else:
            left = mid + 1
            
    end_del = left
    lst = [*lst[:start_del], [x1, x2], *lst[end_del:]]
print(len(lst))
