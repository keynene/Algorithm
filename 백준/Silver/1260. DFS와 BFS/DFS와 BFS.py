import sys
from collections import deque
input = sys.stdin.readline

n,m,v = map(int, input().split())
node = [list(map(int, input().split())) for _ in range(m)]
matrix = [[0]*(n+1) for _ in range(n+1)] #인접행렬

for x,y in node:
    matrix[y][x] = matrix[x][y] = 1

d_visited = [False]*(n+1)
def dfs(v):
    print(v, end=' ')
    d_visited[v] = True

    for i in range(1, n+1):
        if not d_visited[i] and matrix[v][i]:
            dfs(i)


b_visited = [False]*(n+1)
def bfs(v):
    queue = deque([v])
    b_visited[v] = True

    while queue:
        v = queue.popleft()
        print(v, end=' ')

        for i in range(1, n+1):
            if not b_visited[i] and matrix[v][i] == 1:
                queue.append(i)
                b_visited[i] = True

dfs(v)
print()
bfs(v)