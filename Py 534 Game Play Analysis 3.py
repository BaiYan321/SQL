# https://www.bilibili.com/video/BV11U4y1L7SE?spm_id_from=333.788.recommend_more_video.2&vd_source=eae2c885960bda71fb3bd248c305cdbf

import pandas as pd

activity = pd.DataFrame({'player_id': [1,1,2,3,3], \
    'device_id': [2,2,3,11,4], \
    'event_date':['2016-03-01','2016-05-02','2017-06-25','2016-03-02','2018-07-03'],\
    'games_played':[5,6,1,0,5]})

activity = activity.sort_values(['player_id', 'event_date'])

activity['game_played_so_far']= activity.groupby('player_id')['games_played'].cumsum()
result = activity[['player_id', 'event_date', 'game_played_so_far']]
print(result)