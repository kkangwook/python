# 1. 숫자 , 대신 '_' ->읽기편한게
a=100,000   #튜플 (100,000)형태로
b=100_000   # 1000000그대로
print(a,b)


# 2. sort함수 역순으로
a=[1,5,3,6,3]
a.sort(reverse=True)
print(a)


# 3. 함수 파라미터와 아규먼트
   # def 함수명(파라미터):   ->함수 선언때 들어가는 변수를 파라미터 라함
   # print(함수명(아규먼트))  ->함수 출력할때 넣는 변수들을 아규먼트 라함

def custom_sum(list,sum=0):    #여기에 sum넣어놔서 안에 sum=0안해도됨
    for i in list:
        sum+=i
    return sum
print(custom_sum([1,2,3,4]))



# 4. *arg와 **kwarg(keyword argument)
   # arg는 튜플타입으로 들어감, 함수당 딱 한번만 사용가능
   # kwarg는 key=value형태로 들어감
def hap(*args, **kwargs):
    print(type(args), args)
    print(type(kwargs), kwargs)
    return sum(args)+sum(list(kwargs.values()))
print(hap(1, 2, 3, 4, num1=5, num2=6))   # 1,2,3,4는 args의 튜플로, num1=5,num2=6은 kwargs의 key와 value로

# list타입 데이터를 args로 호출하는 법
# *는 풀어버린다는 의미
def gop(n1,n2,n3):
    return n1*n2*n3
ls=[2,3,4]
print(gop(*ls))   # 길이 같으면 호출할때 *를 앞에써줌 



# 5. if문과 for문 한줄에 쓰기->메모리 줄이기 가능
def x(a):
    result=[i+100 if not i else i*2 for i in range(len(a))]
    return result
print(x('asdf'))



# 6. docstring->함수에 대한 설명 "3개씩으로 감싸기
def exam(x):
    """
    함수에 대한 설명을 여기 작성
    """
    print('hi')
print(help(exam))   #help함수 사용


# 7. 지역변수, 전역변수->함수안에 global사용
data=100        #이 data는 전역변수
def gv1():
    data=50      #이 data는 지역변수(함수안)
    print(data)
gv1()   #50으로 나옴
print(data)  #하지만 data는 100

def gv2():
    global data   #밖에꺼 가져와서 내부에서 가공이 가능해짐(지역변수가 전역변수가 됨)
    data=50
    print(data)
gv2()
print(data)   #50으로 나옴->global에 의해 data 바뀜



# 8. 함수안에 함수(inner function)
def outer(a,b):
    def inner(c,d):
        return c+d
    return inner(a,b)
print(outer(1,2))   # 3나옴
#해석: 1,2가 들어가면 일단 inner함수가 내부에 있구나 하고 넘어가다 return을 만남
 #근데 여기서 inner(a,b)를 반환하라함->그럼 inner(c,d)에 a,b를 넣어 inner(1,2)가되고
 #결과 1+2는 3이 나옴
# print(inner(1,2)) 얘는 지정한적 없으므로 에러남

##그렇다면 내부 inner함수 쓰는 법은?
def outer2(a,b):
    def inner(c,d):
        return c+d
    return inner
#그냥 outer2(1,2)하면 inner함수 정보만 나옴
print(outer2(3,4)(1,2)) #outer2(3,4)는 inner가 되고 따라서 inner(1,2)를 계산하게됨



# 9. callback function: 함수를 다른 함수의 파라미터로 설정해서 사용
   #주로 재귀함수에 사용
def calc(func,a,b):    #func에 함수넣음
    return func(a,b)   #return에 함수사용

def add(a,b):
    return a+b
def mul(a,b):
    return a*b
print(calc(add,3,4), calc(mul,3,4))



# 10. reduce함수: list데이터를 순서대로 적용하여 결과 누적
from functools import reduce
listt=[3,1,2,4,5]
reduce_result=reduce(lambda x,y: x+y,listt)  # 누적값이 x로 치환되고 새로운 y값을 더해 다시 x로 치환하며 이를 반복
print(reduce_result)



# 11-1. decorator
  # -함수에서 코드를 바꾸지 않고 기능을 추가하거나 수정하고 싶을때 사용
  # -inner function을 선언했을때 인스턴트처럼 사용(class개념)
  # -큰 틀을 만들어두고 함수를 선언해서 집어넣기
def mother(func):    # <-inner function을 포함하고 있는 mother가 decorator 
    def wrapper(*args,**kwargs):   #inner function
        print('decorator activated')
        result=func(*args,**kwargs)
        print(result)
        print('decorator done!')
        return result
    return wrapper

@mother    # @으로 decorator 선언
def plus(a,b):    # @과 그 밑에 plus가 같이 선언되어 mother란 decorator의 func에 plus가 들어간 개념
    res=a+b
    return res

print(plus(3,4))      ## decorator의 print문들도 같이 나오게됨  

# 11-2. decorator 실행 예제1(함수의 실행 시간을 출력하는 함수)
def timer(func):
    import time
    def wrapper(*args,**kwargs):
        start_time=time.time()    # 실행될때의 시간
        res=func(*args,**kwargs)
        end_time=time.time()
        print(f'running time:{end_time-start_time}')  #걸리는시간
        return res
    return wrapper

@timer               # 할때만다 @하고 밑에 넣을 함수
def test1(n1,n2):
    data=range(n1,n2+1)
    return sum(data)

@timer               #할때마다 @하고 밑에 넣을 함수
def test2(n1,n2):
    res=0
    for i in range(n1,n2+1):
        res+=i
    return res

print(test1(1,100_000))   #decorator적용되어 timer의 시간들 나옴
print(test2(1,100_000))


# 11-3. decorator 실행예제2(비밀번호가 일치할때만 연산)
def check_pw(func):
    def wrapper(*args,**kwargs):
        pw='3179'
        login=input('password?:')
        if login==pw: 
            return func(*args,**kwargs)
        return 'wrong password!!'
    return wrapper
@check_pw
def pwadd(a,b):
    return a+b
print(pwadd(1,2))   # 실행후 정확한 비번을 입력해야 함수 실행



# 12-1. class로컬변수
# 추가로 슈퍼클래스는 부모, 서브클래스는 부모(슈퍼클래스)를 상족한 애들
class account:
    loan=0    #여기에 loan값
    deposit=0
    def add_loan(self,money):
        self.loan+=money            # self.loan가능
        return self.loan
print(account.loan)   # 0나옴, __init__없어도 가능
local_loan=account()
print(local_loan.add_loan(100))  #100이 더해진 100출력


# 12-2 생성자 (__init__)
# __init__에 self만 있으면 변수설정때 ()로 하면됨
# 하지만 self외에 파라미터 설정했다면 ()안에 어규먼트들 다 넣어야함
class account2:
    def __init__(self):
        self.loan=0
        self.deposit=0
        print('계좌가 생성되었습니다')
    def add_loan(self,money):
        self.loan+=money            # self.loan가능
        return self.loan
initiator=account2()  # 계좌가 생성되었습니다 문구 뜸


# 12-3 소멸자 (__del__)-> del로 삭제시 해당 작업 실행
class account3:
    def __init__(self):
        self.loan=0
        self.deposit=0
        print('계좌가 생성되었습니다')
    def add_loan(self,money):
        self.loan+=money            # self.loan가능
        return self.loan
    def __del__(self):
        print('계좌가 폐쇄되었습니다')
delete=account3()
del delete     # 계좌가 폐쇄되었습니다 문구 뜸



# 13. mangling: class변수명 앞에 __를 붙여 접근할 수 없도록 설정
class mang:
    def __init__(self,value):
        self.__mangle=10   # mang앞에 __(두개)
        self.value=value
    def add(self):
        self.value+=self.__mangle
        return self.value
m=mang(5)
m.__mangle=20
print(m.add(),m.__mangle)   # 20으로 바꿨지만 10으로 고정



# 14.슈퍼 super()-> 서브클래스에서 부모클래스이 함수 사용
class phone:
    def __init__(self,function=None):
        self.name=function
        print(f'{function} phone 개통')
class subphone(phone):                  #자식에 새로운 생성자 만들면 자식의 생성자 조건을 따라야함!!!!
    def __init__(self,function=None):  #부모 생성자는 이용되지않음
        super().__init__(function)    #따라서 부모 생성자 가져와서 사용하겠다 
a=subphone('fwef')   # phone클래스의 생성자로 출력

#이해 더 쉬운 예시
class x:
    def __init__(self):
        self.value=0
    def hi(self):
        print('hi')
class newx(x):
    def __init__(self):
        super().__init__()
    def add(self,num):
        super().hi()       # class x의 hi메서드 가져와서 씀
        return self.value+num
k=newx()
print(k.add(100))  # hi가 프린트 되고 100값 출력


# 15. class다중상속->,를 사용
class multi(account,phone,mang):
    pass
mul=multi(1)


# 16. 사용자 정의 예외처리
class myerr(Exception):   #exception 슈퍼클래스 사용
    def __str__(self):  # __str__로 오류시 출력할 문장 설정
        return 'number is greater than 10'
def morethan_10(num):
    if num<=10: raise myerr()
    print(num)

# print(morethan_10(9))  #에러 발생->원인도 __str__이 설명




# 17. 리스트 두개를 합쳐 딕셔너리화
a=[1,2,3,4]
b=['a','b','c','d'] 
c=zip(a,b)
print(list(c))
print(dict(zip(a,b)))   # dict함수로 딕셔너리화
# or
d=[[1,'a'],[2,'b'],[3,'c'],[4,'d']]
print(dict(d))



# 18. 중첩함수
def outer_func(data) : # outer 함수 
    dataset = data # dataset 생성
    
    # inner 함수 
    def tot() : # 합계
        tot_val = sum(dataset)
        return tot_val

    def avg(tot_val) : # 평균 
        avg_val = tot_val / len(dataset)
        return avg_val        
    
    return tot, avg # inner 함수 반환 

tot, avg=outer_func([1,2,3,4,5])    #두개로 받아옴
print(tot())     # ->15
print(avg(tot()))    # ->3.0


# 문제
'''
문7) 중첩함수 응용 : 아래와 같이 outer와 inner 함수의 역할에 맞게 두 개의 내부함수(innder)를 
     완성하시오.

 1.outer 함수 역할 : 3명 학생의 점수(scores) 저장, inner 함수 포함 
 2.inner 함수 역할 : 
   tot_df 함수 : 각 학생의 점수(3개 과목)를 이용하여 촘점을 계산한 후 총점을 반환한다.
   avg_df 함수 : 각 학생의 총점과 과목수를 인수로 받아서 평균을 계산하고 결과를 출력한다.
     
 <출력 결과>
  평균 = [70.0, 85.0, 79.0]
'''

def scores_pro(scores) : # outer 
    scores = scores
    
    # 총점 계산 : inner
    def tot_df() :
        pass
        
    # 평균 계산 : inner
    def avg_df(tots, cnt) : # (총점, 과목수)
        pass
    
    return tot_df, avg_df # 내부함수 반환 


# 실인수로 사용할 3명의 학생 성적(과목수 3개) 
scores = [[60,80,70], [80,85,90], [70,82,85]]


# 19. nonlocal 명령어 

def main_func(num) : # outer
    num_val = num # data 생성 
    
    # inner 
    def get_func() : # 값 획득 : 획득자 ->함수내의 값을 외부로 넘기는 함수
        return num_val  
    
    def set_func(value) : # 값 지정 : 지정자 ->함수내의 값을 수정하는 함수
        nonlocal num_val    # ->outer의 main_func에서 만든 변수를 가져오겠다
        num_val = value  # 새로운 value로 num_val수정-> return이 없음
        
    return get_func, set_func
   
a,b=main_func(99)
print(a())    # ->99
print(b(88))   #none
print(a())   # ->88  :set_func(88)로 수정했으므로

#20. mangling추가

class Account : 
   
    # 생성자 
    def __init__(self, bal, name, no):
        # 동적 멤버 변수 
        self.__balance = bal # 잔액(은닉 멤버변수)
        self.name = name # 예금주  
        self.no = no # 계좌번호         
            
    # 잔액확인 : 획득자(getter) - return문 
    def getBalance(self): 
        return self.__balance     #이렇게 맹글링 부르는 것은 가능!!!!!!!!!!1
    
    # 입금하기 : 지정자(setter) - 매개변수 
    def deposit(self, money):
        self.__balance += money
    
    # 출금하기 : 지정자(setter) - 매개변수  
    def withdraw(self, money): 
        self.__balance -= money

#객체 생성
acc1=account(1000,'홍길동','12345')

#맹글링의 특징
# 1. dir에 안나옴
dir(acc1)해도 name이나 no는 나오는데 __balance는 안나옴
#2. 부를수 없음
print(acc1.__balance, acc1.balance)  #둘다 에러남/또한 acc1.__balance=2000과 같은 행위도 불가!!!!!!

#따라서 획득자로 불러야 됨!!!!!!!!!
print(acc1.getBalance)
여기서 dir(
