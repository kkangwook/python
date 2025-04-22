df.함수의 default는 axis=0(아래로==열별) 하지만  axis=1도 가능!!!!(행별)
df의 컬럼의 리스트로:  df[col].tolist()

--딕셔너리 컴프리헨션가능
x=['a','b','c']
y=[1,2,3]

dict={i:j for i,j in zip(x,y)}
print(dict)   # {'a': 1, 'b': 2, 'c': 3}
