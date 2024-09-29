# 3,4-주민등록번호 나누기
pin='881120-1068234'
yyyymmdd=pin[:6]
num=pin[7:]
sex=pin[7]

# 5-문자열 바꾸기 a:b:c:d -> a#b#c#d
a='a:b:c:d'
b=a.replace(':','#')
print(b)

# 6-리스트 역순정렬
a=[1,3,5,4,2]
a.sort()
a.reverse()
print(a)

# 7-리스트를 문자열로
a=['life','is','too','short']
b=' '.join(a)
print(b)

# 8-튜플더하기
a=(1,2,3)
a=a+(4,)
print(a)

# 10-딕셔너리 값 추출  (80만 빼내기)
dic={'a':90,'b':80,'c':70}
result=dic.pop('b')
print(dic)
print(result)

# 11-리스트에서 중복 제거하기
a=[1,1,1,2,2,3,3,3,4,4,5]
a=set(a)
a=list(a)
print(a)