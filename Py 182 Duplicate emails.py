# https://www.bilibili.com/video/BV1ZZ4y1c7YJ/?spm_id_from=333.337.search-card.all.click&vd_source=eae2c885960bda71fb3bd248c305cdbf

import pandas as pd

person = pd.DataFrame({'Id':[1, 2, 3], \
    'email': ['a@b.com', 'b@c.com', 'a@b.com']})

a = person['Email'].value_counts() # count occurance of each value

a[a>1].index[0]