-- https://www.bilibili.com/video/BV11U4y1L7SE?spm_id_from=333.788.recommend_more_video.2&vd_source=eae2c885960bda71fb3bd248c305cdbf
WITH CTE AS (
    SELECT t.Request_at, t.Status
    FROM Trips AS t
    LEFT JOIN USERS AS u1
    ON t.Client_Id = u1.User_Id
    LEFT JOIN USER AS u2
    ON t.Driver_id = u2.User_Id
    WHERE t.Request_at BETWEEN '2013-10-01' AND '2013-10-03'
    AND u1.Banned = 'No'
    AND u2.Banned = 'No'
)

SELECT Request_at
COUNT(CASE WHEN Status in ('cancelled_by_driver', 'cancelled_by_user') THEN 1) / COUNT(Request_at)
FROM CTE
GROUP BY Request_at
