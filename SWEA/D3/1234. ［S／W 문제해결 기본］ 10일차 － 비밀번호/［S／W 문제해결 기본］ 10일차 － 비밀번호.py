for t in range(1,11):
    N, num = map(int,input().split())
    num = list(map(int, str(num)))
    cnt = 1

    while cnt > 0:
        cnt = 0
        for i in range(1,len(num)):
            if num[i] == num[i-1]:
                cnt += 1
                del num[i], num[i-1]
                break
            

    while num[0] <= 0:
        del num[0]
        
    print("#",t," ",*num,sep="")