import sys
input = sys.stdin.readline

n = int(input().rstrip())
m = int(input().rstrip())
node = [list(map(int, input().split())) for _ in range(m)]
amap = [[] for _ in range(n+1)]
visited = [0]*(n+1)

for u,v in node:
    amap[u].append(v)
    amap[v].append(u)

def dfs(v):
    visited[v] = 1
    for i in amap[v]:
        if not visited[i]:
            dfs(i)

for i in amap[1]:
    if not visited[i]:
        dfs(i)

print(sum(visited)-1)