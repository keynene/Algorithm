# [Silver III] N과 M (1) - 15649 

[문제 링크](https://www.acmicpc.net/problem/15649) 

### 성능 요약

메모리: 118748 KB, 시간: 212 ms

### 분류

백트래킹(backtracking)

### 문제 설명

<p>자연수 N과 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오.</p>

<ul>
	<li>1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열</li>
</ul>

### 입력 

 <p>첫째 줄에 자연수 N과 M이 주어진다. (1 ≤ M ≤ N ≤ 8)</p>

### 출력 

 <p>한 줄에 하나씩 문제의 조건을 만족하는 수열을 출력한다. 중복되는 수열을 여러 번 출력하면 안되며, 각 수열은 공백으로 구분해서 출력해야 한다.</p>

<p>수열은 사전 순으로 증가하는 순서로 출력해야 한다.</p>

## 📖[Python/파이썬][🥈3] 백준 알고리즘 15649 - N과 M (1)
### 📜문제
![](https://velog.velcdn.com/images/keynene/post/5cba689e-4c00-4d04-8135-3cf408b70749/image.png)
![](https://velog.velcdn.com/images/keynene/post/bddf7a0d-bcc8-496b-b0e6-34bfa15e27ed/image.png)
![](https://velog.velcdn.com/images/keynene/post/8bb14586-ddbf-4b8a-9bfd-04976ac96280/image.png)

* * *

### 📕풀이방향
#### Back-Tracking(백트래킹)
- 가능한 모든 경우의 수 중에서 <span style="color:red">특정한 조건을 만족하는 경우만</span> 탐색하는 알고리즘
- 즉, 해가 될 만한지 사전에 판단하고 그렇지 않으면 되돌아가여(Back-Tracking) 탐색함

n,m을 입력받고 num이라는 list를 정의하자
자릿수마다 n의 경우의 수만큼 순서대로 고르는 함수 bt()를 만들자
for loof으로 i를 1~n만큼 증가시키면서 num에 append()하여 num 길이가 m이면 출력, 
m보다 작으면 bt()를 재호출하자 

※ m자릿수만큼 append() 해야하므로 재귀함수로 구현했음

* * * 

### 📝알고리즘 구현순서
1. n, m, num(list), bt(funtion)정의 후 실행하자
```python
#bt()는 재귀함수로, 아래와 같이 설계하자

def bt():
  if num길이가 m일때:
    결과출력
  for i를 1~n까지:
    자릿수만큼 bt()호출하며 숫자뽑기
bt()
```

* * *

### 💻결과코드

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
        if i not in num:
            num.append(i)
            bt()
            num.pop()
bt()
```

* * *

#### ✏️1. n가지 숫자를 m자릿수만큼 중복없이 출력하기 (전체코드분석)
```python
import sys
input = sys.stdin.readline

n,m = map(int, input().split())
num = []

def bt():
	#num의 길이를 확인하여 m이면 출력 후 return
    if len(num) == m:
        print(*num)
        return

	#1~n까지 숫자 뽑기
    for i in range(1,n+1):
    	#i가 현재 num에 없을 때만 실행 (중복제거)
        if i not in num:
            num.append(i)
            
            #다음자릿수 뽑기위해 bt()재호출 (재귀)
            bt()
            
            #bt() 상단의 num 길이 확인하는 if에서 return 되면,
            #제일 마지막 요소 제거
            num.pop()
bt()
```

❓어떻게 동작하게 될까
```
※n,m = 4,2인 경우
1. bt()의 if는 넘어가고 for loof에서 i에 [1]이 들어온다.
2. num에 1이 append된다. (num = [1])
3. for loof에서 bt()가 재호출 된다.
4. 2번째 호출된 bt()의 for loof의 i는 1부터 다시 동작하는데, 
   "if i not in num"에 충족되지 않으므로 (1이 중복) i=2가 된다.
5. num에 2가 append된다. (num = [1,2])
6. for loof에서 bt()가 또 재호출 된다. (3번째)
7. 3번째 bt()에서 "if len(num)==m"조건을 만족하여 num을 출력하고 return
8. return 후 num.pop()을 만나, num의 제일 마지막 요소를 제거한다. (num = [1])
9. 4번에서 다시 도는 for loof의 i는 3이 되어, 위 과정을 반복한다.

👉🏻동작과정
[1] → [1,2]출력 → [1] → [1,3]출력 → [1] → [1,4]출력 ...
```

* * *

### 📚초기 알고리즘 오류와 정리

※초기 알고리즘
```python
import sys
input = sys.stdin.readline

n,m = map(int, input().split())
num = []

def bt():
    if len(num) == m:
        print(*num)
        del num[-1]

    for i in range(1,n+1):
        if i not in num:
            num.append(i)
            bt()
bt()
```
```
❓내 알고리즘이 틀린 이유

num에 초기값 [1,2]를 저장하고, bt()가 재호출되어 if문 만족 후 출력했는데,
재귀함수 bt()가 종료되지 않아서 for loof의 i가 다시 1부터 돌기 때문에,
[1] → [1,2] → [1] → for loof i=1이라 다시 2부터 저장 [1,2]가 반복된다.

❗재귀함수 사용 시 for loof의 값을 저장해야 한다면, 재귀된 함수의 종료(return)은 필수!
```


