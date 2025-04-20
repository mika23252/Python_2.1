# Деревья решений и случайные леса
# СЛ - непараметрический алгоритм (в формуле обучающей функции данные не заложены)
# СЛ - пример ансамблевого метода, основанного на агрегации результатов множества простых моделей
# В реализациях дерева принятия решений в машинном обучении, вопросы обычно ведут к разделению данных по осям,
# т.е. каждый узел разбивает данные на две группы по одному из признаков

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from sklearn.tree import DecisionTreeClassifier

iris = sns.load_dataset("iris")

species_int = []
for f in iris.values:
    match f[4]:
        case 'setosa':
            species_int.append(1)
        case 'versicolor':
            species_int.append(2)
        case 'virginica':
            species_int.append(3)

species_int_df = pd.DataFrame(species_int)

data = iris[["sepal_length", "petal_length", "species"]]

data['species'] = species_int_df

data_df = data[(data["species"] == 3) | (data["species"] == 2)]

X = data_df[["sepal_length", "petal_length"]]
y = data_df["species"]

data_df_virginica = data_df[data_df["species"] == 3]
data_df_versicolor = data_df[data_df["species"] == 2]

max_depth = [[1, 2, 3, 4], [5, 6, 7, 8]]

fig, ax = plt.subplots(2, 4, sharex='col', sharey='row')

for i in range(2):
    for j in range(4):

        ax[i, j].scatter(data_df_virginica["sepal_length"], data_df_virginica["petal_length"])
        ax[i, j].scatter(data_df_versicolor["sepal_length"], data_df_versicolor["petal_length"])

        model = DecisionTreeClassifier(max_depth=max_depth[i][j])
        model.fit(X, y)

        x1_p = np.linspace(min(data_df["sepal_length"]), max(data_df["sepal_length"]), 100)
        x2_p = np.linspace(min(data_df["petal_length"]), max(data_df["petal_length"]), 100)

        X1_p, X2_p = np.meshgrid(x1_p, x2_p)

        X_p = pd.DataFrame(
            np.vstack([X1_p.ravel(), X2_p.ravel()]).T, columns=["sepal_length", "petal_length"]
        )
        y_p = model.predict(X_p)

        ax[i, j].contourf(X1_p, X2_p, y_p.reshape(X1_p.shape), alpha=0.4, levels=2, cmap='inferno', zorder=1)

# X_p['species'] = y_p

# X_p_setosa = X_p[X_p["species"] == 3]
# X_p_versicolor = X_p[X_p["species"] == 2]

# plt.scatter(X_p_setosa["sepal_length"], X_p_setosa["petal_length"], alpha=0.4)
# plt.scatter(X_p_versicolor["sepal_length"],X_p_versicolor["petal_length"], alpha=0.4)

# plt.contourf(X1_p, X2_p, y_p.reshape(X1_p.shape), alpha=0.4, levels=2, cmap='inferno', zorder=1)

plt.show()
