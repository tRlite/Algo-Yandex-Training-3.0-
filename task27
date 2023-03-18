n, m = map(int, input().split())

a = [[0 for i in range(m + 1)] for j in range(n + 1)] 
dp = [[0 for i in range(m + 1)] for j in range(n + 1)]

#dx = [-2, 2, 0, 0]
#dy = [0, 0, -2, 2]

for i in range(1, n + 1):
    a[i][1:] = list(map(int, input().split()))
    
    
for i in range(1, n + 1):
    for j in range(1, m + 1):
        dp[i][j] = max(dp[i-1][j], dp[i][j-1]) + a[i][j]

    
print(dp[n][m])   

ans = []

i, j = n, m

while i > 1 or j > 1:
    if dp[i - 1][j] > dp[i][j - 1] or j == 1:
        i -= 1
        ans.append('D')
    else:
        j -= 1 
        ans.append('R')
print(*ans[::-1])

