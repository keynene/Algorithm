import sys
input  = sys.stdin.readline

H,W = map(int,input().split())
space = [list(input().rstrip()) for _ in range(H)]

for y in range(H):
    cnt = 0
    for x in range(W):
        if cnt == 0 and space[y][x] == '.':
            space[y][x] = '-1'
        elif space[y][x] == 'c':
            space[y][x] = '0'
            cnt = 1
        else:
            space[y][x] = str(cnt)
            cnt += 1

for y in range(H):
    for x in range(W):
        print(space[y][x], end=" ")
    print()