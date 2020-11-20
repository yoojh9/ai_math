import csv
f = open('data/temp_ice.csv', encoding='utf-8')
data = csv.reader(f)
header = next(data)
temp = []
ice = []

for row in data:
    temp.append(float(row[1]))
    ice.append(int(row[4]))

print(min(temp), max(temp))

## 1. 도수분포 구간을 설정하여 출력하기
import numpy as np 

## arange() 함수는 range() 함수와 같이 특정 범위에 해당하는 연속된 값을 생성하는 역할을 하며, 하나의 배열로 저장한다는 의미에서 명령어의 맨 앞에 a를 붙인다.
## 따라서 min(temp) 값부터 시작하여 max(temp) 값보다 1 작은 수까지의 범위에서 5만큼의 간격을 갖는 숫자들이 bins 배열에 저장한다.
bins = np.arange(min(temp), max(temp)+5, 5)       

print(bins) # -3.8이상 ~ 1.2미만, ... , 21.2이상 ~ 26.2 미만 => 26.2와 같은 값들은 누락 되므로 max 값에 계급 간격만큼 다시 더한다.

## 2. 각 계급에 해당하는 도수값 
hist, bins = np.histogram(temp, bins)
print(hist)
print(bins)

## 3. 계급별 아이스크림 쇼핑 클릭량 합계 구하기
ice_buy = np.zeros(7)

'''
for i in range(0, len(temp)):       # 평균 기온 데이터 전체 탐색하기
    if bins[0] <= temp[i] and temp[i] < bins[1]:    # 첫 번째 계급에 해당한다면
        ice_buy[0] = ice_buy[0] + ice[i]
    elif bins[1] <= temp[i] and temp[i] < bins[2]:
        ice_buy[1] = ice_buy[1] + ice[i]
    elif bins[2] <= temp[i] and temp[i] < bins[3]:
        ice_buy[2] = ice_buy[2] + ice[i]
    elif bins[3] <= temp[i] and temp[i] < bins[4]:
        ice_buy[3] = ice_buy[3] + ice[i]
    elif bins[4] <= temp[i] and temp[i] < bins[5]:
        ice_buy[4] = ice_buy[4] + ice[i]
    elif bins[5] <= temp[i] and temp[i] < bins[6]:
        ice_buy[5] = ice_buy[5] + ice[i]
    else :
        ice_buy[6] = ice_buy[6] + ice[i]
print(ice_buy)
'''

## 위 코드를 더 간단하게 줄이면 아래와 같다
for i in range(0, len(temp)):
    for j in range(0, len(bins)):
        if j == len(bins):          # 인덱스가 가장 끝 번호일 경우
            ice_buy[j] = ice_buy[j] + ice[i]
        else :
            if bins[j] <= temp[i] and temp[i] < bins[j+1]:
                ice_buy[j] = ice_buy[j] + ice[i]
print(ice_buy)

## 4. 계급별 아이스크림 쇼핑 클릭량의 평균 구하기
ice_buy_a = np.zeros(7)

for i in range(0, len(ice_buy)):
    ice_buy_a[i] = ice_buy[i] / hist[i]    # 계급별 아이스크림 쇼핑 클릭량 평균 구하기

for i in range(0, len(ice_buy)):
    print('%0.2f' %ice_buy_a[i])


## 5. 데이터 시각화하기
import matplotlib.pyplot as plt 
plt.xlabel('Average temperature') 
plt.ylabel('Number of icecream shopping')
plt.bar(bins[0:7], ice_buy_a, width=2, align='edge')    # align='edge'로 두어 막대의 왼쪽 가장자리에 x값 위치를 맞춤
plt.xticks(bins[0:7])   # x축 눈금 이름 설정하기
plt.show()

## 6. 평균 기온과 아이스크림 쇼핑 클릭량에 대한 분산형 그래프 그리기
plt.scatter(temp, ice)
plt.show()