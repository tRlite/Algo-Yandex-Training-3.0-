from collections import deque 

q = deque()

n = int(input())

graph = [[[[-1 for i in range(n)]] for j in range(n)] for k in range(n)]


for i in range(n):
    input()
    for j in range(n):
        graph[i][j] = list(input())
        if 'S' in graph[i][j]:
            for k in range(n):
                if graph[i][j][k] == 'S':
                    graph[i][j][k] = 0
                    q.append((i, j, k))
                

dxs = [-1, 1, 0, 0, 0, 0]
dys = [0, 0, -1, 1, 0, 0]
dzs = [0, 0, 0, 0, -1, 1]

while q:
    x, y, z = q.popleft()
    for dx, dy, dz in zip(dxs, dys, dzs):
        if (0 <= x + dx < n and 0 <= y + dy < n and 0 <= z + dz < n and\
             graph[x + dx][y + dy][z + dz] == '.'):
            graph[x + dx][y + dy][z + dz] = graph[x][y][z] + 1
            q.append((x + dx, y + dy, z + dz))
 
ans = 40 ** 3           
for i in graph[0]:
    for j in i:
        if j != '#' and j != '.':
            ans = min(ans, j)
print(ans)
