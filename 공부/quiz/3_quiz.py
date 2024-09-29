# 2- 3의 배수의 합 구하기(1-1000까지의 자연수)
result=0
i=0
while i<1000:
    i+=1
    if i%3==0:
        result+=i
print(result)

# 3- while문으로 별 표시하기
i=0
while i<5:
    i+=1
    print('*'*i)
    
# 4- 1부터 100까지 출력하기
for i in range(1,101):
    print(i,end=' ')
    
# 5- 평균점수 구하기(for문 사용하여)
a=[70,60,55,75,95,90,80,80,85,100]
result=0
for i in a:
    result+=i
avg=result/len(a)
print(avg)

# 6-리스트 컴프리헨션 사용하기(홀수만 골라 2곱하기)
numbers=[1,2,3,4,5]
a=[i*2 for i in numbers if i%2!=0]
print(a)