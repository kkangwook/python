#except 종류
try:
    a=[1,2]
    print(a[3])
    4/0
except ZeroDivisionError:               # 1.except:
    print('0으로 나눌 수 없습니다')      # 2.except errorname:
except IndexError as e:                 #3. except errorname as e:
    print(e)
    
  
#try-except-else-finally
try:
    age=int(input('나이를 입력하시오:'))
except:
    print('숫자가 아닙니다')
else:                           #오류가 없으면 진행
    if age>18:
        print('성인입니다')
    else:
        print('미성년자입니다')
finally:                        #어떤상황이돈 무조건 실행
    print('안내해드리겠습니다')

#오류회피하기
try:
    f=open('asdfgervre.txt','r')
except:
    pass


#오류 일부러 발생시키기
# NotImplementedError
#exception class사용하여 error raise하기
class myerror(Exception):
    def __str__(self):                      #오류내용 적기
        return '허용되지 않는 별명입니다'
def x(a):
    if a=='바보':
        raise myerror()         # or raise NotImplementedError
    print(a)
try:
    x('천사')
    x('바보')
except myerror as e:
    print(e)
