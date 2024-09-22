# if True:->진행
#비교연산자: <, >, ==, !=, >=, <=
# or-둘중하나만 참이면, and-둘다 참이면, not x-x가 아니면 참
# x in list,tuple,string vs x not in //

money=1000
pocket=['phone','card','key']

if money >2000:
    print('take the bus')    
elif 'card' in pocket:
    print('take the taxi')
else:
    pass        #pass:그냥 흘허감-주로 조건문에서 넣어줄 조건이 딱히 없을경우나 class 선언할 때, 초기에 넣어줄 값이 없을 때 정도에 넣어줌
    print('just walk')  
    
#if문 짧게 표현하기
score=70
if score>65:
    message='success'
else: message='fail'
print(message)
#를 다음과 같이 쓸 수 있음
message='success' if score>65 else 'fail'  #참일떄 나오는결과 if 조건문 else 거짓일때 나오는 결과
print(message)