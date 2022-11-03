# [Silver IV] 숫자 카드 2 - 10816 

[문제 링크](https://www.acmicpc.net/problem/10816) 

### 성능 요약

메모리: 262632 KB, 시간: 1776 ms

### 분류

이분 탐색(binary_search), 자료 구조(data_structures), 해시를 사용한 집합과 맵(hash_set), 정렬(sorting)

### 문제 설명

<p>숫자 카드는 정수 하나가 적혀져 있는 카드이다. 상근이는 숫자 카드 N개를 가지고 있다. 정수 M개가 주어졌을 때, 이 수가 적혀있는 숫자 카드를 상근이가 몇 개 가지고 있는지 구하는 프로그램을 작성하시오.</p>

### 입력 

 <p>첫째 줄에 상근이가 가지고 있는 숫자 카드의 개수 N(1 ≤ N ≤ 500,000)이 주어진다. 둘째 줄에는 숫자 카드에 적혀있는 정수가 주어진다. 숫자 카드에 적혀있는 수는 -10,000,000보다 크거나 같고, 10,000,000보다 작거나 같다.</p>

<p>셋째 줄에는 M(1 ≤ M ≤ 500,000)이 주어진다. 넷째 줄에는 상근이가 몇 개 가지고 있는 숫자 카드인지 구해야 할 M개의 정수가 주어지며, 이 수는 공백으로 구분되어져 있다. 이 수도 -10,000,000보다 크거나 같고, 10,000,000보다 작거나 같다.</p>

### 출력 

 <p>첫째 줄에 입력으로 주어진 M개의 수에 대해서, 각 수가 적힌 숫자 카드를 상근이가 몇 개 가지고 있는지를 공백으로 구분해 출력한다.</p>

## 📖[Python/파이썬] [🥈4] 백준 알고리즘 10816 - 숫자카드2
### 📜문제
![](https://velog.velcdn.com/images/keynene/post/11903f2a-be6d-4f70-9bd5-9de9c3b24c74/image.png)
![](https://velog.velcdn.com/images/keynene/post/7f7a1a8f-0931-4510-9afa-3b2563af9c04/image.png)

* * *

### 📕풀이방향
이분탐색(binary_search)하여 원하는 카드의 개수를 찾아내는 bs()함수를 만들고, N,M,각 카드를 입력받아 dictionary에 저장하자
(카드 개수는 dictionary의 <code>.get()</code>을 이용하여 가져옴)
반복문으로 돌리면서 bs()함수를 통해 M의 각 카드가 N에 몇개가 있는지 탐색하여 출력해보자

* * *

### 📝알고리즘 구현순서
1. bs(arr, target, start, end)함수 구현
2. N, M 등 각 카드 입력받기
3. dictionary 정의 및 값 넣기
4. M카드수만큼 bs()호출하여 dictionary에 저장되어있는 카드개수 출력

* * *

### 💻결과코드
```python
import sys

def bs(arr, target, start, end):
    if start > end:
        return 0
    mid = (start+end)//2
    if arr[mid] == target :
    	#target 일치할경우 dictionary의 값 return
        return cnt.get(target)
    elif arr[mid] > target :
    	#num[mid]값이 M의 해당 카드보다 크다면 end = mid-1
        return bs(arr, target, start, mid-1)
    else:
    	#num[mid]값이 M의 해당 카드보다 작다면 start = mid+1
        return bs(arr, target, mid+1, end)

n = int(sys.stdin.readline().rstrip())
#N의 카드는 정렬하여 저장 (※이분탐색 기본조건! arr정렬하기)
num = sorted(list(map(int, sys.stdin.readline().split())))
m = int(sys.stdin.readline().rstrip())
comp = list(map(int, sys.stdin.readline().split()))

#빈 dictionary
cnt = {} 

#num값을 차례대로 "카드:개수"형태로 저장
for i in num :
	#dictionary에 num의 i값이 있다면 +1
    if i in cnt :
        cnt[i] += 1
    #dictionary에 num의 i값이 없다면, cnt[i]만들고 1저장 
    else :
        cnt[i] = 1

for i in comp :
    print(bs(num, i, 0, len(num)-1), end=' ')
```

#### ✏️1. 이분탐색(binary_search)함수 구현
```python
def bs(arr, target, start, end):
    if start > end:
        return 0
    mid = (start+end)//2
    if arr[mid] == target :
        return cnt.get(target) #dictionary 값 가져오기
    elif arr[mid] > target :
        return bs(arr, target, start, mid-1)
    else:
        return bs(arr, target, mid+1, end)
```
```
※이분탐색(binary_search)
  1. 배열(arr)을 오름차순 정렬하여 저장한다
  2. 비교할 값(target)이 arr의 중간(arr[mid])에 있는 값보다 작으면,
     end = mid-1하여 이분탐색을 재실행한다
     (ex/ 0~9배열에 target이 arr[4]보다 작으면, 0~3사이를 재실행)
  2. 비교할 값(target)이 arr의 중간(arr[mid])에 있는 값보다 크면,
     start = mid+1하여 이분탐색을 재실행한다
     (ex/ 0~9배열에 target이 arr[4]보다 크면, 5~9사이를 재실행)
  3. 마침내 비교할 값(target)이 arr[mid]와 같으면 해당 값 return
  
※탐색함수는 위 예제처럼 재귀함수로 구현해도 되지만,
  while start >= end와 if/else로 반복실행도 가능하다
```

* * *

#### ✏️2. N, M 등 값 입력받기
```python
import sys

n = int(sys.stdin.readline().rstrip())
num = sorted(list(map(int, sys.stdin.readline().split())))
m = int(sys.stdin.readline().rstrip())
comp = list(map(int, sys.stdin.readline().split()))
```

* * *

#### ✏️3. dictionary에 "카드:개수"형태로 저장하기
```python
#빈 dinctionary 선언
#여기에 {카드:개수, ...} → {-10:2 ...}형태로 저장될꺼임
cnt = {}

for i in num :

	#cnt에 num의 i가 있으면 +1
    #ex) cnt안에 -10:1 이 있으면 -10:2으로 +1해줌
    if i in cnt :
        cnt[i] += 1
    
    #cnt에 num의 i가 없으면 등록
    #ex) -10없으면 -10:1 등록
    else :
        cnt[i] = 1
```
```
자바스크립트의 객체 개념이라고 생각하면 이해하기 쉬움
※cnt.get(-10)형식으로 값 가져올 수 있음
```

* * *

#### ✏️4. bs()호출하여 dictionary에 저장되어있는 카드개수 출력
```python
for i in comp :
    print(bs(num, i, 0, len(num)-1), end=' ')
```

* * *

### 📚기존 내 알고리즘의 오류와 정리
#### 1. 잉? 왜 시간초과?
```python
import sys

n = int(sys.stdin.readline().strip())
num = list(map(int, sys.stdin.readline().split()))

m = int(sys.stdin.readline().strip())
comp = list(map(int, sys.stdin.readline().split()))

res = ''
for i in comp :
    cnt = 0
    for j in num :
        if i == j :
            cnt += 1
    res += str(cnt)+' '
print(res)
```
```
🙅🏻‍♀️브루트포스 알고리즘 방식으로 접근한 것이 문제!
   문제에서 제시한 O(N)보다 더 많은 시간을 소요했음
```
아! 이분탐색(binary_search)이라는 알고리즘이 있군
이제야 알고리즘다운 알고리즘 문제를 풀어보는 것 같네
이분탐색 함수 재귀함수로 만들면 끝나겠네?🤷🏻‍♀️

#### 2. 하.. 런타임에러
```python
import sys

n = int(sys.stdin.readline().rstrip())
num = list(map(int, sys.stdin.readline().split()))
s_num = sorted(num)

m = int(sys.stdin.readline().rstrip())
comp = list(map(int, sys.stdin.readline().split()))

def binary(arr, target, start, end) :
    cnt = 0

    mid = (start+end)//2

    if start > end:
        return 0
    elif arr[mid] == target :
        cnt = num.count(arr[mid])
        return str(cnt)
    elif arr[mid] > target :
        return (binary(arr, target, start, mid-1))
    else:
        return (binary(arr, target, start+1, end))


for i in comp :
    print(binary(s_num, i, 0, len(num)-1), end=' ')
```
```
🙅🏻‍런타임 에러 (IndexError)
   ㅠㅠ 제일 이해안가고 에러이유를 모르겠는 에러다.
   해당 알고리즘에서 에러가 난 이유는 cnt=num.count(arr[mid])인 것으로 추정!
   검색해보니까 .count()가 생각보다 시간을 많이 잡아먹는 것 같음
```

* * *

1. 탐색하는 문제는 탐색 기준이 있는지 살펴보자
   (무조건 브루트포스가 답이 아니다)
2. 이분탐색(binary_search)는 단골문제다. 잘 기억하자
   (dictionary는 한 세트로 생각하면 편함)
3. 이분탐색 알고리즘은 라이브러리가 있다던데....
   (추후 알아보고 포스팅하기)