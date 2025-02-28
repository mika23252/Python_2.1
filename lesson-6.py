import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import matplotlib as mpl

# rng = np.random.default_rng(1)
# data = rng.normal(size=1000)

# plt.hist(
#     data,
#     bins=30, # 'корзинка для сбора данных'
#     density=True,
#     alpha=0.9,
#     histtype='step' # default - 'stepfilled'
# )

# x1 = rng.normal(0, 0.8, 1000)
# x2 = rng.normal(-2, 1, 1000)
# x3 = rng.normal(3, 2, 1000)

# args = dict(
#     alpha=0.6,
#     bins=30
# )
#
# plt.hist(x1, **args)
# plt.hist(x2, **args)
# plt.hist(x3, **args)

# plt.show()

# как посчитать количество элементов в кусочке диаграммы

# print(np.histogram(x1, bins=1))
# print(np.histogram(x1, bins=2))
# print(np.histogram(x3, bins=30))

# Двумерные гистограммы

# mean = [0, 0]
# cov = [[1, 1], [1, 2]]
#
# x, y = rng.multivariate_normal(mean, cov, 10000).T
#
# plt.hist2d(x, y, bins=30)
# plt.hexbin(x, y, gridsize=30)
#
# cb = plt.colorbar()
# cb.set_label('Points in interval')
#
# print(np.histogram2d(x, y, bins=1))
# print(np.histogram2d(x, y, bins=30))

# Легенды

# x = np.linspace(0, 10, 1000)
#
# fig, ax = plt.subplots()
#
# y = np.sin(x[:, np.newaxis] + np.pi * np.arange(0, 2, 0.5))
#
# lines = plt.plot(x, y) # plt.Line2d

# plt.legend(
#     lines, ['1', '2', '3', '4'],
#     loc='center left' # 'best', 'upper right', 'upper left', 'lower left', 'lower right',
    # 'right', 'center left', 'center right', 'lower center', 'upper center', 'center'
# )

# plt.legend(lines[:2], ['1', '2'])

# ax.plot(x, np.sin(x), label='Синус')
# ax.plot(x, np.cos(x), label='Косинус')
# ax.plot(x, np.cos(x) + 2)
# ax.axis('equal')
#
# ax.legend(
#     frameon=True, # прямоугольник вокруг легенды
#     fancybox=True, # сглаживает углы прямоугольника
#     shadow=True
# )

# cities = pd.read_csv('california_cities.csv')
# lat, lon, pop, area = cities['latd'], cities['longd'], cities['population_total'], cities['area_total_km2']
#
# plt.scatter(lon, lat, c=np.log10(pop), s=area) # c - color, s - size
# plt.xlabel('Широта')
# plt.ylabel('Долгота')
# plt.colorbar()
# plt.clim(3, 7) # ограничили colorbar
#
# plt.scatter([], [], c='k', alpha=0.7, s=100, label='100 $km^2$')
# plt.scatter([], [], c='k', alpha=0.7, s=300, label='300 $km^2$')
# plt.scatter([], [], c='k', alpha=0.7, s=500, label='500 $km^2$')
#
# plt.legend(labelspacing=2, frameon=False)

# fig, ax = plt.subplots()
#
# lines = []
# styles = ['-', '--', '.-', ':']
# x = np.linspace(0, 10, 1000)
# for i in range(4):
#     lines += ax.plot(
#         x,
#         np.sin(x - i + np.pi/2),
#         styles[i]
#     )
#
# ax.axis('equal')
#
# ax.legend(lines[:2], ['line 1', 'line 2'], loc='upper right')
#
# # Добавим еще одну легенду (создаем доп слой)
#
# leg = mpl.legend.Legend(ax, lines[1:], ['line 2', 'line 3', 'line 4'], loc='lower left')
#
# ax.add_artist(leg)


# Шкалы

# x = np.linspace(0, 10, 1000)
# y = np.sin(x) * np.cos(x[:, np.newaxis])

##################

# Карты цветов:
# последовательные
# дивергентные (2 цвета)
# дивергентные (2 цвета)
# качественные (смешиваются без четкого порядка)

# 1
# plt.imshow(y, cmap='viridis')
# plt.imshow(y, cmap='binary')

# 2
# plt.imshow(y, cmap='RdBu')
# plt.imshow(y, cmap='GnBu')

# 3
# plt.imshow(y, cmap='rainbow')
# plt.imshow(y, cmap='jet')

# plt.colorbar()

###################

# plt.figure()
# plt.subplot(1, 2, 1)
# plt.imshow(y, cmap='viridis')
# plt.colorbar()
#
# plt.subplot(1, 2, 2)
# plt.imshow(y, cmap='viridis')#cmap=plt.cm.get_cmap('viridis', 6)) # не сработало
# plt.colorbar()
# plt.clim(-0.25, 0.25)

# plt.show()
