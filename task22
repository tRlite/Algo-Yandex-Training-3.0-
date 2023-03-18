n, k = map(int, input().split())

dp = [0] * n
dp[0] = 1

for i in range(n):
    for j in range(max(0, i - k), i):
        dp[i] += dp[j]
        
print(dp[n - 1])
