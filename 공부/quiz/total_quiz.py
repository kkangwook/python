# 1. 문자열 바꾸기 (split과 join을 사용하여)
str='a:b:c:d'
str=str.split(':')
str='#'.join(str)
print(str)

# 2. 딕셔너리에서 없는 값 추출하기
dic={'a':90,'b':80}
print(dic.get('c',70))    #70나옴
print(dic)

# 4.리스트 총합 구하기(50이상만)
data=[20,55,67,82,45,33,90,87,100,25]
sum=0
for i in data:
    if i>=50:
        sum+=i
print(sum)

# 5.피보나치함수 (첫번째 항=0, 두번째 항=1)
def x(y):
    if y==1:
        return [0]
    elif y==2:
        return [0,1]
    else:
        a=x(y-1)+[int(x(y-1)[-1])+int(x(y-1)[-2])]
        return a
print(x(10))
    
# 6.숫자를 입력받아 숫자 총합 구하기(숫자는 ','로 구분하여 입력)
a=input("숫자를 ','를 사이에 두고 입력하시오:")
a=a.split(',')
sum=0
for i in a:
    sum+=int(i)
print(sum)

# 7.한줄구구단(입력받아 해당 숫자의 구구단만)
a=int(input('숫자를 입력하시오:'))
for i in range(1,10):
    print(a*i,end=' ')

# 8. 메모장에적힌 글 역순으로 바꾸기
f=open('c:/doit/공부/새파일.txt','r')
a=f.readlines()
f.close()
a.reverse()
f=open('c:/doit/공부/새파일.txt','w')
for i in a:
    i=i.strip()
    f.write(i)
    f.write('\n')
f.close()

# 9. 메모장의 각 줄에 숫자를 적고 총 10개 적은 후 총합과 평균값을 읽어 새 메모장에 작성
f=open('c:/doit/공부/새파일.txt','r')
a=f.readlines()
f.close()
sum=0
for i in a:
    i=i.strip()
    sum+=int(i)
average=sum/len(a)
f=open('c:/doit/공부/result.txt','w',encoding='UTF-8')
f.write(f'총합은 {sum}이고 평균값은{average}입니다')
f.close()

# 10. 계산기 만들기(리스트를 받으면 각 요소의 합계와 평균을 보여줌)
class cal:
    def __init__(self,a):
        self.a=a
    def sum(self):
        b=0
        for i in self.a:
            b+=i
        return b
    def avg(self):
        b=0
        for i in self.a:
            b+=i
        return b/len(self.a)

a=cal([6,7,8,9,10])
print(a.sum())
print(a.avg())

# 13. 문자열 입력받은 뒤 홀수연속이면 사이에'-', 짝수연속이면 '*'집어넣는 함수
def x(a):
    a=list(a)
    b=[]
    for i in range(len(a)-1):
        b.append(a[i])
        if int(a[i])%2==0 and int(a[i+1])%2==0:
            b.append('*')
        elif int(a[i])%2!=0 and int(a[i+1])%2!=0:
            b.append('-')
        else:
            continue
    b.append(a[len(a)-1])
    b=''.join(b)
    return b
print(x('4546793'))        

# 14. 문자열 압축하기(aaabbcccccca->a3b2c6a1)
def x(a):
    result=[]
    a=list(a)
    num=1
    for i in range(len(a)-1):
        if a[i]==a[i+1]:
            num+=1
        else:
            result.extend([a[i],str(num)])
            num=1
    result.extend([a[len(a)-1],str(num)])
    result=''.join(result)
    return result
print(x('aaabbcccccca'))
            
# 15. 0-9의 숫자의 문자열을 받았을때 0-9의 모든 숫자를 각각 한번씩만 사용한 것인지 확인하는 함수
def x(a):
    if len(a)!=10:
        return False
    else:
        for x in range(10):
            for y in range(10):
                if x==y:
                    continue
                else:
                    if a[x]==a[y]:
                        return False
        return True 
    print(x('0123456789'))
    print(x('1234'))
    print(x('0123345678'))
    
# 16. 모스부호 해독하기
dic = { '.-'   : 'A',
	'-...' : 'B',
	'-.-.' : 'C',
	'-..'  : 'D',
	'.'    : 'E',
	'..-.' : 'F',
	'--.'  : 'G',
	'....' : 'H',
	'..'   : 'I',
	'.---' : 'J',
    '-.-'  : 'K',
	'.-..' : 'L',
	'--'   : 'M',
	'-.'   : 'N',
	'---'  : 'O',
	'.--.' : 'P',
	'--.-' : 'Q',
	'.-.'  : 'R',
	'...'  : 'S',
	'-'    : 'T',
	'..-'  : 'U',
	'...-' : 'V',
	'.--'  : 'W',
	'-..-' : 'X',
	'-.--' : 'Y',
	'--..' : 'Z',}
a=input('모스부호로 입력하시오:')
a=a.split('  ')
result=[]
for i in a:
    i=i.split(' ')
    for x in i:
        result.append(dic.get(x))
    result.append(' ')
result=''.join(result)
print(result)

# 19.휴대폰 번호 뒷자리 4개만 ####으로 변경
data='''
park 010-9999-9988
kim 010-9909-7789
lee 010-8789-7768'''
import re
a=re.compile(r'(\w+\s\d{3}-\d{4}-)\d{4}')
b=a.sub('\g<1>####',data)
print(b)