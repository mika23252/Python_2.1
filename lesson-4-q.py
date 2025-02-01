import pandas as pd
import numpy as np

# 1
#---

# 2

index = pd.MultiIndex.from_product(
    [
        ['city_1', 'city_2'],
        [2010, 2020]
    ],
    names = ['city', 'year']
)

columns = pd.MultiIndex.from_product(
    [
        ['person_1', 'person_2', 'person_3'],
        ['job_1', 'job_2']
    ],
    names = ['worker', 'job']
)

rng = np.random.default_rng(1)

data = rng.random((4,6))
print(data)
data_df = pd.DataFrame(data, index=index, columns=columns)
print(data_df)
print(data_df.loc[(slice(None), 2020), :])
print(data_df.loc[:, (slice(None), 'job_1')])
print(data_df.loc[('city_1', slice(None)), (slice(None), 'job_2')])

print('##############')

# 3
index = pd.MultiIndex.from_product(
    [
        ['city_1', 'city_2'],
        [2010, 2020]
    ],
    names=['city', 'year']
)
columns = pd.MultiIndex.from_product(
    [
        ['person_1', 'person_2', 'person_3'],
        ['job_1', 'job_2']
    ],
    names=['worker', 'job']
)

rng = np.random.default_rng(1)

data = rng.random((4,6))
print(data)
data_df = pd.DataFrame(data, index=index, columns=columns)
print(data_df)
print(data_df.loc[:,(['person_1', 'person_3'], slice(None))])
print(data_df.loc[('city_1', slice(None)), (slice('person_1','person_2'), slice(None))])

# пример  pd.IndexSlice
index = pd.MultiIndex.from_tuples(
    [('2021', 'Moscow', 'person_1'),
     ('2021', 'Moscow', 'person_2'),
     ('2021', 'Saint-Petersburg', 'person_1'),
     ('2022', 'Moscow', 'person_1'),
     ('2022', 'Moscow', 'person_3')],
    names=['year', 'city', 'person']
)

data = {
    'data': [10, 20, 30, 40, 50]
}

data_df = pd.DataFrame(data, index=index)

print(data_df)
idx = pd.IndexSlice
print(data_df.loc[idx[:, :, ['person_1', 'person_2']], :]) # выводит всю информацию по 'person_1', 'person_2'

print('##############')

# 4
df1 = pd.DataFrame(
    {
        "A": ["A0", "A1", "A2", "A3"],
        "B": ["B0", "B1", "B2", "B3"],
        "C": ["C0", "C1", "C2", "C3"],
        "D": ["D0", "D1", "D2", "D3"],
    },
    index=[0, 1, 2, 3],
)

df4 = pd.DataFrame(
    {
        "B": ["B2", "B3", "B6", "B7"],
        "D": ["D2", "D3", "D6", "D7"],
        "F": ["F2", "F3", "F6", "F7"],
    },
    index=[2, 3, 6, 7],
)

result = pd.concat([df1, df4], join='outer')
print(result)

result = pd.concat([df1, df4], join='inner')
print(result)
