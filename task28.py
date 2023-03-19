n, m = map(int, input().split())

dp = [[0 for i in range(m)] for j in range(n)]

dxs = [-2, -1]
dys = [-1, -2]
    
dp[0][0] = 1

for i in range(n):
    for j in range(m):
        for dx, dy in zip(dxs, dys):
            if i + dx >= 0 and j + dy >= 0:
                dp[i][j] += dp[i + dx][j + dy]

    
print(dp[n - 1][m - 1])   
