from collections import deque, defaultdict

q = deque()

n = int(input())
m = int(input())
graph = defaultdict(list)

for i in range(m):
    l, *line = list(map(int, input().split()))
    for j in range(l):
        st = line[j]
        if j:
            prev = line[j-1]
            graph[st].append((prev, i))
            graph[prev].append((st, i))
     
            
first, last = map(int, input().split())

marked = set()

q.append((first, None, 0))

while q:
    st, line, trans = q.popleft()
    if st == last:
        print(trans)
        break
    marked.add((st, line))
    for new_st, trans_line in graph[st]:
        if (new_st, trans_line) not in marked:
            if line is None or line == trans_line:
                q.appendleft((new_st, trans_line, trans))
            else:
                q.append((new_st, trans_line, trans + 1))
else:
    print(-1)
    
    
