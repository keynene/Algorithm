import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)

n = int(input().rstrip())
graph = [list(input().rstrip()) for _ in range(n)]
amap = []
rgmap = []
acnt = 0
rgcnt = 0

def dfs(x,y,map,num):
    if x<0 or y<0 or x>=n or y>=n:
        return
    if map[y][x] == 3 and map[y][x] != num:
        return
    elif map[y][x] == num:
        map[y][x] = 3
        dfs(x-1,y,map,num)
        dfs(x,y-1,map,num)
        dfs(x+1,y,map,num)
        dfs(x,y+1,map,num)
        return
    else:
        return


for rgb in graph:
    string = 0
    num = ''
    rgnum = ''
    for string in rgb:
        if string == 'R':
            num += str(0)+' '
            rgnum += str(0)+' '
        elif string == 'B':
            num += str(1)+' '
            rgnum += str(1)+' '
        elif string == 'G':
            num += str(2)+' '
            rgnum += str(0)+' '
    amap.append(list(map(int, num.split())))
    rgmap.append(list(map(int, rgnum.split())))

for y in range(n):
    for x in range(n):
        if amap[y][x] != 3:
            dfs(x,y,amap,amap[y][x])
            acnt += 1
        if rgmap[y][x] != 3:
            dfs(x,y,rgmap,rgmap[y][x])
            rgcnt += 1

print(acnt, rgcnt,sep=' ')