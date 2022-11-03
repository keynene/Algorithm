# [Silver III] N과 M (4) - 15652 

[문제 링크](https://www.acmicpc.net/problem/15652) 

### 성능 요약

메모리: 115808 KB, 시간: 148 ms

### 분류

백트래킹(backtracking)

### 문제 설명

<p>자연수 N과 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오.</p>

<ul>
	<li>1부터 N까지 자연수 중에서 M개를 고른 수열</li>
	<li>같은 수를 여러 번 골라도 된다.</li>
	<li>고른 수열은 비내림차순이어야 한다.
	<ul>
		<li>길이가 K인 수열 A가 A<sub>1</sub> ≤ A<sub>2</sub> ≤ ... ≤ A<sub>K-1</sub> ≤ A<sub>K</sub>를 만족하면, 비내림차순이라고 한다.</li>
	</ul>
	</li>
</ul>

### 입력 

 <p>첫째 줄에 자연수 N과 M이 주어진다. (1 ≤ M ≤ N ≤ 8)</p>

### 출력 

 <p>한 줄에 하나씩 문제의 조건을 만족하는 수열을 출력한다. 중복되는 수열을 여러 번 출력하면 안되며, 각 수열은 공백으로 구분해서 출력해야 한다.</p>

<p>수열은 사전 순으로 증가하는 순서로 출력해야 한다.</p>

## 📖[Python/파이썬] [🥈3] 백준 알고리즘 15652 - N과 M (4)
### 📜문제
![](https://velog.velcdn.com/images/keynene/post/ce0e4897-06f5-48eb-bb87-3dcd9d2756c1/image.png)
![](https://velog.velcdn.com/images/keynene/post/86b73810-1bdc-4589-8943-bd2b501d94a5/image.png)
![](https://velog.velcdn.com/images/keynene/post/34e9ac33-4089-4731-8053-2c1313288643/image.png)

* * *

### 📕풀이방향
#### Back-Tracking(백트래킹)
-가능한 모든 경우의 수 중에서 <span style="color:red">특정한 조건을 만족하는 경우만</span> 탐색하는 알고리즘
-즉, 해가 될 만한지 사전에 판단하고 그렇지 않으면 되돌아가여(Back-Tracking) 탐색함

[내 포스팅 : [Python/파이썬] 백준 알고리즘 15649 - N과 M (1)](https://velog.io/@keynene/Python%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EB%B0%B1%EC%A4%80-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-15649-N%EA%B3%BC-M-1)
이전 포스팅과 같은데, 중복이 가능하고 비내림차순이란 조건이 추가되었다.

전과 똑같이 n,m과 num이라는 list와 bt() 함수를 정의하자
bt()는 또 재귀함수로 구현할껀데, 이전과 조건을 다르게 제시하면 될 것같다.
bt에 매개변수 start를 전달받아 start~n까지 증가시키면서(비내림차순),
num에 append()하여 num 길이가 m이면 출력, m보다 작으면 bt(i)를 재호출하자

```
❓bt(start)를 i로 호출하는 이유

for loof에서 i가 start~n만큼 증가할텐데, num[1]값이 num[0]값과 같거나 크려면(비내림차순)
start를 for loof의 i로 넘겨주면 된다.

※1일때는 1을 넘기고, 2일때는 2를 넘기면서 "2,1"과 같은 내림차순의 상황을 아예 걸러버리기
  (Back-Tracking)
```

* * *

### 📝알고리즘 구현순서

n, m, num(list), bt(funtion)정의 후 실행하자
#bt()는 재귀함수로, 아래와 같이 설계하자

```python
def bt(start):
  if num길이가 m일때:
    결과출력
  for i를 start부터 n까지: #비내림차순
    자릿수만큼 bt()호출하며 숫자뽑기
bt(1) #1부터 시작해야 하므로
```

* * *

### 💻결과코드
```python
import sys
input = sys.stdin.readline

n,m = map(int, input().split())
num = []

def bt(start):
    if len(num) == m:
        print(*num)
        return
    for i in range(start,n+1):
        num.append(i)
        bt(i)
        num.pop()
bt(1)
```

* * *

#### ✏️1. n가지 숫자를 m자릿수만큼 비내림차순 출력하기 (전체코드분석)
```python
import sys
input = sys.stdin.readline

n,m = map(int, input().split())
num = []

#bt()함수의 시작점 매개변수로 받기
def bt(start):
    if len(num) == m:
        print(*num)
        return
        
    #for loof를 매개변수 start부터 n까지만 검사 (비내림차순)
    for i in range(start,n+1):
        num.append(i) #num값에 i를 append하고나서
        bt(i)         #bt(i)를 재호출한다 (Back-Tracking)
        num.pop()
bt(1)
```
❓어떻게 동작하게 될까

 자세한 동작순서는 [내 포스팅 : [Python/파이썬] 백준 알고리즘 15649 - N과 M (1)](https://velog.io/@keynene/Python%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EB%B0%B1%EC%A4%80-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-15649-N%EA%B3%BC-M-1) 참고
```
※n,m = 4,2인 경우
전체 동작순서는 위 링크와 비슷한데 bt에 매개변수 start를 적용하는 데서 다르다.

👉🏻동작과정
[1] bt(1) → [1,1] return, pop → [1] bt(2) .... → [1,4] return, pop, pop →
[2] bt(2) → [2,2] ....
※bt에 i의 값에 따라 start를 전달하여 실행되므로 오름참순일때만 실행된다
```

* * *

### 📚초기 알고리즘과 정리
※초기 알고리즘
```python
import sys
input = sys.stdin.readline

n,m = map(int, input().split())
num = []

def bt():
    if len(num) == m:
        print(*num)
        return
    for i in range(1,n+1):
    	#매개변수 대신 if문으로 조건을 걸어 Back-Tracking 구현
        if len(num)==0 or i>= num[-1]:
            num.append(i)
            bt()
            num.pop()
bt()
```
```
❓내 알고리즘이 틀린 이유

틀리지않았다. 정답이다.
그러나 내 풀이는 bt() 호출될 때마다 for loof에서 if 조건문을 매번 확인한다.
물론 이게 Back-Tracking의 정석이긴 하나, 
처음부터 조건을 만족하는 매개변수를 전달하면 불필요한 비교과정을 줄일 수 있다.
```