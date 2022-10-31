N = int(input())

def Han(N):
    if N > 110 : #110보다 클 때 한수는 99에서 더해가야함
        cnt = 99;
        for j in range(110, int(N)+1):
            han_list = list(map(int,str(j))) # [1],[1],[0]
            num_list = [0]*(len(han_list)-1)
            for i in range(len(han_list)):
                if i+1 < len(han_list) :
                    num_list[i] = (han_list[i+1])-(han_list[i])
            if num_list.count(num_list[0]) == (len(han_list)-1) :
                cnt += 1;
    
    elif N < 100 : #100보다 작으면 한수는 N개
        cnt = N;

    else: #100보다 크고 110보다 작을땐 한수는 99개
        cnt = 99;

    return cnt

print(Han(N))