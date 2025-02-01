import pandas as pd
import numpy as np

# population = [
#     101,
#     201,
#     102,
#     202,
#     103,
#     203,
# ]
#
# index = [
#     ('city_1', 2010),
#     ('city_1', 2020),
#     ('city_2', 2010),
#     ('city_2', 2020),
#     ('city_3', 2010),
#     ('city_3', 2020),
# ]
#
# pop = pd.Series(population, index=index)

# print(pop)
# print(pop[
#           [i for i in pop.index if i[1] == 2020]
#       ])

# MultiIndex

# index = pd.MultiIndex.from_tuples(index)
#
# pop = pop.reindex(index)
# print(pop)
#
# print(pop[:, 2020])
#
# pop_df = pop.unstack()
# print(pop_df)
# print('#################')
# print(pop_df.stack())
#####################################

# index = [
#     ('city_1', 2010, 1),
#     ('city_1', 2010, 2),
#
#     ('city_1', 2020, 1),
#     ('city_1', 2020, 2),
#
#     ('city_2', 2010, 1),
#     ('city_2', 2010, 2),
#
#     ('city_2', 2020, 1),
#     ('city_2', 2020, 2),
#
#     ('city_3', 2010, 1),
#     ('city_3', 2010, 2),
#
#     ('city_3', 2020, 1),
#     ('city_3', 2020, 2),
# ]
#
# population = [
#     101,
#     1010,
#
#     201,
#     2010,
#
#     102,
#     1020,
#
#     202,
#     2020,
#
#     103,
#     1030,
#
#     203,
#     2030,
# ]
#
# pop = pd.Series(population, index=index)
# print(pop)
#
# # index = pd.MultiIndex.from_tuples(index)
# # pop = pop.reindex(index)
# # print(pop)
# # print(pop[:, 2020])
# # print(pop[:, :, 2].unstack())
#
# pop_df = pd.DataFrame(
#     {
#         'total': pop,
#         'something': [
#             10,
#             11,
#
#             12,
#             13,
#
#             14,
#             15,
#
#             16,
#             17,
#
#             18,
#             19,
#
#             20,
#             21,
#         ]
#     }
# )
#
# print(pop_df)

# pop_df_1 = pop_df.loc['city_1', 'something']
# pop_df_1 = pop_df.loc???[['city_1', 'city_3'], ['total', 'something']] - это нужно вывести
# pop_df_1 = pop_df.loc???[['city_1', 'city_3'], 'something']

# print(pop_df_1)

# Задаем MultiIndex:
# 1 - через список массивов
# 2 - через список кортежей
# 3 - через декартово произведение
# 3 - через описание внутреннего представления: levels, codes

# уровням можно задавать названия

# data = {
#     ('city_1', 2010): 100,
#     ('city_1', 2020): 200,
#     ('city_2', 2010): 1001,
#     ('city_2', 2020): 2001,
# }
#
# s = pd.Series(data)
# print(s)
#
# s.index.names = ['city', 'year']
# print(s)

# index = pd.MultiIndex.from_product(
#     [
#         ['city_1', 'city_2'],
#         [2010, 2020]
#     ],
#     names = ['city', 'year']
# )
#
# columns = pd.MultiIndex.from_product(
#     [
#         ['person_1', 'person_2', 'person_3'],
#         ['job_1', 'job_2']
#     ],
#     names = ['worker', 'job']
# )
#
# rng = np.random.default_rng(1)
#
# data = rng.random((4,6))
# print(data)
# data_df = pd.DataFrame(data, index=index, columns=columns)
# print(data_df)

# Перегруппировка мультииндексов

# rng = np.random.default_rng(1)
#
# index = pd.MultiIndex.from_product(
#     [
#         ['a', 'c', 'b'],
#         [1, 2]
#     ]
# )
#
# data = pd.Series(rng.random(6), index=index)
# data.index.names = ['char', 'int']
#
# print(data)
# # print(data['a':'b']) # не сработает если ['a', 'c', 'b'], т е не по алфавиту
#
# data = data.sort_index()
# print(data)
# print(data['a':'b'])

# index = [
#     ('city_1', 2010, 1),
#     ('city_1', 2010, 2),
#
#     ('city_1', 2020, 1),
#     ('city_1', 2020, 2),
#
#     ('city_2', 2010, 1),
#     ('city_2', 2010, 2),
#
#     ('city_2', 2020, 1),
#     ('city_2', 2020, 2),
#
#     ('city_3', 2010, 1),
#     ('city_3', 2010, 2),
#
#     ('city_3', 2020, 1),
#     ('city_3', 2020, 2),
# ]
#
# population = [
#     101,
#     1010,
#
#     201,
#     2010,
#
#     102,
#     1020,
#
#     202,
#     2020,
#
#     103,
#     1030,
#
#     203,
#     2030,
# ]
#
# pop = pd.Series(population, index=index)
#
# print(pop)
#
# i = pd.MultiIndex.from_tuples(index)
#
# pop = pop.reindex(i)
# print(pop)
# print(pop.unstack())
# print(pop.unstack().unstack())

# NumPy Конкатенация

# x = [1,2,3]
# y = [4,5,6]
# z = [7,8,9]
#
# print(np.concatenate([x,y,z]))
#
# x = [[1,2,3]]
# y = [[4,5,6]]
# z = [[7,8,9]]
#
# print(np.concatenate([x,y,z]))
# print(np.concatenate([x,y,z], axis=1))
# print(np.concatenate([x,y,z], axis=0))

# Pandas - concat

# ser1 = pd.Series(['a', 'b', 'c'], index=[1,2,3])
# ser2 = pd.Series(['d', 'e', 'f'], index=[1,2,6])
#
# print(pd.concat([ser1, ser2], verify_integrity=False)) # == print(pd.concat([ser1, ser2]))
# print(pd.concat([ser1, ser2], ignore_index=True))
# print(pd.concat([ser1, ser2], keys=['x', 'y']))
#
#
# ser2 = pd.Series(['b', 'c', 'f'], index=[1,2,6])
# print(pd.concat([ser1, ser2], join='outer'))
# print(pd.concat([ser1, ser2], join='inner'))
