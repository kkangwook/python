#for i in (list,tuple,string): i는 순서대로 각 요소가 됨
a='python'
for i in a:
    print(i)
    
#딕셔너리
dic={'a':1,'b':2,'c':3}
a=dic.items()
for x,y in a:
    print(f'{x}는 key이고 {y}는 value입니다')
    
#사용예시-학생의 시험점수 합/불 여부
score=[90,25,67,45,80]
a=0
for i in score:
    a+=1
    if i>=60:
        print(f'{a}번째 학생은 합격입니다')
    else:
        print(f'{a}번째 학생은 불합격입니다')
        
#for문에서 continue-while에서와 마찬가지
a=0
for i in score:
    a+=1
    if i<60:
        continue        # print없이 for문의 처음으로
    print(f'{a}번째 학생은 합격입니다')
    
# range사용
#range(10):0-9를 의미,  range(1,10):1-9를 의미

score=[90,25,67,45,80]

for i in range(len(score)):     # i:0-4
    if score[i]>=60:
        print(f'{i+1}번째 학생은 합격입니다')
    else: print(f'{i+1}번째 학생은 불합격입니다')
    
#구구단
for x in range(2,10):
    for y in range(1,10):
        c=x*y
        print(c,end=' ')   #end=''다음줄로 넘기지 않고 ''사이 값을 각각 집어넣음
    print('')       #인위적으로 다음줄로 가기위해
    
# list comprehension: list안에 for문을 사용하여 리스트만들기
#주어진 리스트를 3배하여 돌려받기
a=[1,2,3,4]
b=[]
for i in a:
    b.append(i*3)
print(b)
# list comprehension으로 더 쉽게
b=[i*3 for i in a]
#if 문도 같이 사용 가능
b=[i*3 for i in a if i%2==0]  #2의 배수인 요소들만 사용
print(b)