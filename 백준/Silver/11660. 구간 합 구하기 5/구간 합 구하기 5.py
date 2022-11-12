import sys
input = sys.stdin.readline

N,M = map(int,input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
node = [list(map(int, input().split())) for _ in range(M)]
prefix = [[0]*(N+1) for _ in range(N+1)]

for x in range(1,N+1):
    for y in range(1,N+1):
        prefix[x][y] = prefix[x-1][y] + prefix[x][y-1] - prefix[x-1][y-1] + arr[x-1][y-1]

for x1, y1, x2, y2 in node:
    print(prefix[x2][y2] - prefix[x1-1][y2] - prefix[x2][y1-1] + prefix[x1-1][y1-1])