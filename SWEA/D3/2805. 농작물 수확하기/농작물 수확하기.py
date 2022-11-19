for t in range(int(input())):
    N = int(input())
    M = N//2
    arr = [list(map(int, str(input()))) for _ in range(N)]
    ans = 0

    for i in range(N):
        if i <= M:
            for j in range(M-i,M+i+1):
                ans += arr[i][j]
        else:
            for j in range(i-M, N-(i-M)):
                ans += arr[i][j]

    print(f'#{t+1} {ans}')