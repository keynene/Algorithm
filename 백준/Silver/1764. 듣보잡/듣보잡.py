import sys
input = sys.stdin.readline

n,m = map(int, input().split())

dud = set(input().strip() for _ in range(n))
bo = set(input().strip() for _ in range(m))
dud_bo = sorted(dud&bo)

print(len(dud_bo))
for i in dud_bo:
    print(i)
