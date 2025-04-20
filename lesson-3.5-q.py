# ДЗ убрать из данных iris часть точек, на которых обучаемся, и убедиться, что на предсказание влияют только опорные вектора

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from sklearn.svm import SVC

iris = sns.load_dataset("iris")

fig, (ax1, ax2) = plt.subplots(1, 2, sharex='col', sharey='row')

print(iris.head())

data = iris[["sepal_length", "petal_length", "species"]]
data_df = data[(data["species"] == "setosa") | (data["species"] == "versicolor")]

X = data_df[["sepal_length", "petal_length"]]
y = data_df["species"]

data_df_setosa = data_df[data_df["species"] == "setosa"]
data_df_versicolor = data_df[data_df["species"] == "versicolor"]

ax1.scatter(data_df_setosa["sepal_length"], data_df_setosa["petal_length"])
ax1.scatter(data_df_versicolor["sepal_length"], data_df_versicolor["petal_length"])

model_full_data = SVC(kernel='linear', C=10000)
model_full_data.fit(X, y)

print(model_full_data.support_vectors_)
ax2.scatter(
    model_full_data.support_vectors_[:, 0],
    model_full_data.support_vectors_[:, 1]
)

############################################################
X_new = X.iloc[model_full_data.support_]
y_new = y.iloc[model_full_data.support_]

model_support_vectors = SVC(kernel='linear', C=10000)
model_support_vectors.fit(X_new, y_new)
############################################################

x1_p = np.linspace(min(data_df["sepal_length"]), max(data_df["sepal_length"]), 100)
x2_p = np.linspace(min(data_df["petal_length"]), max(data_df["petal_length"]), 100)

X1_p, X2_p = np.meshgrid(x1_p, x2_p)

X_p = pd.DataFrame(
    np.vstack([X1_p.ravel(), X2_p.ravel()]).T, columns=["sepal_length", "petal_length"]
)
y_p = model_full_data.predict(X_p)
y_new_p = model_support_vectors.predict(X_p)

X_p['species'] = y_p

X_p_setosa = X_p[X_p["species"] == "setosa"]
X_p_versicolor = X_p[X_p["species"] == "versicolor"]

ax1.scatter(X_p_setosa["sepal_length"], X_p_setosa["petal_length"], alpha=0.2)
ax1.scatter(X_p_versicolor["sepal_length"],X_p_versicolor["petal_length"], alpha=0.2)
ax1.set_title('Все данные')

X_p['species'] = y_new_p

X_p_setosa = X_p[X_p["species"] == "setosa"]
X_p_versicolor = X_p[X_p["species"] == "versicolor"]

ax2.scatter(X_p_setosa["sepal_length"], X_p_setosa["petal_length"], alpha=0.2, color='green')
ax2.scatter(X_p_versicolor["sepal_length"], X_p_versicolor["petal_length"], alpha=0.2, color='red')
ax2.set_title('Только опорные векторы')

plt.show()

