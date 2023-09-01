# <импорт библиотеки pandas>
import matplotlib.pyplot as plt
import pandas as pd

# <чтение файла с данными с сохранением в df>
user = pd.read_csv('https://code.s3.yandex.net/datasets/users_go.csv')
df = pd.DataFrame(user)
# <проверка: вычисление суммарного количества пропусков, выявленных в таблице df>
df['user_id'] = df['user_id'].fillna('unknown')
df['name'] = df['name'].fillna('unknown')
df['age'] = df['age'].fillna('unknown')
df['city'] = df['city'].fillna('unknown')
df['subscription_type'] = df['subscription_type'].fillna('unknown')
#df.isnull().sum()- проверка пропущеных значений

# <удаление всех дубликатов из таблицы df специальным методом>
df=df.drop_duplicates().reset_index(drop=True)
#print(df.duplicated().sum()) - проверка дубликатов

#визуализация данных

#частота встречаемости городов
city_counter = df['city'].value_counts()
city_counter.plot.bar()
#соотношение пользователей с подпиской и без подписки
subscription = df['subscription_type'].value_counts()
subscription.plot.bar()
#возраст пользователей
age_counter = df['age'].value_counts()
age_counter.plot.bar()

plt.show() #команда активации визуализации (всавить под нужной схемой)

