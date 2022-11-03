# [Silver III] 문자열 집합 - 14425 

[문제 링크](https://www.acmicpc.net/problem/14425) 

### 성능 요약

메모리: 125888 KB, 시간: 284 ms

### 분류

자료 구조(data_structures), 해시를 사용한 집합과 맵(hash_set), 문자열(string), 트리를 사용한 집합과 맵(tree_set)

### 문제 설명

<p>총 N개의 문자열로 이루어진 집합 S가 주어진다.</p>

<p>입력으로 주어지는 M개의 문자열 중에서 집합 S에 포함되어 있는 것이 총 몇 개인지 구하는 프로그램을 작성하시오.</p>

### 입력 

 <p>첫째 줄에 문자열의 개수 N과 M (1 ≤ N ≤ 10,000, 1 ≤ M ≤ 10,000)이 주어진다. </p>

<p>다음 N개의 줄에는 집합 S에 포함되어 있는 문자열들이 주어진다.</p>

<p>다음 M개의 줄에는 검사해야 하는 문자열들이 주어진다.</p>

<p>입력으로 주어지는 문자열은 알파벳 소문자로만 이루어져 있으며, 길이는 500을 넘지 않는다. 집합 S에 같은 문자열이 여러 번 주어지는 경우는 없다.</p>

### 출력 

 <p>첫째 줄에 M개의 문자열 중에 총 몇 개가 집합 S에 포함되어 있는지 출력한다.</p>

## 📖[Python/파이썬] [🥈3] 백준 알고리즘 14425 - 문자열 집합
### 📜문제
![](https://velog.velcdn.com/images/keynene/post/f625f74b-ff70-4e6a-aa01-53de1e3e4bce/image.png)
![](https://velog.velcdn.com/images/keynene/post/ae31c542-ab9b-4a18-9d52-fe873e613d78/image.png)

* * *

### 📕풀이방향
S는 집합<code>.set()</code>로, M개의 비교문자열은 <code>list()</code>로 선언하고,
M 비교문자열 요소를 처음부터 끝까지 집합 S에 포함되어 있는지 검사하면서
포함되어 있으면 cnt를 증가시키자
```
🤷🏻‍♀️S는 집합, M개의 문자로 구성된 문자열은 리스트로 구현하는 이유?
    문제에서 S는 중복되지 않는다라는 조건이 있고, 문자열은 중복될 수도 있기 때문임
    ex)
    M개의 문자열 comp에 "abc"라는 요소가 2개가 있는데, S에 abc가 있다면
    정답은 2개이기 때문에 문자열 comp는 집합이 아닌 리스트로 선언
```

* * *

### 📝알고리즘 구현순서
1. N,M을 입력받고, S를 <code>.set()</code>으로, comp(문자열)을 <code>list()</code>로 선언
2. comp의 요소가 S에 포함되어있는지 <code>in</code>으로 확인 후 카운팅

* * *

### 💻결과코드
```python
import sys
input = sys.stdin.readline

n,m = map(int, input().split())
S = set(input().rstrip() for _ in range(n))
comp = list(input().rstrip() for _ in range(m))

cnt = 0
for comp_str in comp:
    if comp_str in S:
        cnt += 1
print(cnt)
```

* * *

#### ✏️1. N, M저장, S는 set(), comp는 list()에 저장
```python
import sys
input = sys.stdin.readline

n,m = map(int, input().split())
#S는 집합으로 입력받으며 중복을 제거함
S = set(input().rstrip() for _ in range(n))
#문자열을 리스트에 저장 (중복포함)
comp = list(input().rstrip() for _ in range(m))
```

* * *

#### ✏️2. comp 각 요소 S에 포함(in) 되어있는지 확인
```python
cnt = 0
for comp_str in comp:
	#a "in" b : a가 b에 포함되어 있으면 "True"를 반환
    if comp_str in S:
        cnt += 1
print(cnt)
```

* * *

### 📚다른 알고리즘과 정리
```python
import sys
input = sys.stdin.readline

n,m = map(int, input().split())
S = set(input().rstrip() for _ in range(n))

cnt = 0
for _ in range(m):
    comp = input().rstrip()
    if comp in S:
        cnt += 1
print(cnt)
```
```
뭐 내 알고리즘과 거의 비슷하지만 comp를 list로 저장하지 않고, 
for문으로 그때그때 입력받으면서 검사한다는 점에서 차이가 있음
```
※하지만, 시간복잡도는 O(N+M) == O(N+M+comp) 로 똑같음!
👉🏻어떻게 코딩하든 그저 취향차이..
