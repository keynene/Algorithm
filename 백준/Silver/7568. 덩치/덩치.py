import sys

tc = int(sys.stdin.readline())
person = []

for _ in range(tc):
    a, b = map(int,sys.stdin.readline().split())
    person.append([a,b])

for info in person: 
    rank = 1;
    for compare_info in person:
        if info[0] < compare_info[0] and info[1] < compare_info[1]:
            rank += 1
    print(rank, end=' ')
