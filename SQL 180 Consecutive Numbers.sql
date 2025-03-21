-- https://www.bilibili.com/video/BV1Xa4y1n7Dh/?spm_id_from=333.337.search-card.all.click&vd_source=eae2c885960bda71fb3bd248c305cdbf
SELECT DISTINCT a.num
FROM
(
    SELECT num,
    lead(num, 1) OVER (ORDER BY id ASC) AS num_1,
    lead(num, 2) OVER (ORDER BY id ASC) AS num_2,
    FROM logs
) AS a
WHERE a.num = a.num_1
AND a.num = a.num_2