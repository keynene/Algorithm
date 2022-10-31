import sys
input = sys.stdin.readline

n = int(input().rstrip())
time = sorted(list(map(int,input().split())))

for i in range(1,n):
    time[i] += time[i-1]

print(sum(time))