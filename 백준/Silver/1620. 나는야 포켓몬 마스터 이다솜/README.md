# [Silver IV] 나는야 포켓몬 마스터 이다솜 - 1620 

[문제 링크](https://www.acmicpc.net/problem/1620) 

### 성능 요약

메모리: 146764 KB, 시간: 428 ms

### 분류

자료 구조(data_structures), 해시를 사용한 집합과 맵(hash_set)

### 문제 설명

<p><img alt="" src="https://www.acmicpc.net/upload/201004/p1.PNG" style="height:184px; width:274px"></p>

<p>안녕? 내 이름은 이다솜. 나의 꿈은 포켓몬 마스터야. 일단 포켓몬 마스터가 되기 위해선 포켓몬을 한 마리 잡아야겠지? 근처 숲으로 가야겠어.</p>

<p>(뚜벅 뚜벅)</p>

<p>얏! 꼬렛이다. 꼬렛? 귀여운데, 나의 첫 포켓몬으로 딱 어울린데? 내가 잡고 말겠어. 가라! 몬스터볼~</p>

<p>(펑!) 헐랭... 왜 안 잡히지?ㅜㅜ 몬스터 볼만 던지면 되는 게 아닌가...ㅜㅠ</p>

<p>(터벅터벅)</p>

<p>어? 누구지?</p>

<p><img alt="" src="https://www.acmicpc.net/upload/201004/p2.PNG" style="height:184px; width:274px"></p>

<p>오박사 : 나는 태초마을의 포켓몬 박사 오민식 박사라네. 다솜아, 포켓몬을 잡을 때는, 일단 상대 포켓몬의 체력을 적당히 바닥으로 만들어놓고 몬스터 볼을 던져야 한단다. 자, 내 포켓몬 이상해꽃으로 한번 잡아보렴. 포켓몬의 기술을 쓰는 것을 보고 포켓몬을 줄지 안줄지 결정을 하겠네. 자 한번 해보아라. 다솜아.</p>

<p>이다솜 : 이상해꽃이라...음.. 꽃이니깐 왠지 햇빛을 받아서 공격을 할 것 같은데... 음... 이상해꽃! 햇빛공격!!!</p>

<p>(꼬렛이 이상해꽃에게 공격을 받아 체력이 25 감소했다.)    가라! 몬스터 볼!!!    (꼬렛을 잡았습니다.)    야호! 신난다. 꼬렛을 잡았다.</p>

<p>오박사 : 오우!! 방금 쓴 공격은 솔라빔이라고 하네.. 어떻게 공격을 한 건가? 솔라빔이란 공격에 대해서 공부를 한 건가?</p>

<p>이다솜 : 꽃이니깐 왠지 햇빛을 제대로 받으면 광합성을 해서 음.. 그냥 그럴 것 같아서요 ☞☜</p>

<p>오박사 : 다른 아이들은 넝쿨채찍이나, 나뭇잎 공격을 하는데, 다솜이는 역시 뭔가 다르구나. 그럼 나와 함께 연구소로 가자꾸나. 내가 포켓몬을 한 마리 줄 테니, 너의 꿈을 펼쳐보아라. 꿈은 이루어진단다.</p>

<p>이다솜 : 네! 오박사님, 고마워요.ㅜㅜ</p>

<p>오박사 : 가자. 나의 연구소는 너의 옆집의 아랫집이란다. 같이 가도록하자. 지금 포켓몬을 주마.</p>

<p>이다솜 : 네. 야호!!</p>

<p>'<img alt="" src="https://www.acmicpc.net/upload/201004/p3.PNG" style="height:181px; width:274px"></p>

<p>오영식 : 어? 오박사님 얘는 누구인가요?</p>

<p><img alt="" src="https://www.acmicpc.net/upload/201004/p4.PNG" style="height:182px; width:274px"></p>

<p>오박사 : 얘는 너의 라이벌이 될 친구 이다솜이라고 하네. 자, 포켓몬을 한 마리 골라보도록 해봐라 다솜아. 레이디퍼스트 네가 먼저 골라봐라.</p>

<p>이다솜 : 저는 생각해둔 포켓몬이 있어요. 피카츄 골라도 될까요?</p>

<p>오박사 : 그래 여기 피카츄가 한 마리 있단다. 피카츄를 가져가거라.</p>

<p>오영식 : 그럼 저는 이브이를 가져가겠어요. 그럼 나중에 보자 이다솜.</p>

<p>이다솜 : 그럼 꼬렛을 다시 잡으러 가야겠다. 영식아, 그리고 민식박사님 빠잉!</p>

<p><img alt="" src="https://www.acmicpc.net/upload/201004/p5.PNG" style="height:179px; width:274px"></p>

<p>이다솜 : 피카츄 공격!</p>

<p><img alt="" src="https://www.acmicpc.net/upload/201004/p6.PNG" style="height:182px; width:274px"></p>

<p>가라 몬스터 볼!</p>

<p><img alt="" src="https://www.acmicpc.net/upload/201004/p7.PNG" style="height:184px; width:274px"></p>

<p>이다솜 : 야호! 신난다. 꼬렛을 잡았다!!!!!</p>

<p>이다솜 : 그럼! 일단 사천왕을 이기고 오겠어!</p>

<p><img alt="" src="https://www.acmicpc.net/upload/201004/p8.PNG" style="height:181px; width:274px"></p>

<p>이다솜 : 여기가 사천왕과 대결하려면 가야하는 곳인가..</p>

<p><img alt="" src="https://www.acmicpc.net/upload/201004/p9.PNG" style="height:181px; width:274px"></p>

<p>경비원 : 사천왕과 대결을 하려면, 마을의 체육관 리더를 이겨서 배지를 8개를 모아야 한다네... 배지를 모아서 오도록 하게</p>

<p>이다솜 : 잉ㅠㅜ... 그럼 배지부터 모아야 하는구나ㅠㅜㅠㅜ 나쁘당 그냥 좀 봐주지..</p>

<p><1 년 후></p>

<p>그동안의 줄거리 : 이다솜은 일단 상록 숲의 체육관 리더에게 도전을 했다. 하지만 상록숲 체육관의 리더는 실종된 상태. 따라서 회색마을부터 도전하기로 했다. 체육관의 리더를 이기면서, 로켓단을 해체시키기도 하고, 여러 가지 사건도 있었다. 결국 전설의 포켓몬도 잡고, 이제 사천왕을 이기려고 도전하기로 했다. 사천왕은 모두 가볍게 이기고, 이제 마지막 라이벌 오!영!식! 이다.</p>

<p><img alt="" src="https://www.acmicpc.net/upload/201004/pa.PNG" style="height:183px; width:274px"></p>

<p>오영식 : 훗. 1년 전의 그 이다솜이 사천왕을 이기고 현재 포켓몬 마스터인 나에게 덤벼? 어디 한번 덤벼보시지.</p>

<p>이다솜 : 헐랭... 나를 우습게보네.... 한번 두고 보시지! 그럼 대결이닷!</p>

<p><img alt="" src="https://www.acmicpc.net/upload/201004/pb.PNG" style="height:181px; width:274px"></p>

<p><img alt="" src="https://www.acmicpc.net/upload/201004/pc.PNG" style="height:183px; width:274px"></p>

<p><img alt="" src="https://www.acmicpc.net/upload/201004/pd.PNG" style="height:182px; width:274px"></p>

<p><img alt="" src="https://www.acmicpc.net/upload/201004/pe.PNG" style="height:183px; width:274px"></p>

<p><img alt="" src="https://www.acmicpc.net/upload/201004/pf.PNG" style="height:183px; width:274px"></p>

<p><img alt="" src="https://www.acmicpc.net/upload/201004/pg.PNG" style="height:181px; width:274px"></p>

<p><img alt="" src="https://www.acmicpc.net/upload/201004/ph.PNG" style="height:184px; width:274px"></p>

<p><img alt="" src="https://www.acmicpc.net/upload/201004/pi.PNG" style="height:184px; width:274px"></p>

<p>이다솜 : 휴... 이겼다.</p>

<p>오영식 : 내가 지다니 분하다. ㅜㅜ</p>

<p>오박사 : 그럼 다솜아 이제 진정한 포켓몬 마스터가 되기 위해 도감을 완성시키도록 하여라. 일단 네가 현재 가지고 있는 포켓몬 도감에서 포켓몬의 이름을 보면 포켓몬의 번호를 말하거나, 포켓몬의 번호를 보면 포켓몬의 이름을 말하는 연습을 하도록 하여라. 나의 시험을 통과하면, 내가 새로 만든 도감을 주도록 하겠네.</p>

### 입력 

 <p>첫째 줄에는 도감에 수록되어 있는 포켓몬의 개수 N이랑 내가 맞춰야 하는 문제의 개수 M이 주어져. N과 M은 1보다 크거나 같고, 100,000보다 작거나 같은 자연수인데, 자연수가 뭔지는 알지? 모르면 물어봐도 괜찮아. 나는 언제든지 질문에 답해줄 준비가 되어있어.</p>

<p>둘째 줄부터 N개의 줄에 포켓몬의 번호가 1번인 포켓몬부터 N번에 해당하는 포켓몬까지 한 줄에 하나씩 입력으로 들어와. 포켓몬의 이름은 모두 영어로만 이루어져있고, 또, 음... 첫 글자만 대문자이고, 나머지 문자는 소문자로만 이루어져 있어. 아참! 일부 포켓몬은 마지막 문자만 대문자일 수도 있어. 포켓몬 이름의 최대 길이는 20, 최소 길이는 2야. 그 다음 줄부터 총 M개의 줄에 내가 맞춰야하는 문제가 입력으로 들어와. 문제가 알파벳으로만 들어오면 포켓몬 번호를 말해야 하고, 숫자로만 들어오면, 포켓몬 번호에 해당하는 문자를 출력해야해. 입력으로 들어오는 숫자는 반드시 1보다 크거나 같고, N보다 작거나 같고, 입력으로 들어오는 문자는 반드시 도감에 있는 포켓몬의 이름만 주어져. 그럼 화이팅!!!</p>

### 출력 

 <p>첫째 줄부터 차례대로 M개의 줄에 각각의 문제에 대한 답을 말해줬으면 좋겠어!!!. 입력으로 숫자가 들어왔다면 그 숫자에 해당하는 포켓몬의 이름을, 문자가 들어왔으면 그 포켓몬의 이름에 해당하는 번호를 출력하면 돼. 그럼 땡큐~</p>

<p><img alt="" src="/upload/201004/pn.PNG" style="height:122px; width:141px"></p>

<p>이게 오박사님이 나에게 새로 주시려고 하는 도감이야. 너무 가지고 싶다ㅠㅜ. 꼭 만점을 받아줬으면 좋겠어!! 파이팅!!!</p>

## 📖[Python/파이썬] [🥈4] 백준 알고리즘 1620 <br>- 나는야 포켓몬 마스터 이다솜
### 📜문제
...(포켓몬 가지고 치고박고 싸우는 건)중략...
![](https://velog.velcdn.com/images/keynene/post/ee895dae-f511-4534-84e5-fbf697d54c88/image.png)
![](https://velog.velcdn.com/images/keynene/post/ea854094-975c-4fe0-b303-9f594114a67a/image.png)
![](https://velog.velcdn.com/images/keynene/post/a1b2f70d-2f8c-4f7b-8eb4-e93ee0181169/image.png)

* * *

### 📕풀이방향
N,M을 입력받고 pok_name, pok_num을 딕셔너리(dictionary)로 선언하자
pok_name은 이름을 가져올 수 있게, pok_num은 순서값을 가져올 수 있게 저장하자
M크기만큼 리스트 test에 입력값을 저장하고 test의 모든요소를 탐색하여
문자는 순서를, 순서는 문자를 출력하자

* * *

### 📝알고리즘 구현순서
1. N, M, pok_name, pok_num 정의하여 pok_name과 pok_num에 입력값을 dictionary 형태로 저장하자
```
/*저장되는 방법*/
pok_name = {1: 'Bulbasaur', 2: 'Ivysaur', ...}  key : 순서 (이름을 가져오기 위함)
pok_num =  {'Bulbasaur': 1, 'Ivysaur': 2, ...}  key : 이름 (순서를 가져오기 위함)
#딕셔너리는 key값을 탐색하여 value를 반환하기 때문에 2가지 케이스로 저장했음
```
2. test에 리스트로 입력값을 받아 요소를 순서대로 검색하면서 숫자인지 확인하고,
   문자 → 숫자(pok_num), 숫자 → 문자(pok_name)로 결과값을 출력하자

* * *

### 💻결과코드
```python
import sys
input = sys.stdin.readline

n,m = map(int, input().split())
pok_name = {}
pok_num = {}

for i in range(1,n+1):
	#1~N까지 입력값 받기
    name = input().rstrip()
    pok_name[i] = name  
    pok_num[name] = i   

#testcase 탐색하면서 숫자→문자 / 문자→숫자를 반환
test = [input().rstrip() for _ in range(m)]
for i in test:
    if i.isdigit():
        print(pok_name[int(i)])
    else:
        print(pok_num[i])
```

* * *

#### ✏️1. N, M 저장하고 pok_name, pok_num을 딕셔너리로 저장
```python
import sys
input = sys.stdin.readline

n,m = map(int, input().split())
pok_name = {}
pok_num = {}

for i in range(1,n+1):
    name = input().rstrip()
    pok_name[i] = name
    pok_num[name] = i
```
```python
    ※2가지 케이스를 다르게 저장하는 이유?
    입력값이 숫자(순서)라면 포켓몬의 이름을 반환, pok_name을 사용
    ##pok_name = {1: 'Bulbasaur', 2: 'Ivysaur', ...}
    입력값이 문자(이름)라면 포켓몬의 순서를 반환, pok_num을 사용
    ##pok_num = {'Bulbasaur': 1, 'Ivysaur': 2, ...}
```

* * *

#### ✏️2. 비교값(test)이 숫자인지(.isdigit())확인하여 결과값 출력
```python
test = [input().rstrip() for _ in range(m)]
for i in test:
    if i.isdigit(): #숫자라면 name을 반환
        print(pok_name[int(i)])
    else:  #숫자가 아니라면 num을 반환
        print(pok_num[i])
```

* * *

### 📚초기 알고리즘 오류와 정리
※초기 알고리즘
```
pok = {} 으로 {name:num, name:num ...}저장 후 
비교값으로 name이 들어오면 num으로, num이 들어오면 name으로 반환하려고 했으나,
딕셔너리를 2가지 경우로 저장해서 비교하면 더 간단한 것이라고 판단함
```
* * *
1. 비교값이 n인경우 m을, m인경우 n을 출력하는 케이스는 딕셔너리를 2가지로 나누면 편함
2. <code>str() == true</code>뿐 아니라 <code>.isdigit()</code>이라는 훌륭한 내장함수가 있다는 것을 깨달음
<code>.isdigit()</code>같은 내장함수의 종류는 아래 링크 참고! 정리가 잘 되어있음
[code_angler님 포스팅 (파이썬(Python) 문자/숫자인지 확인하기[isalpha, isdigit, isalnum])](https://velog.io/@code_angler/%ED%8C%8C%EC%9D%B4%EC%8D%ACPython-%EB%AC%B8%EC%9E%90%EC%88%AB%EC%9E%90%EC%9D%B8%EC%A7%80-%ED%99%95%EC%9D%B8%ED%95%98%EA%B8%B0isalpha-isdigit-isalnum)



