def dfs(graph, visited, node):
    ans = [node]
    visited.add(node)
    for neigh in graph[node]:
        if neigh not in visited:
            ans.extend(dfs(graph, visited, neigh))
    return ans
    
v, e = map(int, input().split())
graph = [[] for _ in range(v + 1)]
visited = set()

for i in range(e):
    v1, v2 = map(int, input().split())
    graph[v1].append(v2)
    graph[v2].append(v1)
    
ans = sorted(dfs(graph, visited, 1))
print(len(ans))
print(*ans)
