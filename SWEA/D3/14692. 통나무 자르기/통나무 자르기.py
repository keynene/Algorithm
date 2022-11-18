for t in range(int(input())):
    N = int(input())
    ans = 'Bob'
    if N%2 == 0:
        ans = 'Alice'

    print(f'#{t+1} {ans}')