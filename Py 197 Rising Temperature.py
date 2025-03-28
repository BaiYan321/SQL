# https://www.bilibili.com/video/BV11U4y1L7SE?spm_id_from=333.788.recommend_more_video.2&vd_source=eae2c885960bda71fb3bd248c305cdbf

import pandas as pd

weather = pd.DataFrame({'id':[1,2,3,4], \
    'RecordDate':['2015-01-01', '2015-01-02','2015-01-03','2015-01-04'], \
    'temperature': [10, 25, 20, 30]})

# sort by the date
weather = weather.sort_values(["RecordDate"])

weather['previous_day'] = weather['RecordDate'].shift(1)
weather['previous_temp'] = weather['temperature'].shift(1)

weather['date_diff'] = pd.to_datetime(weather['RecordDate']) - pd.to_datetime(weather['previous_day'])
weather['date_diff'] =  weather['date_diff'].apply(lambda x: x.days)
print(weather)
result = weather[(weather['temperature'] > weather['previous_temp']) & (weather['date_diff']==1.0)]

print(result)