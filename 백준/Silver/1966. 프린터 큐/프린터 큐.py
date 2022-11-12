import sys
from collections import deque
input = sys.stdin.readline

for _ in range(int(input())):
    N, M = map(int,input().split())
    imfort = list(map(int, input().split()))
    cnt = 0

    queue = deque()

    for i in range(N):
        queue.append((i, imfort[i]))

    while queue:
        idx, imfo = queue.popleft()

        if imfo == max(imfort):
            cnt += 1
            if idx == M:
                print(cnt)
                break
            else:
                imfort[idx] = 0
        else:
            queue.append((idx, imfo))