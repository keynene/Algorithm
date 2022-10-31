import sys
input = sys.stdin.readline

n,m = map(int, input().split())
num = set(input().rstrip() for _ in range(n))
comp = list(input().rstrip() for _ in range(m))

cnt = 0
for i in comp:
    if i in num:
        cnt += 1
print(cnt)
