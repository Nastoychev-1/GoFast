# <импорт библиотеки pandas>
import matplotlib.pyplot as plt
import pandas as pd

# <чтение файла с данными с сохранением в df>
user = pd.read_csv('https://code.s3.yandex.net/datasets/users_go.csv')
user_df = pd.DataFrame(user)
# <проверка: вычисление суммарного количества пропусков, выявленных в таблице df>
user_df['user_id'] = user_df['user_id'].fillna('unknown')
user_df['name'] = user_df['name'].fillna('unknown')
user_df['age'] = user_df['age'].fillna('unknown')
user_df['city'] = user_df['city'].fillna('unknown')
user_df['subscription_type'] = user_df['subscription_type'].fillna('unknown')
#df.isnull().sum()- проверка пропущеных значений

# <удаление всех дубликатов из таблицы df специальным методом>
user_df = user_df.drop_duplicates().reset_index(drop=True)
#print(df.duplicated().sum()) - проверка дубликатов

#визуализация данных

#частота встречаемости городов
city_counter = user_df['city'].value_counts()
city_counter.plot.bar()
#соотношение пользователей с подпиской и без подписки
subscription = user_df['subscription_type'].value_counts()
subscription.plot.bar()
#возраст пользователей
age_counter = user_df['age'].value_counts()
age_counter.plot.bar()

#plt.show() #команда активации визуализации (всавить под нужной схемой)

