# [Silver V] 소수 - 2581 

[문제 링크](https://www.acmicpc.net/problem/2581) 

### 성능 요약

메모리: 114488 KB, 시간: 800 ms

### 분류

수학(math), 정수론(number_theory), 소수 판정(primality_test)

### 문제 설명

<p>자연수 M과 N이 주어질 때 M이상 N이하의 자연수 중 소수인 것을 모두 골라 이들 소수의 합과 최솟값을 찾는 프로그램을 작성하시오.</p>

<p>예를 들어 M=60, N=100인 경우 60이상 100이하의 자연수 중 소수는 61, 67, 71, 73, 79, 83, 89, 97 총 8개가 있으므로, 이들 소수의 합은 620이고, 최솟값은 61이 된다.</p>

### 입력 

 <p>입력의 첫째 줄에 M이, 둘째 줄에 N이 주어진다.</p>

<p>M과 N은 10,000이하의 자연수이며, M은 N보다 작거나 같다.</p>

### 출력 

 <p>M이상 N이하의 자연수 중 소수인 것을 모두 찾아 첫째 줄에 그 합을, 둘째 줄에 그 중 최솟값을 출력한다. </p>

<p>단, M이상 N이하의 자연수 중 소수가 없을 경우는 첫째 줄에 -1을 출력한다.</p>

## 📖[Python/파이썬] [🥈5] 백준 알고리즘 2581 - 소수
### 📜문제
![](https://velog.velcdn.com/images/keynene/post/187d93f8-d91f-472c-887e-f9e2fd9ac28d/image.png)
![](https://velog.velcdn.com/images/keynene/post/da6f9d79-2884-42f7-a236-d0e17b0ca3f4/image.png)

* * *

### 📕풀이방향
입력값m,n과 number(m~n까지)리스트로 저장하자
sosu라는 리스트를 만들어서 소수를 저장할껀데,
number[x]를 순서대로 '2~(number[x]-1)'로 나눠보면서 나머지가 0인 수가 존재하지 않으면
<span style="color:red">(number[x]를 '2~number[x]-1'까지 나눴을 때 나누어 떨어지는 수가 존재하지 않으면)</span> 
소수이므로 sosu에 저장하고
나머지가 0인 수가 존재하면 소수가 아니므로 저장하지 않고 넘어가게 구현하자

* * *

### 📝알고리즘 구현순서
1. m, n, number저장, sosu 빈리스트 선언하기
2. number[x]가 '2~number[x]-1'로 나누어떨어지면 소수X, 아니면 sosu에 저장하고
   소수합 <code>sum(sosu)</code>과 최소값<code>sosu[0]</code>을 출력하자
   
* * *

### 💻결과코드
```python
import sys
input = sys.stdin.readline

m = int(input().rstrip())
n = int(input().rstrip())
number = [i for i in range(m,n+1)] #m~n까지 저장(검색용)
sosu = [] #저장용

for num in number:
    err = 0
    if num > 1: #1은 소수가 아니니까 패스
    
    	#소수가 아닌경우 err += 1
        for i in range(2,num):
            if num % i == 0:
                err += 1
                
        #소수인경우 sosu에 값 저장
        if err == 0:
            sosu.append(num)
if len(sosu) == 0:
    print(-1)
else:
    print(sum(sosu),sosu[0], sep="\n")
```

* * *

#### ✏️1. 입력값저장, number(검사리스트) 및 sosu(저장리스트) 선언
```python
import sys
input = sys.stdin.readline

m = int(input().rstrip())
n = int(input().rstrip())
number = [i for i in range(m,n+1)]
sosu = []

```
※m~n값 number에 저장하는 다른 방법
```python
number = []
for i in range(m,n+1):
  number.append(i)

현예제에서는 굳이 .append()를 사용하지 않고 
본코드대로 한줄에 입력받으면서 저장하는 것이 효과적이나,
입력받으면서 추가 계산을 하고 저장할 때는 위와 같은 방법이 효과적일 수 있음
```

* * *

#### ✏️2. 소수인 값 / 소수가 아닌 값 분리하여 저장 및 출력
```python
for num in number:
	#소수를 판별하는 err값 초기화
    err = 0
    
    #1은 소수가 아니므로 1이상의 수만 확인
    if num > 1:
        for i in range(2,num): #2~num-1까지 i를
            if num % i == 0:   #num에 나눠서 나머지 값이 0이면
                err += 1       #err += 1하여 소수가 아님을 판별!
        if err == 0:           #왜냐면 err == 0(나누어떨어지는 값이 없는 수만)
            sosu.append(num)   #sosu리스트에 추가할꺼니까!
            
if len(sosu) == 0: #sosu에 저장된 값이 없을 때 (초기값과 같이 빈리스트일 때)
    print(-1)
else: #빈리스트가 아니면 합계, 최소값 출력
    print(sum(sosu),sosu[0], sep="\n")
```

* * *

### 📚정리
개념은 알고있으므로 크게 어려운 문제는 아니었는데 소수를 어떻게 구현하는지가 관건이었음
소수는 <span style="color:red">2이상인 수에 나누어 떨어지지 않는 수</span>이므로, 
말 그대로 <span style="color:red">'2~자기자신-1'까지 나누면서 검사</span>하는 반복문을 돌려 완성하였음
이보다 덜 무식하고 빠른 방법이 있겠지만, 
가장 빠르게 떠올랐고 빨리 구현할 수 있는 방법이었으므로 패스....