from collections import deque

for _ in range(10):
    t = int(input())
    arr = list(map(int, input().split()))
    queue = deque()
    queue.append(arr)
    cnt = 1

    while queue:
        if cnt > 5:
            cnt = 1

        arr2 = queue.popleft()
        temp = arr2[0]-cnt
        del arr2[0]

        if temp <= 0:
            arr2.append(0)
            print("#",t,sep="",end = " ")
            print(*arr2,sep=" ")
            break
        else:
            arr2.append(temp)
            queue.append(arr2)
            cnt += 1