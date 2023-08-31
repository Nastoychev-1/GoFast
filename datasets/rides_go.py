# <импорт библиотеки pandas>
import pandas as pd

# <чтение файла с данными с сохранением в df>
rides = pd.read_csv('https://code.s3.yandex.net/datasets/rides_go.csv')
df = pd.DataFrame(rides)
# Создание столбца month
df['date'] = pd.to_datetime(df['date'])
df['month'] = df['date'].dt.month
# <проверка: вычисление суммарного количества пропусков, выявленных в таблице df>
df['user_id'] = df['user_id'].fillna('unknown')
df['distance'] = df['distance'].fillna('unknown')
df['duration'] = df['duration'].fillna('unknown')
df['date'] = df['date'].fillna('unknown')
#df.isnull().sum()- проверка пропущеных значений
#print(df.duplicated().sum()) - проверка дубликатов