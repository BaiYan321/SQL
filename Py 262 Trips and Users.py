# https://www.bilibili.com/video/BV11U4y1L7SE?spm_id_from=333.788.recommend_more_video.2&vd_source=eae2c885960bda71fb3bd248c305cdbf

import pandas as pd

trips = pd.DataFrame({'Id':[1,2,3,4,5], \
    'Client_id': [45,43,56,77,88], \
    'Driver_id': [223, 6657,889,88,689], \
    'City_id':[1,1,1,1,1], \
    'Request_at':['2013-10-01','2013-10-01','2013-10-02','2013-10-02','2013-10-03'],\
    'Status':['cancelled_by_driver', 'cancelled_by_user', 'complete','cancelled_by_driver','cancelled_by_user']})

users = pd.DataFrame({'user_id':[45,43,56,77,88], \
    'banner':['yes','no','no','yes','yes'], \
    'user':['driver','user','user','user','driver']})

trips = trips[(trips['Request_at'] >= '2013-10-01') & (trips['Request_at'] <= '2013-10-03')]
trip_u = trips.merge(users, how = 'left', left_on='Client_id', right_on="user_id")
trip_u_u = trip_u.merge(users, how = 'left', left_on='Client_id', right_on="user_id")

trip_u_u = trip_u_u[(trip_u_u['banner_x']=='no') & (trip_u_u['banner_y']=='no')]
print(trip_u_u)
################ WIP  ###############
result = trip_u_u[trip_u_u['Status'].isin(['cancelled_by_user', 'cancelled_by_driver'])].groupby('Request_at')['Status'].count() / trip_u_u.groupby('Request_at')['Status'].count()
print(result)


