import sys
from collections import deque
input = sys.stdin.readline

F,S,G,U,D = map(int, input().split())
visited_building = [False]*(F+1)
dv = [U,-1*D]

def bfs(v):
    queue = deque()
    queue.append((v,0))
    visited_building[v] = True

    while queue:
        v,dep = queue.popleft()

        if v == G:
            print(dep)
            return

        for i in range(2):
            nv = v+dv[i]

            if v == nv:
                continue

            elif 0<nv<=F and not visited_building[nv]:
                visited_building[nv] = True
                queue.append((nv,dep+1))

    print("use the stairs")

bfs(S)