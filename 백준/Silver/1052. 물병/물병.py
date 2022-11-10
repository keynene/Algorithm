import sys
input = sys.stdin.readline

N,K = map(int, input().split())
buy = 0

while bin(N).count('1') > K:
    N += 1
    buy += 1

print(buy)