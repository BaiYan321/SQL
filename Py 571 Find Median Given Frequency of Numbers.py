# https://www.bilibili.com/video/BV11U4y1L7SE?spm_id_from=333.788.recommend_more_video.2&vd_source=eae2c885960bda71fb3bd248c305cdbf

import pandas as pd
import numpy as np

numbers = pd.DataFrame({'Number':np.arange(4), \
    'Frequency':[7,1,3,1]})

print(numbers)

numbers['sum_asc'] = numbers.sort_values(by=['Number'], ascending=True)['Frequency'].cumsum()
numbers['sum_desc'] = numbers.sort_values(by=['Number'], ascending=False)['Frequency'].cumsum()
print(numbers)

total_frequency = numbers['Frequency'].sum()
print(total_frequency)

result = numbers[(numbers['sum_asc'] >= (total_frequency/2)) & (numbers['sum_desc'] >= (total_frequency/2))]['Number'].mean()
print(result)