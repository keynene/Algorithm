import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)
t = int(input().rstrip())

def dfs(x,y):
    if x<0 or y<0 or x>=n or y>=m:
        return
    if amap[x][y] == 0:
        return
    else:
        amap[x][y] = 0
        dfs(x-1,y)
        dfs(x,y-1)
        dfs(x+1,y)
        dfs(x,y+1)
        return True

for i in range(t):
    cnt = 0
    m,n,k = map(int, input().split())
    amap = [[0 for _ in range(m)] for _ in range(n)]
    node = [list(map(int, input().split())) for _ in range(k)]
    
    for y,x in node:
        amap[x][y] = 1

    #dfs로 방문검사
    for x in range(n):
        for y in range(m):
            if amap[x][y]:
                if dfs(x,y):
                    cnt += 1

    print(cnt)