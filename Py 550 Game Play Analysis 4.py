# https://www.bilibili.com/video/BV11U4y1L7SE?spm_id_from=333.788.recommend_more_video.2&vd_source=eae2c885960bda71fb3bd248c305cdbf
# seconday day percentage after registration

import pandas as pd

activity = pd.DataFrame({'player_id': [1,1,2,3,3], \
    'device_id': [2,2,3,11,4], \
    'event_date':['2016-03-01','2016-05-02','2017-06-25','2016-03-02','2018-07-03'],\
    'games_played':[5,6,1,0,5]})

activity.sort_values(['player_id', 'event_date'], inplace=True)

activity['date_difference'] = activity.groupby('player_id')['event_date'].shift(-1) - activity['event_date']
activity['rank_date'] = activity['date_difference'].rank()

second_day_user = activity[(activity['rank_date'] == 1) & (activity['date_difference'] == 1)]['player_id'].nunique()
total_user = activity['player_id'].nunique()
print(round(second_day_user/total_user, 2))