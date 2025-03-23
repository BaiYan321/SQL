# https://www.bilibili.com/video/BV1ZZ4y1c7YJ/?spm_id_from=333.337.search-card.all.click&vd_source=eae2c885960bda71fb3bd248c305cdbf

import pandas as pd
import numpy as np

employee = pd.DataFrame({'Id': [1, 2, 3, 4], \
    'Name': ['Joe', 'Henry', 'Same', 'Max'], \
    'Salary': [70000, 80000, 60000, 90000], \
    'ManagerId': [3,4,np.nan, np.nan]})

a = employee.merge(employee, how="left", left_on='ManagerId', right_on='Id')

a[a['Salary_x'] > a['Salary_y']]['Name_x'].values