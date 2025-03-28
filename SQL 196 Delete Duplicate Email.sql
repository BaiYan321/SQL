-- https://www.bilibili.com/video/BV11U4y1L7SE?spm_id_from=333.788.recommend_more_video.2&vd_source=eae2c885960bda71fb3bd248c305cdbf

SELECT a.Email
FROM 
(
SELECT Email, dense_rank() OVER (PARTITION BY Email ORDER BY Id ASC) as d_rank
FROM Person
) AS a
WHERE a.d_rank=1;
