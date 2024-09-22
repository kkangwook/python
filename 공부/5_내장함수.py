# import가 필요없는 함수

print(abs(-2))  #절대값

print(all([1,'hi','']))     #전부 참이어야 True
print(all([]))      #예외

print(any(['',0,'a']))      #하나만이라도 참이면 True

print(chr(100))     #유니코드->문자
print(ord('d'))     #문자->유니코드

print(dir([]))          #쓸수 있는 변수나 함수
print(dir({'a':1}))

print(divmod(7,4))      # 몫과 나머지를 튜플로

for x,y in enumerate([1,2,'hi','bye']):     #요소에 index화
    print(x,y)
    
print(eval('1+2'))      #실행한 결과를 리턴

a=filter(lambda x: x>0,[1,2,5,-7,4,-3,6,-9,])   #함수에서 참인것만 리턴
print(list(a))                                  #양수만 뽑힘

print(str(2)+'hi')          #숫자를 string화

class A:                           #클라스의 인스턴스인지 확인
    pass
a=A()
print(isinstance(a,A))

a=map(lambda x,y: x+y,[1,2,3],[10,20,30])       #데이터를 받아 순서대로 리턴
print(list(a))

print(max(1,2,3,4))     #최대   str과 int는 같이 못함
print(min('python'))     #최소

print(pow(3,4))     # x의y제곱

for i in range(10,1,-2):    #(시작,끝,변화값)
    print(i)
    
print(round(3.141592,2))    # (반올림할려는 값,볼려는 소수점):3.14

print(sorted([1,5,3,6,4]))  #sort후 리턴

print(sum([1,2,3,4,5]))       #합

print(type([]))         #어떤 타입인지

a=zip([1,2,3],[1,3,4,7],[3,4,5])       #짝 짓기
print(list(a))