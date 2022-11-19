from copy import deepcopy

dx = [1,1,0,-1,-1,-1,0,1]
dy = [0,-1,-1,-1,0,1,1,1]

def visit(x,y,arr):
    varr = deepcopy(arr)
    for i in range(8):
        nx = x
        ny = y
        while 0<=nx<N and 0<=ny<N:
            varr[ny][nx] = True
            nx += dx[i]
            ny += dy[i]
    return varr

def dfs(n,chess):
    global ans,cnt

    if n == N:
        ans += 1
        return

    for y in range(n,N):
        cnt = 0
        for x in range(N):
            if not chess[y][x]:
                cnt += 1
                temp = visit(x,y,chess)
                dfs(n+1,temp)
        if cnt < 1:
            break

for t in range(int(input())):
    N = int(input())
    chess = [[False]*N for _ in range(N)]
    ans = 0
    cnt = 0

    dfs(0,chess)

    print(f'#{t+1} {ans}')