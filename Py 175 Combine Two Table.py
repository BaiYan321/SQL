# https://www.bilibili.com/video/BV1Xa4y1n7Dh/?spm_id_from=333.337.search-card.all.click&vd_source=eae2c885960bda71fb3bd248c305cdbf
import pandas as pd
import numpy as np

Person = pd.DataFrame({"PersonId":[1,2,3], \
    "FirstName": ["Mike", "Lee", "Zoe"], \
    "LastName": ["Zhang", "Zhao", "Liu"]})

Address = pd.DataFrame({"AddressId": [1],\
    "PersonId":[2], \
    "City":["New York"], \
    "State": ["New York"]})

Person.merge(Address, how="left", on='PersonId')[["LastName", "FirstName", "City", "State"]]