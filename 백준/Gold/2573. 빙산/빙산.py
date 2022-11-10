import sys
from collections import deque
from copy import deepcopy
input = sys.stdin.readline
sys.setrecursionlimit(100000)

n,m = map(int,input().split())
ice = [list(map(int, input().split())) for _ in range(n)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def melting(cp_ice):
    ice = deepcopy(cp_ice)

    for y in range(n):
        for x in range(m):
            melted = 0
            if cp_ice[y][x] != 0:
                for i in range(4):
                    mx = x+dx[i]
                    my = y+dy[i]
                    if 0<=mx<m and 0<=my<n and ice[my][mx] == 0:
                        melted += 1
                cp_ice[y][x] = cp_ice[y][x]-melted
                if cp_ice[y][x] < 0 : cp_ice[y][x] = 0

    return(cp_ice)

def bfs(x,y):
    queue = deque()
    queue.append((x,y))

    while queue:
        x,y = queue.popleft()
        visited[y][x] = True

        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]

            if 0<=nx<m and 0<=ny<n and not visited[ny][nx] and ice[ny][nx] != 0:
                visited[ny][nx] = True
                queue.append((nx,ny))

year = 0
while True:
    visited = [[False]*m for _ in range(n)]
    sum_ice = sum(map(sum,ice))
    cnt = 0

    if sum_ice == 0:
        print(0)
        break
    
    for y in range(n):
        for x in range(m):
            if ice[y][x] != 0 and not visited[y][x]:
                bfs(x,y)
                cnt += 1

    if cnt > 1:
        print(year)
        break
    else:
        ice = melting(ice)
        year += 1