# https://www.bilibili.com/video/BV11U4y1L7SE?spm_id_from=333.788.recommend_more_video.2&vd_source=eae2c885960bda71fb3bd248c305cdbf

import pandas as pd

person = pd.DataFrame({'Id':[1, 2, 3], \
    'email': ['a@b.com', 'b@c.com', 'a@b.com']})

print(person)

# transform vs agg. Both of them can be used with groupby, but transform will keep the original shape, while agg will delete apart of the data

# Method 1
person['d_rank'] = person.groupby('email')['Id'].transform('min')

person = person[person['d_rank']==1]

# Method 2
grouped = person.groupby('email').agg(min_id=('Id', 'min'))

# Method 3
person = person.drop_duplicates(subset=['email'], keep='first')