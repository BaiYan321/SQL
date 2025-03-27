# https://www.bilibili.com/video/BV1ZZ4y1c7YJ/?spm_id_from=333.337.search-card.all.click&vd_source=eae2c885960bda71fb3bd248c305cdbf

import pandas as pd

employee = pd.DataFrame({'Id': [1,2,3,4,5], \
                        "Name":["Joe", "Henry", "Sam", "Max", "Holly"], \
                        'Salary': [70000, 90000, 80000, 60000, 90000], \
                        'DepartmentId': [1,1,2,2,1]})

department = pd.DataFrame({'Id':[1,2], \
    'Name': ["IT", "Sales"]})

# rank the salary by demparment
employee['d_rank'] = employee.groupby('DepartmentId')['Salary'].rank('dense', ascending=False)

employee = employee[employee['d_rank']==1]

result = employee.merge(department, how = 'inner', left_on='DepartmentId', right_on='Id')
result = result[['Name', 'Salary','Department']]