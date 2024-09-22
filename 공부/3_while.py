# while True:일때 True할때까지 반복수행

#나무 찍기
i=0
tree=10
while i<10:
    i+=1   #i=i+1을 표현한것
    print(f'나무를 {i}번 찍었습니다')
    tree-=1
    if tree==0:
        print('나무넘어갑니다')

# continue-while문의 처음으로 돌아감
a=0
while a<20:
    a+=1
    if a%2==0:
        continue    #a가 짝수면 멈추고 밑의 print없이 while문의 a+=1수행
    print(a)     #20이하의 홀수값만나옴
    

# 무한 루프
while True:             #항상 참이므로 계속 실행
    print('ctrl+c를 눌러 멈추세요')   #ctrl+c키로 탈출
    
#break으로 빠져나오기
i=0
while True:
    print(i)
    if i==10:
        break
    

