import sys
input = sys.stdin.readline

n = int(input().rstrip())
km = list(map(int,input().split()))
won = list(map(int,input().split()))
del won[-1]

p_won = won[0]
money = won[0]*km[0]


for i in range(1,len(won)):
    if won[i] < p_won:
        p_won = won[i]
    money += p_won*km[i]
print(money)