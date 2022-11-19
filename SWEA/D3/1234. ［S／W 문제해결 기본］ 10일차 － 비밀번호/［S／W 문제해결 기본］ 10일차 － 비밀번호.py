for t in range(1,11):
    N, num = map(int, input().split())
    arr = list(map(int, str(num)))
    n = 1
    cnt = 1

    while cnt > 0:
        cnt = 0
        for i in range(n,len(arr)):
            if arr[i-1] == arr[i]:
                del arr[i]
                del arr[i-1]
                n = i-1
                cnt += 1
                break

    ans = int("".join(map(str, arr)))

    print(f'#{t} {ans}')