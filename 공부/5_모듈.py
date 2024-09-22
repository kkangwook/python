#.py로 만든 파이썬 파일들은 모두 모듈임
#같은 dir에 있어야 import 가능
#import 할려는 애들은 c:/doit/공부에 있어야 함
import mod1         # .py를 import
a=mod1.add(1,2)
print(a)

from mod1 import add as a       #이러면 함수import 가능 as 약어
b=a(3,4)
print(b)

from mod1 import add, sub              
print(add(4,5))
print(sub(7,3))



# mod1.py에 if __name__=='__main__':하고 print하면 여기서 실행안됨
# 왜냐면 import한 애의 __name__이 __main__이 되지 않고 mod1이 된다
print(mod1.__name__)        #mod1


#class의 import
print(mod1.pi)
a=mod1.math(4)
print(a.solv())

from mod1 import math       #class도 import
a=math(4)
print(a.solv())

#다른 dir에 있는 mod2.py import하기(c:/doit에 존재, 현재 위치는 c:/doit/공부)
import sys
print(sys.path)     #쓸수있는 모듈들이 있는 dir들(c:/doit/공부도 포함-현재 5_모듈.py의 위치이므로)
sys.path.append('c:/doit')  #c:/doit의 모듈도 가능하게끔 추가
print(sys.path)

import mod2
print(mod2.mul(2,7))




#c:/doit/공부/mod1.py정보    (전체 주석처리는 드래그후 ctrl+/)
# def add(a,b):
#     return a+b
# def sub(a,b):
#     return a-b

# pi=3.141592
# class math:
#     def __init__(self,r):
#         self.r=r
#     def solv(self):
#         return pi*(self.r)**2
    
# if __name__=='__main__': #이거 없이 import하면 맨 첫결과에 11이 다른 모듈실행에 뜸
#     print(add(1,10))


#c:/doit/mod2.py정보
# def mul(a,b):
#     return a*b
# def div(a,b):
#     return a/b