import sys
input = sys.stdin.readline

graph = [[0]*100 for _ in range(100)]

for _ in range(int(input().rstrip())):
    x,y = map(int, input().split())
    for i in range(y,y+10):
        graph[i][x:x+10] = [1]*10

print(sum(map(sum,graph)))