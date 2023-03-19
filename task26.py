n, m = map(int, input().split())

a = [[0 for i in range(m)] for j in range(n)] 
dp = [[0 for i in range(m)] for j in range(n)]

for i in range(n):
    a[i] = list(map(int, input().split()))
    
    
for i in range(n):
    for j in range(m):
        if i and j:
            dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + a[i][j]
        elif i:
            dp[i][j] = dp[i-1][j] + a[i][j]
        elif j:
            dp[i][j] = dp[i][j-1] + a[i][j]
        else:
            dp[i][j] = a[i][j]
    
print(dp[n - 1][m - 1])    
