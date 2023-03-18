n = int(input())

a, b, c = [0] * (n + 1), [0] * (n + 1), [0] * (n + 1)
dp = [0] * (n + 1)
a[1], b[1], c[1] = map(int, input().split())
dp[1] = a[1]

if n >= 2:
    a[2], b[2], c[2] = map(int, input().split())
    dp[2] = min(a[1] + a[2], b[1])
if n >= 3:
    a[3], b[3], c[3] = map(int, input().split())
    dp[3] = min(dp[2] + a[3], c[1], a[1] + b[2])

for i in range(4, n + 1):
    a[i], b[i], c[i] = map(int, input().split())
    dp[i] = min(dp[i - 1] + a[i], dp[i - 2] + b[i - 1],
                 dp[i - 3] + c[i - 2])
print(dp[n])
        
