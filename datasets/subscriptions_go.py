# <импорт библиотеки pandas>
import pandas as pd
# <чтение файла с данными с сохранением в df>
subsciptions = pd.read_csv('https://code.s3.yandex.net/datasets/subscriptions_go.csv')
df = pd.DataFrame(subsciptions)
print(subsciptions)