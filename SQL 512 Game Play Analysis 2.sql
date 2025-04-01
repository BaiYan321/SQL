-- https://www.bilibili.com/video/BV11U4y1L7SE?spm_id_from=333.788.recommend_more_video.2&vd_source=eae2c885960bda71fb3bd248c305cdbf

-- Method 1
WITH CTE AS
(
    SELECT player_id, min(event_date) AS min_date
    FROM Activity
    GROUP BY player_id
)

SELECT CTE.player_id, Activity.device
FROM CTE
LEFT JOIN Activity
ON CTE.player_id = Activity.player_id
AND CTE.min_date = Activity.event_date;

-- Method 2
SELECT a.player_id, a.device
FROM
(
    SELECT player_id, event_date, device
    dense_rank() OVER(PARTITION BY player_id ORDER BY event_date ASC) AS d_rank
    FROM Activity
) AS A
WHERE a.d_rank = 1