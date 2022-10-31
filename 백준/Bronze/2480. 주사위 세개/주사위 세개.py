a,b,c = map(int,input().split())
dice = [a,b,c]
most = 0;

if dice.count(dice[0]) == 3:
    print(10000+dice[0]*1000)
elif dice.count(dice[0]) == 2:
    print(1000+dice[0]*100)
elif dice.count(dice[1]) == 2:
    print(1000+dice[1]*100)
else:
    for i in range(len(dice)):
        if dice[i] > most: 
            most = dice[i];
    print(most*100)

