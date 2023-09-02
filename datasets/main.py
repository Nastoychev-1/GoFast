#импорт библиотек
import matplotlib.pyplot as plt
import pandas as pd
from subscriptions_go import all_df

#данныt о пользователях без подписки
non_subscription = all_df[all_df['subscription_type'] == 'free']
#print(non_subscription.head())

#данные о пользователях c подпиской
subscribed = all_df[all_df['subscription_type'] == 'ultra']
#print(subscribed.head())

#визуализация расстояния без подписки
distance_freeuser = non_subscription['distance'].value_counts()
distance_freeuser.plot.bar()

#визуализация расстояния c подпиской
distance_ultrauser = subscribed['distance'].value_counts()
distance_ultrauser.plot.bar()

#визуализация времени без подписки
duration_freeuser = non_subscription['duration'].value_counts()
duration_freeuser.plot.bar()

#визуализация времени с подпиской
duration_ultrauser = subscribed['duration'].value_counts()
duration_ultrauser.plot.bar()

#plt.show() #команда активации визуализации (всавить под нужной схемой)