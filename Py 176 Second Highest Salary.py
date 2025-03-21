# https://www.bilibili.com/video/BV1Xa4y1n7Dh/?spm_id_from=333.337.search-card.all.click&vd_source=eae2c885960bda71fb3bd248c305cdbf
import pandas as pd

employee = pd.DataFrame({"Salary":[1000, 3000, 5000]})

sorted(employee['Salary'].unique(), reverse=True)[1]
