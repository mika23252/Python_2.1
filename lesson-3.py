import numpy as np
import pandas as pd

# Pandas - расширение NumPy (структурированные массивы). Строки и столбцы индексируются метками, а не только числовыми значениями

# Series, DataFrame, Index - структуры pandas


# Series

# data = pd.Series([0.25, 0.5, 0.75, 1.0])
# print(data)
# print(type(data))
#
# print(data.values)
# print(type(data.values))
#
# print(data.index)
# print(type(data.index))
############
# data = pd.Series([0.25, 0.5, 0.75, 1.0])
# print(data[0])
# print(data[1:3])
# print('##########')
# data = pd.Series([0.25, 0.5, 0.75, 1.0], index=['a', 'b', 'c', 'd'])
# print(data)
# print(data['a'])
# print(data['b':'d'])
# print(type(data.index))

# data = pd.Series([0.25, 0.5, 0.75, 1.0], index=[1, 10, 7, 'd'])
# print(data)
# print(data[1])
# print(data[10:'d'])

###################

# population_dict = {
#     'city_1': 1001,
#     'city_2': 1002,
#     'city_3': 1003,
#     'city_4': 1004,
#     'city_5': 1005
# }
# population = pd.Series(population_dict)
# print(population)
#
# print(population['city_4'])
# print(population['city_4':'city_5'])

# Для создания Series можно использовать
# - списки Python или массивы NumPy
# - скалярные значение
# - словари


# DataFrame - двумерн. массив с явно определенными индек-ми. Послед-ть "согласованных" Series

# population_dict = {
#     'city_1': 1001,
#     'city_2': 1002,
#     'city_3': 1003,
#     'city_4': 1004,
#     'city_5': 1005
# }
#
# area_dict = {
#     'city_1': 9991,
#     'city_2': 9992,
#     'city_3': 9993,
#     'city_4': 9994,
#     'city_5': 9995
# }
#
# popelation =  pd.Series(population_dict)
# area = pd.Series(area_dict)
#
# states = pd.DataFrame({
#     'population1': popelation,
#     'area1': area
# })

# print(states)
# print(states.values)
# print(states.index)
# print(states.columns)

# print(states['area1'])

# DataFrame. Способы создания
# - через объекты Series
# - списки словарей
# - словари объектов Series
# - двумерный массив NumPy
# - структурированный массив Numpy


# Index - способ организации ссылки на данные объектовв Series & DataFrame.
# Он неизменяем, упорядочен явл. мультимножеством(могут быть повторяющ. знач-я)

# ind = pd.Index([2,3,5,7,11])
# print(ind[1])
# print(ind[::2])
# # ind[1] = 4 # так нельзя
#
# #Index - следует соглашениям объекта set (python)
# indA = pd.Index([1,2,3,4,5])
# indB = pd.Index([2,3,4,5,6])
# print(indA.intersection(indB))


# Выборка данных из Series

# data = pd.Series([0.25, 0.5, 0.75, 1.0], index=['a', 'b', 'c', 'd'])
# print('a' in data)
# print('z' in data)
#
# print(data.keys())
# print(list(data.items()))
#
# data['a'] = 100
# data['z'] = 100
# print(data)

# как одномерный массив
# data = pd.Series([0.25, 0.5, 0.75, 1.0], index=['a', 'b', 'c', 'd'])
#
# print(data['a':'c'])
# print(data[0:2])
# print(data[(data > 0.5) & (data < 1)])
# print(data[['a', 'd']])


# Выборка данных из DataFrame
# как словарь

# population_dict = {
#     'city_1': 1001,
#     'city_2': 1002,
#     'city_3': 1003,
#     'city_4': 1004,
#     'city_5': 1005
# }
#
# area_dict = {
#     'city_1': 9991,
#     'city_2': 9992,
#     'city_3': 9993,
#     'city_4': 9994,
#     'city_5': 9995
# }
#
# pop = pd.Series({
#     'city_1': 1001,
#     'city_2': 1002,
#     'city_3': 1003,
#     'city_4': 1004,
#     'city_5': 1005,
# })
# area = pd.Series({
#     'city_1': 1001,
#     'city_2': 1002,
#     'city_3': 1003,
#     'city_4': 1004,
#     'city_5': 1005
# })
#
# data = pd.DataFrame({'area1': area, 'pop1': pop})
# print(data)
# print(data['area1'])
# print(data.area1 is data['area1'])
# data['new'] = data['area1']
# print(data)


# двумерный Numpy-массив

# data = pd.DataFrame({'area1': area, 'pop1':pop, 'pop':pop})
# print(data)
# print(data.values)
# print(data.T)
#
# print(data['area1'])
# print(data.values[0:3])

# атрибуты-индексаторы

# print(data)
# print(data.iloc[:3, 1:2])
# print(data.loc[:'city_3', 'pop1':'pop'])
# print(data.loc[data['pop'] > 1002, ['area1','pop']])
#
# data.iloc[0, 2] = 99999999
# print(data)

# универсальные функции

# rng = np.random.default_rng()
# s = pd.Series(rng.integers(0, 10, 4))
#
# print(s)
# print(np.exp(s))

# pop = pd.Series({
#     'city_1': 1001,
#     'city_2': 1002,
#     'city_3': 1003,
#     'city_41': 1004,
#     'city_51': 1005,
# })
# area = pd.Series({
#     'city_1': 1001,
#     'city_2': 1002,
#     'city_3': 1003,
#     'city_42': 1004,
#     'city_52': 1005
# })
#
# print(pop + area)
# data = pd.DataFrame({'area1': area, 'pop1': pop})
# print(data)
#
# rng = np.random.default_rng()
# dfA = pd.DataFrame(rng.integers(0, 10, (2,2)), columns=['a', 'b'])
# dfB = pd.DataFrame(rng.integers(0, 10, (3,3)), columns=['a', 'b', 'c'])
#
# print(dfA)
# print(dfB)
#
# print(dfA + dfB)


# rng = np.random.default_rng()
#
# A = rng.integers(0, 10, (3,4))
# print(A)
#
# print(A[0])
# print(A - A[0])
#
# df = pd.DataFrame(A, columns=['a', 'b', 'c', 'd'])
# print(df)
#
# print(df.iloc[0])
# print(df - df.iloc[0])
#
# print(df.iloc[0, ::2])
# print(df - df.iloc[0, ::2])


# NA-значения: NaN, null, -99999

# Pandas. Два способа хранения отсутствующих значений
# - индикаторы None, None
# - null

# None - объект (накладные расходы). Не работает с sum, min

# val1 = np.array((1, None, 2, 3))
# print(val1.sum()) # ошибка

# val1 = np.array((1, 2, 3))
# print(val1.sum())
#
# val1 = np.array([1, np.nan, 2, 3])
# print(val1)
# print(val1.sum())
# print(np.nansum(val1))

# x = pd.Series(range(10), dtype=int)
# print(x)
#
# x[0] = None
# x[1] = np.nan
# print(x)
#
# x1 = pd.Series(['a', 'b', 'c'])
# print(x1)
# x1[0] = None  # будет None потому что замена объекта на объект
# x1[1] = np.nan
# print(x1)


x2 = pd.Series([1, 2, 3, np.nan, None, pd.NA])
x3 = pd.Series([1, 2, 3, np.nan, None, pd.NA], dtype="Int32")
print(x2)
print(x3)

print(x3.isnull())
print(x3[x3.isnull()])
print(x3[x3.notnull()])
