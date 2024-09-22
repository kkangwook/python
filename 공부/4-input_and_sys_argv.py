#input
a=input('a값을 입력하시오:')        #입력한 값이 a값이 됨
print(a)
b=int(input('숫자를 입력하시오:'))      #숫자여야 오류 안남
print(3+b)

#print란
#숫자, 문자열, 리스트, 튜플, 집합, 딕셔너리, 함수등을 출력해줌
print('hello''world''nice''too''meet''you')         #1과
print('hello'+'world'+'nice'+'too'+'meet'+'you')    #2는 같음
print('hello','world','nice','too','meet','you')    #3은 ,가 뛰어쓰기

#명령자에 적은것을 print(dir위치는 .py위치와 같아야 하므로 cd dir필요)
import sys

args=sys.argv[1:]       #argv[0]=파일이름.py  그 뒤에 부터가 argv[1],argv[2]....
for i in args:
    print(i)