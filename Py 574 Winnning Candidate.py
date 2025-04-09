# https://www.bilibili.com/video/BV1VY411b7Po?spm_id_from=333.788.player.player_end_recommend_autoplay&vd_source=eae2c885960bda71fb3bd248c305cdbf

import pandas as pd
import numpy as np

candidate = pd.DataFrame({'id':np.arange(1,6), \
    'Name':['A', 'B', 'C', 'D','E']})

vote = pd.DataFrame({'id':np.arange(1,6), \
    'CandidateId':[2,4,3,2,5]})

it = vote.groupby('CandidateId')['id'].count().reset_index()
winner_id = it[it['id'] == (it['id'].max())]['CandidateId'].item()
print(winner_id)

result = candidate[candidate['id'] == winner_id]['Name']
print(result)