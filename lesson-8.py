import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

# Трехмерные точки и линии

# fig = plt.figure()
# ax = plt.axes(projection='3d')
#
# z = np.linspace(0, 15, 1000)
# y = np.cos(z)
# x = np.sin(z)

# ax.plot3D(x, y, z, 'green')

# z2 = 15*np.random.random(100)
# y2 = np.cos(z2) + 0.1*np.random.random(100)
# x2 = np.sin(z2) + 0.1*np.random.random(100)

# ax.scatter3D(x2, y2, z2, c=z2, cmap='GnBu')

######################################

# def f(x, y):
#     return np.sin(np.sqrt(x**2 + y**2))

# x = np.linspace(-6, 6, 62)
# y = np.linspace(-6, 6, 62)
#
# X, Y = np.meshgrid(x, y)
# Z = f(X, Y)

# ax.contour3D(X, Y, Z, 50, cmap='inferno')
# ax.set_xlabel('x')
# ax.set_ylabel('y')
# ax.set_zlabel('z')
#
# ax.view_init(30, 50) # угол над плоскостью ХоY, поворот относительно оси Z


# типы графиков

# ax.scatter3D(X, Y, Z, c=Z, cmap='Greens') # просто точки

# ax.plot_wireframe(X, Y, Z) # каркасный

# ax.plot_surface(X, Y, Z, cmap='viridis') # поверхностный
# ax.set_title('Example')


# можно делать срез

# r = np.linspace(0, 6, 20)
# theta = np.linspace(-0.9*np.pi, 0.8*np.pi, 40)
#
# R, Theta = np.meshgrid(r, theta)
#
# X = R*np.cos(Theta)
# Y = R*np.sin(Theta)
# Z = f(X, Y)
#
# ax.plot_surface(X, Y, Z, cmap='viridis')


# триангуляция поверхности

# theta = 2*np.pi + np.random.random(1000)
# r = 6 * np.random.random(1000)
#
# x = r*np.cos(theta)
# y = r*np.sin(theta)
#
# z = f(x, y)
#
# ax.scatter(x, y, z, c=z, cmap='viridis')
#
# ax.plot_trisurf(x, y, z, cmap='viridis')


# Seaborn
# - DataFrame (mpl работает с pd)
# - более высокоуровневый

# data = np.random.multivariate_normal([0,0], [[5,2], [2,2]], size=2000)
# data = pd.DataFrame(data, columns=['x', 'y'])
#
# print(data.head())
#
# fig = plt.figure()
# plt.hist(data['x'], alpha=0.5)
# plt.hist(data['y'], alpha=0.5)
#
# # на sns:
# fig1 = plt.figure()
# sns.kdeplot(data=data)


# примеры с готовыми датасетами

# iris = sns.load_dataset('iris')
# print(iris.head())
#
# sns.pairplot(iris, hue='species') # используем если много переменных и мы хотим их сравнить

# tips = sns.load_dataset('tips') # чаевые
# print(tips.head())

# гистограммы
# grid = sns.FacetGrid(tips, col='sex', row='day', hue='time')
# grid.map(plt.hist, 'tip', bins=10)

# sns.catplot(data=tips, x='day', y='total_bill', kind='box') # kind='box' меняет 'круги' на 'блоки'

# sns.jointplot(data=tips, x='tip', y='total_bill', kind='hex')


# графики временных рядов
# planets = sns.load_dataset('planets')
# print(planets.head())
#
# sns.catplot(data=planets, x='year', kind='count', hue='method', order=range(2005, 2015)) # 'count' - кол-во записей


# датасеты для ml
tips = sns.load_dataset('tips')
print(tips.head())

# сравнение числовых столбцов
# числовые пары
# sns.pairplot(tips)

# тепловая карта
# tips_corr = tips[['total_bill', 'tip', 'size']]
# sns.heatmap(tips_corr.corr(), cmap='RdBu_r', annot=True, vmin=-1, vmax=1)
# 0 - незвасимы
# 1 - положительная (чем больше одно тем больше другое)
# -1 - отрицательная (чем больше одно тем меньше другое)

# диаграмма рассеяния
# sns.scatterplot(data=tips, x='total_bill', y='tip', hue='sex')

# sns.regplot(data=tips, x='total_bill', y='tip') # линейная регрессия
# sns.relplot(data=tips, x='total_bill', y='tip', hue='sex') # по сути тот же scatterplot, но можно изменить его стиль

# линейный график
# sns.lineplot(data=tips, x='total_bill', y='tip')

# сводная диаграмма
# sns.jointplot(data=tips, x='total_bill', y='tip')


# сравнение числовых и категориальных данных
# гистограмма

# sns.barplot(data=tips, x='day', y='total_bill', hue='sex') # столбцы

# sns.pointplot(data=tips, x='day', y='total_bill', hue='sex') # вместо столбцов точки

# ящик с "усами"
# sns.boxplot(data=tips, x='day', y='total_bill')
# линия на ящике - медиана, квантиль 2
# границы ящика - квантили 1 и 3
# точки вне ящика с усами - выбросы

# скрипичная диаграмма
# sns.violinplot(data=tips, x='day', y='total_bill')
# аналогично ящику

# одномерная диаграмма рассеяния

# sns.stripplot(data=tips, x='day', y='total_bill')

# plt.show()
