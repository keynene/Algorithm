import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)

n,m,k = map(int, input().split())
trash = [list(map(int, input().split())) for _ in range(k)]

amap = [[0 for _ in range(m)] for _ in range(n)]

def dfs(r,c):
    global dep
    if r<0 or c<0 or r>=n or c>=m:
        return
    if not amap[r][c]:
        return
    else:
        dep += 1
        amap[r][c] = 0
        dfs(r-1,c)
        dfs(r,c-1)
        dfs(r+1,c)
        dfs(r,c+1)
        return 

for r,c in trash:
    amap[r-1][c-1] = 1

res = []
for r in range(n):
    for c in range(m):
        if amap[r][c]:
            dep = 0
            dfs(r,c)
            res.append(dep)

print(max(res))