# https://www.bilibili.com/video/BV1ZZ4y1c7YJ/?spm_id_from=333.337.search-card.all.click&vd_source=eae2c885960bda71fb3bd248c305cdbf

import pandas as pd

customers = pd.DataFrame({"id":[], \
    "Name":["Joe", "Henry", "Sam", "Max"]})

orders = pd.DataFrame({"Id": [1, 2] ,\
    "CustomerId": [3, 1]})

total = customers.merge(orders, how='Left', left_on="Id", right_on="CustomerId")

total[total["CustomerId"].isna()]['Name'].values()
# total[total["CustomerId"]==np.nan]['Name']