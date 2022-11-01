import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)

n = int(input().rstrip())
hmap = [list(map(int, input().rstrip())) for _ in range(n)]
cnt = 0
res = []

def dfs(x,y):
    global dep
    if x<0 or y<0 or x>=n or y>=n:
        return
    if not hmap[y][x]:
        return
    else:
        dep += 1
        hmap[y][x] = 0
        dfs(x-1,y)
        dfs(x,y-1)
        dfs(x+1,y)
        dfs(x,y+1)
    return

for y in range(n):
    for x in range(n):
        if hmap[y][x]:
            dep = 0
            dfs(x,y)
            cnt += 1
            res.append(dep)
print(cnt, *sorted(res), sep="\n")