import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)

m,n,k = map(int, input().split())
node = [list(map(int,input().split())) for _ in range(k)]
amap = [[0 for _ in range(n)] for _ in range(m)]
cnt = 0
res = []

def dfs(x,y):
    global dep
    if x<0 or y<0 or x>=n or y>=m:
        return
    if amap[y][x]:
        return
    else:
        dep += 1
        amap[y][x] = 1
        dfs(x-1,y)
        dfs(x,y-1)
        dfs(x+1,y)
        dfs(x,y+1)
    return

for sx,sy,ex,ey in node:
    for x in range(sx,ex):
        for y in range(sy,ey):
            amap[y][x] = 1

for y in range(m):
    for x in range(n):
        if not amap[y][x]:
            dep = 0
            dfs(x,y)
            res.append(dep)
            cnt += 1
print(cnt)
print(*sorted(res))