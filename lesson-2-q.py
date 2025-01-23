import numpy as np

# суммирование значений

# rng = np.random.default_rng(1)
# s = rng.random(50)
#
# print(s)
# print(sum(s))
# print(np.sum(s))
# a = np.array([
#     [1,2,3,4,5],
#     [6,7,8,9,10]
# ])
# print(np.sum(a))
# print(np.sum(a, axis=0))
# print(np.sum(a, axis=1))
#
# print(np.min(a))
# print(np.min(a, axis=0))
# print(np.min(a, axis=1))
# print(a.min())
# print(a.min(0))
# print(a.min(1))
#
# print(np.nanmin(a))
# print(np.nanmin(a, axis=0))
# print(np.nanmin(a, axis=1))

# Транслирование (broadcasting)
# набор правил, которые позвволяют осуществлять бинарные операции с массивами разных форм и размеров

# a = np.array([0,1,2])
# b = np.array([5,5,5])
#
# print(a+b)
# print(a+5)
#
# a = np.array([0,1,2])
# b = np.array([[0], [1], [2]])
# print(a + b)

# Правила
# 1. Если размерности массивов отличаются, то форма массива с меньшей размерностью дополняется 1 с левой стороны
# 2. Если формы массивов не совпадают в каком-то измерении, то если у массива форма равна 1, то он
# "растягивается" до соответствия формы второго массива

# 3. Если в каком либо измерении размеры отличаются и ни один из них не равен 1, то генерируется ошибка

# a = np.array([[0,1,2], [3,4,5]])
# b = np.array([5])
#
# print(a.ndim, a.shape)
# print(b.ndim, b.shape)
# print(a+b)

# a = np.ones((2,3))
# b = np.arange(3)
# print(a)
# print(b)
# print(a.ndim, a.shape)
# print(b.ndim, b.shape)
#
# c = a + b
# print(c, c.shape)

# последний пример

# a = np.ones((3,2))
# b = np.arange(3)
# c = a + b
# print(c)

# X = np.array([
#     [1,2,3,4,5,6,7,8,9],
#     [9,8,7,6,5,4,3,2,1]
# ])

# способ отцентрировать массив
# Xmean = X.mean(0)
# print(Xmean)
# Xcenter = X - Xmean
# print(Xcenter)

############################################################

# сравнение
x = np.array([1,2,3,4,5])
y = np.array([[1,2,3,4,5], [6,7,8,9,10]])
print (x < 3)
print(np.less(x,3))

print(np.sum(y < 4, axis=0))
print(np.sum(y < 4, axis=1))
print(np.sum(y<4)) # кол-во элементов