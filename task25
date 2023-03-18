def f(arr, i, d):
    if i == 0:
        return arr[1] - arr[0]
    
    if i < 0:
        return 0
    
    if len(arr) - 1 == i:
        if d[i] == -1:
            d[i] = (arr[i] - arr[i - 1]) + f(arr, i - 2, d)
        return d[i]
        
    if d[i] == -1:
        d[i] = min(arr[i + 1] - arr[i] + f(arr, i - 1, d), 
              arr[i] - arr[i - 1] + f(arr, i-2, d))
    return d[i]
    



n = int(input())

arr = sorted(map(int, input().split()))

d = [-1] * (n + 1)

print(f(arr, n - 1, d)) 
