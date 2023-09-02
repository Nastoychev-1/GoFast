# <импорт библиотеки pandas>
import pandas as pd
from rides_go import user_rides


# <чтение файла с данными с сохранением в df>
subsciptions = pd.read_csv('https://code.s3.yandex.net/datasets/subscriptions_go.csv')
subsciptions_df = pd.DataFrame(subsciptions)
# print(subsciptions)

#объединение данных в один DF по ключу subscription_type
all_df = pd.merge(subsciptions_df, user_rides,
                  how='left', on='subscription_type')
#print(all_df.head())
