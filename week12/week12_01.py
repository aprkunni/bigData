import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression # 적용모델 : 선형 회구 분석 모델
from sklearn.model_selection import train_test_split # 훈련 / 검증 셋트 분할 함수


# 나이에 따른 생존율 계산


titanic = sns.load_dataset('titanic') # 데이터 로딩
median_age = titanic['age'].median() # 나이 중앙값 산출
titanic_fill_row = titanic.fillna({'age' : median_age}) # 결측치 처리

X = titanic_fill_row[['age']] # 독립변수 설정
y = titanic_fill_row[['survived']] # 종족변수 설정

# 훈련/검증 데이터 분할
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# 모델 선택
model = LinearRegression()

# 선형 회귀 모델 훈련
model.fit(X_train, y_train)

# 예측
y_pred = model.predict(X_test) # 검증 셋트를 인수로 예측

# 시각화
plt.figure(figsize=(3, 2))
plt.scatter(X_test, y_test, color='blue', label='Real')
plt.scatter(X_test, y_pred, color='red', label='Predicted')
plt.title('Linear Regression: Real VS Predicted')
plt.xlabel('Age')
plt.ylabel('Survived')
plt.show()

# 2) 생존율 계산
titanic_fill_row['survived'] = titanic_fill_row['survived'].astype(float)
# 3) 시각화
plt.figure(figsize=(3, 2))
sns.histplot(data=titanic_fill_row, x='age', weights='survived', bins=8, kde=False)
plt.title('Survival Rate by Age (Fill with Median)')
plt.xlabel('Age')
plt.ylabel('Survival Rate (Weighted)')
plt.show()

# # 1) 결측치 행들을 제거
# titanic_drop_row = titanic.dropna(subset=['age'])
# #print(titanic_drop_row.info())
# # 2) 생존율 계산
# titanic_drop_row['survived'] = titanic_drop_row['survived'].astype(float)
# print(titanic_drop_row['survived'])
# # 3) 시각화
# plt.figure(figsize=(3, 2))
# sns.histplot(data=titanic_drop_row, x='age', weights='survived', bins=8, kde=False)
# plt.title('Survival Rate by Age (Drop NaN rows)')
# plt.xlabel('Age')
# plt.ylabel('Survival Rate (Weighted)')
# plt.show()


# print(titanic['sex'].head())
# print(titanic.info())

# gender_survival = titanic.groupby(by='sex')['survived'].mean()
# print(type(gender_survival))  # <class 'pandas.core.series.Series'>

# gender_survival = titanic.groupby(by='sex')['survived'].mean().reset_index()
# print(gender_survival)
# #print(type(gender_survival))
# print(gender_survival.info())
#
# sns.barplot(data=gender_survival, x='sex', y='survived')
# plt.title('Survival Rate by Gender')
# plt.ylabel('Survival Rate')
# plt.show()




# titanic['deck'] = titanic['deck'].cat.add_categories('Unknown')
# titanic['deck'].fillna('Unknown', inplace=True)
# print(titanic['deck'])
# print(titanic.info())

# print(titanic['survived'])
# print(titanic.info())

# 생존자 수와 사망자 수 시각화
# sns.countplot(data=titanic, x='survived')
# plt.title('Survived (0 = No, 1 = Yes)')
# plt.xlabel('Survived')
# plt.ylabel('Count')
# plt.show()