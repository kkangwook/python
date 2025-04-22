#기본파이썬

-- 딕셔너리 컴프리헨션가능
x=['a','b','c']
y=[1,2,3]
dict={i:j for i,j in zip(x,y)}
print(dict)   # {'a': 1, 'b': 2, 'c': 3}

--통계함수
import scipy as sp
import seaborn as sns
  -정규성검사: sp.stats.shapiro(df)
  -ttest: sp.stats.ttest_ind(adf,bdf)
  -상관분석: df.corr(method='pearson') # nXn형태로 출력
             sns.pairplot(df) or sns.heatmap(df)  #plt.show()로 표시
#판다스
-- df.함수의 default는 axis=0(아래로==열별) 하지만  axis=1도 가능!!!!(행별)
-- df의 컬럼의 리스트로:  df[col].tolist()
-- df['col']과 df.col은 같음

#맷플롯립
-- 수직선 긋기: plt.vlines(x,-1,n,colors,linestyles)
-- 수평선 긋기: plt.hlines(y,-1,n,colors,linestyles)
