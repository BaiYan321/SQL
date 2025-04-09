-- https://www.bilibili.com/video/BV1VY411b7Po?spm_id_from=333.788.player.player_end_recommend_autoplay&vd_source=eae2c885960bda71fb3bd248c305cdbf

SELECT candidate.name
FROM candidate
INNER JOIN
(
    SELECT candidateId, COUNT(candidateId) AS vote_number
    FROM Vote
    GROUP BY candidateId
    ORDER BY COUNT(candidateId) DESC
    LIMIT 1
) AS a
ON candidate.id = a.candidateId
