from collections import deque 

queue = deque()

n, m, s, t, q = map(int, input().split())
dist = {}
dist[(s, t)] = 0

graph = [[-1] * (m + 1)] * (n + 1)

queue.append((s, t))
dxs = [-2, -2, -1, -1, 1, 1, 2, 2]
dys = [-1, 1, -2, 2, -2, 2, -1, 1]

while queue:
    x, y = queue.popleft()
    for dx, dy in zip(dxs, dys):
        if (0 < x + dx <= n and 0 < y + dy <= m and \
              (x + dx, y + dy) not in dist):
            dist[(x + dx, y + dy)] = dist[(x, y)] + 1
            queue.append((x + dx, y + dy))
 
 
ans = 0            
for i in range(q):
    x, y = map(int, input().split())
    if (x, y) not in dist:
        print(-1)
        break
    else:
        ans += dist[(x, y)]
else:
    print(ans)

