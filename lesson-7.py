import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl
import pandas as pd

from datetime import datetime

# fig, ax = plt.subplots(2, 3)
# fig, ax = plt.subplots(2, 3, sharex='col', sharey='row') # по оси х склеиваем столбцы и по оси у строки
#
# for i in range(2):
#     for j in range(3):
#         ax[i, j].text(0.5, 0.5, str((i,j)), fontsize=16, ha='center')


# если хотим чтобы график занимал сразу несколько частей:
# grid = plt.GridSpec(2, 3)
#
# plt.subplot(grid[:2, 0])
# plt.subplot(grid[0, 1:])
# plt.subplot(grid[1, 1])
# plt.subplot(grid[1, 2])


# пример с нормальным распределением
# mean = [0, 0]
# cov = [[1,1], [1,2]]
#
# rng = np.random.default_rng(1)
# x, y = rng.multivariate_normal(mean, cov, 3000).T
#
# fig = plt.figure()
# grid = plt.GridSpec(4, 4, hspace=0.5, wspace=0.5)
#
# main_ax = fig.add_subplot(grid[:-1, 1:])
# main_ax.plot(x, y, 'o', markersize=3, alpha=0.2)
#
# y_hist = fig.add_subplot(grid[:-1, 0], xticklabels=[], sharey=main_ax) # xticklabels=[] убирает подписи к оси х
#
# x_hist = fig.add_subplot(grid[-1, 1:], yticklabels=[], sharex=main_ax)
#
# y_hist.hist(y, 30, orientation='horizontal')
# x_hist.hist(x, 30, histtype='step')


# Поясняющие надписи

# births = pd.read_csv('../2.6/births-1969.csv')
#
# # births['day'] = births['day'].astype(int)
#
# births.index = pd.to_datetime(births.year*10000 + 100*births.month + births.day, format='%Y%m%d')
#
# # print(births.head())
#
# births_by_date = births.pivot_table('births', [births.index.month, births.index.day])
# # print(births_by_date)
#
# births_by_date.index = [datetime(1969, month, day) for (month, day) in births_by_date.index]
# # print(births_by_date)
#
# fig, ax = plt.subplots()
# births_by_date.plot(ax=ax)
#
# style = dict(size=10, alpha=0.5)
# ax.text('1969-01-01', 5500, 'Новый год', **style)
# ax.text('1969-09-01', 4000, 'День знаний')
#
# ax.set(title='Рождаемость в 1969', ylabel='Число рождений')
#
# # можно отформатировать оси:
# ax.xaxis.set_major_formatter(plt.NullFormatter())
# ax.xaxis.set_minor_formatter(mpl.dates.DateFormatter('%h'))
# ax.xaxis.set_minor_locator(mpl.dates.MonthLocator(bymonthday=15)) # 12 делений на 15 днях месяцев

# fig = plt.figure()
# ax1 = plt.axes()
#
# ax2 = plt.axes([0.4, 0.3, 0.1, 0.2])
#
# ax1.set_xlim(0, 2)
# ax1.text(0.6, 0.8, 'Data1 (0.6, 0.8)', transform=ax1.transData)
# ax1.text(0.6, 0.8, 'Data2 (0.6, 0.8)', transform=ax2.transData)
#
# ax1.text(0.5, 0.1, 'Data3 (0.5, 0.1)', transform=ax1.transAxes)
# ax1.text(0.5, 0.1, 'Data4 (0.5, 0.1)', transform=ax2.transAxes)
#
# ax1.text(0.2, 0.2, 'Data5 (0.2, 0.2)', transform=fig.transFigure)

# fig, ax = plt.subplots()
#
# x = np.linspace(0, 20, 1000)
# ax.plot(x, np.cos(x))
#
# ax.axis('equal')
#
# ax.annotate('Локал макс', xy=(6.28, 1), xytext=(10,4), arrowprops=dict(facecolor='red'))
# ax.annotate('Локал мин', xy=(3.14, -1), xytext=(6,-4), arrowprops=dict(facecolor='blue', arrowstyle='->'))
#
# fig, ax = plt.subplots(4, 4, sharex=True, sharey=True)
#
# for axi in ax.flat:
#     axi.xaxis.set_major_locator(plt.MaxNLocator(5))
#     axi.yaxis.set_major_locator(plt.MaxNLocator(3))

plt.show()
