def dfs(graph, visited, node, prev):
    visited[node] = 1
    for neigh in range(len(graph[node])):
        if graph[node][neigh]: 
            if neigh in visited:
                if visited[neigh] == 1 and prev != neigh:
                    final_state = neigh
                    is_final = node == neigh
                    return True, [node + 1], final_state, is_final
            else:
                outp = dfs(graph, visited, neigh, node)
                if outp[0]:
                    if outp[3]:
                        return outp
                    is_final = False
                    if outp[2] == node:
                        is_final = True
                    return True, outp[1] + [node + 1], outp[2], is_final
    visited[node] = 2
    return False, 
    
n = int(input())
graph = []
visited = {}

for i in range(n):
    graph.append(list(map(int, input().split())))
    
for i in range(n):
    if i not in visited:
        outp = dfs(graph, visited, i, i)
        if outp[0]:
            print("YES")
            print(len(outp[1]))
            print(*outp[1])
            break
else:
    print("NO")
