# 큰따옴표or 작은 따옴표
print('')
print("''")
print('""')
print('\'')

#줄바꾸기
print('''
asdasd
sdf
sd''')

print('asdasd\nsdf\nsd')

#표현법: \n=줄바꾸기, \'=', \t=탭, \\=\
print('red apple\rpine')    # \r:커서를 맨앞으로
print('redd\b apple')       # \b:한글자 삭제

#문자열 더하기 곱하기
a='py' 
b='thon'
print(a+b)
print(a*10)

#길이, 인덱싱, 슬라이싱
c=a+b
print(len(c))
print(c[0],c[1],c[2],c[3],c[4],c[5])
print('py=',c[:2])
print('thon=',c[2:])
d='life is too short, you need python'
print(d[-1])
print(d[-6:])

#문자열 포매팅
print('i ate %dapples %dbananas and %d%%beer' %(2,3,7))
print('i ate {0}apples {1}bananas and {2}%beer'.format(2,3,7))
age=27
print(f'i\'m {age}years old and {age+1} next year')

#count find index
print(d.count('i'))
print(d.find('i'))
index=d.index('i')    #제일 처음 나오는 i위치
print(index)
index=d.index('i',index+1)    #전에 찾은 i 다음 나오는 i 위치, index(a,x)에서 x는 시작 위치(0부터)
print(index)

#join:리스트(문자열)를 문자열로, split:문자열을 리스트로
print(','.join('abcde'))
e=['life','is','too','short']
print(' '.join(e))
print(d.split(' '))

# 소문자 대문자 공백지우기
a='python'
b='PYTHON'
c='\npython'
d='python\n'
e='\npython\n'
print(a.upper(),b.lower())
print(c.lstrip(),d.rstrip(),e.strip())
