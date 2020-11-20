## scikit-learn 모듈을 이용하여 K-Menas 모델을 적용할 수도 있음

# 1. 데이터 불러오기
import pandas as pd 
fifa2020 = pd.read_csv('data/players_20.csv')
df = pd.DataFrame.copy(fifa2020.sort_values(by='overall', ascending=False).head(200))
test_features=['short_name','power_stamina','attacking_short_passing', 'dribbling', 'mentality_penalties']
test_df = pd.DataFrame(df, columns = test_features)
print(test_df.head(5))

# 2. 학습 데이터 준비하기
import numpy as np 
XY = np.array(test_df)
X = XY[:,1:3]   # 배열 XY의 특성 열은 name, stamina, short passing, penalties 순서로 나열되어 있다. 이중 우리가 필요한 것은 두번째와 세번째 열의 모든 행이므로 XY[:,1:3]만을 슬라이싱 한다

# 3. K-평균 군집화 알고리즙 적용하기
## 3-1) 표본공간에 K개의 중심을 무작위로 생성하기
k=3
C_x = np.random.choice(X[:,0], k)   # 데이터 셋에서 k개를 무작위로 선택하고, 선택된 체력 데이터의 값을 중심의 x축 좌표로 지정한다
C_y = np.random.choice(X[:,1], k)   # 선택된 드리블 데이터의 값을 중심의 y축 좌표로 지정한다.
C = np.array(list(zip(C_x, C_y)))   # 위에서 만든 배열 C_x, C_y를 하나의 배열 C로 만들기 위해 zip()함수를 사용한다.
print(C_x)
print(C)

## 3-2) 각 표본을 가까운 중심에 할당하기
from copy import deepcopy

def Distance(A,B):
    return np.sqrt(np.sum(np.power((A-B), 2))) # 유클리디안 거리 계산 함수

C_old = np.zeros(C.shape)
clusters = np.zeros(len(X))
flag = Distance(C, C_old)
print(C_old)

distances = []
while flag != 0:
    for i in range(len(X)):
        for j in range(3):
            temp = Distance(X[i], C[j])
            distances.append(temp)
        cluster = np.argmin(distances)      # argmin(): 최소값을 가지는 값의 인덱스 번호를 리턴
        clusters[i] = cluster
        distances = []

    C_old = deepcopy(C)
    
    for i in range(k):
        points = [X[j] for j in range(len(X)) if clusters[j] == i]
        C[i] = np.mean(points)
    
    flag = Distance(C,C_old)

# 4. 데이터 시각화하기
import matplotlib.pyplot as plt 
power_stamina = test_df['power_stamina']
sort_passing = test_df['attacking_short_passing']
plt.title('Stamina & Short Passing')
plt.xlabel('Stamina')
plt.ylabel('Sort Passing')
plt.scatter(power_stamina, sort_passing, marker='^', c='blue', s= 10, label='players') # s: 점의 size
plt.scatter(C_x, C_y, marker='*', s=200, c='orange', label='centroids')
plt.legend(loc='best')  
plt.grid()
plt.show()


# 5. 군집화 결과 시각화
a=0
b=0
c=0
for cluster in clusters:
    if(cluster==0):
        a=a+1
    elif(cluster==1):
        b=b+1
    else:
        c=c+1

print('a=',a,',b=',b,'c=',c)
print(clusters[0])
plt.scatter(X[clusters==0,0], X[clusters==0,1], s=50, c='red', marker='o', edgecolor='black', label='A')
plt.scatter(X[clusters==1,0], X[clusters==1,1], s=50, c='yellow', marker='x', edgecolor='black', label='B')
plt.scatter(X[clusters==2,0], X[clusters==2,1], s=50, c='blue', marker='^', edgecolor='black', label='C')

## 군집의 중심 좌표
plt.scatter(C[:,0], C[:,1], s=250, marker='*', c='black', edgecolor='black', label='Centroids')
plt.legend()
plt.grid()
plt.show()