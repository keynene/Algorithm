import sys
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(100000)

m,n = map(int, input().split())
toma = [list(map(int, input().split())) for _ in range(n)]
cooked = []

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(arr):
    queue = deque()
    for x,y in arr:
        queue.append((x,y))

    while queue:
        x,y = queue.popleft()

        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]

            if 0<=nx<m and 0<=ny<n and toma[ny][nx] == 0:
                toma[ny][nx] = toma[y][x] + 1
                queue.append((nx,ny))


for y in range(n):
    for x in range(m):
        if toma[y][x] == 1:
            cooked.append([x,y])

bfs(cooked)
cnt = 0
max_R = 0
for y in range(n):
    for x in range(m):
        if toma[y][x] > max_R:
            max_R = toma[y][x]
        if toma[y][x] == 0:
            cnt += 1
if cnt > 0:
    print(-1)
else:
    print(max_R-1)