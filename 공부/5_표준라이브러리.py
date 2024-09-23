#import 필요
#구글에 python module index치면 import할수있는 모듈들 나옴

#날짜관련함수
import datetime as d
a1=d.date(2022,4,16)
a2=d.date(2020,6,18)
print(a1.weekday())     # 5->0월-6일이므로 토요일을 의미
print(a1-a2)            #날짜 차이

#시간관련함수
import time
print(time.time())      #1970 1월 1일 0시 기준으로 몇초 지났는지
print(time.ctime())     #현재 날짜와 시간

#출력 시간 정하기-time.sleep
for i in range(5):
    print(i)
    time.sleep(2)       # 2초마다 출력
    
#최대공약수, 최소공배수
import math
print(math.gcd(100,60,70))      #최대공약수
print(math.lcm(2,3,6,7,30))     #최소공배수

#random
import random
print(random.randint(1,45))         # 1에서 45중 랜덤하나
print(random.choice([1,2,3,4,5]))     #요소중 하나
print(random.sample([1,2,3,4,5],3))     #요소중 x개 랜덤으로 뽑기

#다른 개수를 zip
import itertools as i
students=['kim','park','han','lee','hwang']
snacks=['candy','chocolate','jelly']
a=i.zip_longest(students,snacks,fillvalue='nothing')    #남은요소는 fillvalue로 채움
print(list(a))

#순열, 조합
a=i.permutations([1,2,3,4],2)       #순서있이 2개고르기
print(list(a))
b=i.combinations([1,2,3,4],2)       #순서없이 2개고르기
print(list(b))
#로또
c=i.combinations(range(1,46),6)
print(len(list(c)))                 #1-45중 6개 순서상관없이 고르는 경우의 수=로또

#data를 특정 요소에 따라 sort: operator.itemgetter
import operator as o
data=[
('kim',22,'A'),
('park',32,'B'),
('lee',17,'B'),
('kang',27,'A')
]
result=sorted(data,key=o.itemgetter(1))     # 1번 요소인 나이 순으로 정렬(튜플,리스트)
print(result)                               # dic시 key값을 입력해줘야함

#파일을 리스트로 만들기
import glob
a=glob.glob('c:/doit/공부/*.py')        #이 위치의 ~.py파일들을 리스트로
print(a)                                #mod*로 표현시 mod~인 애들 전부 뽑음

#os자원을 제어해주는 모듈
import os
os.environ                  #현재시스템의 환경변숫값 리턴
print(os.getcwd())          #현재 디렉터리 위치
os.chdir('c:/doit/공부')    #디렉터리 위치 바꾸기
print(os.getcwd())

#os.mkdir-디렉터리 생성
#os.rmdir-디렉터리 삭제
#os.remove-파일 지우기
#os.rename(a,b)-a라는 이름의 파일을 b로 이름바꿈


#발생한 오류를 추적하는 모듈-traceback
import traceback
def a():
    return 1/0
def b():
    a()
def main():
    try:
        b()
    except:
        print('오류발생')
        print(traceback.format_exc())       #오류추적결과를 문자열로 리턴
main()

#사이트를 html파일로
import urllib.request

def x(a):
    i=f'https://wikidocs.net/{a}'
    with urllib.request.urlopen(i) as s:
        with open(f'wikidocs_{a}.html','wb') as f:
            f.write(s.read())

