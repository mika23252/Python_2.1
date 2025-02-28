# 1. Сценарий
# 2. командная строка python
# 3. Jupyter

# 1
# plt.show() - запускается только 1 раз в конце
# Figure

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0,10, 100)
# plt.plot(x, np.sin(x))
#
# plt.show()
#
# plt.plot(x, np.cos(x)) # не сработает если стоит после plt.show()

# 2
# используем команду %matplotlib
# import matplotlib.pyplot as plt
# plt.plot(...)
# plt.show()

# 3
# 2 вариации:
#  %matplotlib inline - в блокнот добавл-ся статич. картинка
#  %matplotlib notebook - графики интерактивные

# есть возможность сохранять картинки
# fig = plt.figure()
# fig.savefig('saved.png')

# fig = plt.figure()
# print(fig.canvas.get_supported_filetypes())

# 2 способа вывода графиков
# matlab-подобный стиль
# в объектно-ориентированном стиле

# matlab
# plt.figure()

# plt.subplot(2, 1, 1) #2 строки, 1 колонка, номер
# plt.plot(x, np.sin(x))
#
# plt.subplot(2, 1, 2)
# plt.plot(x, np.cos(x))
# проблема с возвращением к предыдущим графикам

# oo

# fig:Figure - контейнер, содержит все объекты (СК, текст, метки...), ax:Axes - СК (прямоугольник, деления, метки...)

# fig, ax = plt.subplots(2)

# Цвета линий color
# 'blue'
# 'rgbcmyk' -> 'rg'
# '0.14' - градация серого от 0 до 1
# RRGGBB - 'FF00EE'
# RGB - (1.0, 0.2, 0,3)
# HTML - 'salmon'

# Стиль линии linestyle
# '-', 'solid' - сплошная
# '--', 'dashed' - штриховая
# '-.', 'dashdot' - штрихпунктирная
# ':', 'dotted' - пунктирная

# ax[0].plot(x, np.sin(x), color='red', linestyle='solid')
# ax[1].plot(x, np.cos(x), color='g', linestyle='dashdot') # или просто прописать '-.g'
#
# plt.show()

###############################

# fig, ax = plt.subplots(4)
# ax[0].plot(x, np.sin(x))
# ax[1].plot(x, np.sin(x))
# ax[2].plot(x, np.sin(x))
# ax[3].plot(x, np.sin(x))
#
# ax[1].set_xlim(-2, 12) # определяем пределы графика
# ax[1].set_ylim(-1.5, 1.5) # определяем пределы графика
#
# ax[2].set_xlim(12, -2) # можно отзеркалить
# ax[2].set_ylim(1.5, -1.5)
#
# ax[3].autoscale(tight=True) # график подстраивается под размеры прямоугольника

# plt.subplot(3, 1, 1)
# plt.plot(x, np.sin(x))
#
# plt.title('Синус')
# plt.xlabel('x')
# plt.ylabel('y')
#
# plt.subplot(3, 1, 2)
# plt.plot(x, np.sin(x), '-.g', label='sin(x)')
# plt.plot(x, np.cos(x), ':b', label='cos(x)')
# plt.title('Синус и косинус')
# plt.xlabel('x')
# plt.ylabel('y')
#
# plt.legend()
#
# plt.subplot(3, 1, 3)
# plt.plot(x, np.sin(x), '-.g', label='sin(x)')
# plt.plot(x, np.cos(x), ':b', label='cos(x)')
# plt.title('Синус и косинус')
# plt.xlabel('x')
# plt.ylabel('y')
# plt.axis('equal')
#
# plt.subplots_adjust(hspace=1)

# маркеры

# x = np.linspace(0, 10, 30) # график слегка ломаный
# plt.plot(x, np.sin(x), 'og') # поэтому можем нарисовать без соединения точек
# plt.plot(x, np.sin(x)+1, '.-g')
# plt.plot(x, np.sin(x)+2, '>g')
# plt.plot(x, np.sin(x)+3, 's-g', markersize=7, linewidth=4, markerfacecolor='white', markeredgecolor='grey', markeredgewidth=2)


# диаграмма scatter

# x = np.linspace(0, 10, 30)

# rng = np.random.default_rng(0)
# colors = rng.random(30)
# sizes = 30*rng.random(30)
#
# plt.scatter(x, np.sin(x), marker='o', c=colors, s=sizes)
# plt.colorbar()

# Если точек больше 1000, то plot предпочтительнее из-за производительности

# работа с ошибками

# x = np.linspace(0, 10, 50)
#
# dy = 0.4
# y = np.sin(x) + dy * np.random.randn(50)
#
# plt.errorbar(x, y, yerr=dy, fmt='.')
# plt.fill_between(x, y-dy, y+dy, color='red', alpha=0.4)
# plt.plot(x, np.sin(x), 'g')

plt.show()
