# https://www.bilibili.com/video/BV1VY411b7Po?spm_id_from=333.788.player.player_end_recommend_autoplay&vd_source=eae2c885960bda71fb3bd248c305cdbf

import pandas as pd
import numpy as np

employee = pd.DataFrame({'empId':np.arange(1,5), \
    'name':['John', 'Dan', 'Brad', 'Thomas'], \
    'supervisor':[3,3,np.nan,3], \
    'salary':[1000,2000,4000,4000]})

bonus = pd.DataFrame({'empId':[2,4], \
    'bonus':[500,2000]})

result = employee.merge(bonus, how='left', on='empId')
print(result)
result = result[(result['bonus']<1000) | (result['bonus'].isna()) ][['name','bonus']]
print(result)