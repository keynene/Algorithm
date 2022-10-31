N = int(input())

point = []
for i in range(N):
    a,b = map(int, input().split());
    point.append([a,b])
    
point.sort()
for j in range(len(point)):
    print(point[j][0],point[j][1])