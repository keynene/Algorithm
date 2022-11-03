# [Silver I] 연산자 끼워넣기 - 14888 

[문제 링크](https://www.acmicpc.net/problem/14888) 

### 성능 요약

메모리: 118648 KB, 시간: 204 ms

### 분류

백트래킹(backtracking), 브루트포스 알고리즘(bruteforcing)

### 문제 설명

<p>N개의 수로 이루어진 수열 A<sub>1</sub>, A<sub>2</sub>, ..., A<sub>N</sub>이 주어진다. 또, 수와 수 사이에 끼워넣을 수 있는 N-1개의 연산자가 주어진다. 연산자는 덧셈(+), 뺄셈(-), 곱셈(×), 나눗셈(÷)으로만 이루어져 있다.</p>

<p>우리는 수와 수 사이에 연산자를 하나씩 넣어서, 수식을 하나 만들 수 있다. 이때, 주어진 수의 순서를 바꾸면 안 된다.</p>

<p>예를 들어, 6개의 수로 이루어진 수열이 1, 2, 3, 4, 5, 6이고, 주어진 연산자가 덧셈(+) 2개, 뺄셈(-) 1개, 곱셈(×) 1개, 나눗셈(÷) 1개인 경우에는 총 60가지의 식을 만들 수 있다. 예를 들어, 아래와 같은 식을 만들 수 있다.</p>

<ul>
	<li>1+2+3-4×5÷6</li>
	<li>1÷2+3+4-5×6</li>
	<li>1+2÷3×4-5+6</li>
	<li>1÷2×3-4+5+6</li>
</ul>

<p>식의 계산은 연산자 우선 순위를 무시하고 앞에서부터 진행해야 한다. 또, 나눗셈은 정수 나눗셈으로 몫만 취한다. 음수를 양수로 나눌 때는 C++14의 기준을 따른다. 즉, 양수로 바꾼 뒤 몫을 취하고, 그 몫을 음수로 바꾼 것과 같다. 이에 따라서, 위의 식 4개의 결과를 계산해보면 아래와 같다.</p>

<ul>
	<li>1+2+3-4×5÷6 = 1</li>
	<li>1÷2+3+4-5×6 = 12</li>
	<li>1+2÷3×4-5+6 = 5</li>
	<li>1÷2×3-4+5+6 = 7</li>
</ul>

<p>N개의 수와 N-1개의 연산자가 주어졌을 때, 만들 수 있는 식의 결과가 최대인 것과 최소인 것을 구하는 프로그램을 작성하시오.</p>

### 입력 

 <p>첫째 줄에 수의 개수 N(2 ≤ N ≤ 11)가 주어진다. 둘째 줄에는 A<sub>1</sub>, A<sub>2</sub>, ..., A<sub>N</sub>이 주어진다. (1 ≤ A<sub>i</sub> ≤ 100) 셋째 줄에는 합이 N-1인 4개의 정수가 주어지는데, 차례대로 덧셈(+)의 개수, 뺄셈(-)의 개수, 곱셈(×)의 개수, 나눗셈(÷)의 개수이다. </p>

### 출력 

 <p>첫째 줄에 만들 수 있는 식의 결과의 최댓값을, 둘째 줄에는 최솟값을 출력한다. 연산자를 어떻게 끼워넣어도 항상 -10억보다 크거나 같고, 10억보다 작거나 같은 결과가 나오는 입력만 주어진다. 또한, 앞에서부터 계산했을 때, 중간에 계산되는 식의 결과도 항상 -10억보다 크거나 같고, 10억보다 작거나 같다.</p>

## 📖[Python/파이썬][🥈1] 백준 알고리즘 14888 - 연산자 끼워넣기
### 📜문제
![](https://velog.velcdn.com/images/keynene/post/f767ec1f-e598-4a9f-b33c-71fdb3e456b7/image.png)
![](https://velog.velcdn.com/images/keynene/post/50306b2c-0d1d-417e-b1f5-eb34b3ae26d1/image.png)
![](https://velog.velcdn.com/images/keynene/post/eef44c72-c61e-41f3-b91a-416e75c0328e/image.png)
![](https://velog.velcdn.com/images/keynene/post/1547c140-28ee-4f49-b5a7-6d5bc076172a/image.png)


* * *

#### DFS(깊이우선탐색)

임의의 한 노드에서 시작해서 다음 분기로 넘어가기 전에 해당 분기를 완벽하게 탐색하는 방법
<span style="color:green">#재귀 #순환 #무한루프탈출 #Back-Tracking</span>

* * *

### 📕풀이방향
사실 **DFS알고리즘**을 이 문제로 처음 접했는데 이제야 정리가 되어 포스팅한다.

우선 n,a(수열),f(연산자)를 저장하고, ```dfs()```함수를 구현하자
```dfs()```함수는 모든 연산자들을 모두 다 방문하여 값을 저장하고,
최댓값 최솟값을 max, min함수로 저장하여 출력하자

* * *

### 📝알고리즘 구현순서
1. n,a(수열),f(연산자리스트)를 저장 및 minR, maxR을 초기화하고, ```dfs()```함수를 구현하자

* * *

### 💻결과코드
```python
import sys
input = sys.stdin.readline

maxR = -1e9  #최댓값 저장용
minR = 1e9   #최솟값 저장용

def dfs(idx, res, sum, sub, mul, div):
    global maxR, minR

    if idx == n:
        maxR = max(res, maxR)
        minR = min(res, minR)
        return

    if sum:
        dfs(idx+1, res+a[idx], sum-1, sub, mul, div)
    if sub:
        dfs(idx+1, res-a[idx], sum, sub-1, mul, div)
    if mul:
        dfs(idx+1, res*a[idx], sum, sub, mul-1, div)
    if div:
        dfs(idx+1, int(res/a[idx]), sum, sub, mul, div-1)

n = int(input().rstrip())
a = list(map(int, input().split()))
f = list(map(int, input().split()))


dfs(1, a[0], f[0], f[1], f[2], f[3])
print(maxR)
print(minR)
```

* * *

#### ✏️1. n, a(수열), f(연산자리스트), dfs()함수 구현
```python
import sys
input = sys.stdin.readline

maxR = -1e9
minR = 1e9

#res값을 파라미터로 주고받으면서 maxR, minR에 값 저장하는 것이 목표
def dfs(idx, res, sum, sub, mul, div):
    global maxR, minR

    if idx == n: #모든 수를 다 방문 시 res를 minR, maxR에 각각 저장 (탈출)
        maxR = max(res, maxR)
        minR = min(res, minR)
        return

    if sum:
        dfs(idx+1, res+a[idx], sum-1, sub, mul, div)
    if sub:
        dfs(idx+1, res-a[idx], sum, sub-1, mul, div)
    if mul:
        dfs(idx+1, res*a[idx], sum, sub, mul-1, div)
    if div:
        dfs(idx+1, int(res/a[idx]), sum, sub, mul, div-1)

n = int(input().rstrip())
a = list(map(int, input().split()))
f = list(map(int, input().split()))


dfs(1, a[0], f[0], f[1], f[2], f[3])
print(maxR)
print(minR)
```

* * *

### 📚동작원리 및 정리
#### ❓동작원리
```python
ex)
n = 6
a = 1 2 3 4 5 6
f = 2 1 1 1

def dfs(idx, res, sum, sub, mul, div):
    global maxR, minR

    if idx == n:
        maxR = max(res, maxR)
        minR = min(res, minR)
        return

    if sum:
        dfs(idx+1, res+a[idx], sum-1, sub, mul, div)
    if sub:
        dfs(idx+1, res-a[idx], sum, sub-1, mul, div)
    if mul:
        dfs(idx+1, res*a[idx], sum, sub, mul-1, div)
    if div:
        dfs(idx+1, int(res/a[idx]), sum, sub, mul, div-1)
```
     
#### 동작원리 (파라미터 순서대로 정리)
```
정의 : def dfs(idx, res, sum, sub, mul, div):
호출 : dfs(1, a[0], f[0], f[1], f[2], f[3])
     즉, dfs(1, 1, 2, 1, 1, 1)

1. 우선 idx값을 1로 넘기고, dfs()가 호출될 때마다 파라미터로 "idx+1"값을 넘긴다. 
   (idx++시키면서 "idx == n" 때 종료시킬꺼니까!)
   
2. res값으로 a[0]를 넘기고, dfs()가 호출될 때마다 res와 연산자마다의 계산을 해준다.
   (a[0]일 때 연산자가 +면, 파라미터로 a[0]+a[idx]해주는데 
    이 떄 idx=idx+1이므로, res의 파라미터로 "a[0]+a[1]"를 넘기게 된다.
    그 다음 호출은 res+a[2], 그다음은 res+a[3] ..... )
    
3. 3번째 파라미터부터는 연산자를 +, -, *, / 순으로 받는다.
   나도 이 부분이 참 헷갈렸는데, 이게 DFS알고리즘의 정석 개념을 이해하기 좋다!
   
    n = 6
	a = 1 2 3 4 5 6
	f = 2 1 1 1
    
      👉🏻dfs(1, 1+2, 1, 1, 1, 1) sum동작:a[0]+a[1]    res = 3
      👉🏻dfs(2, 3+3, 0, 1, 1, 1) sum동작:res+a[2]     res = 6
      👉🏻dfs(3, 6-4, 0, 0, 1, 1) sub동작:res-a[3]     res = 2
      👉🏻dfs(4, 2*5, 0, 0, 0, 1) mul동작:res*a[4]     res = 10
      👉🏻dfs(5, 10/6, 0, 0, 0, 0) div동작:res-a[5]     res = 1
      👉🏻idx == n이므로 res값 minR, maxR에 저장
```

단, 이게 **첫 번째** 동작이라는 점이다!
div까지 동작한 dfs()가 "return"값은 어디로 전달될까?
```
      👉🏻바로, div 이전의 mul에 dfs(4, 2*5, 0, 0, 0, 1) 로 나온다!
      
      👉🏻그 후, mul 이전의 sub에 dfs(3, 6-4, 0, 0, 1, 1) 로 나오게 되는데
        여기서 if mul:을 탈출한 상황이므로, if div:를 방문하게 되어
        dfs(4, 2/5, 0, 0, 1, 0) div 먼저 동작하여 res = 0이 되고
        dfs(5, 0*6, 0, 0, 0, 0) mul이 동작하여 res = 0이 되어 return된다.
        
      👉🏻그 후, sub 이전의 sum에 dfs(2, 3+3, 0, 1, 1, 1) 로 나오게 되는데,
        여기서 또 if sub:를 탈출한 상황이므로 if mul:을 방문하게 되어,
        곱하기 > 나누기 > 빼기 순으로 진행하게 된다.
```
이런식으로 모든 경우의 수를 방문하여 idx == n일 때마다 max와 min함수를 통해
maxR, minR을 도출해내는 것이 이 문제의 핵심이다. 

* * *

#### 정리
1. **DFS알고리즘**은 위에서 예상했다시피 **재귀/순환**구조를 익숙하게 다룰 수 있어야 한다.
2. ```dfs()```를 재귀함수 형태로 만들었다면 함수내부에서 return 후 어떻게 동작하는지
   설계하고 구현해야 원하는 지점에서 **탈출**을 하여 **무한루프**에 빠지지 않을 수 있다.
3. 재귀/순환 문제를 연습하자,,