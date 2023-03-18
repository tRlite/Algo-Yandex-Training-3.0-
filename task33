def dfs(graph, visited, node, color):
    ans = True
    visited[node] = color
    for neigh in graph[node]:
        if neigh in visited:
            if color == visited[neigh]:
                return False
        else:
            ans &= dfs(graph, visited, neigh, 3 - color)
    return ans
    
    
v, e = map(int, input().split())
graph = [[] for _ in range(v + 1)]
visited = {}

for _ in range(e):
    v1, v2 = map(int, input().split())
    graph[v1].append(v2)
    graph[v2].append(v1)
    
for v in range(1, v + 1):
    if v not in visited and not dfs(graph, visited, v, 1):
        print("NO")
        break
else:
    print("YES")
    
