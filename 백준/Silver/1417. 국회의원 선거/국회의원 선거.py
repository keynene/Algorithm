
import sys
input = sys.stdin.readline

N = int(input())
vote = [0]+[int(input().rstrip()) for _ in range(N)]
buy = 0
idx = 0

while True:
    maxV = max(vote)
    if vote.count(maxV) == 1 and vote.index(maxV) == 1:
        print(buy)
        break
    else:
        for i in range(2,len(vote)):
            if vote[i] == maxV:
                idx = i
                break
        vote[idx] -= 1
        vote[1] += 1
        buy += 1