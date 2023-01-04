import sys
input = sys.stdin.readline

#2차원배열로 0으로 초기화해놓고 색종이 받으면서 1로 칠하고 1의 개수를 출력하자

graph = [[0]*100 for _ in range(100)]
node = []

for _ in range(int(input().rstrip())):
    x,y = map(int, input().split())
    for i in range(y,y+10):
        for j in range(x,x+10):
            graph[i][j] = 1

print(sum(map(sum,graph)))