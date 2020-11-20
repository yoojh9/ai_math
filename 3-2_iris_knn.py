# scikit-learn 모듈을 이용하여 K-NN 모델을 적용할 수도 있다.

import pandas as pd 
import numpy as np 

# 1. 데이터 만들기
iris = pd.read_csv('data/iris.csv')
xy = np.array(iris)

## 테이블의 1~4 열벡터를 features에 저장
features = xy[:,1:-1]
## 테이블의 마지막 열 벡터를 target_value에 저장
target_value = xy[:,[-1]]

## 유클리드 거리법을 이용하여 두 데이터 간의 거리 구하는 함수 선언
def Distance(A,B):
    return np.sqrt(np.sum(np.power((A-B),2)))

# 2. 붓꽃 분류기 작성
## 붓꽃 분류 작성하기
def K_NN(UnKnown, features, K):
    # 1) 붓꽃 분류 함수 - 데이터 사이의 거리 계산
    distance_result = np.zeros(150)
    for i in range(150):
        distance_result[i] = Distance(UnKnown, features[i])
    # 2) 붓꽃 분류 함수 - 분류하려는 데이터와 가까운 순서대로 인덱스 정렬
    index = distance_result.argsort()       # 가장 작은 값 부터 인덱스를 반환 함
    # 3) 붓꽃 분류 함수 - K개의 레이블 별 빈도 세기
    target_result = []
    result = [0,0,0]
    for i in range(K):
        target_result.append(target_value[index[i]])
        if target_result[i] == 'Iris-setosa':
            result[0] += 1
        elif target_result[i] == 'Iris-versicolor':
            result[1] += 1
        else:
            result[2] += 1
    # 4) 붓꽃 분류 함수 - 레이블의 빈도가 가장 높은 값 반환
    max_label = result.index(max(result))
    species = {0:'setosa', 1:'versicolor', 2:'virginica'}
    species_result = species[max_label]
    return species_result


# 3. 붓꽃 분류 함수를 사용하여 가상의 데이터 분류하기
## 150개의 붓꽃 데이터 중 마지막 150번 째 데이터와 150번째 데이터와 유사한 가상의 데이터를 만들어 분류 결과를 확인해본다.

### 마지막 150번째 데이터(인덱스 번호는 0부터 이므로 149)
test_1 = features[149]

### 150번째와 유사한 가상의 데이터
test_2 = np.array([6,2.9,5,2])

### K_NN 분류 함수를 이용하여 분류하기
result_1 = K_NN(test_1, features, 3)
result_2 = K_NN(test_2, features, 3)

print('실제 데이터를 분류한 결과: {0}'.format(result_1))
print('가상 데이터를 분류한 결과: {0}'.format(result_2))