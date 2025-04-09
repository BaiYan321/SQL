-- https://www.bilibili.com/video/BV1KQ4y1k7km/?spm_id_from=333.788.recommend_more_video.3&vd_source=eae2c885960bda71fb3bd248c305cdbf
SELECT AVG(a.num)
FROM (
    SELECT num, frequency,
    SUM(frequency) OVER (ORDER BY num ASC) AS sum_asc,
    SUM(frequency) OVER (ORDER BY num DESC) AS sum_desc
    FROM numbers
) AS a
WHERE a.sum_asc >= (SELECT SUM(frequency) FROM numbers)/2
AND a.sum_desc >= (SELECT SUM(frequency) FROM numbers)/2