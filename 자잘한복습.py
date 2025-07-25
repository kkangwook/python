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


--glob: 패턴 인식해서 파일을 가져옴
from glob import glob
glob(path + '/data/*.jpg') # jpg파일 가져옴
-----------------------------------------------------------------------------
#판다스
-- df.함수의 default는 axis=0(아래로==열별) 하지만  axis=1도 가능!!!!(행별)

-- df의 컬럼의 리스트로:  df[col].tolist()

-- df['col']과 df.col은 같음

--판다스는 연산에 na가 있으면 na
-- but!! 집계함수는 na무시

--합병 두가지
	merge: sql의 조인(on + inner, left, rigth, outer join)
	concat: 공통된 컬럼없어도 그냥 이어줌(사이즈 달라도 됨)
	
--데이터 프레임의 1차원화
	1D=df.stack() -> 1차원화
	2D=1D.unstack() -> 다시 원상태의 2차원으로

-- 데이터프레임도 행/열 바꾸기 가능
	df.T

--함수를 개별로 적용시키고 싶을때
	-집계함수는 행or열단위로 실행하거나 일반함수를 각 요소마다도 실행가능
    -apply: df와 df.groupby(), Series에 사용가능
		df.apply(func,axis=1 or 0)
		df[col].apply(func) #이 함수는 집계함수X !!!
    -map: series나 df['column']에 사용가능
@딕셔너리 적용
    def encoding_df(x):  #여기서 x는 df나 series안의 하나의 값
    	encoding = {'red':[1,0], 'white':[0,1]}
    	return encoding[x]
   얘는 딕셔너리라서 map으로 권장하지만 apply도 가능

--applymap(func)는 전체 원소에 함수 적용

----group by---- : 그룹 고유값을 인덱스로 두겠다 
- 주로 범주형을 하나 또는 여러개 그룹화(수치형도 가능하긴함)

- df.groupby([col1,col2,...,coln])은 인덱스에 왼쪽부터 col1,col2,...,coln순으로 나옴

- df.groupby후 표로 나타낼려면 .get_group말고는 전부 집계함수써야함(count, max, sum등) 

- groupby후 .agg(['mean','sum'])처럼 집계함수 여러개 사용가능-> 각 변수당 함수개수만큼 컬럼개수로 늘어남 

-- df.groupby()에서 바로 시각화하기 by .plot()
wine_group = wine_df.groupby(['type','quality'])
grp_mean = wine_group.mean()
 !!!반드시 그룹바이 후 집계함수 사용된 이후여야 .plot가능!!! 
grp_mean.plot(kind='bar', title='main title',y=['pH','citric acid'])  #플롯 종류 kind로 지정
plt.show()

!!! x에는 모든 인덱스가(그룹,다중그룹이면 튜플로 표시) y에는 요소값이, 그리고 각 컬럼별로 레이블 됨 !!!
	-> y지정안하면 모든 컬럼의 요소들이 전부 표시, .pie할때는 y컬럼 하나만 가



--df.plot() : 인덱스를 x, 값들은 y로하고 모든 컬럼의 값들 표시(색과 레이블 다르게)
	- x지정하면 그 컬럼의 *고유값*들을 x로, y지정하면 그 지정한 컬럼들의 값들만 표시 
	- or df[col].plot()으로 x지정도 가능
 kind종류: 불연속적 데이터(이산형) - line, bar, barh, pie, 
	   연속적 데이터 - hist, kde, box  #kde는 커널밀도추정: 히스토그램의 선형화 버전
	   	scatter는 df.plot(kind='scatter',x='',y='')필요 
		or pandas.plotting.scatter_matrix-> scatter_matrix(df)+ plt.show()
			-> df각 컬럼들간 모든 조합의 scatter_plot을 matrix로 보여줌(수치형 아닌것들은 df에서 제외필요)
df[['High', 'Low']].plot(color = ['r', 'b']): 컬럼 여러개도 가능
			
-- 카이제곱표 만들기 by pd.crosstab() ->두 개 이상의 범주형 변수 간의 교차표
ex1)
data = pd.DataFrame({
    '성별': ['남', '여', '남', '여', '남'],
    '흡연': ['예', '아니오', '예', '아니오', '아니오']})
pd.crosstab(index=data['성별'], columns=data['흡연'])# values, 함수 없으면 디폴트는 count

ex2) values는 반드시 aggfunc와 같이씀
data = pd.DataFrame({
    '성별': ['남', '여', '남', '여', '남'],
    '흡연': ['예', '아니오', '예', '아니오', '아니오'],
    '나이': [25, 30, 27, 22, 35]})
pd.crosstab(index=data['성별'], columns=data['흡연'], values=data['나이'], aggfunc='mean')


--pivot_tabel: 결국group by와 비슷 
pivot_table(DF, values='값',
                index = '행 칼럼', columns = '열 칼럼'
                ,aggFunc = '값에 적용될 함수')  #집계함수 생략하면 평균으로!!!!!
각 요소에 값 여러개 넣을 수 있음-> 리스트 형식으로 넣으면 됨
ex)
ptable = pd.pivot_table(data=pivot_data, 
               values='price', 
               index=['year','quarter'],   #인덱스는 두개 이상이면 인덱스 전부를 사용해 그룹화
               columns='size', aggfunc='sum')

table = pd.pivot_table(iris, values=['Sepal.Length', 'Petal.Length'], # 교차셀 칼럼
                       columns='Species', # 열 칼럼 
                       aggfunc= ['sum', 'mean'])  #함수두개면 각각의 컬럼을 추가로 생성

-pivot_table의 시각화도 가능
ptable.plot(kind='barh', stacked=True, title='main title')



--datetime64의 날짜형 인덱싱
df = df.set_index('Date') :datetime64형태인 date컬럼의 인덱스화
date값의 예시: 2016-02-01, 2016-01-29등
df.loc['2016'] : 모든 2016년도 데이터 가져옴
df.loc['2016-02']: 모든 2016년 2월 데이터 가져옴
df.loc['2016-01':'2016-02']: sort_index하고 2016년 1월, 2월 다가져올 수 있음


-- n일 단위 평균계산: n개치를 평균한 새로운 컬럼 생성
# rolling은 특정 기준으로 n개를 가져옴
roll_mean5 = pd.Series.rolling(df.High,   #high컬럼을 기준으로 
                               window=n, center=False).mean() #window에 개수지정/ 그룹바이처럼 함수써야 보여짐
# center가 false면 n번째 행부터 그 전 n행개를 가져옴
# center가 true면 n번째 행은 앞뒤로 n/2행씩 가져옴


--카테고리컬(범주형) 데이터타입 관리
-지정
df['class'] = pd.Categorical(df['class'],  #지정방법
                                   categories=['first', 'second', 'third'],  # 카테고리 순서 정의
                                   ordered=True)  # 순서가 있는 경우 True
-카테고리 ordered에 따라 정렬
df.sort_values(by = 'class') # category 오름차순:  First > Second > Third

-카테고리 순서변경
df['class_new'] = df['class'].cat.set_categories(['Third', 'Second', 'First'])
----------------------------seaborn-----------------------------------

--dataset 불러오기: nltk.corpus와 유사
import seaborn as sn
sn.get_dataset_names()  : 들어있는 데이터들 이름 보여줌
df=sn.load_dataset('iris') :이런식으로 불러옴

-- 다양한 시각화: kind로 타입, hue로 범주형 변수지정해 서로 다른 색상으로 시각화 (scatter의 c)
# seaborn 한글과 음수부호, 스타일 지원 
sn.set(font="Malgun Gothic", 
            rc={"axes.unicode_minus":False}, style="darkgrid")

# 1-1. displot : 히스토그램
sn.displot(data=iris, x='sepal_length', kind='hist')  
plt.title('iris Sepal length hist') # 단위 : Count 
plt.show()


# 1-2. displot : 밀도분포곡선 
sn.displot(data=iris, x='sepal_length', kind="kde", hue='species') 
plt.title('iris Sepal length kde') # 단위 : Density
plt.show()


# 2. 산점도 행렬(scatter matrix)  
sn.pairplot(data=iris, hue='species') 
plt.show()


# 3. 산점도 : 연속형+연속형   
sn.scatterplot(x="sepal_length", y="petal_length", data=iris)
plt.title('산점도 행렬(scatter matrix)')
plt.show()

# 4. 범주형(카테고리) 변수의 count_values시각화
sn.countplot(x = 'smoker', data = tips) #somker가 카테고리 컬럼
plt.title('smoker of tips')
plt.show()

# 5. 오차대역폭을 갖는 시계열 : x:시간축, y:통계량 
sn.lineplot(x = 'year', y = 'passengers',hue='month', data = flights)
plt.show()


# 6. 선형회귀모델 : 산점도 + 회귀선 
sn.regplot(x = 'sepal_length', y = 'petal_length',  data = iris)  
plt.show()


# 7. heatmap : 상관관계를 표현
y_true = pd.Series([1,0,1,1,0]) # 정답 
y_pred = pd.Series([1,0,0,1,0]) # 예측치 

# 1) 교차분할표(혼동 행렬) 
tab = pd.crosstab(y_true, y_pred, 
            rownames=['관측치'], colnames=['예측치'])

# 2) heatmap
sn.heatmap(data=tab, annot = True) # annot = True : box에 빈도수 
plt.show()

-----------------------------------------------------------------------
# matplotlib에 추가

--산점도행렬: n개의 데이터를 받아 nXn행렬로 두개 샘플간의 산점도 표현 
from pandas.plotting import scatter_matrix
scatter_matrix(iris[cols[:4]])  #데이터 여러개 들어감
plt.show()


-- 3차원 산점도
from mpl_toolkits.mplot3d import Axes3D
fig = plt.figure()
chart = fig.add_subplot(projection='3d')

chart.scatter(col_x, col_y, col_z, c = group) #df 국어 수학 영어
chart.set_xlabel('Sepal.Length')
chart.set_ylabel('Sepal.Width')
chart.set_zlabel('Petal.Length')
plt.show()



#맷플롯립
-- 수직선 긋기: plt.vlines(x,-1,n,colors,linestyles)
-- 수평선 긋기: plt.hlines(y,-1,n,colors,linestyles)


-- 이상치 제거 또 다른 방법
 plt.boxplot(df['키'])해서 이상치 점들 기준으로 new_df=df[df['키']>165] 가능


# 넘파이
R vs numpy:
	R: 열 우선 구조라 벡터를 더할때도 열형태로 더하고 차원도 (행,열,3차원)
	   이미지는 (100,100,3) ->차원이 3개(RGB) 
	numpy: 행 우선 구조라 벡터를 더할때도 행으로 더하고 차원도 (4차원,3차원,행,열)
	   이미지는 (100,100,3) -> (height, width, channel)형태로 들어감-> 열에 RGB값이 한쌍으로
		->이때 pytorch로 plt.imshow하면 (3,100,100)형태
-- 1차원으로 만들기 flatten,ravel말고 arr.reshape(-1) or arr.reshape(m*n)으로 가능 # (m,n) 일때


--시드값 적용하면 모든 이용자들은 같은 값 나옴
np.random.seed(234) 하고 이후에 작동하는 것들은 전부 동일

--np.log(arr) : 밑수 e인 로그함수
--np.exp(arr) : e^x제곱

--넘파이에서 결측치 보기: np.isnan(arr)
arr=np.array([1, 2.5,  np.nan, 3.3, 4.6, np.nan])
arr[~np.isnan(arr)] : 결측치 제거해서 표현

--난수 생성
-이항분포: 성공/실패 같은 두 가지 결과만 있는 시행
np.random.binomial(n=1, p=0.5, size=10) n=시행횟수, p= 성공확률
	-> 몇번성공했는지를 샘플size별로 출력 ex) n=10, p=0.5, size=1에서 [6]나옴: 10번 시도해서 6번 성공했다가 하나의 샘플
-정규분포 
np.random.normal(173, 5, 2000) mu, sigma, size
-표준정규분포
np.random.randn(size) mu=0 sigma=1
- 균등분포
np.random.uniform(10, 100, 1000) a,b사이를 c개수만큼


--10진수 숫자필기체 데이터 가져오기
from sklearn.datasets import load_digits 
digits = load_digits()
X = digits.data # 입력변수(X) 추출 
y = digits.target # 출력변수(y) 추출 
이후 x는 (64,)를 (8,8)로 reshape

--이미지 크기를 조정
from PIL import Image # PIL=python image lib
img = Image.open("~.jpg") : plt.imread처럼 이미지를 배열로 읽어옴
img.shape: (360, 540, 3)라 하면
img_re = img.resize( (150, 100) ) # (가로, 세로)
np.shape(img_re) 는 (100,150,3)이 됨
plt.imshow(img_re) 하면 화질이 구려진 버젼


--선형대수학
- 단위행렬 E
np.eye(n): nXn에서 대각만 1

-대각성분만 추출
np.diag(arr): arr의 대각성분만

-대각성분의 합
np.trace(arr)

-diagnol matrix만드는법
np.eye(3)X[a,b,c]: 3X3행렬에 대각이 a,b,c

-행렬식(determinant)
np.linalg.det(arr) #행렬에 같은 행이 하나라도 존재하면 determinant는 0

-역행렬
np.linalg.inv(arr)

-행렬내적: @
-행렬위적:np.cross(a, b)
