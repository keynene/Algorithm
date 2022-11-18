def check(x,y):
    global ans
    for i in range(x+1,N):
        if 0<=i<N and chess[y][i] == 'O':
            ans = 'no'
            return
    for i in range(y+1,N):
        if 0<=i<N and chess[i][x] == 'O':
            ans = 'no'
            return

for t in range(int(input())):
    N = 8
    chess = [list(map(str,input())) for _ in range(N)]
    ans = 'yes'
    cnt = 0

    for y in range(N):
        for x in range(N):
            if chess[y][x] == 'O':
                cnt += 1
                check(x,y)
    if cnt != 8:
        ans = 'no'
    print(f'#{t+1} {ans}')