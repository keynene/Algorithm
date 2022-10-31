T = int(input());
num = [input() for _ in range(T)]

for i in range(T):
    n = int(num[i])
    while n >= 10 :
        n = sum(map(int,str(n)))
    print('#',i+1,' ',n, sep="")