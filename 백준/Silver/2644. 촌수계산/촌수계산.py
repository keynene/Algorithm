import sys
input = sys.stdin.readline

n = int(input().rstrip())
start,end = map(int, input().split())
m = int(input().rstrip())
node = [map(int, input().split())for _ in range(m)]

amap = [[] for _ in range(n+1)]
visited = [1e9]*(n+1)

for x,y in node:
    amap[x].append(y)
    amap[y].append(x)

def dfs(start, end, amap, dep):
    if start == end:
        visited[end] = min(visited[end],dep)
        return

    for i in amap[start]:
        if visited[i] > dep:
            visited[i] = dep
            dfs(i, end, amap, dep+1)

dfs(start, end, amap, 1)

if visited[end] == 1e9:
    print(-1)
else:
    print(visited[end])