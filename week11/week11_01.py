import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# 나이에 따른 생존율 계산
titanic = sns.load_dataset('titanic')
# print(titanic.info()) # age 칼럼은 177개의 결측값 존재
# 1) 결측치 행들을 중앙값(평균값)으로 채워넣기
median_age = titanic['age'].median()
# mean_age = titanic['age'].mean()
# print(median_age, mean_age)
titanic_fill_low = titanic.fillna({'age' : median_age})
# print(titanic_fill_low)
# # 2) 생존율 계산
titanic_fill_low['survived'] = titanic_fill_low['survived'].astype(float)
print(titanic_fill_low['age'])
# # 3) 시각화
plt.figure(figsize=(10, 5))
sns.histplot(data=titanic_fill_low, x='age', weights='survived', bins=8, kde=True)
plt.title('Survival Rate by Age (Fill with median)')
plt.xlabel('Age')
plt.ylabel('Survival Rate (Weighted)')
plt.show()


# 1) 결측치 행들을 제거
titanic_drop_low = titanic.dropna(subset=['age'])
# print(titanic_drop_low.info())
# 2) 생존율 계산
titanic_drop_low['survived'] = titanic_drop_low['survived'].astype(float)
print(titanic_drop_low['survived'])
# 3) 시각화
plt.figure(figsize=(10, 5))
sns.histplot(data=titanic_drop_low, x='age', weights='survived', bins=8, kde=True)
plt.title('Survival Rate by Age (Drop NaN rows)')
plt.xlabel('Age')
plt.ylabel('Survival Rate (Weighted)')
plt.show()


# print(titanic['sex'].head())
# print(type(gender_survival))  # <class 'pandas.core.series.Series'>
# gender_survival = titanic.groupby(by='sex')['survived'].mean()

# gender_survival = titanic.groupby(by='sex')['survived'].mean().reset_index()
# print(gender_survival)
# print(type(gender_survival))
# print(gender_survival.info())

# sns.barplot(data=gender_survival, x='sex', y='survived')
# plt.title('Survival Rate by Gender')
# plt.ylabel('Survival Rate')
# plt.show()

# sns.histplot()
#
# df = pd.DataFrame(titanic)
#
# df.plot.hist()
# df.plot.scatter(x='w',y='h')

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