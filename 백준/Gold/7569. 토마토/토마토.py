import sys
from collections import deque
input = sys.stdin.readline

dx = [-1,1,0,0,0,0]
dy = [0,0,-1,1,0,0]
dz = [0,0,0,0,-1,1]

def bfs(arr):
    queue = deque()

    for x,y,z in arr:
        queue.append((x,y,z,1))
    
    while queue:
        x,y,z,dep = queue.popleft()

        for i in range(6):
            nx = x+dx[i]
            ny = y+dy[i]
            nz = z+dz[i]

            if 0<=nx<m and 0<=ny<n and 0<=nz<h and tomato[nz][ny][nx] == 0:
                tomato[nz][ny][nx] = dep+1
                queue.append((nx,ny,nz,dep+1))


# m=x n=y h=z
m,n,h = map(int, input().split())
tomato = [[list(map(int, input().split())) for _ in range(n)] for _ in range(h)]
cooked = []

for z in range(h):
    for y in range(n):
        for x in range(m):
            if tomato[z][y][x] == 1:
                cooked.append([x,y,z])

bfs(cooked)
cnt = 0
maxTomato = 0
for z in range(h):
    for y in range(n):
        for x in range(m):
            if tomato[z][y][x] == 0:
                cnt += 1
            if tomato[z][y][x] > maxTomato:
                maxTomato = tomato[z][y][x]

if cnt > 0:
    print(-1)
else:
    print(maxTomato-1)