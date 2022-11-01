import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)

t = int(input().rstrip())

def dfs(y,x):
    if x<0 or y<0 or x>=m or y>=n:
        return
    if not amap[y][x]:
        return
    else:
        amap[y][x] = 0
        dfs(y-1,x)
        dfs(y,x-1)
        dfs(y+1,x)
        dfs(y,x+1)
        return True


for _ in range(t):
    cnt = 0
    m,n,k = map(int, input().split())
    node = [list(map(int, input().split())) for _ in range(k)]
    amap = [[0 for _ in range(m)] for _ in range(n)]

    for x,y in node:
        amap[y][x] = 1

    for y in range(n):
        for x in range(m):
            if amap[y][x]:
                dfs(y,x)
                cnt += 1
    print(cnt)