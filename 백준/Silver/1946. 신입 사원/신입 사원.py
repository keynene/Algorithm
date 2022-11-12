import sys
input = sys.stdin.readline

for _ in range(int(input())):
    N = int(input())
    people = sorted([list(map(int,input().split())) for _ in range(N)])
    success = [people[0]]

    for i in range(1,len(people)):
        if people[i][1] < success[-1][1]:
            success.append(people[i])
    
    print(len(success))