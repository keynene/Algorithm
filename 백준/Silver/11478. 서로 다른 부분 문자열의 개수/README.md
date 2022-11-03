# [Silver III] 서로 다른 부분 문자열의 개수 - 11478 

[문제 링크](https://www.acmicpc.net/problem/11478) 

### 성능 요약

메모리: 316944 KB, 시간: 556 ms

### 분류

자료 구조(data_structures), 해시를 사용한 집합과 맵(hash_set), 문자열(string), 트리를 사용한 집합과 맵(tree_set)

### 문제 설명

<p>문자열 S가 주어졌을 때, S의 서로 다른 부분 문자열의 개수를 구하는 프로그램을 작성하시오.</p>

<p>부분 문자열은 S에서 연속된 일부분을 말하며, 길이가 1보다 크거나 같아야 한다.</p>

<p>예를 들어, ababc의 부분 문자열은 a, b, a, b, c, ab, ba, ab, bc, aba, bab, abc, abab, babc, ababc가 있고, 서로 다른것의 개수는 12개이다.</p>

### 입력 

 <p>첫째 줄에 문자열 S가 주어진다. S는 알파벳 소문자로만 이루어져 있고, 길이는 1,000 이하이다.</p>

### 출력 

 <p>첫째 줄에 S의 서로 다른 부분 문자열의 개수를 출력한다.</p>

## 📖[Python/파이썬] [🥈3] 백준 알고리즘 11478 - <br>서로 다른 부분 문자열의 개수
### 📜문제
![](https://velog.velcdn.com/images/keynene/post/1459adce-19ec-4a2b-b3d4-ac460c3e0b2b/image.png)

* * *

### 📕풀이방향
문자열 s를 입력받고 s[i:j]와 <cdoe>set()</code>을 이용하여 문자열을 잘라서 저장하자
(set은 중복을 제거하므로 중복케이스는 제거하여 출력해줄 것임!)

* * *

### 📝알고리즘 구현순서
1. s문자열 입력받고 s_set() 빈 집합을 만들고,
   1중첩 n을 len(s)만큼 증가시키고,
   2중첩 i를 1~len(s)+1만큼 증가시키며
   s[n:n+i]값을 s_set에 저장하자

```
※s[n:n+1]인 이유?
  s[0:1] = s문자열을 0~1만큼 잘라줌!
  ...자세한건 아래 코드에서 설명하겠음
```

* * *

### 💻결과코드
```python
import sys
input = sys.stdin.readline

s = input().rstrip()
s_set = set()

for n in range(len(s)):
    for i in range(1,len(s)+1):
        s_set.add(s[n:n+i])

print(len(s_set))
```

* * *

#### ✏️1. 입력값받아 자릿수만큼 자르고, 중복을 제거하여 출력
```python
#1. 입력값받기
import sys
input = sys.stdin.readline

s = input().rstrip()

#3. 중복을 제거하기
s_set = set()

#2. 자릿수만큼 자르기
for n in range(len(s)):
    for i in range(1,len(s)+1):
        s_set.add(s[n:n+i])

print(len(s_set))
```
```
저장해야하는 문자열을 나열해보자 (s = 'ababc'라고 가정)
 1자릿수 : S[0:1], S[1:2], S[2:3], S[3:4], S[4:5]
 2자릿수 : S[0:2], S[1:3], S[2:4], S[3:5]
 3자릿수 : S[0:3], S[1:4], S[2:5]
 4자릿수 : S[0:4], S[1:5]
 5자릿수 : S[0:5]
 
 1. s 문자열의 자릿수만큼 for문을 돌려야겟다
  👉🏻 for n in range(len(s))
  
 2. 자릿수마다 1,2,3,4,5 / 2,3,4,5 / 3,4,5 ... 순으로 증가하려면?
 	for n in range(len(s)):
      for i in range(len(s)):
      	s_set.add(s[n:j]) 
     👉🏻 여기서 j는??? i에서 자릿수(n)만큼 증가하고 있음!!
        ※ j = n+i
```

* * *

### 📚정리
1. 문자열 자르기는? s[i:j]
2. 집합은 중복을 제거하여 저장한다
