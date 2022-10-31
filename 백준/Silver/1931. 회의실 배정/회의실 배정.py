import sys
input = sys.stdin.readline

n = int(input())
conf = sorted([list(map(int,input().split())) for _ in range(n)], key=lambda x:(x[1],x[0]))
max_conf = [0]


for time in conf:
    if time[0] >= max_conf[-1]:
        max_conf.append(time[1])
print(len(max_conf)-1)