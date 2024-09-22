#구조: a=set('hello'), b=set([1,2,3]) 중복X, 순서X, indexing X
a=set('hello')
b=set([1,2,3])
print(a,b)
print(list(a),tuple(b))  #리스트화 튜플화 둘다 가능

#교집합 합집합 차집합
a=set('sjkfhsdjkvndjkvn')
b=set('evrneuivberibe')
print(a|b)          #합집합
print(a&b)          #교집합
print(a-b)          #차집합 2가지방법
print(a.difference(b))

#집합에 요소 추가, 제거
a=set('hello')
a.add('bye')            #하나 추가
print(a)
a.update(['b','y','e'])  #여러개 추가
print(a)
a.remove('bye')   #제거
print(a)