import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.neighbors import KNeighborsRegressor

# Download and prepare the data
data_root = "https://github.com/ageron/data/raw/main/"
life_sat = pd.read_csv(data_root + "lifesat/lifesat.csv")
X = life_sat[["GDP per capita (USD)"]].values
y = life_sat[["Life satisfaction"]].values

print(life_sat.head(27))
# # Visualize the data
# life_sat.plot(kind='scatter', grid=True,
# x="GDP per capita (USD)", y="Life satisfaction")
# plt.axis([23_500, 62_500, 4, 9])
# plt.show()
#
# # Select a linear model
# model = LinearRegression() #선형 회구 모델 적용
model = KNeighborsRegressor(n_neighbors=3) #한국과 1인당 GDP가 가까운 나라 셋을 사용한 최근접 방식
#
# # Train the model
# model.fit(X, y)
#
# # Make a prediction for Cyprus
# X_new = [[32_142.0]] # 대한민국 1인당 GDP 2022년 자료
# print(model.predict(X_new)) # output: [[6.30165767]]