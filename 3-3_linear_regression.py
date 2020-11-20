# scikit-lean 모듈을 이용하여 선형회귀 모델로 적용해볼 수 있음

import pandas as pd 
df = pd.read_csv('data/temp_ice.csv', encoding = 'utf-8')
print(df.head(5))

# 데이터를 입력 변수와 출력 변수로 나누기
import numpy as np 
data = np.array(df)
X = data[:,1]       # 평균 기온 (입력변수)
Y = data[:,-1]      # 아이스크림 쇼핑 클릭량 (출력변수)

# 입력 변수와 출력 변수 각각의 평균(mean) 구하기
mean_x = np.mean(X)
mean_y = np.mean(Y)

# X 변수의 개수 구하기
n = len(X)

# 최소 제곱법을 이용하여 beta0과 beta1 구하기
temp1 = 0
temp2 = 0
for i in range(n):
    temp1 += (X[i] - mean_x) * (Y[i] - mean_y)
    temp2 += (X[i] - mean_x) **2
beta1 = temp1 / temp2
beta0 = mean_y - (beta1 * mean_x)
print('기울기(beta1):{0}, 절편(beta0):{1}'.format(beta1, beta0))

# 학습 결과 시각화하기
import matplotlib.pyplot as plt 
Y_pred = beta0 + beta1 * X 

plt.title('Avg_temp & Clicks')
plt.xlabel('Average temperature(C)')
plt.ylabel('Clicks')
plt.plot(X,Y,'k.')
plt.plot(X,Y_pred, color='red')
plt.axis([-4,30,20,100])
plt.grid()
plt.show()

# 평가하기
def RMSE(beta0, beta1, x, y):
    RMSE = np.sqrt(((y - (beta0 + beta1 * x))**2).mean())
    return RMSE 

results = RMSE(beta0, beta1, X, Y)
print('손실값 결과는?{0}'.format(results))

# 평균 온도 값이 주어졌을 때 아이스크림 쇼핑 클릭량을 예측하는 함수 만들기
def Regression(beta0, beta1, X):
    y_pred = beta0 + beta1 * X 
    return y_pred 

my_temp = float(input('안녕하세요. 오늘의 평균 기온을 입력해주세요 : '))
predicted_value = Regression(beta0, beta1, my_temp)
print('아이스크림 쇼핑 클릭량은 100점 기준으로 {0}만큼 예상됩니다'.format(predicted_value))
