#dic구조
# dic={'a':1,'b':2,'c':3}   앞은key 뒤는 value

#쌍 추가하기
dic={'a':1,'b':2,'c':3}
dic['d']=4          #indexing X
dic['a']=5          # a:5로 replace
print(dic)

#쌍 삭제하기
del dic['d']     #[key]넣기
print(dic)

#dic에서 value 얻기-두가지
print(dic['a'])
print(dic.get('a'))

# key가 없을시
print(dic.get('e','사용가능'))    # e가 dic에 없으면 '사용가능'이 뜸

#key, value, 둘다얻기
print(dic.keys())
print(dic.values())
print(dic.items())
print(list(dic.keys()))   #리스트화 가능
print(list(dic.items()))    #리스트화 하면 안은 튜플

#해당 key가 dic에 있는지 확인
print('a' in dic)
print('d' in dic)

#모두지우기
dic.clear()
print(dic)
