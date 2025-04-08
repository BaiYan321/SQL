# https://www.bilibili.com/video/BV11U4y1L7SE?spm_id_from=333.788.recommend_more_video.2&vd_source=eae2c885960bda71fb3bd248c305cdbf

import pandas as pd
import numpy as np

employee = pd.DataFrame({'Id': np.arange(1,18), \
    'Company': ['A']*6+['B']*6+['C']*5, \
    'Salary': [2341,341,15,15314,451,513,15,13,1154,1345,1221,234,2345,2645,2645,2652,65]})

employee.sort_values(['Company', 'Salary'], inplace=True)
print(employee)

employee['row_number'] = employee.groupby('Company')['Salary'].transform('count')
employee['Salary_rank'] = employee.groupby('Company')['Salary'].rank('dense')
print(employee)
result = employee[(employee['row_number']/2 == employee['Salary_rank']) | (employee['row_number']/2+1 == employee['Salary_rank']) | (employee['row_number']/2+0.5 == employee['Salary_rank'])][['Id', 'Company','Salary']]
print(result)