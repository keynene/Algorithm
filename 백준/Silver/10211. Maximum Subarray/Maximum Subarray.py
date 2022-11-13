for _ in range(int(input())):
    n = int(input())
    data = list(map(int,input().split())) 

    for i in range(1,n):
        if data[i-1] > 0:
            data[i] += data[i-1]
    
    print(max(data))