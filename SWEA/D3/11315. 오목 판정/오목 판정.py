def move(arr):
    global ans
    dr = [0,1,1,1]
    dc = [1,0,1,-1]
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 'o':
                for d in range(4):
                    r = i
                    c = j
                    cnt = 0
                    while 0<=r<N and 0<=c<N and arr[r][c]=='o':
                        cnt += 1
                        r += dr[d]
                        c += dc[d]
                    if cnt >=5:
                        ans = 'YES'
                        return 
    return 

for t in range(int(input())):
    N = int(input())
    arr = [input() for _ in range(N)]
    ans = 'NO'

    move(arr)

    print(f'#{t+1} {ans}')