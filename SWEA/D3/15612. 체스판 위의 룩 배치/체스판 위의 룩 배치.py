def check(x,y):
    global ans
    for i in range(x+1,N):
        if chess[y][i] == 'O':
            ans = 'no'
            return
    
    for j in range(y+1,N):
        if chess[j][x] == 'O':
            ans = 'no'
            return

for t in range(int(input())):
    N = 8
    chess = [list(map(str, input())) for _ in range(N)]
    ans = 'yes'
    lcnt = 0

    for y in range(N):
        for x in range(N):
            if chess[y][x] == 'O':
                check(x,y)
                lcnt += 1

    if lcnt != 8:
        ans = 'no'
    
    print(f'#{t+1} {ans}')