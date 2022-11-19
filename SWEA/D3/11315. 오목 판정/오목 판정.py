dx = [-1,0,1,1]
dy = [1,1,1,0]

def dfs(x,y):
    global ans
    for i in range(4):
        nx = x
        ny = y
        cnt = 0

        while 0<=nx<N and 0<=ny<N and arr[ny][nx] == 'o':
            cnt += 1
            nx += dx[i]
            ny += dy[i]
        
        if cnt >= 5:
            ans = 'YES'
            return

for t in range(int(input())):
    N = int(input())
    arr = [list(map(str, input())) for _ in range(N)]
    ans = 'NO'

    for y in range(N):
        for x in range(N):
            if arr[y][x] == 'o':
                dfs(x,y)
            if ans == 'YES':
                break
        if ans == 'YES':
            break

    print(f'#{t+1} {ans}')