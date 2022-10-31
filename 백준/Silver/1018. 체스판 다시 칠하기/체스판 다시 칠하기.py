import sys

n, m = map(int,sys.stdin.readline().split())
chess = []

for i in range(n):
    chess.append(sys.stdin.readline().strip())

result = []
for i in range(n-7):
    for j in range(m-7):
        cnt_B = 0;
        cnt_W = 0;
        for a in range(i, i+8):
            for b in range(j, j+8):
                if (a+b)%2 == 0 :
                    if chess[a][b] == 'B' :
                        cnt_W += 1;
                    else:
                        cnt_B += 1;
                else:
                    if chess[a][b] == 'B' :
                        cnt_B += 1;
                    else:
                        cnt_W += 1;
        result.append(cnt_B)
        result.append(cnt_W)
print(min(result))