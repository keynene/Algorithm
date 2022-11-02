import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

def dfs(v):
    global result
    visited[v] = True
    cycle.append(v)
    num = number[v]

    if visited[num]:
        if num in cycle:
            result += cycle[cycle.index(num):]
        return
    else:
        dfs(num)

for _ in range(int(input().rstrip())):
    N = int(input().rstrip())
    number = [0] + list(map(int, input().split()))
    visited = [True] + [False]*N
    result = []

    for i in range(1,N+1):
        if not visited[i]:
            cycle = []
            dfs(i)

    print(N-len(result))
