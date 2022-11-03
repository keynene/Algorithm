# [Silver III] 베르트랑 공준 - 4948 

[문제 링크](https://www.acmicpc.net/problem/4948) 

### 성능 요약

메모리: 115732 KB, 시간: 336 ms

### 분류

수학(math), 정수론(number_theory), 소수 판정(primality_test), 에라토스테네스의 체(sieve)

### 문제 설명

<p>베르트랑 공준은 임의의 자연수 n에 대하여, n보다 크고, 2n보다 작거나 같은 소수는 적어도 하나 존재한다는 내용을 담고 있다.</p>

<p>이 명제는 조제프 베르트랑이 1845년에 추측했고, 파프누티 체비쇼프가 1850년에 증명했다.</p>

<p>예를 들어, 10보다 크고, 20보다 작거나 같은 소수는 4개가 있다. (11, 13, 17, 19) 또, 14보다 크고, 28보다 작거나 같은 소수는 3개가 있다. (17,19, 23)</p>

<p>자연수 n이 주어졌을 때, n보다 크고, 2n보다 작거나 같은 소수의 개수를 구하는 프로그램을 작성하시오. </p>

### 입력 

 <p>입력은 여러 개의 테스트 케이스로 이루어져 있다. 각 케이스는 n을 포함하는 한 줄로 이루어져 있다.</p>

<p>입력의 마지막에는 0이 주어진다.</p>

### 출력 

 <p>각 테스트 케이스에 대해서, n보다 크고, 2n보다 작거나 같은 소수의 개수를 출력한다.</p>

## 📖[Python/파이썬] [🥈3] 백준 알고리즘 4948 - 베르트랑 공준
### 📜문제
![](https://velog.velcdn.com/images/keynene/post/3d6d24ab-fe92-469e-97b1-86ef9de1e540/image.png)
![](https://velog.velcdn.com/images/keynene/post/4d801a4a-6220-40b6-8bba-f72fbe79e0f0/image.png)

* * *

### 📕풀이방향
문제에서 주어진 범위(1 ≤ n ≤ 123,456)를 주의하자 (2n까지이므로 246,912까지..)
가장 최악의 O(N)을 생각해보자 (n=123,456이고 2n=246,912 ..)

[내 포스팅 : [Python] 백준 알고리즘 1929 - 소수 구하기](https://velog.io/@keynene/Python-%EB%B0%B1%EC%A4%80-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-1929-%EC%86%8C%EC%88%98-%EA%B5%AC%ED%95%98%EA%B8%B0)
전에 소수구하기 문제를 푼 적이 있는데, 이런식으로 접근하면 이번에는 시간초과🤦🏻‍♀️

우선 2n이 기준이므로 2~246,912까지 소수를 모두 list(num)에 저장하자
무한루프로 n값이 0아니면 num에 접근하여 n~2n까지 검사하면서,
소수가 존재하면 res+1를 하여 res를 출력하자

* * *

### 📝알고리즘 구현순서
1. 2~246,912까지 소수를 list(num)에 저장하기
2. 무한루프로 n==0이면 break, 아니면 num요소를 n~2n까지 검사하면서 res++ 해주기

* * *

### 💻결과코드
```python
num = []

for i in range(2, 246913):
    cnt = 0

    for p in range(2, int(i**0.5)+1):
        if i % p == 0:
            cnt += 1
            break

    if cnt == 0:
        num.append(i)

while True:
    n = int(input())
    res = 0

    if n == 0:
        break

    for i in num:
        if n < i <= 2*n:  # if i > n and i <=2*n과 같음
            res += 1

    print(res)
```

* * *

#### ✏️1. 2~246,912까지 소수를 list(num)에 저장하기
```python
num = [] #빈리스트

for i in range(2, 246913):
    cnt = 0

    for p in range(2, int(i**0.5)+1): 
        if i % p == 0: 
            cnt += 1
            break #cnt가 0이 아니면 소수아님

    if cnt == 0: #cnt가 0이면 소수이므로 num에 저장
        num.append(i)
```

* * *

#### ✏️2. 무한루프로 list(num)의 개수 출력
```python
while True:
    n = int(input())
    res = 0

    if n == 0:  #0이면 종료
        break

    for i in num: #num요소 하나씩 검사
        if n < i <= 2*n: #i가 n보다 크고 2n보다 작은 값일때마다 res++
            res += 1

    print(res)
```

* * *

### 📚초기 알고리즘 오류와 정리
※초기 알고리즘
#### ✍🏻소수구하는 함수 구현, n값 입력될 때마다 n~2n소수 검사 후 cnt++
```python
import sys
input = sys.stdin.readline

def gj(n):
    for j in range(2,int((n**0.5))+1):
        if n%j == 0:
            return False
    return True

cnt = 0

while True:
    n = int(input().rstrip())
    cnt = 0
    if n == 0:
        break
    else:
        for i in range(n+1,(2*n)+1):
            if gj(i):
                cnt += 1
        print(cnt)
```
```
※구현순서
  1. 소수구하는 gj()함수 만들어놓기
  2. n입력값에따라 함수를 n~2n까지 호출하여 cnt++
```
👉🏻 n값이 들어올 때마다 <span style="color:red">n~2n까지 소수를 계속해서 계산</span>해야 하므로 시간초과🤦🏻‍♀️

* * *

1. 초기 알고리즘 설계가 매우 중요하다
   이 때까지는 모든 케이스를 브루트포스로 계산하다가 오류가 나기 일쑤였는데,
   위 문제는, 주어진 모든 케이스를 저장해두고 꺼내쓰는 것이 더 빠르다....
   ```👉🏻 구현 전 알고리즘 설계 과정에서 과연 어떤 알고리즘이 적합한지 판단하는 연습하자```
   