# matplotlib추기

import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams['font.family'] = 'Malgun Gothic'  
matplotlib.rcParams['font.size'] = 15 
matplotlib.rcParams['axes.unicode_minus'] = False


1. plt.plot()에 값이 하나만일때
원래는 plt.plot(x,y)
하지만 plt.plot(data)라면 x축은 0부터 1씩 증가, y값이 data 값

1-2.plot계단형 차트로 그리기
plt.plot(data,drawstyle='steps-post')

2-1. 정규분포난수 뽑기
random.gauss(mu,sigma)  -> mu=평균(default=0), sigma=표준편차(default=1)
여러개뽑기=[random.gauss() for i in range(100)]
plt.hist(여러개뽑기)  ->정규분포그래프

2-2. 균등분포 난수 뽑기
random.uniform(a=165,b=175)   ->165~175사이값 중 하나 동일한 확률로 가져옴
여러개뽑기=[random.uniform(a=165,b=175) for i in range(100)]
plt.hist(여러개뽑기)하면 거의 직사각형 형태


3. 이산형변수(discrete): 하나하나 셀수있는변수(변수 사이에 값없음-100명과 101명 사이에 100.5명 존재X)
 - bar, barh, pie

4. 연속형변수(continuous): 변수 사이에 무수히 많은 값을 가질 수 있음(키,몸무게)
 - plot, scatter, hist, boxplot, stem

    4-1. scatter: 군집별 산점도
group=df['학년']
plt.scatter(x,y,c=group,s=group*100,marker='o')  #c:색을 달리할 기준(cluser), s=size, marker사용가능

각 포인터에 레이블 표시
for idx, value in enumerate(group):
    plt.text(x[idx],y[idx]+0.05,value,ha='center',size=20)
 or
for idx, value in enumerate(group) : 
    plt.annotate(value, xy=(x[idx], y[idx]))  #value에 넣을 text, xy=(x좌표,y좌표)
#annotate는 화살표 표시에 사용:plt.annotate(text, xy=(), xytext=(), arrowprops=...)
#xy: 화살표가 가리킬 위치    xytext: 텍스트가 표시될 위치   arrowprops: 화살표 스타일

    4-2. hist: 각 범위에대한 개수를 세줌
 기본: plt.hist(data)
 plt.hist(data,bins=n, histtype='type',range=(a1,a2),orientation='vertical',color='red')
# bins-> n개의 막대를 만들겠다
# histtype='bar', 'barstacked', 'step', 'stepfilled' 등
# range= 보여줄 x좌표범위/나머지는 잘림
# orientation='vertivcal', 'horizontal'

-한 plot안에 hist여러개 중첩해서 사용가능
plt.hist(data1)
plt.hist(data2, bins=20)
plt.show()    ->중복해서 표시

-옆으로 여러 막대형식으로 같이 놓기
plt.hist([data1,data2,data3])

-스택으로 위에 쌓기
plt.hist([data1,data2],stacked=True,color=['red','green'])
plt.show()

-누적쌓기(ex:curve growth)
plt.hist(data,cumulative=True)


    4-3. boxplot: 데이터의 분포를 박스로 표시/ 이상치 제공
기본: plt.boxplot(data)

-박스 여러개
plt.boxplot([data1,data2],labels=['1번데이터','2번데이터'])  #리스트나 2D, 판다스 형태로, labels로 x좌표
#외의 파라미터는 챗지피티로

5. 간략어
'color marker linestyle'  ex) 'bo--', 'rv-'

6. 격자무늬넣기
plt.grid()
plt.style.use('ggplot')


'''
색상기호

b : blue
g : green
r : red
c : cyan ( 청록색 )
m : magenta ( 자홍색 )
y : yellow
k : black
w : white

스타일 기호

- 실선 ( 기본값 )
-- 이음선
-. 점 이음선
: 점선
. 점
, 픽셀
o 원
v 역삼각형
^ 정삼각형
< 좌삼각형
> 우삼각형
1 작은 역삼각형
2 작은 정삼각형
3 작은 좌삼각형
4 작은 우삼각형
s 사각형
p 오각형
* 별표
h 육각형
+ 더하기 표
D 다이아몬드 표
X 엑스 표
'''
