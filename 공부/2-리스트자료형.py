# 리스트이름=[1,2,[1,2],'hi',3]같이 가능,자유롭게 변형가능
#인덱싱 슬라이싱 더하기 곱하기 길이 가능, 요소가 몇번째 위치인지 

a=[1,2,[1,2],3]
b=[3,4,5,6]
c=a+b
print(a[2][1])
print(a[2:])
print(a+b)
print(len(a))
print(a.index(2))   #a.index는 1값이 나오므로 1+1인 두번째에 위치
print(c.count(3))   #()안의 요소 숫자를 셈

#숫자를 문자열로-str
print(str(a[2][1])+'apples')   #문자열은 문자열끼리만 더할 수 있음

#리스트 수정
a[2]=4    # 2+1번째 요소를 4로
print(a)

#요소삭제
del a[2]    # 2+1번째 요소를 삭제
print(a)

#마지막에 요소추가
a.append(4)
print(a)

#뒤집기, 정렬
a.reverse()   #그대로 거꾸로
print(a)
a.sort()      #숫자크기나 알파벳 순서로 정렬
print(a)

#원하는 위치에 요소 삽입
a.insert(2,'hi')    #(위치,넣을요소)->3번째에 hi들어감
print(a)

#첫번째로 나오는 값을 제거
a.remove('hi')   #제일앞쪽의 제거할 값을 ()안에
print(a)

#끄집어내고 없애기
print(a.pop())    #()안에 아무것도 없으면 마지막것 보여주고 제거
print(a)
print(a.pop(1))   #()안에는 index
print(a)

#여러개 넣기
a.extend([3,4,5])    #리스트 더하기와 같은 의미
print(a)
a+[3,4,5]
print(a)

#리스트안에 튜플
a.insert(1,(1,2))
print(a)
print(a[1][1])
try:
    a[1][1]=6   
except:
    print('리스트안에 들어온 튜플이라 하더라도 바뀔수 없음')