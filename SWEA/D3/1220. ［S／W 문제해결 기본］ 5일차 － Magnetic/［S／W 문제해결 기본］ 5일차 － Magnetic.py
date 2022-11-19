def find(x,y):
    global ans
    ny = y
    while 0<=ny<N:
        if arr[ny][x] == 2:
            ans += 1
            break
        elif arr[ny][x] == 1:
            break
        else: ny += 1

for t in range(1,11):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    ans = 0

    for y in range(N):
        for x in range(N):
            if arr[y][x] == 1:
                find(x,y+1)

    print(f'#{t} {ans}')