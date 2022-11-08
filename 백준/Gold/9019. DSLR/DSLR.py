import sys
from collections import deque
input = sys.stdin.readline

def bfs(x):
    ans = []
    temp = ''
    queue = deque()
    queue.append((x,''))


    while queue:
        x,temp = queue.popleft()
        visited[x] = True

        if x == B:
            ans.append(temp)
            print(*ans,sep="")
            return
        
        if len(str(x)) == 1:
            d1,d2,d3,d4 = '0','0','0',str(x)
        elif len(str(x)) == 2:
            d1,d2 = '0','0'
            d3,d4 = map(str, str(x))
        elif len(str(x)) == 3:
            d1 = '0'
            d2,d3,d4 = map(str, str(x))
        else:
            d1,d2,d3,d4 = map(str, str(x))

        for type in range(4):
            if type == 0:
                dx = 2*int(d1+d2+d3+d4)
                if dx > 9999 : dx = dx%10000
                if not visited[dx]:
                    queue.append((dx,temp+"D"))
                    visited[dx] = True
            elif type == 1:
                if x == 0 : dx = 9999
                else: dx = int(d1+d2+d3+d4)-1
                if not visited[dx]:
                    queue.append((dx,temp+"S"))
                    visited[dx] = True
            elif type == 2:
                dx = int(str(d2)+str(d3)+str(d4)+str(d1))
                if not visited[dx]:
                    queue.append((dx,temp+"L"))
                    visited[dx] = True
            elif type == 3:
                dx = int(str(d4)+str(d1)+str(d2)+str(d3))
                if not visited[dx]:
                    queue.append((dx,temp+"R"))
                    visited[dx] = True

for _ in range(int(input())):
    A, B = map(int,input().split())
    visited = [False]*10000
    
    bfs(A)