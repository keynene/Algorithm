for t in range(1,11):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    arr_t = list(zip(*arr))
    
    ans = 0
    for lst in arr_t:
        prev = 0
        for n in lst:
            if n:
                if n == 2 and prev == 1:
                    ans += 1
                prev = n
    
    print(f'#{t} {ans}')