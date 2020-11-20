# 1. 데이터 시각화하기
## pandas의 함수를 사용하면 상세한 코드로 데이터를 정리하는 과정을 비교적 간단하게 처리할 수 있다.

import pandas as pd 
iris = pd.read_csv('data/iris.csv')
print(iris.head(2))
print(iris.info())      # 전체 데이터 요약: 열별로 데이터는 몇 개 저장되어 있는지, 유효하지 않은 값(null)은 없는지..
print(iris.describe())  # 전체 데이터의 통계값 요약 출력하기: 평규느 표준편차값, 최소값, 최대값 등

# 2. 꽃받침 길이와 너비를 분산형 그래프로 나타내기
## 붓꽃 세 종류의 꽃받침 길이와 너비를 이용하여 분산형 그래프로 나타낸다
import matplotlib.pyplot as plt 
# 꽃받침(Sepal)길이와 너비에 따른 분산형(scatter) 그래프
fig = iris[iris.Species=='Iris-setosa'].plot(kind='scatter', x='SepalLengthCm', y='SepalWidthCm', color='orange', label='setosa')
iris[iris.Species=='Iris-versicolor'].plot(kind='scatter', x='SepalLengthCm', y='SepalWidthCm', color='blue', label='versicolor', ax=fig)
iris[iris.Species=='Iris-virginica'].plot(kind='scatter', x='SepalLengthCm', y='SepalWidthCm', color='green', label='virginica', ax=fig)
fig.set_xlabel('Sepal Length')
fig.set_ylabel('Sepal Width')
fig.set_title('Sepal Length vs Width')
fig = plt.gcf()             # gcf(): get the current figure, 작업 중인 figure의 설정 정보를 확인할 수 있는 함수
fig.set_size_inches(10,6)
plt.show()

## 3. 꽃잎의 길이와 너비를 분산형 그래프로 나타내기
# 꽃잎(Petal)의 길이와 너비에 따른 분산형(scatter) 그래프
fig = iris[iris.Species=='Iris-setosa'].plot(kind='scatter', x='PetalLengthCm', y='PetalWidthCm', color='orange', label='setosa')
iris[iris.Species=='Iris-versicolor'].plot(kind='scatter', x='PetalLengthCm', y='PetalWidthCm', color='blue', label='versicolor', ax=fig)
iris[iris.Species=='Iris-virginica'].plot(kind='scatter', x='PetalLengthCm', y='PetalWidthCm', color='green', label='virginica', ax=fig)
fig.set_xlabel('Petal Length')
fig.set_ylabel('Petal Width')
fig.set_title('Petal Length vs Width')
fig = plt.gcf()
fig.set_size_inches(10,6)
plt.show()

## 그래프를 통해 확인한 결과 세 가지 종류의 붓꽃을 확인하는 데 꽃받침의 길이와 너비보다 꽃잎의 길이와 너비에 따라 붓꽃을 분류하는 것이 더 쉬운 것을 확인할 수 있다.