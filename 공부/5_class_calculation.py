#큰 class안에 여러개의 메서드, 처음은 무조건 self, 
#두 수를 넣으면 각 메서드에 따라 계산  a1,a2등 들은 객체
class cal:
    def __init__(self,a,b):     #setdata없이 바로 a1=cal(1,4)
        self.a=a
        self.b=b
    def add(self):              #초기설정 이후  a1.add(), a2.add(), a1.mul()이런식으로
        return self.a+self.b
    def sub(self):
        return self.a-self.b
    def mul(self):
        return self.a*self.b
    def div(self):
        return self.a/self.b
#상속 및 메서드 오버라이팅, 오류
class newcal(cal):              #cal class를 그대로 가지고 있으면서 밑에 더 추가
    def pow(self):
        return self.a**self.b
    def div(self):              #a1=newcal(4,0)에서는 0으로 나누면 값이 나옴
        if self.b==0:
            try:
                self.a/self.b
            except:
                print('0으로는 못나눕니다')
            finally:
                print(0)
        else:
            return self.a/self.b
a1=newcal(4,0)
print(a1.add())
print(a1.pow())
print(a1.div())

#다중 상속도 가능
class xcal(cal,newcal):        #cal과 newcal동시에 상속
    pass

#클래스 변수
class family:
    name='조'

a=family()
b=family()
print(a.name,b.name)        #조

family.name='강'            ##**클래스변수는 객체변수와 달리 모든 객체에 공유
print(a.name,b.name)        #강

a.name='조'
print(a.name,b.name)        #조 강


#다른 class예제만들기
class add_cal:
    def __init__(self):
        self.num=0
    def add(self,a):
        self.num+=a
        return self.num
a1=add_cal()
print(a1.add(1))            #0에1=1
print(a1.add(2))            #1에2=3
print(a1.add(5))            #3에5=8
print(a1.add(7))            #8에7=15
