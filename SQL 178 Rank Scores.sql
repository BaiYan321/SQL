-- https://www.bilibili.com/video/BV1Xa4y1n7Dh/?spm_id_from=333.337.search-card.all.click&vd_source=eae2c885960bda71fb3bd248c305cdbf

SELECT dense_rank() OVER (ORDER BY Score ASC) AS Rank
FROM Scores;