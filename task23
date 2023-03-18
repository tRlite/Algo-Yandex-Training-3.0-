n = int(input())

dp = [0] * (n + 1)
prev = [-1] * (n + 1)

for i in range(2, n + 1):
    d1, d2 = None, None
    if i % 3 == 0:
        d1 = dp[i // 3] + 1
    if i % 2 == 0:
        d2 = dp[i // 2] + 1
    d3 = dp[i - 1] + 1
    if d1 is not None and (d2 is None or d1 <= d2) and d1 <= d3:
        prev[i] = i // 3
        dp[i] = d1
    elif d2 is not None and (d1 is None or d2 <= d1) and d2 <= d3:
        prev[i] = i // 2
        dp[i] = d2
    else:
        prev[i] = i - 1
        dp[i] = d3
        
ans = [n]
elem = prev[n]
while elem != -1:
    ans.append(elem)
    elem = prev[elem]

print(dp[n])
print(*ans[::-1])
