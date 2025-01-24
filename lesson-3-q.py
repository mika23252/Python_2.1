import pandas as pd
import numpy as np


# 1 Привести различные способы создания объектов типа Series

# Из списка Python
data_list = [10, 20, 30, 40]
print(pd.Series(data_list), '\n')

# Из массива NumPy
data_array = np.array(data_list)
print(pd.Series(data_array), '\n')

# Из скалярного значения
val = 5
print(pd.Series(val, index=range(5)), '\n')

# Из словаря
data_dict = {'a': 100, 'b': 200, 'c': 300}
print(pd.Series(data_dict))
print('##################################')



# 2 Привести различные способы создания объектов типа DataFrame

# через объекты Series
pop = pd.Series({
    'city_1': 1001,
    'city_2': 1002,
    'city_3': 1003,
})
area = pd.Series({
    'city_1': 2001,
    'city_2': 2002,
    'city_3': 2003,
})

data = pd.DataFrame({'area1': area, 'pop1': pop})
print(data, '\n')

# список словарей
data = [
    {"Name": "John", "Age": 25},
    {"Name": "Bob", "Age": 30}
]

df = pd.DataFrame(data)
print(df, '\n')

# словари объектов Series
population_dict = {
    'city_1': 1001,
    'city_2': 1002,
    'city_3': 1003,
    'city_4': 1004,
    'city_5': 1005
}

area_dict = {
    'city_1': 9991,
    'city_2': 9992,
    'city_3': 9993,
    'city_4': 9994,
    'city_5': 9995
}

popelation = pd.Series(population_dict)
area = pd.Series(area_dict)

states = pd.DataFrame({
    'population1': popelation,
    'area1': area
})

print(states, '\n')

# Двумерный массив NumPy
data = np.array([
    [1, 4, 7],
    [2, 5, 8],
    [3, 6, 9]
])

df = pd.DataFrame(data)
print(df, '\n')

# Структурированный массив NumPy
data = np.array([(1, 'First', 0.5, 1+2j),(2, 'Second', 1.3, 2-2j), (3, 'Third', 0.8, 1+3j)], dtype=('i2, a6, f4, c8'))

df = pd.DataFrame(data)
print(df)
print('##################################')


# 3 Объедините два объекта Series с неодинаковыми множествами ключей (индексов) так, чтобы вместо NaN было установлено значение 1
a = pd.Series(data_array) # [10, 20, 30, 40]
b = pd.Series(val, index=range(5))

print(a.add(b).fillna(1))
print('##################################')


# 4 Переписать пример с транслированием для DataFrame так, чтобы вычитание происходило по СТОЛБЦАМ
rng = np.random.default_rng()
A = rng.integers(0, 10, (3, 4))
df = pd.DataFrame(A, columns=['a', 'b', 'c', 'd'])
result = df.sub(df.iloc[:, 0], axis=0)
print(A, '\n')
print(df, '\n')
print(result)
print('##################################')

# 5 На примере объектов DataFrame продемонстрируйте использование методов ffill() и bfill()
data = {
    'A': [1, None, 3, None, 5],
    'B': [None, 2, None, 4, None],
    'C': [1, None, None, None, 5]
}

df = pd.DataFrame(data)
print(df, '\n')

df_ffill = df.ffill() # заполняет пропущенные значения, копируя последнее известное значение вниз по колонке
print(df_ffill, '\n')

df_bfill = df.bfill() # заполняет пропущенные значения, копируя следующее известное значение вверх по колонке
print(df_bfill)
