import sys

tc = int(sys.stdin.readline().strip())
cnt = 0;
num = 0;

while cnt < tc :
    str_num = str(num)
    if str_num.count('666'):
        cnt += 1;
    num +=1;
      
print(num-1)