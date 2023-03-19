n, m, k = map(int, input().split())
prefix_sums = [[0 for j in range(m + 1)] for i in range(n + 1)]

for i in range(n):
    row = list(map(int, input().split()))
    for j in range(m):
        prefix_sums[i + 1][j + 1] = row[j] + prefix_sums[i][j+1] + prefix_sums[i+1][j] - prefix_sums[i][j]

for i in range(k):
    l1, l2, r1, r2 = map(int, input().split())
    print(prefix_sums[r1][r2] + prefix_sums[l1-1][l2-1] - prefix_sums[r1][l2 - 1] - prefix_sums[l1 - 1][r2])
