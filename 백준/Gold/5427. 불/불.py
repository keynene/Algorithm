import sys
from collections import deque
input = sys.stdin.readline

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(arr):
    queue = deque()

    for x,y,type,dep in arr:
        queue.append((x,y,type,dep))
    

    while queue:
        x,y,type,dep = queue.popleft()
        if (x == 0 or y == 0 or x == w-1 or y == h-1) and building[y][x] == '@':
            print(dep+1)
            return
        
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]

            if type==0 and 0<=nx<w and 0<=ny<h and building[ny][nx]=='.' and building[ny][nx] != '@' :
                building[ny][nx] = '@'
                queue.append((nx,ny,type,dep+1))

            if type==1 and 0<=nx<w and 0<=ny<h and building[ny][nx] != '#' and building[ny][nx] != '*':
                building[ny][nx] = '*'
                queue.append((nx,ny,type,dep+1))

    print("IMPOSSIBLE")



for _ in range(int(input())):
    w,h = map(int, input().split())
    building = [list(map(str, input().rstrip())) for _ in range(h)]
    temp = []

    for y in range(h):
        for x in range(w):
            if building[y][x] == '@':
                temp.append([x,y,0,0])
    
    for y in range(h):
        for x in range(w):
            if building[y][x] == '*':
                temp.append([x,y,1,0])

    bfs(temp)