for _ in range(10):
    t = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
    ans = p1 = p2 = 0

    for i in range(100):
        px = py = 0
        for j in range(100):
            px += arr[i][j]
            py += arr[j][i]
        p2 += arr[i][i]
        p1 += arr[i][99-i-i]
        ans = max(ans, px,py)
    ans = max(ans, p1, p2)
    print(f'#{t} {ans}')