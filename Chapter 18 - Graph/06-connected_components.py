N = int(input("Enter number of nodes: "))
E = int(input("Enter number of edges: "))

graph = [[0 for _ in range(N)] for _ in range(N)]
visited = [0 for _ in range(N)]

for _ in range(E):
    [u,v] = [int(i) for i in input().split()]
    graph[u][v] = 1
    graph[v][u] = 1

def dfs(graph,u):
    if visited[u]:
        return
    visited[u] = 1
    for i in range(len(graph[u])):
        if graph[u][i] == 1:
            dfs(graph,i)

count = 0

for i in range(N):
    if not visited[i]:
        count += 1
        dfs(graph,i)

print(count)