n = int(input())
a1 = list(map(int, input().split()))
m = int(input())
a2 = list(map(int, input().split()))

dp = [[0 for i in range(m + 1)] for j in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, m + 1):
        if a1[i - 1] == a2[j - 1]:
            dp[i][j] = dp[i - 1][j-1] + 1 
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])
            
i, j = n, m
ans = []

while i > 0 and j > 0:
    if dp[i][j] == dp[i-1][j-1] + 1 and a1[i - 1] == a2[j - 1]:
        ans.append(a1[i-1])
        i -= 1
        j -= 1
    elif dp[i][j] == dp[i-1][j]:
        i -= 1
    else:
        j -= 1
print(*ans[::-1])
        
