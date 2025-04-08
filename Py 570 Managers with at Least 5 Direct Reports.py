# https://www.bilibili.com/video/BV11U4y1L7SE?spm_id_from=333.788.recommend_more_video.2&vd_source=eae2c885960bda71fb3bd248c305cdbf

import pandas as pd
import numpy as np

employee = pd.DataFrame({'Id': np.arange(101, 107), \
    'Name':['John','Dan','James','Amy','Anne', 'Ron'], \
    'Department':['A']*5+['B'], \
    'ManagerId':[np.nan]+[101]*5})

t = pd.DataFrame(employee['ManagerId'].value_counts()).reset_index().rename(columns={'Name':'count'})
ma = t[t['count']>4]['ManagerId'].values
print(ma)
result = employee[employee['Id'].isin(ma)]['Name']
print(result)