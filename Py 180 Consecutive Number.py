# https://www.bilibili.com/video/BV1Xa4y1n7Dh/?spm_id_from=333.337.search-card.all.click&vd_source=eae2c885960bda71fb3bd248c305cdbf

import pandas as pd

logs = pd.DataFrame({"id":[1,2,3,4,5,6,7], \
    "Num":[1, 1, 1, 2, 1, 2, 2]})

# Method 1
consecutiveNumber = []

for i in range(logs.shape[0]):
    if logs['Num'][i] == logs['Num'][i+1] and logs['Num'][i] == logs['Num'][i+2]:
        consecutiveNumber.append(logs['Num'][i])

consecutiveNumber.unique()

# Method 2
logs["Lead_1"] = logs["Num"].shift(1)
logs["Lead_2"] = logs["Num"].shift(2)

logs[((logs['Num']==logs["Lead_1"]) & (logs['Num']==logs["Lead_2"]))]['Num'].unique()