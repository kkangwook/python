# def x(a):   함수이름x, 매개변수 a, 리스트등도 가능
#   return a*2    리턴값은 2a
def x(a,b):
    return a+b
print(x(1,2))  #x함수에 1,2를 넣어 1+2=3리턴

#입력값이 없는 경우
def hi():
    return 'hi'
print(hi())
try:
    hi(1)               #오류 발생-입력값이 없어야함
except TypeError:
    print('괄호안에 아무것도 없어야함')
    
#리턴값이 없는 함수-return 대신 print
def no_return(a,b):
    print(f'{a}와{b}')
n=no_return(1,2)        #값을 print
print(n)            #none이 나옴-return값이 없음

#매개변수 지정
print(x(b=2,a=3))       #순서에 상관없이 사용할 수 있다는 장점

#여러개 입력값 받기 *args
def y(a,*b):        #b는 리스트가 아닌 여러 입력값
    if a=='add':
        c=0
        for i in b:
            c+=i
    elif a=='mul':
        c=1
        for i in b:
            c*=i
    return c
print(y('add',1,2,3,4,5))       #15
print(y('mul',1,2,3,4,5))       #120

#매개변수 **kwargs
def k(**a):
    print(a)    #그냥 print
k(a=1,b=2,c='hi')  #{'a': 1, 'b': 2, 'c': 'hi'}로 나옴, key값은''필요X, value는 str시''

#함수의 리턴값은 언제나 하나->return사용시 끝
def r(a,b):
    return a+b, a*b
print(r(1,2))       #튜플로

result1,result2=r(1,2)      #각 각 값을 갖게됨
print(result1)
print(result2)

#return으로 break하기
def name(a):
    if a=='stupid':
        return
    print(f'my name is {a}')
name('stupid')      #break
name('kkangwook')

#매개변수에 초기값 설정:**항상 마지막 요소**
def x(a,b,c=True):
    print(f'{a}and{b}')
    if c:
        print('man')
    else:
        print('woman')
x('hi','bye')           #man
x('hi','bye',True)      #man
x('hi','bye','c')       #man
x('hi','bye',False)     #woman

#예약어
#함수이름=lambda x,y:x+y
add=lambda x,y:x+y
print(add(2,3))
