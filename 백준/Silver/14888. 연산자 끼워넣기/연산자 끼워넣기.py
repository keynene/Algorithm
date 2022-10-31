import sys
input = sys.stdin.readline

maxR = -999999999
minR = 999999999

def dfs(idx, res, sum, sub, mul, div):
    global maxR, minR
    if idx == n:
        maxR = max(res, maxR)
        minR = min(res, minR)
        return 

    if sum:
        dfs(idx+1, res+a[idx], sum-1, sub, mul, div)
    if sub:
        dfs(idx+1, res-a[idx], sum, sub-1, mul, div)
    if mul:
        dfs(idx+1, res*a[idx], sum, sub, mul-1, div)
    if div:
        dfs(idx+1, int(res/a[idx]), sum, sub, mul, div-1)

n = int(input().rstrip())
a = list(map(int, input().split()))
f = list(map(int, input().split()))

dfs(1, a[0], f[0], f[1], f[2], f[3])
print(maxR)
print(minR)