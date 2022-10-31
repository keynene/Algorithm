N = int(input())
for i in range(N):
    arr = list(input())
    score = 0;
    sum_score = 0;
    for j in arr:
        if j == 'O':
            score += 1
            sum_score += score
        else:
            score = 0
    print(sum_score)