# 1-클래스 상속받고 메서드 추가하기1
class cal:
    def __init__(self):
        self.value=0
    def add(self,a):
        self.value+=a
        
class upgradecal(cal):
    def minus(self,a):
        self.value-=a
a=upgradecal()
a.add(3)
a.add(4)
a.minus(5)
print(a.value)
# 2-클래스 상속받고 메서드 추가하기2 cal에서 value는 100이상의 값은 가질 수 없음
class maxlimitcal(cal):
    def add(self,a):
        self.value+=a
        if self.value>100:
            self.value=100
a=maxlimitcal()
a.add(50)
print(a.value)
a.add(60)
print(a.value)

# 4-filter로 음수제거하기
data=[1,-2,3,-5,8,-3]
a=filter(lambda x: x>0,data)
print(list(a))

# 6-map사용하여 리스트를 3 곱하기
data=[1,2,3,4]
a=map(lambda x: x*3,data)
print(list(a))

# 7-최댓값과 최솟값의 합
data=[-8,2,7,5,-3,5,0,1]
a=max(data)+min(data)
print(a)

# 8-소숫점 4자리까지 반오림
a=17/3
print(round(a,4))

# 10-파일확장자가 .py인 파일만 찾기
import glob
print(glob.glob('c:/doit/공부/*.py'))

# 12-로또 번호 생성하기(1-45중 6개 중복없이)
import random
a=[]
while True:
    i=random.randint(1,45)
    if i not in a:
        a.append(i)
    if len(a)==6:
        break
print(a)

# 13-누나는 영철이보다 며칠 더 먼저 태어났을까?
import datetime as d
a1=d.date(1995,11,20)
a2=d.date(1998,10,6)
print(a2-a1)

# 14-기록순으로 정렬 (100m달리기 기록)
data=[
('윤',15.25),
('김',13.31),
('박',15.34),
('송',15.57),
('배',17.9),
('전',13.39),
('최',17.14),
('한',14.84),
('이',17.7),
('황',17.65),
('주',15.67),
('오',15.13),
('윤',16.93),
('문',16.39)]
import operator as o
a=sorted(data,key=o.itemgetter(1))
print(a)

# 15-청소당번 2명뽑기
data=['나지혜','성성민','윤지현','김정숙']
import itertools as i
a=i.combinations(data,2)
print(list(a))

# 16-문자열 나열하기 abcd를 나열할 수 있는 경우
#import itertools as i
a=list(i.permutations(['a','b','c','d'],4))
for q,w,e,r in a:
    print(q+w+e+r,end=' ')

# 17-5명에게 할 일 랜덤으로 부여하기
people=['김승현','김진호','강춘자','이예준','김현주']
work=['청소','빨래','설거지']
import random 
a=random.sample(people,5)
#import itertools as i
b=i.zip_longest(a,work,fillvalue='휴식')
print(list(b))

