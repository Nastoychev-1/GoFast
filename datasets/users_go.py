# <импорт библиотеки pandas>
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