import sys
from collections import deque
input = sys.stdin.readline

dx = [1,-1,0,0,0,0]
dy = [0,0,1,-1,0,0]
dz = [0,0,0,0,-1,1]

def bfs(x,y,z):
    queue = deque()
    queue.append((x,y,z,0))

    while queue:
        x,y,z,dep = queue.popleft()

        if x==ex and y==ey and z==ez:
            print("Escaped in",dep,"minute(s).")
            return
        
        for i in range(6):
            nx = x+dx[i]
            ny = y+dy[i]
            nz = z+dz[i]

            if 0<=nx<C and 0<=ny<R and 0<=nz<L and (building[nz][ny][nx]=='.' or building[nz][ny][nx]=='E'):
                building[nz][ny][nx] = dep+1
                queue.append((nx,ny,nz,dep+1))
    print("Trapped!")

while True:
    L,R,C = map(int, input().split())
    building = []
    sp = 0

    if L==0 and R==0 and C==0:
        break
    else:
        for z in range(L):
            temp = []
            for y in range(R+1):
                temp.append(list(map(str, input().rstrip())))
            temp.pop()
            building.append(list(temp))

        for z in range(L):
            for y in range(R):
                for x in range(C):
                    if building[z][y][x] == 'E':
                        ex, ey, ez = x, y, z

        for z in range(L):
            for y in range(R):
                for x in range(C):
                    if building[z][y][x] == 'S':
                        bfs(x,y,z)