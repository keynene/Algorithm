import sys
import copy
input = sys.stdin.readline
sys.setrecursionlimit(100000)


n = int(input().rstrip())
amap = [list(map(int,input().split())) for _ in range(n)]
end = max(max(amap)) #end값
maxR = []
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def dfs(x,y,num):

    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        
        if 0<=nx<n and 0<=ny<n and not visited[ny][nx] and amap[ny][nx] > num:
            visited[ny][nx] = True
            dfs(nx,ny,num)

for num in range(end):
    cnt = 0
    visited = [[False]*n for _ in range(n)]
    for y in range(n):
        for x in range(n):
            if amap[y][x] > num and not visited[y][x]:
                dfs(x,y,num)
                cnt +=1
    maxR.append(cnt)
print(max(maxR))