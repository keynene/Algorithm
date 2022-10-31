N = int(input())

point = []
for i in range(N):
    a,b = map(int, input().split());
    point.append([b,a]);

point.sort();

for j in range(len(point)):
    print(point[j][1],point[j][0]);

