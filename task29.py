n = int(input())

a = []
for i in range(n):
    a.append(int(input()))

dp = [[None for kupons in range(n + 1)] for days in range(n + 1)]

if n:
    dp[0][0] = 0

for i in range(1, n + 1):
    for j in range(n + 1):
        if j < n - 1 and dp[i - 1][j + 1] is not None:
            dp[i][j] = dp[i - 1][j + 1]
            
        if a[i - 1] > 100:
            if j >= 1 and dp[i - 1][j - 1] is not None:
                if dp[i][j] is None:
                    dp[i][j] = dp[i - 1][j - 1] + a[i-1]
                else:
                    dp[i][j] = min(dp[i][j], dp[i - 1][j - 1] + a[i-1])
                    
        else:
            if dp[i - 1][j] is not None:
                if dp[i][j] is None:
                    dp[i][j] = dp[i - 1][j] + a[i-1]
                else:
                    dp[i][j] = min(dp[i][j], dp[i - 1][j] + a[i-1])


m = None
k1 = 0
for i in range(n + 1):
    if dp[n][i] is not None:
        if m is None or dp[n][i] <= m:
            k1 = i
            m = dp[n][i]
if m is None:
    print(0)
else:
    print(m)

i, j = n, k1

ans = []
k2 = 0

while i > 0:
    if j < n - 1 and dp[i - 1][j + 1] is not None\
                 and dp[i][j] == dp[i - 1][j + 1]:
        i -= 1
        j += 1
        k2 += 1
        ans.append(i + 1)
    elif a[i - 1] > 100:
        i -= 1
        j -= 1
    else:
        i -= 1
print(k1, k2)
print(*ans[::-1], sep='\n')

