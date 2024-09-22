#파일 생성->없는 파일일 경우 'w'으로 만듬
#f=open('파일이름.확장자','x')  x: w(처음부터쓰기),r(읽기),a(추가하기)
#f.close()로 닫기필요
f=open('새파일.txt','w')    #없을 경우 이 이름 의 파일이 같은 dir에 txt로 생성
for i in range(1,11):
    f.write(f'{i}번째 줄입니다')        #f에 해당 str을 적음-for문이랑 달리 다음줄없이 그대로 옆에 적음
f.close()

#업그레이드
f=open('c:/doit/공부/진짜새파일.txt','w')       #직접 위치 지정해줘서 만들기
for i in range(1,11):
    f.write(f'{i}번째 줄입니다')
    f.write('\n')                         #뛰어쓰기
f.close()


#읽는 방법('r')
# 1.readline()-한줄씩 읽음
f=open('c:/doit/공부/진짜새파일.txt','r')
while True:
    a=f.readline()          #밖에 readline하면 1번째줄만 계속 뜸->while문 안에다가
    a=a.strip()             #\n제거
    print(a)
    if not a:               #더이상 읽을 a가 존재하지 않으면 실행->break
        break
f.close()
    
# 2.readlines()
f=open('c:/doit/공부/진짜새파일.txt','r')
a=f.readlines()     #각 줄을 리스트의 형태로
for i in a:
    i=i.strip()
    print(i)
f.close()

# 3.read()
f=open('c:/doit/공부/진짜새파일.txt','r')
a=f.read()
print(a)        #strip필요x
f.close()

# 4 f그자체
f=open('c:/doit/공부/진짜새파일.txt','r')
for i in f:
    i=i.strip()
    print(i)
f.close()


#쓰여진것에 추가하기 'a'
f=open('c:/doit/공부/진짜새파일.txt','a')
for i in range(11,21):
    f.write(f'{i}번째 새로운 줄입니다')     #뒤부분에 11-20까지 새로운 줄
    f.write('\n')
f.close()


#with문
with open('c:/doit/공부/진짜새파일.txt','r') as f:  #f.close()필요x
    a=f.read()
    print(a)