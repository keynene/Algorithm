for t in range(int(input())):
    N,K = map(int,input().split())
    lst = list(map(int,input().split()))
    ans = []

    for i in range(1,N+1):
        if i not in lst:
            ans.append(i)

    print("#",t+1,sep="",end=" ")
    for i in ans:
        print(i,end=" ")
    print()