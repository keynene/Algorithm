from collections import deque

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x,y):
    global ans
    queue = deque()
    queue.append((x,y))
    
    while queue:
        x,y = queue.popleft()
        visited[y][x] = True

        if arr[y][x] == 3:
            ans = 1
            return
        
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]

            if 0<=nx<N and 0<=ny<N and arr[ny][nx] != 1 and not visited[ny][nx]:
                queue.append((nx,ny))

for _ in range(1,11):
    t = int(input())
    N = 16
    arr = [list(map(int, str(input()))) for _ in range(N)]
    visited = [[False]*N for _ in range(N)]
    ans = 0

    for y in range(N):
        for x in range(N):
            if arr[y][x] == 2:
                bfs(x,y)

    print(f'#{t} {ans}')