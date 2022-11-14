for t in range(1,11):
    N = int(input())
    box = list(map(int, input().split()))

    for i in range(N):
        box = sorted(box, reverse=True)

        if box[0]-box[-1] <= 1:
            break

        box[0] -= 1
        box[-1] += 1
        
    print("#",t," ",max(box)-min(box),sep="")