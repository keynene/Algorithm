for t in range(int(input())):
    arr = list(map(int,input()))
    re = 0
    cnt = 0

    for i in arr:
        if i != re:
            cnt += 1
            re = i

    print(f'#{t+1} {cnt}')