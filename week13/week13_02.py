import seaborn as sns2022
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split # 훈련 / 검증 셋트 분할 함수

# minmax 스케일링 standard 스케일링
# MPG - Mile Per Gallon
# Km/L -Kilometer Per Liter

mpg = sns.load_dataset('mpg') #데이터셋 로딩

# 데이터 전처리
mpg.drop(['name'], axis=1, inplace=True) #불필요한 칼럼 삭제 (원본 데이터 변경)
# 1번 방법 소수의 행들은 제외하고 날리자 same으로 만들기
mpg.dropna(inplace=True) # 결측치가 있는 행 제거 (원본 데이터 변경)
mpg = pd.get_dummies(mpg, columns=['origin'], drop_first=True) # One-hot encoding

# 독립변수, 의존변수
X = mpg.drop(['mpg'], axis=1) #레이블 컬럼 제거
y = mpg['mpg'] # 레이블 (타켓 변수)

# 훈련/검증 데이터 분할
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

#모델 선택 및 학습
model = KNeighborsRegressor() # 선형 회귀 모델
model.fit(X_train, y_train)

# 테스트 (예측 값 생성)
y_pred = model.predict(X_test)

# 성능 측정 mse r2점수
mse = mean_squared_error(y_test, y_pred) # 검증셋의 레이블과 예측 레이블의 평균 제곱 오차를 구함
r2 = r2_score(y_test, y_pred) # 결정 계수 계산

# 결과 출력
print(f'Mean squared error: {mse}')
print(f'R2 score: {r2}')

# 시각화
plt.figure(figsize=(10, 6))
plt.scatter(y_test, y_pred, color='blue', alpha=0.6)
plt.plot([y.min(), y.max()], [y.min(), y.max()], color='red', linestyle='--')
plt.title('Actual MPG vs Predicted MPG')
plt.xlabel('Actual MPG')
plt.ylabel('Predicted MPG')
plt.grid(True)
plt.show()
