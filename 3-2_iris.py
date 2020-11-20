import csv

## 1. 데이터 저장하기
f = open('data/iris.csv')
data = csv.reader(f)
header = next(data)
result = []

for row in data:
    result.append(row)
    print(row)          # 행 별로 데이터 저장하기

# result에 저장된 값 중 꽃받침과 꽃잎의 길이. 너비 값을 숫자로 바꾼 후 출력하기
for i in result:
    for j in range(1,5):
        i[j] = float(i[j])
    print(i)

# 꽃 종류별 데이터 저장하기
a = []  # iris-setosa
b = []  # iris-versicolor
c = []  # iris-virginica

for i in result:
    if i[5] == 'Iris-setosa':
        a.append(i[0:5])
    if i[5] == 'Iris-versicolor':
        b.append(i[0:5])
    if i[5] == 'Iris-virginica':
        c.append(i[0:5])


## 2. Iris-setosa의 꽃잎과 꽃받침 길이, 너비에 따른 평균 구하기
SL = []     # 꽃받침 길이(Sepal Length)
SW = []     # 꽃받침 너비(Sepal Width)
PL = []     # 꽃잎 길이(Petal Length)
PW = []     # 꽃잎 너비(Petal Width)

for i in a:
    SL.append(i[1])
    SW.append(i[2])
    PL.append(i[3])
    PW.append(i[4])

print('<Iris-setosa의 특성별 평균>')
print('꽃받침 길이 평균:', round(sum(SL)/len(SL),3), '\n꽃받핌 너비 평균:', round(sum(SW)/len(SW),3), '\n꽃잎 길이 평균:',round(sum(PL)/len(PL),3),'\n꽃잎 너비 평균:',round(sum(PW)/len(PW),3))


## 3. Iris-setosa의 꽃잎과 꽃받침 길이, 너비의 중앙값 구하기
SL.sort()
SW.sort()
PL.sort()
PW.sort()
m = int(len(a)/2)   # iris-setosa의 전체 개수를 2로 나누어 중앙값 구하기

print('<Iris-setosa의 특성별 중앙값>')
print('꽃받침 길이 중앙값:', SL[m], '\n꽃받핌 너비 중앙값:', SW[m], '\n꽃잎 길이 평균:',PL[m],'\n꽃잎 너비 평균:',PW[m])

