# 1-홀수 짝수 판별하기(홀수=true,짝수=false)
def odd_even(a):
    if a%2!=0:
        return True
    if a%2==0:
        return False
print(odd_even(3))
print(odd_even(4))

# 2-모든 입력값의 평균구하기
def avg_number(*a):
    b=0
    for i in a:
        b+=i
    return(b/len(a))
print(avg_number(1,2,3,4))

# 6-사용자가 입력한 내용을 txt파일에 저장
a=input('저장할 내용을 입력하시오:')
f=open('새파일.txt','a',encoding='UTF-8')
f.write(a)
f.write('\n')
f.close()

# 7-txt파일에 적힌 내용을 파이썬에서 바꾸기(java is the best에서 java를 python으로)
f=open('새파일.txt','r')
a=f.read()
f.close()
b=a.replace('java','python')
f=open('새파일.txt','w')
f.write(b)
f.close()

# 8-터미널에서 모든 값 더한것 출력하기
import sys
a=sys.argv[1:]
sum=0
for i in a:
    sum+=int(i)
print(sum)