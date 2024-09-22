#불자료형=True or False --> while, if에 사용
# ==같다 < > !=같지않다

print(type(True),type(False))
print(1==1)
print(1>2)
print(1<2)

#자료형에도 참과 거짓이 있음
#참: 'a', [a], (a), {'a':1}, 1
#거짓: '', [], (), {}, 0, none

#bool함수
print(bool(0))    #False
print(bool(''))     #False
print(bool(['a']))

#id값-주소값과 관련
a=[1,2,3]
print(id(a))            #고유값
b=a
print(id(a)==id(b))          #a와 b는 같음

a[2]=6
print(a,b)          #a가 바뀌면 b도 같이 바뀜

#복사하는 방법 두가지
a=[1,2,3]
b=a[:]          # 1. 슬라이싱 기법
a[2]=6
print(a,b)

from copy import copy   #copy함수, a.copy()도 가능
a=[1,2,3]
b=copy(a)
a[2]=6
print(a,b)

#변수 만드는 법
a,b=1,2             #튜플()생략가능
print(a,b)
(a,b)=1,2
print(a,b)
(a,b)=(1,2)
print(a,b)

[a,b]=[1,2]        #리스트로도 변수만들 수 있음
print(a,b)