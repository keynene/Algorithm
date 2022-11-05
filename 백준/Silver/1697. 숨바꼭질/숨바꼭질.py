import sys
from collections import deque
sys.setrecursionlimit(100001)

n,k = map(int,input().split())
cnt = 0
visited = [0 for _ in range(100001)]

def bfs(v):
    global cnt
    queue = deque()
    queue.append((v,cnt))

    while queue:
        v,dep = queue.popleft()
        dv = [1,-1,v]

        if v == k:
            print(dep)
            return

        for i in range(3):
            nv = v+dv[i]

            if 0<=nv<=100000 and visited[nv] == 0:
                visited[nv] = dep+1
                queue.append((nv,dep+1))

bfs(n)