import sys
input = sys.stdin.readline

N = int(input())
vote = [0]+[int(input().rstrip()) for _ in range(N)]
buy = 0

while True:
    if vote.index(max(vote)) == 1 and vote.count(max(vote)) == 1:
        print(buy)
        break
    else:
        maxV = 0
        maxidx = 0
        for i in range(2, N+1):
            if vote[i] > maxV:
                maxV = vote[i]
                maxidx = i
        vote[maxidx] -= 1
        vote[1] += 1
        buy += 1