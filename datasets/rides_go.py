# <импорт библиотеки pandas>
import pandas as pd
import matplotlib.pyplot as plt
from users_go import user_df

# <чтение файла с данными с сохранением в df>
rides = pd.read_csv('https://code.s3.yandex.net/datasets/rides_go.csv')
rides_df = pd.DataFrame(rides)
# Создание столбца month
rides_df['date'] = pd.to_datetime(rides_df['date'])
rides_df['month'] = rides_df['date'].dt.month
# <проверка: вычисление суммарного количества пропусков, выявленных в таблице df>
rides_df['user_id'] = rides_df['user_id'].fillna('unknown')
rides_df['distance'] = rides_df['distance'].fillna('unknown')
rides_df['duration'] = rides_df['duration'].fillna('unknown')
rides_df['date'] = rides_df['date'].fillna('unknown')
#df.isnull().sum()- проверка пропущеных значений
#print(df.duplicated().sum()) - проверка дубликатов

#визуализация данных

#расстояние, которое пользователь преодолел за одну поездку
distance_counter = rides_df['distance'].value_counts()
distance_counter.plot.bar()
#продолжительность поездок
duration_counter = rides_df['duration'].value_counts()
duration_counter.plot.bar()

#plt.show() #команда активации визуализации (всавить под нужной схемой)

#объединение данных user и rides по ключу user_id
user_rides = pd.merge(rides_df, user_df,
                      how='left', on='user_id')
#print(user_rides.head())