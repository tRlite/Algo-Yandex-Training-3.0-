from collections import deque 

q = deque()

n = int(input())
dist = [-1] * n

graph = []

for i in range(n):
    graph.append(list(map(int, input().split())))

f, l = map(int, input().split())
dist[f - 1] = 0
q.append(f - 1)

while q:
    curr_node = q.popleft()
    for j in range(n):
        if graph[curr_node][j] and dist[j] == -1:
            dist[j] = dist[curr_node] + 1
            q.append(j)
            
print(dist[l - 1])
