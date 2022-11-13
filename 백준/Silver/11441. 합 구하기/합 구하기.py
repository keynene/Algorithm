import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
M = int(input())
prefix = [0]
node = [list(map(int, input().split())) for _ in range(M)]

for i in range(len(arr)):
    prefix.append(prefix[-1]+arr[i])

for left, right in node:
    print(prefix[right]-prefix[left-1])