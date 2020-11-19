import pandas as pd 
fifa2020 = pd.read_csv('data/players_20.csv')
print(fifa2020.shape)

sub1 = fifa2020.loc[43]             # loc: 인덱스 레이블을 기준으로 행 데이터를 읽고, iloc 함수는 행 번호를 기준으로 행 데이터를 읽는다.
#print(sub1)

## 1. 원하는 범위의 데이터 검색하기
sub2 = fifa2020.loc[2:16]
# print(sub2)

## 2. 전체 선수들의 이름과 선호하는 발 정보 출력하기
sub3 = fifa2020.loc[:,['short_name','preferred_foot']]    # 전체 선수들의 데이터를 사용하기 위해 전체 행 값을 선택하고, 선수들의 이름 데이터가 담긴 'Name' 열과 선호하는 발의 정보가 담긴 'Preferred Foot' 열 값만들 선택하여 출력한다.
# print(sub3)

## 3. 여러 행의 데이터 중 원하는 열 값만 골라 출력하기
sub4 = fifa2020.iloc[0:10, 1:3] # 0~9행, 1,2열 값을 sub4에 저장하기
# print(sub4)

## 4. 우리나라 선수들 출력하기
korea_player = fifa2020['nationality']=='Korea Republic'
sub5 = fifa2020.loc[korea_player]
# print(korea_player)
# print(sub5)

## 5. 우리나라 선수들 이름 출력하기
sub6 = sub5['short_name']
# print(sub6)

## 6 visualize
import matplotlib.pyplot as plt 

print(fifa2020['preferred_foot'].value_counts())
fifa2020['preferred_foot'].value_counts().plot(kind='bar')      # value_counts()는 특정 열 값의 개수를 알려주는 명령어, plot()은 그래프를 그리는 명령어로 그래프 종류를 따로 지정하지 않을 경우 꺽은선 그래프로 표시된다.
plt.legend()
plt.show()

fifa2020['preferred_foot'].value_counts().plot(kind='pie', autopct='%1.f%%')  # 원그래프. 첫번쨰 %는 비율을 의미하는 숫자 형식을 지정하는 것, %%는 기호 %를 출력하기 위한 것
plt.legend()
plt.show()

