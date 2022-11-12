import sys
input = sys.stdin.readline

N = int(input())
w = [0]+sorted([int(input()) for _ in range(N)], key=lambda x:-x)

maxW = []
for i in range(1,N+1):
    maxW.append(i*w[i])
print(max(maxW))