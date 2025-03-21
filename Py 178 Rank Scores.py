# https://www.bilibili.com/video/BV1Xa4y1n7Dh/?spm_id_from=333.337.search-card.all.click&vd_source=eae2c885960bda71fb3bd248c305cdbf

import pandas as pd

scores = pd.DataFrame({"id":[1,2,3,4,5,6], \
    "Score":[3.5, 3.65, 4.00,3.85, 4.00, 3.65]})

scores['Rank'] = scores['Score'].rank(method = "dense", ascending=False)
scores[["Score", "Rank"]].sort_values(["Rank", "Score"], ascending=False)