import sys

C = int(input())
N = 0;

for i in range(C):
    score = list(map(int, sys.stdin.readline().split()))
    avg = (sum(score)-score[0])/score[0];
    cnt = 0;
    for num in score[1:]:
        if num > avg :
            cnt += 1;
    rate = (cnt/score[0])*100
    print(f'{rate:.3f}%')
   
