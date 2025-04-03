-- https://www.bilibili.com/video/BV1KQ4y1k7km?spm_id_from=333.788.recommend_more_video.3&vd_source=eae2c885960bda71fb3bd248c305cdbf
-- Methond 1
SELECT
(
    SELECT COUNT(DISTINCT Activity.player_id)
    FROM
    (
        SELECT b.player_id, b.Second_day
        FROM 
        (
            SELECT a.player_id, DATEADD(day, 1, a.first_day) AS Second_day
            FROM 
            (
                SELECT player_id, min(event_date) AS first_day
                FROM Activity
                GROUP BY player_id
            ) AS a
        ) AS b
        LEFT JOIN Activity
        ON b.player_id = Activity.player_id
        AND b.Second_day = Activity.event_date
    ) AS c
    WHERE Activity IS NOT NULL
)
/
(
    SELECT COUNT(DISTINCT player_id)
    FROM Activity
);

-- Method 2
SELECT (
SELECT COUNT(DISTINCT a.player_id)
FROM
(
    SELECT player_id, event_date, 
        dense_rank() OVER (PARTITION BY player_id ORDER BY event_date ASC) AS d_rank,
        lead(event_date, 1) OVER (PARTITION BY player_id) AS Second_day
    FROM  Activity
) AS a
WHERE a.event_date = a.Second_day
AND a.d_rank = 2
)
/
(
    SELECT COUNT(DISTINCT player_id)
    FROM Activity
);

-- Method 3
SELECT round(count(DISTINCT CASE WHEN t1.d_rank = 1 AND t1.date_difference = 1 THEN t1.player_id END) / COUNT(DISTINCT t1.player_id), 2) AS fraction
FROM
(
SELECT player_id,
    dense_rank() OVER (PARTITION BY player_id ORDER BY event_date ASC) AS d_rank,
    datediff(lead(event_date) OVER (PARTITION BY player_id ORDER BY event_date ASC), event_date) AS date_difference
FROM Activity
) AS t1;