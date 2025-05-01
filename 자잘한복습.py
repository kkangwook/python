#기본파이썬

-----------리스트 컴프리헨션----------------
--for문과 if문 순서: if문 먼저오면 무조건 else문 써야함
data=['1','','2','','3']
-if문 먼저오면 ->결측치를 nan으로 대체
result=[i if i else 'nan' for i in data]
-if문 나중에와 else문 없으면->결측치를 제거
result=[i for i in data if i]

--else는 몇번이고 중첩사용가능
d=[i*3 if i>0 else(100 if i==0 else i*(-1)) for i in a]


----------- 딕셔너리 컴프리헨션가능----------
x=['a','b','c']
y=[1,2,3]
dict={i:j for i,j in zip(x,y)}
print(dict)   # {'a': 1, 'b': 2, 'c': 3}


-------------통계함수----------------
import scipy as sp
import seaborn as sns
  -정규성검사: sp.stats.shapiro(df)
  -ttest: sp.stats.ttest_ind(adf,bdf)
  -상관분석: df.corr(method='pearson') # nXn형태로 출력
             sns.pairplot(df) or sns.heatmap(df)  #plt.show()로 표시

from statistics import mean, variance, sqrt, stdev


-----------------print문---------------
--사이에 넣기
print(a,b,sep='-')  #a-b

--다른 줄 이어주기 
for i in range(5):
  print(i,end=',')   #0,1,2,3,4

--파일쓰기
f=open(~,'w')
print('hi',file=f)  #화면이 아닌 파일에 츨략

-- f''표현법/서식   : 는 서식의 시작을 의미
정렬(^<>)-전체출력폭-콤마(천단위마다)-소수점+자리수-데이터타입: f'{x:>8,.2f}'   # f는 float, d는 decimal int


--------------------------문자열---------------------
--문자열의 역방향은 [::-1]

--문자유형여부
testStr.isalpha() # 영어
testStr.isascii() # ascii문자인지
testStr.islower() # 소문자
testStr.startswith('he') # 뭐로시작하는지->true or false로 반환

--문자열 분리
text.split(sep=~)  #sep이 파라미터
text.split()  #구분자 생략시('\n', 공백) 을 기준으로

--escape
문자열에 \쓰고싶으면 r사용 or \\두번
'\hi\na\na'  #\hi 다음줄 a 다음줄 a
r'\hi\na\na'  #\hi\na\na
'\hi\\na\\na'  #\hi\na\na

--문장부호화 특수문자 제거(?$;:.,*등)
s=re.compile(r'[^\w\d\s]')
a=s.sub('',text)


-정규표현식에서 escape
- '\hi'를 꺼내오고 싶으면 re.compile(r'\\hi')으로   --r이후 \\두번으로 escape
-3자 이상을 가져오고싶다-> {3,}사용
-3자 이하를 가져오고싶다-> {1,3}


----------------------------잡-----------------------
--한줄에 변수 여러개 지정 by ;

--함수:x(a) vs 메서드(dir): a.count()

--한글 정규표현식
자음만 가져오기: [ㄱ-ㅎ]  vs 단어가져오기: [가-힣]

--list extend(요소들을 넣어줌) vs append(리스트를 넣어줌)

--def x(a:int,b:int)->int:  #실제로 int값 아니어도 에러안남

--input
 num.append(int(input()))  #프롬프트에 설명없음->값 입력하면 num에 채워짐

--튜플은 변경 불가능이지만 순서가 있다

-- 세트는 중복불가하며 수정불가하고 순서가 없다->indexing불가
			ㄴ하지만 iterable해서 for i in set: print(i)는 가능하다!!!!!!

--a=b=c=d=3가능->모든 변수 다 3의 값

-- 리스트 안의 딕셔너리 삭제할려면 정확히 같은 딕셔너리 값으로 .remove가능

--id값
-리스트 연산: 같은주소 저장->기존 객체 사용
-문자열 연산: 다른 주소 저장->새로운 객체가 만들어진다

--변수
-전역변수: 내/외부에 다 쓰일수잇음  ->global
-지역변수: 함수안에 지정된것으로 외부에서는 못쓰이고 내부에서만   ->nonlocal

--상위디렉토리가는법
	./: 현재
	../:한단계위로
	../../: 두단계위로




-------------------여러 문--------------------------
--다중문 가능
if (a>1 or a<0) or (b>1 or b<0):
	print('다시 입력하세요.)

--break: 해당하는 !!하나!!의 루프문만 빠져나옴

--딕셔너리로 빈도수 만들기
wc2={}
for ch in charset:
    wc2[ch]=wc2.get(ch,0)+1

--람다function
(lambda x, y : x + y)(10, 30)   <-바로사용
lambda data : [x**2 for x in data]  ->리스트를 넣어 리스트 리턴
lambda data: [map_data[i] if i in map_data else -1 for i in data]  ->if/for 동시사용도 가능


--리스트나 튜플 정렬하기
-multi_list=[
 ('홍길동', 3.9, 20160303),
 ('김철수', 3.0, 20160302),
 ('최자영', 4.3, 20160301),
]
sorted(multi_list, key=lambda x: x[1])		->김철수부터
sorted(multi_list, key=lambda x: x[1],reverse=True)	->최자영부터

-dic={'a':1,'b':6,'c':2,'d':4}
sorted(dic, key=lambda x: dic[x])
sorted(dic,key=dic.get,reverse=True)   --람다대신 직접 함수로도 가능
max(dic,key=dic.get)   --최대값



--try문  밑에처럼 가능
for i in range(3):
	try:
		~
	except:
		~
print~


----------------------클래스----------------------------
-- __init__과 __del__의 출력
__init__이나 __del__ 혹은 super().x()로 상속받을애들 출력될려면 return이 아닌 print로

def __del__(self):
	 print('hi')   #return은 안됨
하면 m=mother()만들고 del m하면 'hi'가 출력

-- 에러의 원인(__str__)출력방법
class myerr(Exception):
    def __str__(self):
        return '내맘임'
    
def err(a):
    if a>0:
        raise myerr()
try:
    err(10)
except myerr as e: #혹은 그냥 Exception as e도 가능
    print(e)   ->내맘임


-------------------------파일--------------------------
--파일 입출력
	r넣어서 \그대로 출력되게
path = r'C:\ITWILL\2_Python\workspace\chap06_FileIO\data'
file = open(path + "/etest.txt", mode = 'r')  ->path+형태도 가능

--os모듈
os.getcwd()  #현재 위치
os.chdir(path) # path로 이동->해당위치 파일 바로열기가능



--json(.txt or .json or .js형태->객체를 encoding하고 공유하고 decoding가능)
import json

-encoding
encoded=json.dumps(data, ensure_ascii=False)   #dumps로 data객체를 encoded변수에 저장
with open('./json_data.txt','w',encoding='utf-8') as f:   #데이터가 들어갈 txt형식의 파일생성
	f.write(encoded)

-decoding
f=open('./json_data.txt','r',encoding='utf-8')      
decoded=f.readline()			#파일 열기
f.close()
python_data=json.loads(decoded)   #디코딩해서 파이썬 객체에 저장

-ndjson(여러줄짜리)
file = open(path + "/labels.json", mode='r', encoding='utf-8')  #labels.json->여러줄의 dict형태
json_datas = file.readlines()   #여러줄이므로 readlines로
file.close()
python_list=[]
for each_jdata in json_datas:
    python_list.append(json.loads(each_jdata))




--pickle:파이썬 객체를 이진파일(binary)로 저장->0과1로 이루어져 컴퓨터가 직접 해석
	.pickle이나 .pkl확장자 사용
  -사용이유: 리스트, 딕셔너리뿐만 아니라 **함수, 클래스**등의 모든 파이썬 객체 저장하고 전송, 불러오기가능

1. data라는 객체를 pickle파일로 세이브
import pickle

f= open('./pkl_data.pickle', mode='wb')    # writing binary로 열기
pickle.dump(data, f)        # .dump로 data를 pickle확장자(or pkl)파일에 저장
f.close()

2. pickle파일 불러오기
f = open('./pkl_data.pickle', mode='rb')    # reading binary로 열기
data = pickle.load(f)       #.load로 불러오기
f.close()

3.pickle로 함수 저장하기
import pickle
def add(x,y):
    return x+y

f=open('./function.pickle','wb')
pickle.dump(add,f)
f.close()
-----------------------------------------------------------------------------
#판다스
-- df.함수의 default는 axis=0(아래로==열별) 하지만  axis=1도 가능!!!!(행별)
-- df의 컬럼의 리스트로:  df[col].tolist()
-- df['col']과 df.col은 같음
--판다스는 연산에 na가 있으면 na
-- but!! 집계함수는 na무시


#맷플롯립
-- 수직선 긋기: plt.vlines(x,-1,n,colors,linestyles)
-- 수평선 긋기: plt.hlines(y,-1,n,colors,linestyles)

# 넘파이
R vs numpy:
	R: 열 우선 구조라 벡터를 더할때도 열형태로 더하고 차원도 (행,열,3차원)
	   이미지는 (100,100,3) ->차원이 3개(RGB) 
	numpy: 행 우선 구조라 벡터를 더할때도 행으로 더하고 차원도 (4차원,3차원,행,열)
	   이미지는 (100,100,3) -> (height, width, channel)형태로 들어감-> 열에 RGB값이 한쌍으로
		->이때 pytorch로 plt.imshow하면 (3,100,100)형태
-- 1차원으로 만들기 flatten,ravel말고 arr.reshape(-1) or arr.reshape(m*n)으로 가능 # (m,n) 일때
