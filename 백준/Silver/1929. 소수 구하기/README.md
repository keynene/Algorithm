# [Silver III] 소수 구하기 - 1929 

[문제 링크](https://www.acmicpc.net/problem/1929) 

### 성능 요약

메모리: 117128 KB, 시간: 948 ms

### 분류

수학(math), 정수론(number_theory), 소수 판정(primality_test), 에라토스테네스의 체(sieve)

### 문제 설명

<p>M이상 N이하의 소수를 모두 출력하는 프로그램을 작성하시오.</p>

### 입력 

 <p>첫째 줄에 자연수 M과 N이 빈 칸을 사이에 두고 주어진다. (1 ≤ M ≤ N ≤ 1,000,000) M이상 N이하의 소수가 하나 이상 있는 입력만 주어진다.</p>

### 출력 

 <p>한 줄에 하나씩, 증가하는 순서대로 소수를 출력한다.</p>

## 📖[Python/파이썬] [🥈3] 백준 알고리즘 1929 - 소수 구하기
### 📜문제
![](https://velog.velcdn.com/images/keynene/post/9e77f5ff-19c5-4c44-bb31-ad62bafe79b1/image.png)

* * *

### 📕풀이방향
[내 포스팅 : [Python] 백준 알고리즘 2581 - 소수](https://velog.io/@keynene/Python-%EB%B0%B1%EC%A4%80-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-2581-%EC%86%8C%EC%88%98)
전에 소수에 대해 다룬 문제가 있는데 이렇게 구현하다가 <span style="color:red">시간초과...</span>라는 수모를 겪게됨😭

👉🏻비교범위를 좁혀야한다!
해당 수(num)를 '2부터 num의 <span style="color:red">제곱근</span>'만큼만 나눠보면서 소수인지 판별해보자
(num**0.5까지만 비교해도 소수인지 아닌지는 판별 가능기 때문에!)

하지만, 제곱근을 이용해도 시간초과가 나는 경우가 있다❓
👉🏻문제의 N,M의 범위가 (1 ≤ M ≤ N ≤ 1,000,000)이다
  만약 2중for문으로 구현했다면 → <span style="color:red">for문 2개</span>로 나눠주자
  ```python
  for:
    for: 
      print() #2중for문을 거쳐서 하나씩 출력하므로 
              #O(백만*백만) = O(백만^2)이 되어버림 ㅠㅠ
      
      
   ↓ (해결방법 : 함수를 쓰면 간단히 해결)
   
   
  def prime():
    for: #1중for문으로 일부 해결하고
      return
      
  for: #함수 밖에서 1중for문으로 prime()을 호출하는 방식이므로
    prime()   #O(백만+백만) = O(백만)이 된다!!!
    
  ```

* * *

### 📝알고리즘 구현순서
1. m,n을 입력받고 <code>def sosu(num)</code>을 이용하여 num이 소수면 <code>true</code>, 소수가 아니면 <code>false</code>를 <code>return</code>하는 함수를 만들자
2. m~n까지도는 반복문 i를 'if sosu(i):'하여 소수일때만 출력하자
※조건문(if)은 <span style="color:blue">true</span>일때만 동작하므로!

* * *

### 💻결과코드
```python
import sys
m,n = map(int, sys.stdin.readline().split())

def sosu(num):
    if num == 1: return False
    else:
        for i in range(2, int(num**0.5)+1): #제곱근으로 비교
            if num % i == 0:
                return False
        return True

for i in range(m, n+1):
    if sosu(i):
        print(i)
```

* * *

#### ✏️1. m,n 입력받고 소수판별하는 함수 sosu 정의
```python
import sys
m,n = map(int, sys.stdin.readline().split())

def sosu(num):
    if num == 1: return False #1이면 소수가 아니므로 False
    
    else:
    	#i를 2부터 ※num의 제곱근+1(이유는 아래 설명)으로 지정
        for i in range(2, int(num**0.5)+1):
        
        	#i로 나누어 떨어지면 False
            if num % i == 0:
                return False
                
        #소수이면 True
        return True
```
풀이는 아래블로그 참고하였음!
https://imdona.tistory.com/m/25
```
※i범위를 num의 제곱근까지 하는 이유?

전체케이스를 검사하면 위에서 언급한 것과 같이 "시간초과"가 발생한다
(아무래도 문제에서 1,000,000(백만)경우의 수인데, 
for문을 통하면 백만*백만이 되므로 문제가 될 것 같긴했음)

👉🏻제곱근까지만 계산하더라도 소수인지 아닌지는 판별이 가능하다.



※int(num**0.5)이 아니라 int(num**0.5)+1?

int(num**0.5)으로 진행할 경우, (num**0.5)값이 n.n 즉, 소수일 때 소수점 아랫자리를 절삭해버리므로
한가지 케이스를 아예 배제해버리는 상황이 발생하기 때문에 int(num**0.5)+1로 진행!
  
```

* * *

#### ✏️2. for문을 통해 sosu()함수 호출하여 소수만 출력하기
```python
for i in range(m, n+1):
    if sosu(i):
        print(i)
```
```
※조건문(if)는 true일때만 동작하는데 sosu함수 return값이 true/false이므로
  소수일때만(treu) print문을 통해 출력해준다
```

* * *

### 📚초기 알고리즘 오류와 정리
※초기 알고리즘
#### 1. 제곱근을 다루기 전 알고리즘
[내 포스팅 : [Python] 백준 알고리즘 2581 - 소수](https://velog.io/@keynene/Python-%EB%B0%B1%EC%A4%80-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-2581-%EC%86%8C%EC%88%98)
전에 한 번 다뤘으므로 패스 (똑같은 실수를 반복하지 말자)

#### 2. 제곱근을 사용하였는데도 시간초과가 떠버린 알고리즘(2중for문, O(백만^2))
```python
import sys
input = sys.stdin.readline

m,n = map(int,input().split())

for i in range(m,n+1):
    err = 0
    for j in range(2, int(i**0.5)+1):
        if i > 1:
            if i%j == 0:
                err += 1
    if err == 0:
        print(i)
```
```
알고리즘 맞왜틀(맞는데 왜 틀림?)단계에서 흔히 하는 실수라고 한다.
문제에서 주어진 변수의 범위(1 ≤ M ≤ N ≤ 1,000,000)에 주의하자!!
위 오류코드는 O(백만*백만) = O(백만^2)이므로 당연히 시간초과 될 것이다🤦🏻‍♀️
```
* * *

1. 소수를 구하는 알고리즘은 따로 외워두자 <span style="color:red">(제곱은만큼만 나누기!)</span>
2. 조건문(if)는 <code>True</code>일때만 동작한다 (함수나 딕셔너리 구현시 참고)
3. 문제에서 주어진 범위를 먼저 보고 알고리즘을 설계하자 
   ```'백만*백만'은 딱봐도 오답같잖아.... 다른 알고리즘이 있나 찾아보는 시야를 기르자...```