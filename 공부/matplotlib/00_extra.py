# matplotlib추기

import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams['font.family'] = 'Malgun Gothic'  
matplotlib.rcParams['font.size'] = 15 
matplotlib.rcParams['axes.unicode_minus'] = False


1. plt.plot()에 값이 하나만일때
원래는 plt.plot(x,y)
하지만 plt.plot(data)라면 x축은 0부터 1씩 증가, y값이 data 값

2. 정규분포난수 뽑기
random.gauss(mu,sigma)  -> mu=평균(default=0), sigma=표준편차(default=1)
여러개뽑기=[random.gauss() for i in range(100)]
plt.hist(여러개뽑기)  ->정규분포그래프
