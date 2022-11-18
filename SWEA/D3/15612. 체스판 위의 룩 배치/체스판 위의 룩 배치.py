dx = [1,0]
dy = [0,-1]

def check(x,y):
    global ans
    for i in range(2):
        nx = x
        ny = y
        cnt = 0

        while 0<=nx<N and 0<=ny<N:
            if arr[ny][nx] == 'O':
                cnt += 1
            nx += dx[i]
            ny += dy[i]
        if cnt >= 2:
            ans = 'no'
            return


for t in range(int(input())):
    N = 8
    arr = [list(map(str,input())) for _ in range(N)]
    ans = 'yes'
    lcnt = 0

    for y in range(N):
        for x in range(N):
            if arr[y][x] == 'O':
                check(x,y)
                lcnt += 1
    
    if lcnt != 8:
        ans = 'no'
    
    print(f'#{t+1} {ans}')