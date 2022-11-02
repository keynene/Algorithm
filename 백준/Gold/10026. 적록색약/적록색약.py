import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

n = int(input().rstrip())
rgb = [list(map(str, input().rstrip())) for _ in range(n)]
amap = []
visited = [[0 for _ in range(n)] for _ in range(n)]
cnt = 0
res = []

def dfs(x,y,num):
    if x<0 or y<0 or x>=n or y>=n:
        return
    if visited[y][x] == 1 or amap[y][x] != num:
        return
    elif amap[y][x] == num:
        visited[y][x] = 1
        if num == 2:
            amap[y][x] = 0
        dfs(x-1,y,num)
        dfs(x,y-1,num)
        dfs(x+1,y,num)
        dfs(x,y+1,num)
        return
    

for string in rgb:
    num = ''
    for al in string:
        if al == 'R':
            num += str(0)+' '
        elif al == 'B':
            num += str(1)+' '
        elif al == 'G':
            num += str(2)+' '
    amap.append(list(map(int, num.split())))

for y in range(n):
    for x in range(n):
        if not visited[y][x]:
            dfs(x,y,amap[y][x])
            cnt += 1
res.append(cnt)

cnt = 0
visited = [[0 for _ in range(n)] for _ in range(n)]
for y in range(n):
    for x in range(n):
        if not visited[y][x]:
            dfs(x,y,amap[y][x])
            cnt += 1
res.append(cnt)
print(*res)