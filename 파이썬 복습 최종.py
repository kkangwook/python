import pandas as pd
import numpy as np
from scipy import stats
#1. 7_extra_things.py
#2. 6_정규표현식.py
#3. 5_error.py

#4. x를 키, y를 value로 해서 딕셔너리 컴프리헨션하기
x=['a','b','c']
y=[1,2,3]

#5.리스트컴프리헨션으로 양수면 X2, 음수면 X100, 0이면 999999로
data=[1,10,0,-1,3,-2,0]

#6. print('a','b')사이에 '-'넣기
#print('a','b')

#7. for문에서 print문 이어지게 나오게 하기
#for i in range(10):
#    print(i)
    
#8. f'{x}'의 모든 표현법 사용
num=12345987.342394872987


#9. re로 문장부호화 특수문자 제거(?$;:.,*등)

#10. 함수만들때 정보뜨게하기

#11. 리스트 정렬하기
data=[
 ('홍길동', 3.9, 20160303),
 ('김철수', 3.0, 20160302),
 ('최자영', 4.3, 20160301),
]

#12. 딕셔너리 정렬하기
dic={'a':1,'b':6,'c':2,'d':4}

#13. pickle, json방법

#14. 날짜형으로 변환 후 년도, 월, 일, 시간, 분 가져오기
Date = pd.Series(['2021-10-05 07:10:32', '2022-11-10  10:20:32', '2023-11-15  14:50:32', '2023-12-20  20:30:32'])


#15. disp컬럼에 결측치있는 행들을 제거
a = pd.read_csv('./data/mtcars.csv') 

#16-1. 단일표본 t검정 : 한 집단의 평균이 174인지 검정
data = np.random.uniform(172, 179, size=29)

#16-2. 독립표본 t검정 : 두 집단 평균 검정(남여 평균 점수 차이 검정)
# 필요한 조건들 다 검정해서
female_score = np.random.uniform(50, 100, size=30) # 여학생 점수  
male_score = np.random.uniform(45, 95, size=30) # 남학생 점수  

#16-3. 대응표본 t검정 : 대응 두 집단(복용전 vs 복용후 몸무게 변환)
before = np.random.randint(60, 65, size=30)  # 복용전 몸무게 
after = np.random.randint(59, 64,  size=30)  # 복용후 몸무게 

#17-1. 일원 chi-square(1개 변수 이용) : 적합성 검정
# 위약(가짜약)은 실제 약효는 없지만, 심리적인 요인에 따라 환자에게 긍정적 또는 부작용이 나타날 수 있다.
# 감기약 위약을 투여받은 환자들의 부작용은 다음과 같은 비율로 알려져 있다.
#
# 구분    부작용    비율 
# 1       아픔     10% 
# 2     조금 아픔   5% 
# 3      속쓰림     15% 
# 4     이상 없음   70% 
#
# 한편, 항암약 위약을 투여받은 환자들에게 실제로 관찰된 부작용은 다음과 같다:
# (여기서 값 1은 ‘아픔’, 2는 ‘조금 아픔’, 3은 ‘속쓰림’, 4는 ‘이상 없음’을 의미함)
df = pd.DataFrame({'항암약': [4, 4, 3, 4, 1, 4, 1, 4, 1, 4,
                              4, 2, 1, 4, 2, 3, 2, 4, 4, 4]}) 
#감기약 위약의 부작용 비율(기대값)과 항암약 위약의 부작용 관찰값(관측값)이 통계적으로 차이가 있는지 확인하기 위해 적합도 검정을 수행하시오.


#17-2. 이원 chi-square(2개 변수 이용) :두 변수간 상관성 검정
# education과 smoking간의
smoke = pd.read_csv("./data/smoke.csv")
#print(smoke.head())

#18. 전체 데이터의 상관계수와 공분산을 행렬형식으로 -> score와 다른변수간의 -> score와 iq간의
score_iq = pd.read_csv('./data/score_iq.csv')
#print(score_iq.head())

#19. 다중선형회귀분석:score와의 상관계수가  ±0.3 이상인 독립변수를 사용하여 score를 예측하는 다중선형회귀모형을 실시
# 모델의 요약->각 변수의 p-value값->각 변수의 회귀계수값->모델의 설명력(결정계수)->95% 신뢰수준의 신뢰구간
# new_data = pd.DataFrame({'iq': [110], 'academy': [2], 'tv':[2]})로 예측치와 신뢰구간구하기
score_iq = pd.read_csv('./data/score_iq.csv')

#20. cupon_react 변수와의 상관계수가  ±0.25 이상인 독립변수를 사용하여 cupon_react를 예측하는 로지스틱 회귀모형을 실시
# 모델의 요약->각 변수의 p-value값->각 변수의 회귀계수값 
# age변수가 5단계증가할때 오즈비(odds ratio)값
# 1~10을 다시 예측해보기
cupon = pd.read_csv('./data/cupon.csv')

#21. 신용대출과 담보대출의 합인 총대출액 컬럼을 추가
#->각 지역코드 내에서 성별별(1과 2)로 총대출액의 합계를 계산
#->각 성별을 컬럼화해서 지역코드별 남자/여자의 총대출액 보기
df = pd.read_csv('./data/ex_9_1_1.csv')
#print(df.head())
df['총대출액']=df['신용대출']+df['담보대출']
#print(df.head())

#22. 근속연수의 결측치는 동일한 부서 및 성과등급을 가진 직원들의 평균 근속연수로 대체
df = pd.read_csv('./data/ex_9_1_3.csv')
print(df.head())

"""
#4
dic={i:j for i,j in zip(x,y)}
print(dic)

#5
print([i*2 if i>0 else(i*100 if i<0 else 999999) for i in data])

#6
print('a','b',sep='-')

#7
for i in range(10):
    print(i,end=', ')
    
#8
print(f'{num:<8,.3f}')
"""
#9
#import re
#a=re.compile(r'[^\w\d\s]')
#a.sub('',text)

"""
#10
def x(a:int, b:float)->int:
    return a+b
x()

#11
print(sorted(data,key=lambda x:x[1],reverse=True))

#12
print(sorted(dic,key=lambda x:dic[x],reverse=True))




#13-1 json

-encoding
encoded=json.dumps(data, ensure_ascii=False)   #dumps로 data객체를 encoded변수에 저장
with open('./json_data.txt','w',encoding='utf-8') as f:   #데이터가 들어갈 txt형식의 파일생성
	f.write(encoded)
    
-decoding
f=open('./json_data.txt','r',encoding='utf-8')      
decoded=f.readline()			#파일 열기
f.close()
python_data=json.loads(decoded) 





#13-2 pickle
f= open('./pkl_data.pickle', mode='wb')    # writing binary로 열기
pickle.dump(data, f)        # .dump로 data를 pickle확장자(or pkl)파일에 저장
f.close()

-pickle파일 불러오기
f = open('./pkl_data.pickle', mode='rb')    # reading binary로 열기
data = pickle.load(f)       #.load로 불러오기
f.close()





#14
date=pd.to_datetime(Date)
print(date.dt.year, date.dt.month, date.dt.day_name(), date.dt.hour, date.dt.minute)

#15
print(a.shape)
a=a.dropna(subset=['disp'])
print(a.shape)

#16-1
from scipy import stats
print(stats.ttest_1samp(data,174))

#16-2
s1=stats.shapiro(female_score) #귀무가설이 집단은 정규분포를 따른다
s2=stats.shapiro(male_score)
l=stats.levene(female_score,male_score) #귀무가설이 두 집단은 등분산성을 따른다
st,p=stats.ttest_ind(female_score,male_score,equal_var=True)
print(p,s1,s2,l,sep='\n')

#16-3
t,p=stats.ttest_rel(before,after,alternative='greater')
print(t,p)


#17-1
real_data=df['항암약'].value_counts().sort_index().values
exp_data=np.array([0.1,0.05,0.15,0.7])*len(df)
print(exp_data)
print(real_data)
print(stats.chisquare(real_data,exp_data))


#17-2
table=pd.crosstab(index=smoke['education'], columns=smoke['smoking'])
print(table)
x=stats.chi2_contingency(table) #귀무가설: 두 변수는 독립이다
print(x)




#18
cor=score_iq.corr(); cov=score_iq.cov()
print(cor, cov)
print(cor['score'], cov['score'])
print(score_iq['score'].corr(score_iq['iq']))




#19
print(score_iq.corr()['score']) #iq, academy, tv

from statsmodels.formula.api import ols
model=ols('score~iq+academy+tv',score_iq).fit()
print(model.summary())
print(model.pvalues)
print(model.params)
print(model.rsquared)
print(model.conf_int(0.05))

new_data = pd.DataFrame({'iq': [110], 'academy': [2], 'tv':[2]})
pred=model.predict(new_data)
print(pred)
gp=model.get_prediction(new_data)
conf_int=gp.conf_int(0.05)
print(conf_int)



#20
print(cupon.head())
print(cupon.corr()['cupon_react']) #gender, age, marry

from statsmodels.formula.api import logit
model=logit('cupon_react~gender+age+marry',cupon).fit()
print(model.summary())
print(model.pvalues)
print(model.params) #intercept는 모든 변수가 0일때의 회귀계수값==z(로그오즈값)

log_odds=model.params['age']
print(log_odds)
ratio=np.exp(log_odds*5)
print(ratio)

pred=model.predict(cupon.iloc[:10]) #알아서 변수 설정해서 집어넣음
pred=(pred>=0.5).astype(int)
print(pred)

#21
gby=df.groupby(['지역코드','성별'])['총대출액'].sum()
print(gby)
gby=gby.unstack()
print(gby)

#22
vmean=df.groupby(['부서','성과등급'])['근속연수'].transform('mean')
print(vmean)
print(df.isnull().sum())
df['근속연수']=df['근속연수'].fillna(vmean)
print(df.isnull().sum())
"""