import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split # 훈련 / 검증 셋트 분할 함수

# MPG - Mile Per Gallon
# Km/L -Kilometer Per Liter

mpg = sns.load_dataset('mpg')
# print(mpg.info())

# 1번 방법 소수의 행들은 제외하고 날리자 same으로 만들기
mpg.dropna(inplace=True) # 결측치가 있는 행 제거 (원본 데이터 변경)
print(mpg.info())

# print(mpg.head())
# print(mpg.tail())
# print(mpg[['origin']])
# print(mpg.describe())

