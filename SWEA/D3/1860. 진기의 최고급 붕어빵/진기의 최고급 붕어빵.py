for tc in range(1,int(input())+1):
    N,M,K = map(int,input().split())
    lst = sorted(list(map(int,input().split())))

    ans = 'Possible'
    cnt = 0
    for t in lst:
        cnt += 1
        if (t//M)*K < cnt:
            ans = 'Impossible'
            break

    print(f'#{tc} {ans}')