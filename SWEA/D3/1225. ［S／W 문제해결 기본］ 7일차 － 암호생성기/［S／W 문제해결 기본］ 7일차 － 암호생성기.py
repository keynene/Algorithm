for _ in range(1,11):
    t = int(input())
    arr = list(map(int, input().split()))
    cnt = 0
    i = 0

    while cnt <= 0:
        i += 1
        temp = arr[0] - i
        del arr[0]

        if temp <= 0:
            temp = 0
            cnt += 1
            arr.append(temp)
            break
        else:
            arr.append(temp)

        if i == 5:
            i = 0

    print("#",t,sep="",end=" ")
    print(*arr,sep=" ")