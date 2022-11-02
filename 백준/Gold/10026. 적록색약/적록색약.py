import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

def dfs(x,y):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    visited[y][x] = True
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if 0<=nx<n and 0<=ny<n and amap[y][x] == amap[ny][nx] and not visited[ny][nx]:
            dfs(nx,ny)

n = int(input().rstrip())
amap = [list(map(str, input().rstrip())) for _ in range(n)]
visited = [[False]*n for _ in range(n)]
acnt = 0

for y in range(n):
    for x in range(n):
        if not visited[y][x]:
            dfs(x,y)
            acnt += 1

for y in range(n):
    for x in range(n):
        if amap[y][x] == 'R':
            amap[y][x] = 'G'

rgcnt = 0
visited = [[False]*n for _ in range(n)]
for y in range(n):
    for x in range(n):
        if not visited[y][x]:
            dfs(x,y)
            rgcnt += 1

print(acnt, rgcnt)