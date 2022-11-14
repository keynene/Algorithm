for t in range(1,int(input())+1):
    N = int(input())
    arr = [list(map(int, str(input()))) for _ in range(N)]
    ans = 0
    M = N//2

    for i in range(N):
        if i <= M:
            for j in range(M-i, M+i+1):
                ans += arr[i][j]
        else:
            for j in range(i-M, N-(i-M)):
                ans += arr[i][j]
    
    print(f'#{t} {ans}')