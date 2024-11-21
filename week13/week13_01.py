import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split # 훈련 / 검증 셋트 분할 함수

# MPG - Mile Per Gallon
# Km/L -Kilometer Per Liter

mpg = sns.load_dataset('mpg') #데이터셋 로딩

# 데이터 전처리
mpg.drop(['name'], axis=1, inplace=True) #불필요한 칼럼 삭제 (원본 데이터 변경)
# 1번 방법 소수의 행들은 제외하고 날리자 same으로 만들기
mpg.dropna(inplace=True) # 결측치가 있는 행 제거 (원본 데이터 변경)
mpg = pd.get_dummies(mpg, columns=['origin'], drop_first=True) # One-hot encoding
#print(mpg.info())

# 독립변수, 의존변수
X = mpg.drop(['mpg'], axis=1) #레이블 컬럼 제거
y = mpg['mpg'] # 레이블 (타켓 변수)
print(X.dtypes) # 각 열의 데이터 타입 확인

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)



